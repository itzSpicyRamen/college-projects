import requests
import json

URL2018 = "http://localhost:5000/crime2018"
URL2019 = "http://localhost:5000/crime2019"
URL2020 = "http://localhost:5000/crime2020"
URL2021 = "http://localhost:5000/crime2021"
URL2022 = "http://localhost:5000/crime2022"

response2018 = requests.get(URL2018) 
response2019 = requests.get(URL2019) 
response2020 = requests.get(URL2020) 
response2021 = requests.get(URL2021) 
response2022 = requests.get(URL2022)

crrimes2018 = [0,0,0,0,0,0,0,0,0,0,0,0]
crrimes2019 = [0,0,0,0,0,0,0,0,0,0,0,0]
crrimes2020 = [0,0,0,0,0,0,0,0,0,0,0,0]
crrimes2021 = [0,0,0,0,0,0,0,0,0,0,0,0]
crrimes2022 = [0,0,0,0,0,0,0,0,0,0,0,0]

def addToArray(array,date):
    if "/12/" in date:
        placeHolder=array[11]
        placeHolder+=1
        array[11]=placeHolder
    elif "/11/" in date:
        placeHolder=array[10]
        placeHolder+=1
        array[10]=placeHolder
    elif "/10/" in date:
        placeHolder=array[9]
        placeHolder+=1
        array[9]=placeHolder
    elif "/09/" in date:
        placeHolder=array[8]
        placeHolder+=1
        array[8]=placeHolder
    elif "/08/" in date:
        placeHolder=array[7]
        placeHolder+=1
        array[7]=placeHolder
    elif "/07/" in date:
        placeHolder=array[6]
        placeHolder+=1
        array[6]=placeHolder

    elif "/06/" in date:
        placeHolder=array[5]
        placeHolder+=1
        array[5]=placeHolder
    elif "/05/" in date:
        placeHolder=array[4]
        placeHolder+=1
        array[4]=placeHolder
    elif "/04/" in date:
        placeHolder=array[3]
        placeHolder+=1
        array[3]=placeHolder
    elif "/03/" in date:
        placeHolder=array[2]
        placeHolder+=1
        array[2]=placeHolder
    elif "/02/" in date:
        placeHolder=array[1]
        placeHolder+=1
        array[1]=placeHolder
    elif "/01/" in date:
        placeHolder=array[0]
        placeHolder+=1
        array[0]=placeHolder

column2018 = response2018.json()     
for row in column2018:
    data = row['CrimeDateTime']
    addToArray(crrimes2018,data)
    
column2019 = response2019.json()     
for row in column2019:
    data = row['CrimeDateTime']
    addToArray(crrimes2019,data)

column2020 = response2020.json()     
for row in column2020:
    data = row['CrimeDateTime']
    addToArray(crrimes2020,data)
    
column2021 = response2021.json()     
for row in column2021:
    data = row['CrimeDateTime']
    addToArray(crrimes2021,data)

column2022 = response2022.json()     
for row in column2022:
    data = row['CrimeDateTime']
    addToArray(crrimes2022,data)

def total(array):
    count=0
    for i in range(0,12):
        count+=array[i]
    print(count)
print("2022: ",crrimes2022)
print("2021: ",crrimes2021)
print("2020: ",crrimes2020)
print("2019: ",crrimes2019)
print("2018: ",crrimes2018)
total(crrimes2022)
total(crrimes2021)
total(crrimes2020)
total(crrimes2019)
total(crrimes2018)