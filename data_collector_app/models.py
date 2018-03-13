from django.db import models
from django import forms

# Create your models here.
# list variables
cbo = 'Community Based Organization'
fbo = 'Faith Based Organization'
local_ngo = 'Local NGO'
inter_ngo = 'International NGO'
government = 'Government Organization'
private = 'Private Organization'
org_others = 'Other organization / group - please specify'  # change some kind of list later

lsk = 'Lusaka Province'
cop = 'Copperbelt Province'
east = 'Easten Province'
lua = 'Luapula Province'
much = 'Muchinga Province'
nwest = 'North Westen Province'
north = 'Northern Province'
south = 'Southern Province'
west = 'Western Province'

Q1 = 'Quarter 1'
Q2 = 'Quarter 2'
Q3 = 'Quarter 3'
Q4 = 'Quarter 4'

plhiv = 'People living with HIV/ AIDS (PLHIV)'
ovc = 'Orphans and Vulnerable Children (OVC)'
pregnant_women = 'Pregnant Women'
care_givers = 'Care givers'
health_workers = 'Heath workers'
teachers = 'Teachers'
children = 'Children'
adolecents = 'Adolecents/ Youth'
old_people = 'Old people/ Pensioners'
disabled_people = 'Disabled people'
inmates_wivies = 'Prisoners wivies' # form says 'Prisoners Widows' Confirm this
govt_workers = 'Government workers (work place)'
sex_workers = 'Sex workers'
church_leaders = 'Church leaders'
employee_families = 'Employees and/or Employee families'
gdwg = 'Guardians/ Divorced/ Widows/ Grandparents'
idu = 'Intravenous drug users (IDU)'
msm = 'Men who have sex with men (MSM)'
mobile_population = 'Migrants/ Mobile population'
out_of_school_youth = 'Out of school youth'
inmates = 'Inmates'
street_children = 'Street children'
traditional_healers = 'Traditional healers'
traditional_leaders = 'Traditional leaders'
target_others = 'Other target groups - please specify' # change some kind of list later

food_and_nutrition = 'Food and Nutrition'
shelter_and_care = 'Shelter and Care'
protection_and_legal_aid = 'Protection and Legal aid'
healthcare = 'Healthcare'
psychosocial = 'Psychosocial'
social_support = 'Social support'
spiritual_support = 'Spiritual support'
education_and_vocational_training = 'Education and Vocational training'
economic_strengthening = 'Economic strengthening'

n_a = 'N/A'
no = 'NO materials were distributed this quater'
books = 'Books'
brochures = 'Brochures'
posters = 'Posters'
t_shirts = 'T-Shirts'
tv_spots = 'TV Spots'
radio_spots = 'Radio Spots'
e_spots = 'E spot'
billboards = 'Billboards'
drama = 'Drama' # customized field
material_other = 'Other' # Enter from keyboard -- customized field 

nacmis = 'NAC-MIS'
hmis = 'HMIS'
datim = 'DATIM'
internal_system = 'Internal system'
systems_other = 'Other'

QUARTER_LIST = (
    (Q1, 'Jan - Mar'),
    (Q2, 'Apr - Jun'),
    (Q3, 'Jul - Oct'),
    (Q4, 'Nov - Dec')
)

ORGANIZATION_TYPE_LIST = (
    (cbo, 'Community Based Organization'),
    (fbo, 'Faith Based Organization'),
    (local_ngo, 'Local Non Governmental Organization'),
    (inter_ngo, 'International Non Governmental Organization'),
    (government, 'Government Organization'),
    (private, 'Private Organization'),
    (org_others, 'Other organization / group - please specify')
)

PROVINCES_ZAMBIA = (
    (lsk, 'Lusaka Province'),
    (cop, 'Copperbelt Province'),
    (east, 'Easten Province'),
    (lua, 'Luapula Province'),
    (much, 'Muchinga Province'),
    (nwest, 'North Westen Province'),
    (north, 'Northern Province'),
    (south, 'Southern Province'),
    (west, 'Western Province')
)

