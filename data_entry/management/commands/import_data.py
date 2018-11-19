#!python

import datetime
import json
import os

from django.core.management.base import BaseCommand, CommandError
from data_entry.models import DataEtl

import requests


def get_credentials():
    """ Read credentials from a file credentials.txt that must be located in the
        same directory as this file. It's a simple text file; the first line
        contains the login, the second the password. 
    """
    whereami = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(whereami, "credentials.txt")
    if os.path.exists(path):
        with open(path) as f:
            login = f.readline().strip()
            password = f.readline().strip()
            return (login, password)
    else:
        raise OSError("File does not exist: %s" % path)

class DHIS2Error(Exception):
    pass
class HMISError(Exception):
    pass


# XXX OBSOLETE -- remove?
class DHIS2:
    API_BASE_URL = "https://play.dhis2.org/demo/api/"
    LOGIN_URL = "https://play.dhis2.org/2.30/dhis-web-commons/security/login.action"
    API_URL = "https://play.dhis2.org/demo/api/dataValueSets.json"

    def __init__(self, login, password):
        self.sess = requests.Session()
        self.logged_in = False
        self.cookies = {}
 
        # cached values
        self.orgUnits = []

        self.login(login, password)

    def login(self, login, password):
        print("Logging in...")
        r = self.sess.post(self.LOGIN_URL, auth=(login, password))
        #print(r.status_code)
        #print(r.headers)
        #print(r.encoding)
        #print(r.cookies)
        #import pprint; pprint.pprint(r.__dict__)
        if r.status_code == 200:
            print("Succesfully logged in.")
            self.logged_in = True
            self.cookies = r.cookies
        else:
            print("** Login failed")
            print(r.status_code)
            print(r.headers)
            print(r.cookies)
            print(r.text)
            raise DHIS2Error("Could not login")

    def getPagedResults(self, url, name):
        """ Get results from an API calls, taking into account that there might
            be multiple pages. If there are, fetch all those pages and return
            the combined results.
        """

        def getPageResult(page):
            print("  Fetching page %s..." % page)
            r = self.sess.get(url, cookies=self.cookies, 
                              params={'page': page},
                              headers={'Content-Type': 'application/json'})
            return r.json()

        page = 1
        results = []

        while True:
            j = getPageResult(page)
            results.extend(j[name])
            pager = j['pager']
            # if we reached the last page, break out of the loop
            if pager['page'] >= pager['pageCount']:
                print("All pages fetched")
                break
            page += 1

        return results
        
    def getOrgUnits(self):
        """ Get a list of organisation units. This is a list of dictionaries
            like:

            {
                "displayName": "Adonkia CHP",
                "id": "Rp268JB6Ne4"
            }
        """
        print("Loading organisation units...")
        URL = self.API_BASE_URL + "organisationUnits.json"
        self.orgUnits = self.getPagedResults(URL, 'organisationUnits')
        print("%s organisationunits found" % len(self.orgUnits))

def current_quarter():
    month = datetime.date.today().month
    if month in [1, 2, 3]: return 1
    elif month in [4, 5, 6]: return 2
    elif month in [7, 8, 9]: return 3
    else: return 4

def current_year():
    return datetime.date.today().year

def gen_quarters():
    """ Generator to produce all (year, quarter) pairs, starting at (2018, 1),
        ending (and including) the current year and current quarter. """
    curr_year = current_year()
    curr_quarter = current_quarter()
    year = 2018
    quarter = 1
    while True:
        yield year, quarter
        if year == curr_year and quarter == curr_quarter:
            raise StopIteration
        quarter += 1
        if quarter > 4:
            year += 1
            quarter = 1

