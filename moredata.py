from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base,User ,Job ,Userskill ,Jobskill, Skills

engine = create_engine('sqlite:///jobdatabase.db')
#engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

#creating skill table

skill = Skills(skill_id=1,skill_name="c/c++")

session.add(skill)
session.commit()

skill = Skills(skill_id=2,skill_name="python")

session.add(skill)
session.commit()

skill = Skills(skill_id=3,skill_name="django")

session.add(skill)
session.commit()

skill = Skills(skill_id=4,skill_name="java")

session.add(skill)
session.commit()

skill = Skills(skill_id=5,skill_name="kotlin")

session.add(skill)
session.commit()

skill = Skills(skill_id=6,skill_name="ruby")

session.add(skill)
session.commit()


skill = Skills(skill_id=7,skill_name="flutter")

session.add(skill)
session.commit()

skill = Skills(skill_id=8,skill_name="mysql")

session.add(skill)
session.commit()



#Create first user
User1 = User(user_id = 1, user_name="ramesh", user_phone=7895632145, user_email="ramesh@gmail.com")

session.add(User1)
session.commit()

ski = Userskill(user_skill_id=1,user_id = 1, skill_no=1)

session.add(ski)
session.commit()


ski = Userskill(user_skill_id=2,user_id =1, skill_no=2)

session.add(ski)
session.commit()

ski = Userskill(user_skill_id=3,user_id =1, skill_no=3)

session.add(ski)
session.commit()

ski = Userskill(user_skill_id=4,user_id =1, skill_no=4)

session.add(ski)
session.commit()

ski = Userskill(user_skill_id=5,user_id =1, skill_no=5)

session.add(ski)
session.commit()

#Create secound user
User2 = User(user_id =2, user_name="ankush", user_phone=9568451236, user_email="ankush@gmail.com")

session.add(User2)
session.commit()

ski = Userskill(user_skill_id=6,user_id =2, skill_no=1)

session.add(ski)
session.commit()


ski = Userskill(user_skill_id=7,user_id =2, skill_no=2)

session.add(ski)
session.commit()

ski = Userskill(user_skill_id=8,user_id =2, skill_no=3)

session.add(ski)
session.commit()

#Create third user
User2 = User(user_id =3, user_name="kush", user_phone=456795112, user_email="kush@gmail.com")

session.add(User2)
session.commit()

ski = Userskill(user_skill_id=9,user_id =3, skill_no=1)

session.add(ski)
session.commit()


ski = Userskill(user_skill_id=10,user_id =3, skill_no=2)

session.add(ski)
session.commit()

ski = Userskill(user_skill_id=11,user_id =3, skill_no=5)

session.add(ski)
session.commit()


#Create first job
job1 = Job(job_id=1, job_name="junior_developer", job_contact_person="raj", job_contact_email="raj@lotuspay.com")

session.add(job1)
session.commit()

ski = Jobskill(job_skill_id=1,job_id=1, required_skill_no=1)

session.add(ski)
session.commit()


ski = Jobskill(job_skill_id=2,job_id=1, required_skill_no=3)

session.add(ski)
session.commit()


#Create sec job
job2 = Job(job_id=2, job_name="Senior_developer", job_contact_person="sumit", job_contact_email="sumit@google.com")

session.add(job2)
session.commit()

ski = Jobskill(job_skill_id=3,job_id=2, required_skill_no=3)

session.add(ski)
session.commit()


ski = Jobskill(job_skill_id=4,job_id=2, required_skill_no=5)

session.add(ski)
session.commit()

ski = Jobskill(job_skill_id=5,job_id=2, required_skill_no=7)

session.add(ski)
session.commit()


ski = Jobskill(job_skill_id=6,job_id=2, required_skill_no=2)

session.add(ski)
session.commit()

print ("skills and job skill added")
