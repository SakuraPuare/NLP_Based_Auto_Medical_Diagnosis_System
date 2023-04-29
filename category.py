import asyncio

import httpx
from sqlalchemy import distinct

from api.database import *

url = 'http://localhost:3030/kgdrug/sparql'

client = httpx.Client()
sem = asyncio.Semaphore(10)


def query(q):
    data = {
        "query": f"""SELECT ?subject ?predicate ?object WHERE {{?subject ?predicate ?object}} LIMIT 5000 OFFSET {q}"""}
    insert_data = []
    response = client.post(url, data=data, timeout=9999)
    for i in response.json().get('results', {}).get('bindings', []):
        subject = i.get('subject', {}).get('value', '')
        predicate = i.get('predicate', {}).get('value', '')
        object = i.get('object', {}).get('value', '')
        insert_data.append(raw_data(subject=subject, predicate=predicate, object=object))
    db.inserts(insert_data)
    pass
    # print(f'insert {q}')


def get_detail():
    subject_list = db.session.query(distinct(raw_data.subject)).all()
    file_list = set([i[0] for i in subject_list if i[0].startswith('file://')])
    http_list = set([i[0] for i in subject_list if i[0].startswith('http')])
    type_list = set([i.split('#')[-1].split('/')[0] for i in file_list if '#' in i])
    disease_list = set([i.split('#')[-1].split('/')[-1] for i in file_list if '#' in i])
    id_list = set([i.split('#')[-1].split('/')[-1] for i in file_list])
    pass


def get_all_drug():
    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#drugs'),
        raw_data.predicate == 'http://www.kgdrug.com#proname').all()
    data = [f'{str(i[0]).split("#drugs/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/drug_name.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#drugs'),
        raw_data.predicate == 'http://www.kgdrug.com#pzwh').all()
    data = [
        f'{str(i[0]).split("#drugs/")[-1]},{"国药准字" + str(i[1]).replace(",", "，") if not str(i[1]).startswith("国药准字") else str(i[1]).replace(",", "，")}'.replace(
            '\n', ' ')
        for i in data]
    with open('./data/drug_approval.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#drugs'),
        raw_data.predicate == 'http://www.kgdrug.com#gazhzh').all()
    data = [f'{str(i[0]).split("#drugs/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/drug_usage.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))


def get_all_disease():
    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#jibingname').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/disease_name.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#gaishu').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/disease_overview.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#bingyin').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/disease_reason.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#zhiliao').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/disease_treatment.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#yufang').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/disease_prevention.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#bingfazheng').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/disease_complication.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#disease'),
        raw_data.predicate == 'http://www.kgdrug.com#haszhengzhuang').all()
    data = [f'{str(i[0]).split("#disease/")[-1]},{str(i[1]).split("#symptom/")[-1]}' for i in data]
    with open('./data/disease_related_symptom.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))


def get_all_symptom():
    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#symptom'),
        raw_data.predicate == 'http://www.kgdrug.com#zzname').all()
    data = [f'{str(i[0]).split("#symptom/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/symptom_name.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#symptom'),
        raw_data.predicate == 'http://www.kgdrug.com#zzgaishu').all()
    data = [f'{str(i[0]).split("#symptom/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/symptom_overview.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#symptom'),
        raw_data.predicate == 'http://www.kgdrug.com#zzbingyin').all()
    data = [f'{str(i[0]).split("#symptom/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/symptom_reason.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#symptom'),
        raw_data.predicate == 'http://www.kgdrug.com#zzyufang').all()
    data = [f'{str(i[0]).split("#symptom/")[-1]},{str(i[1]).replace(",", "，")}'.replace('\n', ' ') for i in data]
    with open('./data/symptom_prevent.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))

    data = db.session.query(raw_data.subject, raw_data.object).filter(
        raw_data.subject.startswith('file:///E:/project_code_2018/KG/kg_drug_new.nt#symptom'),
        raw_data.predicate == 'http://www.kgdrug.com#relatedisease').all()
    data = [f'{str(i[0]).split("#symptom/")[-1]},{str(i[1]).split("#disease/")[-1]}' for i in data]
    with open('./data/symptom_related_disease.csv', 'w', encoding='u8') as f:
        f.write('\n'.join(data).encode('u8', errors='ignore').decode('u8', errors='ignore'))


def main():
    pass


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/drug?charset=utf8mb4')
    # get_detail()
    get_all_drug()
    get_all_disease()
    get_all_symptom()
    # db.init()
    pass
    main()
