import pickle

MODEL_PATH = './artifacts/model.bin'
VECTORIZER_PATH = './artifacts/vectorizer.bin'


with open(MODEL_PATH,'rb') as file:
    model = pickle.load(file)
    print("Model has been loaded !")

with open(VECTORIZER_PATH,'rb') as file :
    dv = pickle.load(file)
    print("DV has been loaded !")


from flask import Flask, render_template, redirect, url_for, flash,request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FloatField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length,InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '$$$FLSK'

class EmployeeForm(FlaskForm):
    department = SelectField('Department', choices=[
        ('IT', 'IT'), ('HR', 'HR'), ('Finance', 'Finance'),
        ('Operations', 'Operations'), ('Sales', 'Sales'), ('Customer Support', 'Customer Support'),
        ('Engineering', 'Engineering'),('Marketing','Marketing'),('Legal','Legal')
    ], validators=[DataRequired()], render_kw={"placeholder": "test"})
    
    gender = SelectField('Gender', choices=[
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    ], validators=[DataRequired()])
    
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=70)])
    job_title = SelectField('Job Title',choices=[
        ('Specialist','Specialist'),('Developer','Developer'),('Analyst','Analyst'),
        ('Manager','Manager'),('Technician','Technician'),('Engineer','Engineer'),('Consultant','Consultant')
    ], validators=[DataRequired()])
    years_at_company = IntegerField('Years at Company', validators=[DataRequired()])
    education_level = SelectField('Education Level', choices=[
        ('High School', 'High School'),
        ("Bachelor", "Bachelor's Degree"),
        ("Master", "Master's Degree"),
        ("PhD", "Doctorate")
    ], validators=[DataRequired()])
    
    performance_score = IntegerField('Performance Score', validators=[DataRequired(), NumberRange(min=1, max=10)])
    monthly_salary = FloatField('Monthly Salary', validators=[DataRequired()])
    work_hours_per_week = IntegerField('Work Hours per Week', validators=[DataRequired(), NumberRange(min=0, max=148)])
    projects_handled = IntegerField('Projects Handled', validators=[DataRequired()])
    overtime_hours = IntegerField('Overtime Hours', validators=[DataRequired()])
    sick_days = IntegerField('Sick Days', validators=[DataRequired()])
    remote_work_frequency = IntegerField('Remote Work Frequency', validators=[DataRequired()])
    team_size = IntegerField('Team Size', validators=[DataRequired()])
    training_hours = IntegerField('Training Hours', validators=[DataRequired()])
    promotions = IntegerField('Promotions', validators=[InputRequired("You got to enter some rating!")])
    submit = SubmitField('Predict Satisfaction Score')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = EmployeeForm()
    if form.validate_on_submit():
        # Handle the data to make predictions or further processing
        flash("Prediction successfully submitted!", "success")
        data = {'Department': form.department.data,
                    'Gender': form.gender.data,
                    'Age': form.age.data,
                    'Job_Title': form.job_title.data,
                    'Years_At_Company': form.years_at_company.data,
                    'Education_Level': form.education_level.data,
                    'Performance_Score': form.performance_score.data,
                    'Monthly_Salary': form.monthly_salary.data,
                    'Work_Hours_Per_Week': form.work_hours_per_week.data,
                    'Projects_Handled': form.projects_handled.data,
                    'Overtime_Hours': form.overtime_hours.data,
                    'Sick_Days': form.sick_days.data,
                    'Remote_Work_Frequency': form.remote_work_frequency.data,
                    'Team_Size': form.team_size.data,
                    'Training_Hours': form.training_hours.data,
                    'Promotions': form.promotions.data}
        
        data = dv.transform(data)
        score = model.predict(data)
        return redirect(url_for('result',score=score[0]),code=307)
    return render_template('index.html', form=form)

@app.route('/result/<score>',methods=['GET','POST'])
def result(score):
    if request.method == 'GET':
        return "Server is up"
    satisfaction_score = float(score)
    print(satisfaction_score)
    satisfaction_icon = "😊"  # Icon based on score
    satisfaction_message = "Content with the job!"  # Message based on score

    # Render the template with dynamic values
    return render_template('result.html', 
                           satisfaction_score=satisfaction_score,
                           satisfaction_icon=satisfaction_icon,
                           satisfaction_message=satisfaction_message)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
