import pathlib
from typing import List

import jieba.analyse
from sqlalchemy import Row, func

from database import *


class QuestionPaser:
    symptom_keywords = ['现象', '症候', '症状', '表征', '表现']
    disease_keywords = ['疾病', '病', '病现象', '病症', '病症候', '病症状', '病表征', '病表现', '症']
    prevention_keywords = ['免得', '咋才不', '咋才可不', '咋才可以不', '咋才能不', '咋样才不', '咋样才可不',
                           '咋样才可以不', '咋样才能不', '如何可不', '如何可以不', '如何才不', '如何才能不', '怎么才不',
                           '怎么才可不', '怎么才可以不', '怎么才能不', '怎样才不', '怎样才可不', '怎样才可以不',
                           '怎样才能不', '抵制', '抵御', '绕开', '躲开', '躲掉', '躲避', '逃开', '逃避', '避开', '避掉',
                           '防止', '防范', '预防']
    cause_keywords = ['为什么', '为什么会', '为什么才会', '为何', '为何会', '为何才会', '为啥', '会导致', '会造成',
                      '原因', '咋样才', '因为', '因为什么', '因为何', '因为啥', '因什么', '因何', '因啥', '如何会',
                      '如何才会', '导致', '引起', '怎么会', '怎么才会', '怎样会', '怎样才', '成因', '病因']
    treatment_keywords = ['治愈', '治疗方法', '治疗', '疗法', '怎么医', '治疗措施', '怎么治', '怎么医治', '咋治',
                          '咋办', '治疗途径', '如何治', '怎么办', '治疗办法', '医治', '怎么治疗', '治疗方式',
                          '如何医治', '医治方式', '主治']
    complication_keywords = ['一同出现', '一同发生', '一并出现', '一并发生', '一起出现', '一起发生', '伴随', '伴随发生',
                             '共现', '并发', '并发症']
    usage_keywords = ['主治什么', '主治啥', '医治啥', '有什么好处', '有什么用', '有什么益处', '有何用', '有何益处',
                      '治啥', '治愈啥', '治疗什么', '治疗啥', '用处', '用来', '用来作甚', '用来做啥', '用途', '要',
                      '需要']
    approval_keywords = ['批文', '批准文号', '准字号', '批准号', '批号', '批准文号', '批准证号', '批准证文号', ]

    keywords_list = ['symptom_keywords', 'disease_keywords', 'prevention_keywords', 'cause_keywords',
                     'treatment_keywords', 'complication_keywords', 'usage_keywords', 'approval_keywords']
    disease_list = []
    drug_list = []
    symptom_list = []

    default_answer = '对不起，书樱还不知道怎么回答您的问题呢，您可以换个问题试试哦~'

    # drug_keywords = ['药', '药品', '用药', '胶囊', '口服液', '炎片']

    def __init__(self, database: Union[str, Database]) -> None:
        self.question = None
        self.answer = None

        self.load()
        self.response = Responser(database)

        jieba.initialize()

    def load(self) -> None:
        def load_file(path: pathlib.Path) -> List[str]:
            with open(path, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f.readlines()]

        def load_keyword() -> None:
            file_list = pathlib.Path('../data').glob('*.txt')

            for file in file_list:
                file_content = load_file(file)
                self.__setattr__(file.stem, file_content)
                self.keywords_list.append(file.stem)

        load_keyword()

        for keyword_list in self.keywords_list:
            for keyword in self.__getattribute__(keyword_list):
                jieba.add_word(keyword.strip())

    def parse(self, message: str) -> str:
        def check_disease() -> Union[str, None]:
            for keyword in self.disease_list:
                if keyword in self.question:
                    return keyword
            return None

        def check_symptom() -> Union[str, None]:
            for keyword in self.symptom_list:
                if keyword in self.question:
                    return keyword
            return None

        def check_drug() -> Union[str, None]:
            for keyword in self.drug_list:
                if keyword in self.question:
                    return keyword
            return None

        def check_cause() -> bool:
            for keyword in self.cause_keywords:
                if keyword in self.question:
                    return True
            return False

        def check_complication() -> bool:
            for keyword in self.complication_keywords:
                if keyword in self.question:
                    return True
            return False

        def check_prevention() -> bool:
            for keyword in self.prevention_keywords:
                if keyword in self.question:
                    return True
            return False

        def check_treatment() -> bool:
            for keyword in self.treatment_keywords:
                if keyword in self.question:
                    return True
            return False

        def drug_parse(drug_name: str) -> str:
            def check_drug_approval() -> bool:
                for keyword in self.approval_keywords:
                    if keyword in self.question:
                        return True
                return False

            def check_drug_usage() -> bool:
                for keyword in self.usage_keywords:
                    if keyword in self.question:
                        return True
                return False

            approval_check = check_drug_approval()
            usage_check = check_drug_usage()

            if approval_check:
                return self.response.drug_approval(drug_name)
            elif usage_check:
                return self.response.drug_usage(drug_name)
            else:
                return self.response.drug_info(drug_name)

        self.question = message

        drug_check = check_drug()
        disease_check = check_disease()
        symptom_check = check_symptom()

        if drug_check:
            return drug_parse(drug_check)
        else:
            complication_check = check_complication()
            treatment_check = check_treatment()
            prevention_check = check_prevention()
            cause_check = check_cause()

            if complication_check:
                if disease_check:
                    return self.response.disease_complication(disease_check)
                elif symptom_check:
                    disease_name = self.response.get_disease_form_symptom(symptom_check)
                    return self.response.disease_complication(disease_name)
            elif treatment_check:
                if disease_check:
                    return self.response.disease_treatment(disease_check)
                elif symptom_check:
                    disease_name = self.response.get_disease_form_symptom(symptom_check)
                    return self.response.disease_treatment(disease_name)
            elif prevention_check:
                if disease_check:
                    return self.response.disease_prevention(disease_check)
                elif symptom_check:
                    disease_name = self.response.get_disease_form_symptom(symptom_check)
                    return self.response.disease_prevention(disease_name)
            elif cause_check:
                if disease_check:
                    return self.response.disease_cause(disease_check)
                elif symptom_check:
                    disease_name = self.response.get_disease_form_symptom(symptom_check)
                    return self.response.disease_cause(disease_name)
            else:
                if disease_check:
                    return self.response.disease_info(disease_check)
                elif symptom_check:
                    return self.response.symptom_info(symptom_check)

        # inference

        # return default_answer
        if self.answer is not None:
            return self.answer
        else:
            return self.default_answer

    def random(self) -> str:
        # TODO: random
        pass


