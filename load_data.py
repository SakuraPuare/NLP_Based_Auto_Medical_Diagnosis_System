import pandas

from api.database import *


def load_symptoms():
    data = pandas.read_csv('data/symptom.csv')
    insert = []
    for row in data.itertuples():
        symptom_id, name, overview = map(lambda x: str(x).strip(), row[1:])
        insert.append(symptom(symptom_id=symptom_id, name=name, overview=overview))
    db.inserts(insert)


def load_disease():
    data = pandas.read_csv('data/disease.csv')
    insert = []
    for row in data.itertuples():
        disease_id, name, overview, reason, prevention, treatment, complication = map(lambda x: str(x).strip(), row[1:])
        insert.append(disease(disease_id=disease_id, name=name, overview=overview, reason=reason, prevention=prevention,
                              treatment=treatment, complication=complication))
    db.inserts(insert)


def load_drug():
    data = pandas.read_csv('data/drug.csv')
    insert = []
    for row in data.itertuples():
        drug_id, name, approval, usage = map(lambda x: str(x).strip(), row[1:])
        insert.append(drug(drug_id=drug_id, name=name, approval=approval, usage=usage))
    db.inserts(insert)


def load_relationship():
    insert = []
    data = pandas.read_csv('data/disease_related_symptom.csv')
    for row in data.itertuples():
        disease_id, symptom_id = map(int, row[1:])
        obj = disease_related_symptom(disease_id=disease_id, symptom_id=symptom_id)
        # db.inserts(obj)
        insert.append(obj)
    data = pandas.read_csv('data/symptom_related_disease.csv')
    for row in data.itertuples():
        symptom_id, disease_id = map(int, row[1:])
        obj = disease_related_symptom(symptom_id=symptom_id, disease_id=disease_id)
        # db.inserts(obj)
        insert.append(obj)
    db.inserts(insert)


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/drug?charset=utf8mb4')
    db.create_all_table()
    # load_drug()
    # load_disease()
    # load_symptoms()
    load_relationship()
    pass
