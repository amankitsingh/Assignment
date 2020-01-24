from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Skills(Base):
    __tablename__ = 'skills'

    skill_id = Column(Integer,primary_key=True)
    skill_name =  Column(String(50), nullable=False)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_phone = Column(Integer, unique=True, nullable=False)
    user_email = Column(String(25), unique=True, nullable=False)


class Job(Base):
    __tablename__ = 'job'

    job_id = Column(Integer, primary_key=True)
    job_name = Column(String(50), nullable=False)
    job_contact_person = Column(String(50), nullable=False)
    job_contact_email = Column(String(25), nullable=False)


class Userskill(Base):
    __tablename__ = 'userskill'

    user_skill_id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)
    skill_no = Column(Integer, ForeignKey('skills.skill_id'))
    skills =  relationship(Skills)


class Jobskill(Base):
    __tablename__ = 'jobskill'

    job_skill_id = Column(Integer,primary_key=True)
    job_id = Column(Integer , ForeignKey('job.job_id'))
    job = relationship(Job)
    required_skill_no = Column(Integer,ForeignKey('skills.skill_id'))
    skills =  relationship(Skills)



engine = create_engine('sqlite:///jobdatabase.db')
Base.metadata.create_all(engine)
