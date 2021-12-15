from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, String, BIGINT, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:admin@localhost:5432/', echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class AngioUser(Base):
    __tablename__ = 'tbl_angio_user'

    id = Column(INTEGER, primary_key=True)
    angio_user_name = Column(String(100))
    angio_user_phone_no = Column(BIGINT)
    angio_user_password = Column(VARCHAR(255))

    # Base.metadata.create_all(engine)


def __init__(self, id, angio_user_name, angio_user_phone_no, angio_user_password):
    super().__init__()
    self.id = id
    self.angio_user_name = angio_user_name
    self.angio_user_phone_no = angio_user_phone_no
    self.angio_user_password = angio_user_password


# READ
# Get all data

users = session.query(AngioUser)
for user in users: print(user.angio_user_name)

# Get filter data

# users = session.query(AngioUser).filter(AngioUser.angio_user_name=="Arvi")
# for user in users: print(user.angio_user_name)


# CREATE

# user = AngioUser(id=1, angio_user_name="YuAr", angio_user_phone_no=9753186420, angio_user_password="Pass@123")
# session.add(user)

# UPDATE
# user.name = "ArYu"
# user = session.query(AngioUser).filter(AngioUser.angio_user_name == "Aarvi").first()
# print(user.angio_user_name)
# session.delete(user)


# DELETE
# session.delete(user)

# session.commit()
