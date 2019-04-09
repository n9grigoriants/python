import pprint
people = {}
people['Ford'] = {'name': 'Ford Prefect', 'gender': 'male', 'occupation': 'researcher', 'home planet': 'Betelgeyze 7'}
people['Arthur'] = {'name' : 'Arthur Dent', 'gender' : 'male', 'occupation' : 'making sandwiches', 'home planet' : 'Earth' }
people['Grisha'] = {'name' : 'Grisha McMillan', 'gender' : 'male', 'occupation' : 'mathematician', 'home planet' : 'Earth' }
people['Marvin'] = {'name' : 'Marvin', 'gender' : 'unknown', 'occupation' : 'paranoid robot', 'home planet' : 'unknown' }
pprint.pprint(people)
print(people['Arthur']['occupation'])
#pprint pretty print