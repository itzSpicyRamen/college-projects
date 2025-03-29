from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysqldb import MySQL
import pandas as pd
import mysql.connector
import os
import json
#added some will delete not used
from flask import Flask;
from flask import jsonify, request;
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
import collections


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="cmsc447project"
)
mycursor = mydb.cursor()

app = Flask(__name__)
cors = CORS(app)

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
#added under 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/cmsc447project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)
#added under 
db = SQLAlchemy(app)
ma  = Marshmallow(app)

#---------------------------------------------------------------------------------------
class CovidCases(db.Model):
    __tablename__ = 'covidcases'
    __table_args__ = {'extend_existing': True} 
    OBJECTID = db.Column(db.String(250), primary_key=True)
    DATE = db.Column(db.String(100))
    Baltimore = db.Column(db.String(100))
    Baltimore_CITY = db.Column(db.String(100))

    def __init__(self, OBJECTID, DATE, Baltimore, Baltimore_CITY):
        self.OBJECTID  = OBJECTID
        self.DATE = DATE
        self.Baltimore = Baltimore
        self.Baltimore_CITY = Baltimore_CITY
        
class CovidCaseSchema(ma.Schema):
    class Meta: 
        fields = ('OBJECTID', 'DATE', 'Baltimore', 'Baltimore_CITY')

covidcase_schema = CovidCaseSchema()
covidcases_schema = CovidCaseSchema(many=True)

@app.route('/covidcases', methods = ['GET'])
def get_covidcases():
    all_covidcases = CovidCases.query.all()
    results = covidcases_schema.dump(all_covidcases)
    return jsonify(results)

#---------------------------------------------------------------------------------------
class CovidDeaths(db.Model):
    __tablename__ = 'coviddeaths'
    __table_args__ = {'extend_existing': True} 
    OBJECTID = db.Column(db.String(250), primary_key=True)
    DATE = db.Column(db.String(100))
    Baltimore = db.Column(db.String(100))
    Baltimore_CITY = db.Column(db.String(100))

    def __init__(self, OBJECTID, DATE, Baltimore, Baltimore_CITY):
        self.OBJECTID  = OBJECTID
        self.DATE = DATE
        self.Baltimore = Baltimore
        self.Baltimore_CITY = Baltimore_CITY
        
class CovidDeathSchema(ma.Schema):
    class Meta: 
        fields = ('OBJECTID', 'DATE', 'Baltimore', 'Baltimore_CITY')

coviddeath_schema = CovidDeathSchema()
coviddeaths_schema = CovidDeathSchema(many=True)

@app.route('/coviddeaths', methods = ['GET'])
def get_coviddeaths():
    all_coviddeaths = CovidDeaths.query.all()
    results = coviddeaths_schema.dump(all_coviddeaths)
    return jsonify(results)



#---------------------------------------------------------------------------------------
class CrimeData(db.Model):
    __tablename__ = 'crimedata'
    __table_args__ = {'extend_existing': True} 
    X = db.Column(db.String(250))
    Y = db.Column(db.String(100))
    RowID = db.Column(db.String(100), primary_key=True)
    CrimeDateTime = db.Column(db.String(100))
    CrimeCode = db.Column(db.DateTime())
    Location= db.Column(db.String(100))
    Description= db.Column(db.String(100))
    Inside_Outside= db.Column(db.String(100))
    Weapon= db.Column(db.String(100))
    Post= db.Column(db.String(100))
    Gender= db.Column(db.String(100))
    Age= db.Column(db.String(100))
    Race = db.Column(db.String(100))
    Ethnicity= db.Column(db.String(100))
    District= db.Column(db.String(100))
    Neighborhood= db.Column(db.String(100))
    Latitude= db.Column(db.String(100))
    Longitude= db.Column(db.String(100))
    GeoLocation= db.Column(db.String(100))
    Premise= db.Column(db.String(100))
    VRIName= db.Column(db.String(100))
    Total_Incidents= db.Column(db.String(100))
    Shape= db.Column(db.String(100))
    
    

    def __init__(self, X, Y, RowID, CrimeDateTime, CrimeCode, Location, Description, Inside_Outside, Weapon,
                Post, Gender, Age, Race, Ethnicity, District, Neighborhood, Latitude,
                Longitude, GeoLocation, Premise, VRIName, Total_Incidents, Shape):
        self.X  = X
        self.Y = Y
        self.RowID = RowID
        self.CrimeDateTime = CrimeDateTime
        self.CrimeCode = CrimeCode
        self.Location = Location
        self.Description = Description
        self.Inside_Outside = Inside_Outside
        self.Weapon = Weapon
        self.Post = Post
        self.Gender = Gender
        self.Age = Age 
        self.Race = Race
        self.Ethnicity = Ethnicity
        self.District = District
        self.Neighborhood = Neighborhood
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.GeoLocation = GeoLocation
        self.Premise = Premise
        self.VRIName =VRIName
        self.Total_Incidents = Total_Incidents
        self.Shape = Shape 
        
