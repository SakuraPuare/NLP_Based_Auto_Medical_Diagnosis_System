from sqlalchemy import distinct

from api.database import *


def get_all_items():
    get_disease()
    get_drug()
    get_symptom()


def get_disease():
    item_list = [i[0] for i in db.session.query(distinct(disease.name)).all()]

    with open('./data/disease_list.txt', 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(item_list))


def get_drug():
    item_list = [i[0] for i in db.session.query(distinct(drug.name)).all()]

    with open('./data/drug_list.txt', 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(item_list))


def get_symptom():
    item_list = [i[0] for i in db.session.query(distinct(symptom.name)).all()]

    with open('./data/symptom_list.txt', 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(item_list))


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/drug?charset=utf8mb4')
    get_all_items()
    pass