class Responser:
    def __init__(self, database: Union[Database, str]) -> None:
        if isinstance(database, str):
            self.db = Database(database)
        elif isinstance(database, Database):
            self.db = database
        else:
            raise TypeError('db must be str or Database')

    @staticmethod
    def _to_str(obj, spliter: str = ',') -> str:
        if isinstance(obj, str):
            return obj
        elif isinstance(obj, Row):
            return Responser._to_str(tuple(obj))
        elif isinstance(obj, Iterable):
            return spliter.join([Responser._to_str(i) for i in obj])
        else:
            return str(obj)

    @staticmethod
    def _deflate(obj) -> List:
        if isinstance(obj, Iterable):
            return [Responser._to_str(i) for i in obj]
        else:
            return obj

    def query_random(self, query, count: int = 1) -> List[Row]:
        return self.db.session.query(query).order_by(func.rand()).limit(count).all()

    def query_one(self, query, match_column, value) -> Row:
        return self.db.session.query(query).filter(match_column == value).first()

    def query_all(self, query, match_column, value) -> List[Row]:
        return self.db.session.query(query).filter(match_column == value).all()

    def sub_query(self, query, match_column, value) -> List[Row]:
        return self.db.session.query(query).filter(match_column == value).subquery()

    def query_list(self, column, limit, offset) -> List:
        return [list(i) for i in self.db.session.query(*column).limit(limit).offset(offset).all()]

    def get_disease_form_symptom(self, symptom_name: str) -> str:
        data = self.query_one(disease.name, symptom.name, symptom_name)
        return self._to_str(data)

    def drug_approval(self, drug_name: str) -> str:
        data = self.query_all(drug.approval, drug.name, drug_name)
        data = self._to_str(data)
        return f'{drug_name}的批准文号有{data}'

    def drug_usage(self, drug_name: str) -> str:
        data = self.query_one(drug.usage, drug.name, drug_name)
        data = self._to_str(data)
        return data

    def drug_info(self, drug_name: str) -> str:
        data = self.query_one(drug.usage, drug.name, drug_name)
        data = self._to_str(data)
        return f'{drug_name}，{data}'

    def symptom_related_disease(self, symptom_name: str) -> str:
        symptom_id = self._to_str(self.query_one(symptom.symptom_id, symptom.name, symptom_name))
        disease_id_list = set(
            self._deflate(self.query_all(disease_related_symptom.disease_id, disease_related_symptom.symptom_id,
                                         symptom_id)))
        disease_list = [self.query_one(disease, disease.disease_id, i) for i in disease_id_list]

        msg = ''
        cnt = 1
        for dis in disease_list:
            if not dis:
                continue
            msg += f'{cnt}.\t{dis.name}，{dis.overview}\n'
            cnt += 1
        return msg

    def symptom_info(self, symptom_name: str) -> str:
        data = self.query_one(symptom.overview, symptom.name, symptom_name)
        data = self._to_str(data)
        return f'{symptom_name}，{data}' + \
            f'\n{symptom_name}可能由以下原因引起：' + self.symptom_related_disease(symptom_name)

    def disease_complication(self, disease_name: str) -> str:
        data = self.query_one(disease.complication, disease.name, disease_name)
        return self._to_str(data)

    def disease_treatment(self, disease_name: str) -> str:
        data = self.query_one(disease.treatment, disease.name, disease_name)
        return self._to_str(data)

    def disease_prevention(self, disease_name: str) -> str:
        data = self.query_one(disease.prevention, disease.name, disease_name)
        return self._to_str(data)

    def disease_cause(self, disease_name: str) -> str:
        data = self.query_one(disease.reason, disease.name, disease_name)
        return self._to_str(data)

    def disease_info(self, disease_name: str) -> str:
        data = self.query_one(disease.overview, disease.name, disease_name)
        data = self._to_str(data)
        return f'{disease_name}，{data}' + \
            f'\n{disease_name}的并发症有：' + self.disease_complication(disease_name) + \
            f'\n{disease_name}的治疗方法有：' + self.disease_treatment(disease_name) + \
            f'\n{disease_name}的预防方法有：' + self.disease_prevention(disease_name) + \
            f'\n{disease_name}的病因有：' + self.disease_cause(disease_name)


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/drug?charset=utf8mb4')
    parser = QuestionPaser(db)
    # text = '铝碳酸镁片的批号是什么？'
    # text = '复方南瓜养阴散有什么用？'
    # text = '肝宁片是什么？'
    # text = '反酸由什么引起？'
    # text = '抽筋由什么引起？'
    # text = '反酸是什么？'
    # text = '阳痿的并发症有哪些？'
    # text = '阳痿怎么预防？'
    # text = '阳痿的病因是什么？'
    # text = '阳痿的治疗方法有哪些？'
    # text = '阳痿是什么？'
    # text = '复方南瓜养阴散有什么用？'
    # text = '铝碳酸镁片的批号是什么？'
    # text = '这是个没用的问题？'
    # text = '感冒怎么办？'
    # text = '头痛怎么办？'
    # text = '为什么会头痛？'
    # print('Q:\t' + text)
    # print('A:\t' + parser.parse(text))
    #
    text_list = [
        '铝碳酸镁片的批号是什么？',
        '复方南瓜养阴散有什么用？',
        '肝宁片是什么？',
        '反酸由什么引起？',
        '抽筋由什么引起？',
        '反酸是什么？',
        '阳痿的并发症有哪些？',
        '阳痿怎么预防？',
        '阳痿的病因是什么？',
        '阳痿的治疗方法有哪些？',
        '阳痿是什么？',
        '复方南瓜养阴散有什么用？',
        '铝碳酸镁片的批号是什么？',
        '这是个没用的问题？',
        '感冒怎么办？',
        '头痛怎么办？',
        '为什么会头痛？',
        '复方感冒灵颗粒的批号是什么？',
    ]
    for text in text_list:
        print('Q:\t' + text)
        print('A:\t' + parser.parse(text))