class CrimeDataSchema(ma.Schema):
    class Meta: 
        fields = ('X','Y', 'RowID', 'CrimeDateTime', 'CrimeCode', 'Location', 'Description', 'Inside_Outside', 'Weapon',
                'Post', 'Gender', 'Age', 'Race', 'Ethnicity', 'District', 'Neighborhood', 'Latitude',
                'Longitude', 'GeoLocation', 'Premise', 'VRIName', 'Total_Incidents', 'Shape')

crimedata_schema = CrimeDataSchema()
crimedatas_schema = CrimeDataSchema(many=True)





@app.route('/crimedata', methods = ['GET'])
def get_crimedata():
    all_crimedatas = CrimeData.query.all()
    results = crimedatas_schema.dump(all_crimedatas)
    return jsonify(results)

#---------------------------------------------------------------------------------------
@app.route('/getfilter/endpoint', methods = ['PUT'])
def post_filterBySelection():
    final_command = ""
    string_command = "select * from `crimedata` where "
    final_command += string_command
    str2018 = "`CrimeDateTime` between '2018/01/01 13:40:00+00' and '2018/12/31 14:50:00+00' "
    str2019 = "`CrimeDateTime` between '2019/01/01 13:40:00+00' and '2019/12/31 14:50:00+00' "
    str2020 = "`CrimeDateTime` between '2020/01/01 13:40:00+00' and '2020/12/31 14:50:00+00' "
    str2021 = "`CrimeDateTime` between '2021/01/01 13:40:00+00' and '2021/12/31 14:50:00+00' "
    str2022 = "`CrimeDateTime` between '2022/01/01 13:40:00+00' and '2022/12/31 14:50:00+00' "
    
    input_json = request.get_json(force = True)
    
    data1 = json.dumps(input_json)
    
    row = json.loads(data1)
    
    print(row)
    
    if row['Gender'] == None and row['CrimeDateTime'] == None and row['District'] == None and row['Description'] == None:
        final_command = "select * from `crimedata`;"
    else:    
        if row['CrimeDateTime'] != None:
            if row['CrimeDateTime'] == "2018":
                final_command = final_command + str2018
            elif row['CrimeDateTime'] == "2019":
                final_command = final_command + str2019
            elif row['CrimeDateTime'] == "2020":
                final_command = final_command + str2020
            elif row['CrimeDateTime'] == "2021":
                final_command = final_command + str2021
            else:
                final_command = final_command + str2022
                    
        if row['Description'] != None and row['CrimeDateTime'] != None:
            final_command = final_command + "and `Description` = '" + row['Description'] + "' "
        elif row['Description'] != None and row['CrimeDateTime'] == None:
            final_command = final_command + "`Description` = '" + row['Description'] + "' "
        
                
        if row['Gender'] != None and row['CrimeDateTime'] != None and row['Description'] == None:
            final_command = final_command + "and `Gender` = '" + row['Gender'] + "' "
        elif row['Gender'] != None and row['CrimeDateTime'] != None and row['Description'] != None:
            final_command = final_command + "and `Gender` = '" + row['Gender'] + "' "
        elif row['Gender'] != None and row['CrimeDateTime'] == None and row['Description'] != None:
            final_command = final_command + "and `Gender` = '" + row['Gender'] + "' "
        elif row['Gender'] != None:
            final_command = final_command + "`Gender` = '" + row['Gender'] + "' "
                
        if row['District'] != None and row['CrimeDateTime'] != None and row['Gender'] == None and row['Description'] == None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None and row['CrimeDateTime'] != None and row['Gender'] != None and row['Description'] == None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None and row['CrimeDateTime'] != None and row['Gender'] == None and row['Description'] != None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None and row['CrimeDateTime'] != None and row['Gender'] != None and row['Description'] != None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None and row['CrimeDateTime'] == None and row['Gender'] == None and row['Description'] != None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None and row['CrimeDateTime'] == None and row['Gender'] != None and row['Description'] == None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None and row['CrimeDateTime'] == None and row['Gender'] != None and row['Description'] != None:
            final_command = final_command + "and `District` = '" + row['District'] + "' "
        elif row['District'] != None:
            final_command = final_command + "`District` = '" + row['District'] + "' "
        final_command  = final_command + ";"
        
        object_list = []
        print(final_command)
        mycursor.execute(final_command)
        myresult = mycursor.fetchall()
        for rows in myresult:
            d = collections.OrderedDict()
            #d["X"] = rows[0]
            #d["Y"] = rows[1]
            #d["RowID"] = rows[2]
            #d["CrimeDateTime"] = rows[3]
            #d["CrimeCode"] = rows[4]
            #d["Location"] = rows[5]
            #d["Description"] = rows[6]
            #d["Inside_Outside"] =rows[7]
            #d["Weapon"] = rows[8]
            #d["Post"] = rows[9]
            #d["Gender"] = rows[10]
            #d["Age"] = rows[11]
            #d["Race"] = rows[12]
            #d["Ethnicity"] = rows[13]
            #d["District"] = rows[14]
            #d["Neighborhood"] = rows[15]
            d["Latitude"] = rows[16]
            d["Longitude"] = rows[17]
            #d["GeoLocation"] = rows[18]
            #d["Premise"] = rows[19]
            #d["VRIName"] = rows[20]
            #d["Total_Incidents"] = rows[21]
            #d["Shape"] = rows[22]
            object_list.append(d)
            
        results = json.dumps(object_list)
        result1 = json.loads(results)
        print(type(result1))
        #returns json now 
        return result1
    
    object_list = []    
    mycursor.execute(final_command)
    myresult = mycursor.fetchall()
    for rows in myresult:
            d = collections.OrderedDict()
            #d["X"] = rows[0]
            #d["Y"] = rows[1]
            #d["RowID"] = rows[2]
            #d["CrimeDateTime"] = rows[3]
            #d["CrimeCode"] = rows[4]
            #d["Location"] = rows[5]
            #d["Description"] = rows[6]
            #d["Inside_Outside"] =rows[7]
            #d["Weapon"] = rows[8]
            #d["Post"] = rows[9]
            #d["Gender"] = rows[10]
            #d["Age"] = rows[11]
            #d["Race"] = rows[12]
            #d["Ethnicity"] = rows[13]
            #d["District"] = rows[14]
            #d["Neighborhood"] = rows[15]
            d["Latitude"] = rows[16]
            d["Longitude"] = rows[17]
            #d["GeoLocation"] = rows[18]
            #d["Premise"] = rows[19]
            #d["VRIName"] = rows[20]
            #d["Total_Incidents"] = rows[21]
            #d["Shape"] = rows[22]
            object_list.append(d)
    
    results = json.dumps(object_list)
    result1 = json.loads(results)
    return result1
    
        