class ZambiaHMIS:
    LOGIN_URL = "https://www.zambiahmis.org/dhis-web-commons/security/login.action"
    ORG_UNIT_API = "https://www.zambiahmis.org/api/organisationUnits.json?paging=false"
    DATA_ELEMENTS_API = "https://www.zambiahmis.org/api/dataElements.json"
    DATA_SETS_API = "https://www.zambiahmis.org/api/dataSets.json"
    DATA_VALUE_SET_API = "https://www.zambiahmis.org/api/26/dataValueSets.json?"\
                         "orgUnit={0}&dataSet={1}&period={2}&children=true"

    def __init__(self, login, password):
        self.sess = requests.Session()
        self.logged_in = False
        self.cookies = {}
 
        # cached values
        self.orgUnits = []
        self.dataElements = []
        self.dataSets = []
        # XXX should these (also) be in a dict keyed by ID?

        self.dataElementsById = {}

        self.login(login, password)

    def login(self, login, password):
        # NOTE: if login/password are incorrect, apparently this will endlessly
        # redirect until an error message shows up.
        print("Logging in...")
        r = self.sess.post(self.LOGIN_URL, auth=(login, password))
        #print(r.status_code)
        #print(r.headers)
        #print(r.encoding)
        #print(r.cookies)
        #import pprint; pprint.pprint(r.__dict__)
        if r.status_code == 200:
            print("Succesfully logged in.")
            self.logged_in = True
            self.cookies = r.cookies
        else:
            print("** Login failed")
            print(r.status_code)
            print(r.headers)
            print(r.cookies)
            print(r.text)
            raise HMIS2Error("Could not login")

    # XXX maybe rename to getResults?
    def getPagedResults(self, url, name, paged=True):
        """ Get results from an API call, taking into account that there might
            be multiple pages. If there are, fetch all those pages and return
            the combined results.
        """

        def getPageResult(page):
            print("  Fetching page %s..." % page)
            r = self.sess.get(url, cookies=self.cookies, 
                              params={'page': page},
                              headers={'Content-Type': 'application/json'})
            return r.json()

        page = 1
        results = []

        if not paged:
            j = getPageResult(page)
            return j[name]

        while True:
            j = getPageResult(page)
            results.extend(j[name])
            pager = j['pager']
            # if we reached the last page, break out of the loop
            if pager['page'] >= pager['pageCount']:
                print("All pages fetched")
                break
            page += 1

        return results

    def getOrgUnits(self):
        """ Get a list of organisation units. This is a list of dictionaries
            like:

            {
                "displayName": "Adonkia CHP",
                "id": "Rp268JB6Ne4"
            }
        """
        print("Loading organisation units...")
        self.orgUnits = self.getPagedResults(self.ORG_UNIT_API, 'organisationUnits', 
                                             paged=False)
        print("%s organisation units found" % len(self.orgUnits))

    def getDataElements(self):
        """ Get a list of data elements. This is a list of dictionaries like:
            {"id": "FtxtwvoeA5e", "displayName": "Age females 15-49"}
        """
        print("Loading data elements...")
        self.dataElements = self.getPagedResults(self.DATA_ELEMENTS_API, 
                                                 'dataElements')
        self.dataElementsById = dict([(row['id'], row['displayName']) 
                                      for row in self.dataElements])
        print("%s data elements found" % len(self.dataElements))

    def getDataSets(self):
        print("Loading data sets...")
        self.dataSets = self.getPagedResults(self.DATA_SETS_API, 'dataSets')
        print("%s data sets found" % len(self.dataSets))

    def getDataValueSet(self, orgUnit, dataSet, period):
        url = self.DATA_VALUE_SET_API.format(orgUnit, dataSet, period)
        print(url)
        # fetch and return JSON as-is, no pagination or lookup
        r = self.sess.get(url, cookies=self.cookies, 
                               headers={'Content-Type': 'application/json'})
        try:
            return r.json()
        except json.decoder.JSONDecodeError as e:
            print("Invalid JSON:")
            print(e.args)
            return None

    def populate(self, test=False):
        """ Fetch required data from HMIS and populate the DataEtl table with
            it. 
            If 'test' is True, then we do a test run with one organisation unit
            and one data element. 
        """
        for year, quarter in gen_quarters():
            period = "%04d%02d" % (year, quarter)
            print("Quarter:", period)
            for orgUnit in self.orgUnits:
                print("orgUnit:", orgUnit)
                for dataSet in self.dataSets:
                    print("dataSet:", dataSet)
                    j = self.getDataValueSet(orgUnit['id'], dataSet['id'], period)

                    if j is None:
                        # there was a problem with the JSON; print a
                        # diagnostic message and continue
                        continue

                    if j.get('dataValues'):
                        self.store_data(orgUnit, dataSet, period, j)
                        with open("test.json", "w") as f:
                            json.dump(j, f, indent=4, sort_keys=True)
                        if test:
                            print("Testing ended; exiting")
                            return

    def store_data(self, orgUnit, dataSet, period, dataValueSets):
        for dv in dataValueSets['dataValues']:
            d = DataEtl(dataElementName=self.dataElementsById[dv['dataElement']],
                        dataElementID=dv['dataElement'],
                        orgUnitName=orgUnit['displayName'],
                        orgUnitID=orgUnit['id'],
                        period=int(period),
                        value=int(dv['value'] or 0))
                        # XXX FIXME: value might be boolean!
            d.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        login, password = get_credentials()
        hmis = ZambiaHMIS(login, password)
        if hmis.logged_in:
            hmis.getOrgUnits()
            hmis.getDataSets()
            hmis.getDataElements()
            hmis.populate(test=False)

            # test
            #data = hmis.getDataValueSet("mHs8NE6sJBO", "sHbZC96yrxU", "201801")
            #print(json.dumps(data, indent=4, sort_keys=True))


            return

