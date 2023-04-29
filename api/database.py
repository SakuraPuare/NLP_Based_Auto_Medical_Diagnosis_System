from typing import Union, Iterable

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):

    def json(self):
        result = {}
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=False)
        self.session = sessionmaker(bind=self.engine)()

    def init(self) -> None:
        self.create_all_table()

    def create_all_table(self) -> None:
        Base.metadata.create_all(self.engine)

    def inserts(self, obj: Union[Iterable[Base], Base]) -> None:
        if isinstance(obj, list):
            self.session.add_all(obj)
        else:
            self.session.add(obj)
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)
            # raise e
        finally:
            self.close()

    def close(self) -> None:
        self.session.close()
        self.engine.dispose()


class raw_data(Base):
    __tablename__ = 'raw_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(LONGTEXT)
    predicate = Column(LONGTEXT)
    object = Column(LONGTEXT)

    def __repr__(self):
        return f'<raw_data {self.subject} {self.predicate} {self.object}>'


class drug_raw(Base):
    __tablename__ = 'drug_raw'
    id = Column(Integer, primary_key=True, autoincrement=True)
    drug_id = Column(Integer)
    predicate = Column(LONGTEXT)
    object = Column(LONGTEXT)

    def __repr__(self):
        return f'<drug_raw {self.drug_id} {self.predicate} {self.object}>'


class disease(Base):
    __tablename__ = 'disease'
    id = Column(Integer, primary_key=True, autoincrement=True)
    disease_id = Column(Integer, index=True)
    name = Column(String(255))
    overview = Column(LONGTEXT)
    reason = Column(LONGTEXT)
    prevention = Column(LONGTEXT)
    treatment = Column(LONGTEXT)
    complication = Column(LONGTEXT)

    def __repr__(self):
        return f'<disease {self.disease_id} {self.name} {self.overview[:10]}>'

    def __bool__(self):
        return bool(self.disease_id)


#
#
class drug(Base):
    __tablename__ = 'drug'
    id = Column(Integer, primary_key=True, autoincrement=True)
    drug_id = Column(Integer)
    name = Column(String(255))
    approval = Column(String(255))
    usage = Column(LONGTEXT)

    def __repr__(self):
        return f'<drug {self.drug_id} {self.name} {self.approval} {self.usage[:10]}>'


class symptom(Base):
    __tablename__ = 'symptom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symptom_id = Column(Integer, index=True)
    name = Column(String(255))
    overview = Column(LONGTEXT)

    # disease_related_symptom_ibfk_1 = Index('disease_related_symptom_ibfk_1', 'disease_id')

    def __repr__(self):
        return f'<symptom {self.symptom_id} {self.name} {self.overview[:10]}>'


class disease_related_symptom(Base):
    __tablename__ = 'disease_related_symptom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    disease_id = Column(Integer)
    symptom_id = Column(Integer)

    def __repr__(self):
        return f'<disease_related_symptom {self.disease_id} {self.symptom_id}>'


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/drug?charset=utf8mb4')
    db.create_all_table()
    pass