#---------------------------------------------------------------------------------------
#filters only data for 2018
@app.route('/crime2018', methods = ['GET'])
def get_crimedata2018():
    first_date = '2018/01/01 13:40:00+00'
    last_date = '2018/12/31 13:40:00+00'
    transactions = CrimeData.query.filter(CrimeData.CrimeDateTime.between(first_date, last_date)).all()
    results = crimedatas_schema.dump(transactions)
    return jsonify(results)

#filters only data for 2019
@app.route('/crime2019', methods = ['GET'])
def get_crimedata2019():
    first_date = '2019/01/01 13:40:00+00'
    last_date = '2019/12/31 13:40:00+00'
    transactions = CrimeData.query.filter(CrimeData.CrimeDateTime.between(first_date, last_date)).all()
    results = crimedatas_schema.dump(transactions)
    return jsonify(results)

#filters only data for 2020
@app.route('/crime2020', methods = ['GET'])
def get_crimedata2020():
    first_date = '2020/01/01 13:40:00+00'
    last_date = '2020/12/31 13:40:00+00'
    transactions = CrimeData.query.filter(CrimeData.CrimeDateTime.between(first_date, last_date)).all()
    results = crimedatas_schema.dump(transactions)
    return jsonify(results)

#filters only data for 2021
@app.route('/crime2021', methods = ['GET'])
def get_crimedata2021():
    first_date = '2021/01/01 13:40:00+00'
    last_date = '2021/12/31 13:40:00+00'
    transactions = CrimeData.query.filter(CrimeData.CrimeDateTime.between(first_date, last_date)).all()
    results = crimedatas_schema.dump(transactions)
    return jsonify(results)