ORGANIZATION_TARGET_LIST = (
    (plhiv, 'People living with HIV/ AIDS'),
    (ovc, 'Orphans and Vulnerable Children'),
    (pregnant_women, 'Pregnant Women'),
    (care_givers, 'Care givers'),
    (health_workers, 'Heath workers'),
    (teachers, 'Teachers'),
    (children, 'Children'),
    (adolecents, 'Adolecents/ Youth'),
    (old_people, 'Old people/ Pensioners'),
    (disabled_people, 'Disabled people'),
    (inmates_wivies, 'Prisoners wivies'),
    (govt_workers, 'Government workers (work place)'),
    (sex_workers, 'Sex workers'),
    (church_leaders, 'Church leaders'),
    (employee_families, 'Employees and/or Employee families'),
    (gdwg, 'Guardians/ Divorced/ Widows/ Grandparents'),
    (idu, 'Intravenous drug users (IDU)'),
    (msm, 'Men who have sex with men (MSM)'),
    (mobile_population, 'Migrants/ Mobile population'),
    (out_of_school_youth, 'Out of school youth'),
    (inmates, 'Inmates'),
    (street_children, 'Street children'),
    (traditional_healers, 'Traditional healers'),
    (traditional_leaders, 'Traditional leaders'),
    (target_others, 'Other target groups - please specify')
)


DISTRICT_AREA_LIST = () # Auto populated area tuple from, dependant on district 

TYPE_OF_SUPPORT_LIST = (
    (food_and_nutrition, 'Food and Nutrition'),
    (shelter_and_care, 'Shelter and Care'),
    (protection_and_legal_aid, 'Protection and Legal aid'),
    (healthcare, 'Healthcare'),
    (psychosocial, 'Psychosocial'),
    (social_support, 'Social support'),
    (spiritual_support, 'Spiritual support'),
    (education_and_vocational_training, 'Education and Vocational training'),
    (economic_strengthening, 'Economic strengthening')
)

IEC_MATERIALS = (
    (books, 'Books'),
    (brochures, 'Brochures'),
    (posters, 'Posters'),
    (t_shirts, 'T-Shirts'),
    (tv_spots, 'TV Spots'),
    (radio_spots, 'Radio Spots'),
    (e_spots, 'E spot'),
    (billboards, 'Billboards'),
    (drama, 'Drama'),
    (material_other, 'Other')
)

SOURCES_OF_INFORMATION = (
    (nacmis, 'NAC-MIS'),
    (hmis, 'HMIS'),
    (datim, 'DATIM'),
    (internal_system, 'Internal system'),
    (systems_other, 'Other')
)
#               STAKEHOLDER DIRECTORY
# *************************************************

