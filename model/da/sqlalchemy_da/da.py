from sqlalchemy_utils import create_database, drop_database, database_exists
from sqlalchemy import create_engine, and_, or_, Update
from sqlalchemy.orm import sessionmaker

from model.entity.base import Base

connection_string = "mysql+pymysql://root:saman20@localhost:3306/insurance_project"

if not database_exists(connection_string):
    create_database(connection_string)


# else:
#     drop_database(connection_string)
#     create_database(connection_string)


class DataAccess:
    def __init__(self, class_name):
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.class_name = class_name

    def save(self, entity):
        session = self.Session()
        session.add(entity)
        session.commit()
        session.close()

    def edit(self, entity):
        session = self.Session()
        session.execute(
            Update(self.class_name).where(self.class_name.person_id == entity.person_id).values(_phone=entity.phone,
                                                                                                password=entity.password,
                                                                                                status=entity.status))
        session.commit()
        session.close()

    def remove(self, object_id):
        session = self.Session()
        entity = session.get(self.class_name, object_id)
        session.delete(entity)
        session.commit()
        session.close()

    def find_all(self):
        session = self.Session()
        entity_list = session.query(self.class_name).all()
        session.close()
        return entity_list

    def find_by_id(self, object_id):
        session = self.Session()
        entity = session.get(self.class_name, object_id)
        session.close()
        return entity

    def find_by(self, find_statement):
        session = self.Session()
        entity = session.query(self.class_name).filter(find_statement).all()
        return entity