#filters only data for 2020
@app.route('/crime2022', methods = ['GET'])
def get_crimedata2022():
    first_date = '2022/01/01 13:40:00+00'
    last_date = '2022/12/31 13:40:00+00'
    transactions = CrimeData.query.filter(CrimeData.CrimeDateTime.between(first_date, last_date)).all()
    results = crimedatas_schema.dump(transactions)
    return jsonify(results)

#signin route
@app.route('/signin', methods = ['PUT'])
def signin_user():
    content = request.get_json(force = True)
    username = content['username'][0]
    password = content['password'][0]
    if((username == 'admin') and (password == 'admin')):
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}

#----------------------------------------------------------------------------------------
@app.route('/', methods =["GET", "POST"])
def defaultpage():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def uploadFiles():
    # get the uploaded file
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file
    return redirect(url_for('index'))

#-------------------------------------------------------------------------------------------

#Crime Routes
class CrimeCases(db.Model):
  __tablename__ = 'crimedata'
  __table_args__ = {'extend_existing': True} 
  X = db.Column(db.Integer)
  Y = db.Column(db.Integer)
  RowID = db.Column(db.Integer, primary_key=True)
  CrimeDateTime = db.Column(db.Integer)
  CrimeCode = db.Column(db.Integer)
  Location = db.Column(db.String(250))
  
  def __init__(self, X, Y, RowID, CrimeDateTime, CrimeCode, Location):
    self.X = X
    self.Y = Y
    self.RowId = RowID
    self.CrimeDateTime = CrimeDateTime
    self.CrimeCode = CrimeCode
    self.Location = Location
    
class CrimeCasesSchema(ma.Schema):
  class Meta:
    fields = ('X', 'Y', 'RowID', 'CrimeDateTime', 'CrimeCode', 'Location')
    
crimecase_schema = CrimeCasesSchema()
crimecases_schema = CrimeCasesSchema(many=True)

@app.route('/getcrimecases',methods = ['GET'])
def getCrimeCases():
  all_crimecases= CrimeCases.query.all()
  results = crimecases_schema.dump(all_crimecases)
  return jsonify(results)


# @app.route('/getcrimecase/<id>', methods =['GET'])
# def getCrimeCase(id):
#   crimecase = CrimeCases.query.get(id)
#   RowID = request.json['RowID']
#   CrimeDateTime = request.json['CrimeDateTime']
#   CrimeCode = request.json['CrimeCode']
#   Location = request.json['Location']
#   crimecase.RowID = RowID
#   crimecase.CrimeDateTime = CrimeDateTime
#   crimecase.CrimeCode = CrimeCode
#   crimecase.Location = Location
#   db.session.commit()
#   return crimecase_schema.jsonify(crimecase)
  
 #-----------------------------------------------------------------------------------
 
  
def parseCSV_covidcases(filePath):
    mycursor.execute("CREATE TABLE COVIDcases (OBJECTID VARCHAR(255), DATE VARCHAR(255), Baltimore VARCHAR(255), Baltimore_CITY VARCHAR(255))")
    # CVS Column Names
    col_names = ['OBJECTID','DATE', 'Allegany', 'Anne_Arundel', 'Baltimore', 'Baltimore_CITY', 'Calvert', 'Caroline',
                 'Carroll', 'Cecil', 'Charles', 'Dorcheste', 'Fredick', 'Garret', 'Harford','Howard', 'Kent', 'Montgomery',
                 'Prince_Georges', 'Queen_Annes', 'Somerset', 'St_Marys', 'talbot', 'Washington', 'Wicomico', 'Worcester', 'Unknown']
    # Use Pandas to parse the CSV file
    col_needed = ['OBJECTID', 'DATE', 'Baltimore', 'Baltimore_CITY']
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    csvData = csvData.where((pd.notnull(csvData)), None)
    csvDataParse = csvData.iloc[1:, [0,1,4,5]]
    
    # Loop through the Rows
    for i,row in csvDataParse.iterrows():
        sql = "INSERT INTO COVIDcases (OBJECTID, DATE, Baltimore, Baltimore_CITY) VALUES (%s, %s, %s, %s)"
        value = (row['OBJECTID'],row['DATE'],row['Baltimore'],row['Baltimore_CITY'])
        mycursor.execute(sql, value)
        mydb.commit()

