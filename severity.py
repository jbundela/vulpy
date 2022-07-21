import json


file = open('banditreport.json',)
file1 = open('DependencyCheckReport.json',)

data = json.load(file)
data2 = json.load(file1)


print('*****************************************************************')
print('Bandit Python Code Analysis')
print('*****************************************************************')

for i in data['results']:
    if i['issue_severity'] == 'MEDIUM':
        print("ISSUE SEVERITY Vulnerability = MEDIUM")
        print("1")
    elif i['issue_severity'] == 'HIGH':
        print("0")
    else:
        print("No Vulnerabilities Found!")

    if i['issue_confidence'] == 'HIGH':
        print("ISSUE CONFIDENCE Vulnerability = HIGH")
        print("1")
    elif i['issue_confidence'] == 'MEDIUM':
        print("0")
    else:
        print("No Vulnerabilities Found!")



print('*****************************************************************')
print('OWASP Dependency Checker')
print('*****************************************************************')


for i in data2['dependencies']:
    if (i['evidenceCollected']['productEvidence'][0]['confidence']) == 'HIGHEST':
        print("Vulnerability = HIGHEST")
        print("1")
    elif (i['evidenceCollected']['productEvidence'][0]['confidence']) == 'HIGH':
        print("Vulnerability = HIGH")
        print("1")
    elif(i['evidenceCollected']['productEvidence'][0]['confidence']) == 'MEDIUM':
        print("0")
    else:
        print("No Vulnerabilities Found!")

    if (i['evidenceCollected']['versionEvidence'][0]['confidence']) == 'HIGHEST':
        print("Vulnerability = HIGHEST")
        print("1")
    elif (i['evidenceCollected']['versionEvidence'][0]['confidence']) == 'HIGH':
        print("Vulnerability = HIGH")
        print("1")
    elif(i['evidenceCollected']['versionEvidence'][0]['confidence']) == 'MEDIUM':
        print("0")
    else:
        print("No Vulnerabilities Found!")


