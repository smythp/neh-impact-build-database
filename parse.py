import sys
import sqlite3
import xml.etree.ElementTree as ET

# pull in XML file passed as argument when running the script
tree = ET.parse(sys.argv[1])


root = tree.getroot()


fields = (
    'ApplicantType',
    'Institution',
    'OrganizationType',
    'InstCity',
    'InstState',
    'InstPostalCode',
    'InstCountry',
    'CouncilDate',
    'YearAwarded',
    'ProjectTitle',
    'Program',
    'Division',
    'ApprovedOutright',
    'ApprovedMatching',
    'AwardOutright',
    'AwardMatching',
    'OriginalAmount',
    'BeginGrant',
    'EndGrant',
    'ProjectDesc',
    'ToSupport',
    'PrimaryDiscipline',
    'SupplementCount',
    'ParticipantCount',
    'DisciplineCount'
    )

explicit_fields = ''

for field in fields:
    explicit_fields += field
    explicit_fields += ', '

explicit_fields += 'ShortPostal'
# explicit_fields = explicit_fields[:-2]    

conn = sqlite3.connect('grants.db')
cur = conn.cursor()


for grant in root:
    # for field in fields:
    #     print(grant.find(field).text)
    data_list = []
    for field in fields:

        data_list.append(grant.find(field).text)

        # add 5-digit postal code as "ShortPostal"

    if data_list[5]:
        long_zip = data_list[5][:5]
    
        # print(type(long_zip))
    
        data_list.append(long_zip)
        # print(data_list)
    else:
        data_list.append(None)
        
    cur.execute("INSERT INTO grants (%s) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);" % explicit_fields, tuple(data_list))

conn.commit()    
conn.close()



    
# for grant in root:
#     state = grant.find('InstState').text
#     matching = float(grant.find('AwardMatching').text)
#     outright = float(grant.find('AwardOutright').text)
#     award = matching + outright


#     if state == 'CA' or state == 'ca':
#         # print(state)
#         print(matching)
#         print(outright)
#         print(award)
#         print()
#         ca_total += award
#         ca_total_matching += matching
#         ca_total_outright += outright

# print("Total all", ca_total)
# print("Total matching", ca_total_matching)
# print("Total outright", ca_total_outright)