def parseCSV_coviddeaths(filePath):
    mycursor.execute("CREATE TABLE COVIDdeaths (OBJECTID VARCHAR(255), DATE VARCHAR(255), Baltimore VARCHAR(255), Baltimore_CITY VARCHAR(255))")
    # CVS Column Names
    col_names = ['OBJECTID','DATE', 'Allegany', 'Anne_Arundel', 'Baltimore', 'Baltimore_CITY', 'Calvert', 'Caroline',
                 'Carroll', 'Cecil', 'Charles', 'Dorcheste', 'Fredick', 'Garret', 'Harford','Howard', 'Kent', 'Montgomery',
                 'Prince_Georges', 'Queen_Annes', 'Somerset', 'St_Marys', 'talbot', 'Washington', 'Wicomico', 'Worcester', 'Unknown']
    # Use Pandas to parse the CSV file
    col_needed = ['OBJECTID', 'DATE', 'Baltimore', 'Baltimore_CITY']
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    csvData = csvData.where((pd.notnull(csvData)), None)
    csvDataParse = csvData.iloc[1:, [0,1,4,5]]
    
    # Loop through the Rows
    for i,row in csvDataParse.iterrows():
        sql = "INSERT INTO COVIDdeaths (OBJECTID, DATE, Baltimore, Baltimore_CITY) VALUES (%s, %s, %s, %s)"
        value = (row['OBJECTID'],row['DATE'],row['Baltimore'],row['Baltimore_CITY'])
        mycursor.execute(sql, value)
        mydb.commit()

def parseCSV_crime(filePath):
    mycursor.execute("CREATE TABLE crimedata (X VARCHAR(255), Y VARCHAR(255), RowID VARCHAR(255), CrimeDateTime VARCHAR(255), CrimeCode VARCHAR(255), Location VARCHAR(255), \
                    Description VARCHAR(255), Inside_Outside VARCHAR(255), Weapon VARCHAR(255), Post VARCHAR(255), Gender VARCHAR(255), Age VARCHAR(255), \
                    Race VARCHAR(255), Ethnicity VARCHAR(255), District VARCHAR(255), Neighborhood VARCHAR(255), Latitude VARCHAR(255), Longitude VARCHAR(255), \
                    GeoLocation VARCHAR(255), Premise VARCHAR(255), VRIName VARCHAR(255), Total_Incidents VARCHAR(255), Shape VARCHAR(255))")
    # CVS Column Names
    col_names = ['X','Y', 'RowID', 'CrimeDateTime', 'CrimeCode', 'Location', 'Description', 'Inside_Outside', 'Weapon',
                'Post', 'Gender', 'Age', 'Race', 'Ethnicity', 'District', 'Neighborhood', 'Latitude',
                'Longitude', 'GeoLocation', 'Premise', 'VRIName', 'Total_Incidents', 'Shape']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    csvData = csvData.where((pd.notnull(csvData)), None)
    
    # Loop through the Rows
    for i,row in csvData.iterrows():
            sql = "INSERT INTO crimedata (X, Y, RowID, CrimeDateTime, CrimeCode, Location, Description, Inside_Outside, Weapon,\
                    Post, Gender, Age, Race, Ethnicity, District, Neighborhood, Latitude, Longitude, GeoLocation,\
                    Premise, VRIName, Total_Incidents, Shape) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value = (row['X'],row['Y'],row['RowID'],row['CrimeDateTime'],row['CrimeCode'],row['Location'], row['Description'],row['Inside_Outside'],row['Weapon'],row['Post'],
                    row['Gender'],row['Age'],row['Race'],row['Ethnicity'], row['District'],row['Neighborhood'],row['Latitude'],row['Longitude'],
                    row['GeoLocation'],row['Premise'],row['VRIName'],row['Total_Incidents'],row['Shape'])
            mycursor.execute(sql, value)
            mydb.commit()


def main():
    #parseCSV_crime(r"C:\Users\opeye\Downloads\Part_1_Crime_Data_.csv")
    #parseCSV_covidcases(r"C:\Users\opeye\Downloads\MDCOVID19_CasesByCounty.csv")
    #parseCSV_coviddeaths(r"C:\Users\opeye\Downloads\MDCOVID19_ConfirmedDeathsByCounty.csv")
    app.run(host='localhost', port=5000)
    #ADDED 

if __name__=="__main__":
    main()
    
