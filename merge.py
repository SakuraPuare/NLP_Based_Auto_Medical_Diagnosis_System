import pathlib

import pandas

data = pathlib.Path('./data')


def glob_drug():
    name = pandas.read_csv(data / 'drug_name.csv', header=None)
    approval = pandas.read_csv(data / 'drug_approval.csv', header=None)
    usage = pandas.read_csv(data / 'drug_usage.csv', header=None)

    # 合并
    name.columns = ['id', 'name']
    approval.columns = ['id', 'approval']
    usage.columns = ['id', 'usage']

    # name['id'] = name['id'].astype('int32')

    df = pandas.merge(name, approval, on='id')
    df = pandas.merge(df, usage, on='id')
    df.to_csv(data / 'drug.csv', index=False)

    pass


def glob_disease():
    name = pandas.read_csv(data / 'disease_name.csv', header=None)
    overview = pandas.read_csv(data / 'disease_overview.csv', header=None)
    reason = pandas.read_csv(data / 'disease_reason.csv', header=None)
    prevention = pandas.read_csv(data / 'disease_prevention.csv', header=None)
    treatment = pandas.read_csv(data / 'disease_treatment.csv', header=None)
    complication = pandas.read_csv(data / 'disease_complication.csv', header=None)

    # 合并
    name.columns = ['id', 'name']
    overview.columns = ['id', 'overview']
    reason.columns = ['id', 'reason']
    prevention.columns = ['id', 'prevention']
    treatment.columns = ['id', 'treatment']
    complication.columns = ['id', 'complication']

    # name['id'] = name['id'].astype('int32')

    df = pandas.merge(name, overview, on='id')
    df = pandas.merge(df, reason, on='id')
    df = pandas.merge(df, prevention, on='id')
    df = pandas.merge(df, treatment, on='id')
    df = pandas.merge(df, complication, on='id')
    df.to_csv(data / 'disease.csv', index=False)

    pass


def glob_symptom():
    name = pandas.read_csv(data / 'symptom_name.csv', header=None)
    overview = pandas.read_csv(data / 'symptom_overview.csv', header=None)

    # 合并
    name.columns = ['id', 'name']
    overview.columns = ['id', 'overview']

    # name['id'] = name['id'].astype('int32')
    # overview['id'] = overview['id'].astype('int32')

    df = pandas.merge(name, overview, on='id')
    df.to_csv(data / 'symptom.csv', index=False)

    pass


if __name__ == '__main__':
    glob_drug()
    glob_disease()
    glob_symptom()
    pass
