import requests
import json
import datetime  
import itertools
import random


url = ' http://68.183.246.238:8080/cdss/rest/ehr/rule/DHIndia/execute'

current_time = datetime.datetime.now()  
print ("Report Generated at :",current_time)  


data =  {
 "age": "65",
"conditions": [
   {
     "conditionCode": "73211009",
     "conditionName": "Diabetes",
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    },
   {
     "conditionCode": "38341003",
     "conditionName": "Heart disease",
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
     },
   {
     "conditionCode": "38341003",
     "conditionName": "Hypertension",
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    },
   {
     "conditionCode": "38341003",
     "conditionName": "COPD",
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    },
   {
     "conditionCode": "38341003",
     "conditionName": "Kidney disease",
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
     }
 ],
 "exposure":  
   {
   "agentCode": "840533007",
   "agentName": "SARS-CoV-2",
   "confirmedCode": "at0029",
   "confirmedValue": "Present/Absent/Unknown",
   "type": "Contact with covid-19 patient in the last 14 days/Travel to COVID-19 hotspot in the last 14 days/Living in COVID-19 hotspot"              
 },
 "symptoms": [
   {
    "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",
    "symptomName": "Breathlessness",
    "symtomCode": "386661006"
   },
   {
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    "symptomName": "Sore throat",
   "symtomCode": "11833005"
   },
   {
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",
   "symptomName": "Fever",
   "symtomCode": "11833005"
   },
   {
    "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",
     "symptomName": "Cough",
   "symtomCode": "11833005"
   },
   {
   "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown", 
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",    "symptomName": "Dry Cough",
   "symtomCode": "11833005"
   },
   {
    "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown",
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",   "symptomName": "Muscle pain",
   "symtomCode": "11833005"
   },
   {
    "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown", 
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",   "symptomName": "Fatigue",
   "symtomCode": "11833005"
   },
   {
    "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown", 
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",   "symptomName": "Diarrhea",
   "symtomCode": "11833005"
   },
   {
    "presenceCode": "at0023/at0024,at0027",
    "presenceValue": "Present/Absent/Unknown", 
    "severity": "Mild/Moderate/Severe",
    "severityCode": "at0.2,at0.3,at0.4",   "symptomName": "Sneezing",
   "symtomCode": "11833005"
   }]                
}
presence = ["Present","Absent","Unknown"];
severity = ["Mild","Moderate","Severe"];
#create a file named data.txt in the file directory of the program the cases are store in this txt file
a=open("data.txt",'a')
a.write("| Breathlessness ||   Sore throat  ||    Fever       ||     Cough      ||    Dry Cough   ||   Muscle pain  ||    Fatigue     ||    Diarrhea    ||    Sneezing    |\n")
a.close()
#create all the possible combination of conditions
# where 0--->Present
# 1--->Absent
# 2--->unknown
conditionlist=list(itertools.product([0,1,2],repeat=5))   #all the possible combination of condtions are created here        
#create all the possible combination of sevirity
# where 0--->Mild
# 1--->Moderate
# 2--->severe
sysptomlist=list(itertools.product([0,1,2],repeat=9))
#shuffle the list to see all posible cases from[0 0 0 0 0 0 0 0 0 0] to[2 2 2 2 2 2 2 2 2]
random.shuffle(conditionlist)   #shuffle the cases to get all the cases faster
random.shuffle(sysptomlist)
count=0
countun=0
countl=0
countint=0
maincount=0
syscount=0
#loop through all the possible conditions
for i in  (conditionlist):# take a condition value for example [0 1 0 1 0] which means that COPD and Heart disesse is present rest absent      
  
  maincount=maincount+1
  for j,k in zip(range(len(i)),i):          #create a tuple of each element of condition list and the elements
    data['conditions'][j]['presenceValue'] = presence[k]    #chage the values in the json structure data by assigning the presence value to each condition
  #loop through all the possible symptoms for a condition
  for x in sysptomlist:#consider each element in sysptomlist that creates a combination of symptoms for [0 0 0 1 0 0 0 1] which means that diarreha and cough are present rest absent 
    syscount=syscount+1
    for i,k in zip(x,range(9)):    
      data['symptoms'][k]['presenceValue'] = presence[i]  # here we assign the values of the presence values from the sysptomlist
    list1=list()
    list2=list()
    #find the number of presence value of symptoms
    for i in range(len(x)):     #create two lists holding the position where the sysmptoms from the sysmptomlist is 0 which means collect all the places where the sysptom is present
      if x[i]==0:
        list1.append(i)
      else:
        list2.append(i)            # this list collects all the places where the symptoms are not present
    for i in list2:
      data['symptoms'][i]['severity'] = 'None'                    # assign all the places where the symptom is not present value to zero
    #create a combination of list of severity value
    l1=list(itertools.product([0,1,2],repeat=len(list1)))# from the list1 we have all the positions where symptoms are present and there are 3 severity for each symptoms so create a combination of all the possible severity comnations
    for j in l1:                 #for each element in the severity list combination
      for n,m in zip(list1,j):
        data['symptoms'][n]['severity'] = severity[m]   #assign the severity for each  symptoms and run trough all the possible combination of severity 
      print(count)
      count=count+1
      print("main count  :",maincount)
      print("systom count   :",syscount)
      resp = requests.post(url=url,json=data)
      if "\"UnLikely\"" in resp.text:                            #counter to collect the presence value of COVID for each combination
        countun=countun+1
      if "\"Likely\"" in resp.text:
        countl=countl+1
      if "\"Indeterminate\"" in resp.text:
        countint=countint+1
        a=open("data.txt",'a')
        for i in range(9):
          
          if str(data['symptoms'][i]['severity'])=="Mild":
            a.write("|     Mild       |")
          elif str(data['symptoms'][i]['severity'])=="Severe":
            a.write("|     Severe     |")
          elif str(data['symptoms'][i]['severity'])=="Moderate":
            a.write("|     Moderate   |")
          else:
            a.write("|     None       |")
        a.write("\n")
        a.close()   
        
      print("Unlikely "+str(countun)+"   "+"Likely "+str(countl)+"     "+"Indeterminate"+str(countint))
      print("--------------------------------------------------")  
      
a.close()
      