class StakeHolderDirectory(models.Model):
    # --> Basic details on the organization
    organization_name = models.CharField(max_length=200)
    start_year = models.DateTimeField('start_year')
    permanent_employee_female = models.IntegerField(default=0)
    permanent_employee_male = models.IntegerField(default=0)
    temporary_employee_female = models.IntegerField(default=0)
    temporary_employee_male = models.IntegerField(default=0)
    volunteer_employee_female = models.IntegerField(default=0)
    volunteer_employee_male = models.IntegerField(default=0)
    description = models.TextField()

    # --> Contact details
    contact_name = models.CharField(max_length=50)
    contact_organization = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    alternative_phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)

    organization_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_LIST, default='N/A')
    # organization_target = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    #check box fileds the 'organization_target' attribute
    plhiv = models.BooleanField('people living with HIV/ AIDS')
    ovc = models.BooleanField('orphans and vulnerable children')
    pregnant_women = models.BooleanField()
    care_givers = models.BooleanField()
    health_workers = models.BooleanField()
    teachers = models.BooleanField()
    children = models.BooleanField()
    adolecents = models.BooleanField('adolecents/ youth')
    old_people = models.BooleanField('old people/ pensioners')
    disabled_people = models.BooleanField()
    inmates_wivies = models.BooleanField()
    govt_workers = models.BooleanField('government workers (work place)')
    sex_workers = models.BooleanField()
    church_leaders = models.BooleanField()
    employee_families = models.BooleanField('employees and/or employee families')
    gdwg = models.BooleanField('guardians/ divorced/ widows/ grandparents')
    idu = models.BooleanField('intravenous drug users (IDU)')
    msm = models.BooleanField('men who have sex with men (MSM)')
    mobile_population = models.BooleanField('migrants/ mobile population')
    out_of_school_youth = models.BooleanField()
    inmates = models.BooleanField()
    street_children = models.BooleanField()
    traditional_healers = models.BooleanField()
    traditional_leaders = models.BooleanField()
    target_others = models.BooleanField('other target groups - please specify')

    # --> Geographic activities - High impact interventions
    elimination_of_mother_child_transmission = models.BooleanField('elimination of mother-to-child transmission (eMTCT)')
    condom_programming = models.BooleanField()
    voluntary_medical_male_circumcision = models.BooleanField('voluntary medical male circumcision (VMMC) ')
    hiv_counselling_testing = models.BooleanField('HIV counselling and testing (HCT)')
    social_behaviour_change = models.BooleanField('social and behaviour change communication')
    anti_retroviral_treatment = models.BooleanField('treatment through provision of Anti-Retroviral Treatment (ART)')

    # --> Geographic activities - Critical enablers
    gender_equality_empowerment = models.BooleanField('gender equality and empowerment')
    laws_legal_policies_practices = models.BooleanField('laws, legal policies and practices')
    leadership_commitment_good_governance = models.BooleanField('leadership commitment and good governance')
    resource_mobilization_sustainable_financing = models.BooleanField('resource mobilization and sustainable financing')

    # --> Geographic activities - Synergies with development sectors
    post_exposure_prophylaxis = models.BooleanField('post exposure prophylaxis (PEP)')
    blood_safety = models.BooleanField('poverty alleviation and livelihoods')
    poverty_alleviation_livelihoods = models.BooleanField('food and nutrition security')
    food_nutrition_security = models.BooleanField('food and nutrition security')
    mainstreaming_hiv_into_capital_projects = models.BooleanField()

    # --> Funding sources
    funder_organization = models.CharField(max_length=100)
    funder_support_type = models.CharField(max_length=100, choices=ORGANIZATION_TYPE_LIST, default='N/A')
    amount = models.IntegerField()
    comment = models.TextField()

    # --> Target groups and prevention messages
    condom_use = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    mc_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    mcp_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    pmtct_promotion = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    vct_hct_promotion = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    pep_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    sti_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    tb_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    gbv_information = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    social_norms = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    message_other = models.CharField(max_length=100, choices=ORGANIZATION_TARGET_LIST, default='N/A')
    # message_other = forms.ChoiceField(choices=ORGANIZATION_TARGET_LIST)

# HIV ACTIVITIES ORGANIZATION PARTICIPATES IN FORM
# *************************************************

