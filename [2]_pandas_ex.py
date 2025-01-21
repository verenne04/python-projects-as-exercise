import pandas as pd

FNAME = 'files/pd.disease_symptoms.csv'
STOP = 'STOP'

dfds = pd.read_csv(FNAME)

t_dfds = dfds.melt(id_vars='Disease', var_name='SymptomNum', value_name='Symptom')
t_dfds['Symptom'] = t_dfds['Symptom'].str.strip().str.lower()

# Create a function that returns the list of diseases associated with a given symptom (received in input) 
def getDiseaseFromSympt(s):
    dislst = t_dfds[t_dfds['Symptom'] == s]['Disease'].unique()
    return dislst

#print(getDiseaseFromSympt('vomiting'))

# Create a function that, given a list of diseases, returns the lists of symptoms associated with them.
def getSymptFromDisease(dlst):
    symlst = t_dfds[t_dfds['Disease'].isin(dlst)]['Symptom'].unique()
    return symlst

#print(getSymptFromDisease(['Cholera', 'hepatitis A', 'Jaundice']))

# Create a function that iteratively asks the user a symptom and reports the 
# diseases (and other symptoms) till the user enters "STOP" and returns the 
# lists of associated diseases with the selection of specified symptoms, one 
# at a time. 

def askForSymptom():
    cronology = []
    s = input('Write a symptom: ')
    while s !=  STOP:
        dis = t_dfds[t_dfds.Symptom == s]
        print(dis)
        dislst = t_dfds[t_dfds.Symptom == s]['Disease'].unique()
        cronology.append(f'Symptom: {s} | Diseases: {dislst}')
        s = input('Write a new symptom: ')
    return cronology

cro = askForSymptom()
for elem in cro:
    print(elem)