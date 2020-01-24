from flask import Flask, render_template
from flask import request, redirect, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database import Base, User, Job,Userskill ,Jobskill, Skills

from flask import make_response
import requests
import random
app = Flask(__name__)

# Connecting to Database and createing database session
engine = create_engine('sqlite:///jobdatabase.db',
connect_args={'check_same_thread': False})
#engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Initial page
@app.route('/')
def initialpage():
    skills = session.query(Skills).order_by(asc(Skills.skill_id))
    return render_template('infopage.html', skills=skills)

# Show all user
@app.route('/allusers/')
def showalluserdetails():
    users = session.query(User)

    return render_template('showalluserdetails.html',users=users)

# Show all job
@app.route('/alljobs/')
def showalljobdetails():
    jobs = session.query(Job).all()
    return render_template('showalljobdetails.html', jobs=jobs)


@app.route('/user/<int:user_id>/details')
def userdetail(user_id):
    user = session.query(User).filter_by(user_id=user_id).one()
    userskill = session.query(Userskill).filter_by(user_id=user_id).all()
    return render_template("userdetail.html", user=user, userskill=userskill)


@app.route('/job/<int:job_id>/details')
def jobdetail(job_id):
    job = session.query(Job).filter_by(job_id=job_id).one()
    jobskill = session.query(Jobskill).filter_by(job_id=job_id).all()
    return render_template("jobdetail.html", job=job, jobskill=jobskill)

'''
@app.route('/user/new/skill', methods=['GET', 'POST'])
def addskill():
    if request.method =='POST':
        global x
        x = random.randrange(8,100)
        skilluser = Userskill(
                    user_skill_id = x,
                    user_id = x,
                    skill_no = request.form['skill'])
        session.add(skilluser)
        session.commit()
        return redirect(url_for('addskill'))
    else:
        return render_template('addskill.html')
'''

# Create a new user
@app.route('/user/new/', methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        x = random.randrange(8,100)
        newuser = User(
            user_id=x,
            user_name=request.form['name'],
            user_phone=request.form['phone'],
            user_email=request.form['email'])
        session.add(newuser)
        flash('New User %s Successfully Created' % newuser.user_name)
        session.commit()
        return redirect(url_for('initialpage'))
    else:
        return render_template('newuser.html')


# Edit a user
@app.route('/user/<int:user_id>/edit/', methods=['GET', 'POST'])
def edituser(user_id):

    edituser = session.query(User).filter_by(user_id=user_id).one()
    editskill = session.query(Userskill).filter_by(user_id=user_id).all()
    if request.method == 'POST':
        if request.form['name']:
            edituser.user_name = request.form['name']
        if request.form['phone']:
            edituser.user_phone = request.form['phone']
        if request.form['email']:
            edituser.user_email = request.form['email']
        if request.form['skill']:
            editskill.skill_no = request.form['skill']

        flash('User Successfully Edited %s' % edituser.user_name)
        return redirect(url_for('showalluserdetails'))
    else:
        return render_template(
            'edituserdetails.html', user=edituser, userskill=editskill)


# Delete a user
@app.route('/user/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteuser(user_id):

    userToDelete = session.query(
        User).filter_by(user_id=user_id).one()

    if request.method == 'POST':
        session.delete(userToDelete)

        flash('%s Successfully Deleted' % userToDelete.user_name)
        session.commit()
        return redirect(url_for('initialpage'))
    else:
        return render_template(
            'deleteuser.html', user=userToDelete)

_jobskill_no_ =1
# Create a new job
@app.route('/job/new/', methods=['GET', 'POST'])
def newjob():

    if request.method == 'POST':
        x = random.randrange(1,1000)
        newjob = Job(

            job_id=x,
            job_name=request.form['name'],
            job_contact_person=request.form['contact_person'],
            job_contact_email=request.form['email'])
        session.add(newjob)
        skilljob = Jobskill(job_skill_id=x,
                    job_id=x,
                    required_skill_no=request.form['skill'])
        session.add(skilljob)
        flash('New Job %s Successfully Created' % newjob.job_name)
        session.commit()
        return redirect(url_for('showalljobdetails'))
    else:
        return render_template('newjob.html')


# Edit a job
@app.route('/job/<int:job_id>/edit/', methods=['GET', 'POST'])
def editjob(job_id):

    editjob = session.query(Job).filter_by(job_id=job_id).one()
    editskill = session.query(Jobskill).filter_by(job_id=job_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editjob.job_name = request.form['name']
        if request.form['email']:
            editjob.job_contact_email = request.form['email']
        if request.form['contact_person']:
            editjob.job_contact_person = request.form['contact_person']
        if request.form['skill']:
            editskill.required_skill_no = request.form['skill']
        flash('Job Successfully Edited %s' % editjob.job_name)
        return redirect(url_for('showalljobdetails'))
    else:
        return render_template(
            'editjobdetails.html', job=editjob, jobskill=editskill)


# Delete a job
@app.route('/job/<int:job_id>/delete/', methods=['GET', 'POST'])
def deletejob(job_id):


    jobToDelete = session.query(
        Job).filter_by(job_id=job_id).one()

    if request.method == 'POST':
        session.delete(jobToDelete)

        flash('%s Successfully Deleted' % jobToDelete.job_name)
        session.commit()
        return redirect(url_for('initialpage'))
    else:
        return render_template(
            'deletejob.html', job=jobToDelete)

def my_function(x):
  return list(dict.fromkeys(x))

#job search
@app.route('/topjobs/<int:user_id>/search',methods=['GET'])
def jobsearchbyuser(user_id):
    user = session.query(User).filter_by(user_id=user_id).one()
    userskill = session.query(Userskill).filter_by(user_id=user_id).all()
    jobskill = session.query(Jobskill).all()
    finaljoblist = list()
    userarray=list()
    for i in userskill:
        userarray.append(i.skill_no)
    jobcount=0

    for i in jobskill:
        jobarray=list()
        for j in jobskill:
            if j.job_id == i.job_id:
                jobarray.append(j.required_skill_no)
        for k in userarray:
            for l in jobarray:
                if k == l:
                    jobcount-=-1
        if jobcount >= len(jobarray)-1:
            finaljoblist.append(i.job_id)
            jobcount=0
    mylist = my_function(finaljoblist)
    jobs =  session.query(Job).filter(Job.job_id.in_(mylist)).all()
    return render_template('jobsearch.html', job=jobs, user = user)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
