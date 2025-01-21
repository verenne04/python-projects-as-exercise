import pandas as pd

SYMP = 'files/pd.symptom.csv'
DIS_SYMP = 'files/pd.disease_symptoms.csv'
PREC = 'files/pd.disease_precaution.csv'

# import dataset
symp = pd.read_csv(SYMP)
#print(symp.head())

# Identify severe symptoms, identified by a weight equal to or higher than 5.
severe_symp = symp[symp.Weight >= 5]
#print(severe_symp)

# Create a tidy dataframe for the diseases and symptoms.
dis_symp = pd.read_csv(DIS_SYMP)
tidy_dis_symp = dis_symp.melt(id_vars=['Disease'], var_name='SymptomNum', value_name='Symptom')

#Find how many different symptoms have been detected in association with the visited patients.
num_diff_symp = tidy_dis_symp['Symptom'].nunique()
#print(num_diff_symp)

# Report the number of precautions per disease.
dfp = pd.read_csv(PREC)
t_dfp = dfp.melt(id_vars='Disease', var_name='PrecNum', value_name='Precaution')
prec_per_dis = t_dfp.groupby('Disease')['Precaution'].count()
#print(prec_per_dis)

# Report the number of different symptoms per disease
num_symp_per_dis = tidy_dis_symp.groupby('Disease')['Symptom'].nunique()
#print(num_symp_per_dis)

# Report the list of unique symptoms per disease.
symp_per_dis = tidy_dis_symp.groupby('Disease')['Symptom'].unique()
#print(symp_per_dis)

# Report how many times each precaution is suggested (independently of a disease)
num_prec_sug = t_dfp.groupby('Precaution')['Disease'].nunique()
#print(num_prec_sug)