# --> Social behaviour change communication
class ActivityReportForm(models.Model):

    IEC_distributed_books_num = models.IntegerField('books distributed', default=0)
    IEC_distributed_brochures_num = models.IntegerField('brochures distributed', default=0)
    IEC_distributed_posters_num = models.IntegerField('posters distributed', default=0)
    IEC_distributed_t_shirts_num = models.IntegerField('t shirts distributed', default=0)
    IEC_distributed_tv_spots_num = models.IntegerField('tv spots distributed', default=0)
    IEC_distributed_radio_spots_num = models.IntegerField('radio spots distributed', default=0)
    IEC_distributed_e_spots_num = models.IntegerField('e spots distributed', default=0)
    IEC_distributed_billboards_num = models.IntegerField('billboards distributed', default=0)
    IEC_distributed_drama_num = models.IntegerField('drama distributed', default=0)
    IEC_distributed_other_num = models.IntegerField('Other distributed', default=0)

    localized_books = models.BooleanField()
    localized_brochures = models.BooleanField()
    localized_posters = models.BooleanField()
    localized_t_shirts = models.BooleanField()
    localized_tv_spots = models.BooleanField()
    localized_radio_spots = models.BooleanField()
    localized_e_spots = models.BooleanField()
    localized_billboards = models.BooleanField()
    localized_drama = models.BooleanField()
    localized_other = models.BooleanField()

    # --> Social behaviour change communication for key populations
    # in_school
    adolescents_female_10_14 = models.IntegerField('female adolescents of ages 10 to 14', default=0)
    adolescents_female_15_19 = models.IntegerField('female adolescents of ages 15 to 19', default=0)
    adolescents_female_20_24 = models.IntegerField('female adolescents of ages 20 to 24', default=0)

    adolescents_male_10_14 = models.IntegerField('male adolescents of ages 10 to 14', default=0)
    adolescents_male_15_19 = models.IntegerField('male adolescents of ages 15 to 19', default=0)
    adolescents_male_20_24 = models.IntegerField('male adolescents of ages 20 to 24', default=0)
 
    # out_school
    out_school_female_10_14 = models.IntegerField('out of school females of ages 10 to 14', default=0)
    out_school_female_15_19 = models.IntegerField('out of school females of ages 15 to 19', default=0)
    out_school_female_20_24 = models.IntegerField('out of school females of ages 20 to 24', default=0)

    out_school_male_10_14 = models.IntegerField('out of school males of ages 10 to 14', default=0)
    out_school_male_15_19 = models.IntegerField('out of school males of ages 15 to 19', default=0)
    out_school_male_20_24 = models.IntegerField('out of school males of ages 20 to 24', default=0)

    # sex_workers
    sex_workers_female_num = models.IntegerField('female sex workers reached', default=0)
    sex_workers_male_num = models.IntegerField('male sex workers reached', default=0)

    # inmates
    inmates_female_num = models.IntegerField('female inmates reached', default=0)
    inmates_male_num = models.IntegerField('male inmates reached', default=0)

    # correctional facility staff
    correctional_staff_female_num = models.IntegerField('female correctional facility staff reached', 
        default=0)
    correctional_staff_male_num = models.IntegerField('male correctional facility staff reached', 
        default=0)

    # persons with disabilty
    pwd_female_num = models.IntegerField('female persons with disabilities reached', default=0)
    pwd_male_num = models.IntegerField('male persons with disabilities reached', default=0)

    # mobile workers
    mobile_workers_female_num = models.IntegerField('female mobile workers reached', default=0)
    mobile_workers_male_num = models.IntegerField('male mobile workers reached', default=0)

    # men who have sex with men
    men_with_men = models.IntegerField('men who have sex with men (MSM) reached', default=0)

    # Condom programming
    condom_dist_point_num = models.IntegerField('number of distribution points', default=0)
    female_condom_distributed_num = models.IntegerField('female condoms distributed', default=0)
    male_condom_distributed_num = models.IntegerField('male condoms distributed', default=0)

    # Crtical enablers
    accessed_pep_female_num = models.IntegerField('females who experienced physical or \
        sexual violence, and accessed Post Exposure Prophylaxis (PEP)', default=0)
    accessed_pep_male_num = models.IntegerField('males who experienced physical or sexual \
        violence, and accessed Post Exposure Prophylaxis (PEP)', default=0)

    # Synergies with other development sectors
    employees_reached_female_num = models.IntegerField('female employees reached through \
        workplace programmes', default=0)
    employees_reached_male_num = models.IntegerField('male employees reached through workplace \
        programmes', default=0)

    # Community health systems
    plhiv_female_num = models.IntegerField('female persons living with HIV (PLHIV) currently \
        enrolled in active groups', default=0)
    plhiv_male_num = models.IntegerField('male persons living with HIV (PLHIV) currently \
        enrolled in active groups', default=0)

    ovc_female_num = models.IntegerField('female vulnerable people', default=0)
    ovc_male_num = models.IntegerField('male vulnerable people', default=0)
    ovc_care_support_0_9 = models.IntegerField('vunerable people of ages 0 to 9', default=0)
    ovc_care_support_10_14 = models.IntegerField('vunerable people of ages 10 to 14', default=0)
    ovc_care_support_15_19 = models.IntegerField('vunerable people of ages 15 to 19', default=0)
    ovc_care_support_20_24 = models.IntegerField('vunerable people of ages 20 to 24', default=0)
    ovc_care_support_25_plus = models.IntegerField('vunerable people of ages 25 and above', default=0)

    # Types of care and support organization provides
    food_and_nutrition = models.BooleanField()
    shelter_and_care = models.BooleanField()
    protection_and_legal_aid = models.BooleanField()
    healthcare = models.BooleanField()
    psychosocial = models.BooleanField()
    social_support = models.BooleanField()
    spiritual_support = models.BooleanField()
    education_and_vocational_training = models.BooleanField()
    economic_strengthening = models.BooleanField()

    # Monitoring and Evaluation
    nacmis = models.BooleanField('NAC-MIS')
    hmis = models.BooleanField('HMIS')
    datim = models.BooleanField('DATIM')
    internal_system = models.BooleanField('Internal system')
    systems_other = models.BooleanField('Other')