import requests
import json

null = None
data = '''
{ "CrimeDateTime": "2018", "Description" : "ROBBERY", "Gender": "M", "District": "NORTHERN"}
'''
json.loads(data)

#test 1
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 1: Pass")
else:
    print("Test 1: Fail")

#test 2
data = '''
{ "CrimeDateTime": "2018", "Description" : "ROBBERY", "Gender": "M", "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 2: Pass")
else:
    print("Test 2: Fail")
    
#test 3
data = '''
{ "CrimeDateTime": "2018", "Description" : "ROBBERY", "Gender": null, "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 3: Pass")
else:
    print("Test 3: Fail")

#test 4
data = '''
{ "CrimeDateTime": "2018", "Description" : null, "Gender": null, "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 4: Pass")
else:
    print("Test 4: Fail")
    
#test 5
data = '''
{ "CrimeDateTime": null, "Description" : null, "Gender": null, "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 5: Pass")
else:
    print("Test 5: Fail")
    
#test 6
data = '''
{ "CrimeDateTime": null, "Description" : "ROBBERY", "Gender": null, "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 6: Pass")
else:
    print("Test 6: Fail")
    
#test 7
data = '''
{ "CrimeDateTime": null, "Description" : "ROBBERY", "Gender": "M", "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 7: Pass")
else:
    print("Test 7: Fail")
    
#test 8
data = '''
{ "CrimeDateTime": null, "Description" : "ROBBERY", "Gender": "M", "District": "NORTHERN"}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 8: Pass")
else:
    print("Test 8: Fail")
    
#test 9
data = '''
{ "CrimeDateTime": null, "Description" : null, "Gender": "M", "District": "NORTHERN"}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 9: Pass")
else:
    print("Test 9: Fail")
    
#test 10
data = '''
{ "CrimeDateTime": null, "Description" : null, "Gender": null, "District": "NORTHERN"}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 10: Pass")
else:
    print("Test 10: Fail")
    
#test 11
data = '''
{ "CrimeDateTime": null, "Description" : null, "Gender": "M", "District": null}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 11: Pass")
else:
    print("Test 11: Fail")
    
#test 12
data = '''
{ "CrimeDateTime": null, "Description" : "ROBBERY", "Gender": null, "District": "NORTHERN"}
'''
json.loads(data)
r = requests.put('http://localhost:5000/getfilter/endpoint', data)
if r.status_code == 200:
    print("Test 12: Pass")
else:
    print("Test 12: Fail")
    
#test 13
r = requests.get("http://localhost:5000/crime2018")
if r.status_code == 200:
    print("Test 13: Pass")
else:
    print("Test 13: Fail")
    
#test 14
r = requests.get("http://localhost:5000/crime2019")
if r.status_code == 200:
    print("Test 14: Pass")
else:
    print("Test 14: Fail")
    
#test 15
r = requests.get("http://localhost:5000/crime2020")
if r.status_code == 200:
    print("Test 15: Pass")
else:
    print("Test 15: Fail")
    
#test 16
r = requests.get("http://localhost:5000/crime2021")
if r.status_code == 200:
    print("Test 16: Pass")
else:
    print("Test 16: Fail")
    
#test 17
r = requests.get("http://localhost:5000/crime2022")
if r.status_code == 200:
    print("Test 17: Pass")
else:
    print("Test 17: Fail")
    
