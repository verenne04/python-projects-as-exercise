import pandas as pd

precaution = pd.read_csv("esame/come usare pd/esercizi in classe/disease/files-2/pd.disease_precaution.csv")
precaution = precaution.applymap(lambda x: x.strip() if isinstance(x, str) else x)

disease_symp = pd.read_csv("esame/come usare pd/esercizi in classe/disease/files-2/pd.disease_symptoms.csv")
disease_symp = disease_symp.applymap(lambda x: x.strip() if isinstance(x, str) else x)

disease = pd.read_csv("esame/come usare pd/esercizi in classe/disease/files-2/pd.disease.csv")
disease = disease.applymap(lambda x: x.strip() if isinstance(x, str) else x)

symp = pd.read_csv("esame/come usare pd/esercizi in classe/disease/files-2/pd.symptom.csv")
symp = symp.applymap(lambda x: x.strip() if isinstance(x, str) else x)




"""
# Identify severe symptoms, identified by a weight equal to or higher than 5
severe = symp.loc[symp["Weight"] >= 5].reset_index().drop(columns=["index"])
print("####################################################")
print("Identify severe symptoms, identified by a weight equal to or higher than 5")
print("\n")
print(severe)
print("\n")
print("####################################################")
"""

# Count for each severity level (weight), how many diseases symptoms there are
sym_severity = symp["Weight"].value_counts().sort_index()
# print(sym_severity)

# Create a tidy dataframe for the diseases and symptoms.

# USO LA FUNZIONE MELT
grouped_symptoms = (
    disease_symp.melt(id_vars=["Disease"], value_name="Symptom", var_name = "Symptom_Num"))  # Trasforma in formato lungo
grouped_symptoms_dropped = grouped_symptoms.drop(columns = ["Symptom_Num"])
# id_vars: colonne che non vuoi trasformare.
# value_vars: colonne che vuoi "trasformare" in righe, se non specificato, Pandas usa tutte le colonne che non sono in id_vars.
# var_name: nome della nuova colonna che contiene i nomi originali delle colonne sciolte. Default: "variable".
# value_name: nome della nuova colonna che contiene i valori delle colonne sciolte. Default: "value".

grouped_symptoms_dropped = grouped_symptoms_dropped.dropna()
grouped_symptoms_dropped =  grouped_symptoms_dropped.drop_duplicates()
# print(grouped_symptoms_dropped)

# Find how many different symptoms have been detected in association with the visited patients.
num_sym = grouped_symptoms_dropped["Symptom"].nunique()
# print(num_sym)


# Report the number of precautions per disease.
# precaution["Total"] = precaution.drop("Disease", axis = 1).count(axis = "columns")
# print (precaution[["Disease","Total"]])


# USO FUNZIONE PIVOT_TABLE
# pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean')
# data: Il DataFrame da trasformare.
# values: Colonne con i dati numerici da aggregare. Se omesso, considera tutte le colonne numeric-only.
# index: Colonne che vuoi utilizzare come righe.
# columns: Colonne che vuoi trasformare in intestazioni.
# aggfunc: Funzione di aggregazione da applicare ai dati (default: 'mean'). Può essere sum, count, min, max, ecc.

# Report the number of different symptoms per disease.
data = grouped_symptoms_dropped.groupby("Disease")["Symptom"].count()
# print(data)

# Report the list of unique symptoms per disease.
#list_dis = grouped_symptoms_dropped.groupby("Disease").agg(list("Symptom"))
# df.groupby(['id', 'time'])['value'].apply(list)
#list_dis = grouped_symptoms_dropped.groupby("Disease")["Symptom"].apply(list)
#print(list_dis)

list_dis = grouped_symptoms_dropped.groupby("Disease")["Symptom"].apply(list).reset_index()
list_dis['Symptom'] = list_dis['Symptom'].apply(lambda x: list(x) if isinstance(x, list) else [])

print(list_dis)

#list_dis = grouped_symptoms_dropped.groupby("Disease").agg(list).reset_index()
# print(list_dis)


# Report how many times each precaution is suggested (independently of a disease)
tidy_pre = precaution.melt(id_vars= "Disease", value_name="Precauzione", var_name = "Precaution_Num")
tidy_pre = tidy_pre.dropna().drop(columns = ["Precaution_Num"])
# print(tidy_pre)
count = tidy_pre.groupby("Precauzione").count()
# print(count)

# Create a function that returns the list of diseases associated with a given symptom (received in input)
symptoms = grouped_symptoms_dropped.groupby("Symptom").agg(list)
# symptoms = symptoms.reset_index()

# print(symptoms)
# sintomo = input("Inserire cosa si sente: ")

# possibili_malattie = symptoms[symptoms["Symptom"] == sintomo]
# print(possibili_malattie)
"""
# Create a function that, given a list of diseases, returns the lists of symptoms associated with them.
def list_sintomi (malattie, list_dis ): 
    listasintomi = []
    for malattia in malattie:
        sintomi = list_dis.loc[list_dis["Disease"] == malattia, "Symptom"].tolist()
        print(sintomi)
        listasintomi.append(sintomi)
    return listasintomi

dis = input("Inserire le malattie con separatore , : ")
dis = dis.split(",")
listasintomi = list_sintomi(dis, list_dis)
# print(listasintomi)
"""

# Create a function that iteratively asks the user a symptom and reports the diseases (and other symptoms) till the user enters
# "STOP" and returns the lists of associated diseases with the selection of specified symptoms, one at a time.

def malassociate (grouped_symptoms_dropped,list_dis):
    sintomo = input("Sintomo:")
    tuttemal = []
    while sintomo != "STOP":
        malattie = grouped_symptoms_dropped.loc[grouped_symptoms_dropped["Symptom"] == sintomo, "Disease"].tolist()
        #print(malattie)
        for malattia in malattie:
            sintomi_associati = []
            sintomi_associati = list(list_dis.loc[list_dis["Disease"] == malattia, "Symptom"].iloc[0])
            #print(sintomi_associati)
            sintomi_associati.remove(sintomo)
            #print(sintomi_associati)
            print(f"\nla malattia: {malattia} ha {sintomo} tra i sintomi, e ha anche altri sintomi, tra cui {sintomi_associati}" )
            tuttemal.append(malattia)
        sintomo = input("\nSintomo:")
    return(tuttemal)

tuttemalattie = malassociate(grouped_symptoms_dropped,list_dis)
print(tuttemalattie)
