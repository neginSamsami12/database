from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        host="78.38.35.219",
        database="401463151",
        user="401463151",
        password="123456",
        port="5432"
    )

@app.route('/')
def index():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        
        # Select all records from EmploymentQuestionnaire table
        cursor.execute('SELECT * FROM EmploymentQuestionnaire')
        records = cursor.fetchall()

        # Aggregated data query
        cursor.execute('''
            SELECT 
                SUM(salary_code), 
                AVG(salary_code), 
                MAX(salary_code), 
                MIN(salary_code),
                SUM(detention_code * cooperation_number * medical_history_code * salary_code) AS calculation_result
            FROM EmploymentQuestionnaire
        ''')
        aggregated_data = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return render_template('index.html', records=records, aggregated_data=aggregated_data)
    except Exception as error:
        return f"Error retrieving Employment Questionnaires: {error}"



@app.route('/dependents')
def dependents():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Dependents')
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('dependents.html', records=records)
    except Exception as error:
        return f"Error retrieving Dependents: {error}"

@app.route('/insert_employment_questionnaire', methods=['GET', 'POST'])
def insert_employment_questionnaire():
    if request.method == 'POST':
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO EmploymentQuestionnaire (questionnaire_id, PersonalInformation, medical_history_code, detention_code, 
                EducationalBackground, TechnicalCourses, salary_code, job_requested, WorkExperience, 
                insurance_and_benefits, RelativesInformation, reason_for_leaving_previous_job, 
                ResidentialAddress, cooperation_number, Dependents)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                request.form['questionnaire_id'], request.form['PersonalInformation'], request.form['medical_history_code'], 
                request.form['detention_code'], request.form['EducationalBackground'], request.form['TechnicalCourses'], 
                request.form['salary_code'], request.form['job_requested'], request.form['WorkExperience'], 
                request.form['insurance_and_benefits'], request.form['RelativesInformation'], 
                request.form['reason_for_leaving_previous_job'], request.form['ResidentialAddress'], 
                request.form['cooperation_number'], request.form['Dependents']
            ))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect('/')
        except Exception as error:
            return f"Error adding Employment Questionnaire: {error}"
    return render_template('insert_employment_questionnaire.html')

@app.route('/insert_dependent', methods=['GET', 'POST'])
def insert_dependent():
    if request.method == 'POST':
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO Dependents (questionnaire_id, full_name, gender, relationship, birth_date, education_level, job)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (
                request.form['questionnaire_id'], request.form['full_name'], request.form['gender'], 
                request.form['relationship'], request.form['birth_date'], request.form['education_level'], 
                request.form['job']
            ))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect('/dependents')
        except Exception as error:
            return f"Error adding Dependent: {error}"
    return render_template('insert_dependent.html')

@app.route('/update_employment_questionnaire', methods=['GET', 'POST'])
def update_employment_questionnaire():
    if request.method == 'POST':
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE EmploymentQuestionnaire 
                SET PersonalInformation = %s, job_requested = %s, medical_history_code = %s, detention_code = %s, EducationalBackground = %s,
                TechnicalCourses = %s, salary_code = %s, WorkExperience = %s, insurance_and_benefits = %s, RelativesInformation = %s,
                reason_for_leaving_previous_job = %s, ResidentialAddress = %s, cooperation_number = %s, Dependents = %s
                WHERE questionnaire_id = %s
            ''', (
                request.form['PersonalInformation'], request.form['job_requested'], request.form['medical_history_code'], 
                request.form['detention_code'], request.form['EducationalBackground'], request.form['TechnicalCourses'], 
                request.form['salary_code'], request.form['WorkExperience'], request.form['insurance_and_benefits'], 
                request.form['RelativesInformation'], request.form['reason_for_leaving_previous_job'], 
                request.form['ResidentialAddress'], request.form['cooperation_number'], request.form['Dependents'], 
                request.form['questionnaire_id']
            ))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect('/')
        except Exception as error:
            return f"Error updating Employment Questionnaire: {error}"
    else:
        questionnaire_id = request.args.get('id')
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM EmploymentQuestionnaire WHERE questionnaire_id = %s', (questionnaire_id,))
            record = cursor.fetchone()
            cursor.close()
            connection.close()
            if record:
                return render_template('update_employment_questionnaire.html', record=record)
            else:
                return f"No record found with questionnaire_id = {questionnaire_id}"
        except Exception as error:
            return f"Error retrieving Employment Questionnaire: {error}"

@app.route('/update_dependent', methods=['GET', 'POST'])
def update_dependent():
    if request.method == 'POST':
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE Dependents
                SET full_name = %s, gender = %s, relationship = %s, birth_date = %s, education_level = %s, job = %s
                WHERE questionnaire_id = %s
            ''', (
                request.form['full_name'], request.form['gender'], request.form['relationship'],
                request.form['birth_date'], request.form['education_level'], request.form['job'],
                request.form['questionnaire_id']
            ))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect('/dependents')
        except Exception as error:
            return f"Error updating Dependent: {error}"
    else:
        questionnaire_id = request.args.get('questionnaire_id')
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Dependents WHERE questionnaire_id = %s', (questionnaire_id,))
            record = cursor.fetchone()
            cursor.close()
            connection.close()
            if record:
                return render_template('update_dependent.html', record=record)
            else:
                return f"No record found with questionnaire_id = {questionnaire_id}"
        except Exception as error:
            return f"Error retrieving Dependent: {error}"
        
@app.route('/delete_employment_questionnaire', methods=['GET', 'POST'])
def delete_employment_questionnaire():
    if request.method == 'POST':
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM EmploymentQuestionnaire WHERE questionnaire_id = %s', (request.form['questionnaire_id'],))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect('/')
        except Exception as error:
            return f"Error deleting Employment Questionnaire: {error}"
    else:
        questionnaire_id = request.args.get('id')
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM EmploymentQuestionnaire WHERE questionnaire_id = %s', (questionnaire_id,))
            record = cursor.fetchone()
            cursor.close()
            connection.close()
            if record:
                return render_template('delete_employment_questionnaire.html', record=record)
            else:
                return f"No record found with questionnaire_id = {questionnaire_id}"
        except Exception as error:
            return f"Error retrieving Employment Questionnaire: {error}"

@app.route('/delete_dependent', methods=['POST'])
def delete_dependent():
    questionnaire_id = request.form['questionnaire_id']
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Dependents WHERE questionnaire_id = %s', (questionnaire_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect('/dependents')
    except Exception as error:
        return f"Error deleting Dependent: {error}"

@app.route('/join_employment_dependents')
def join_employment_dependents():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT eq.questionnaire_id, eq.PersonalInformation,eq.job_requested ,d.full_name, d.relationship,d.gender
            FROM EmploymentQuestionnaire eq
            JOIN Dependents d ON eq.questionnaire_id = d.questionnaire_id
        ''')
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('join_employment_dependents.html', records=records)
    except Exception as error:
        return f"Error performing JOIN: {error}"

@app.route('/left_join_employment_dependents')
def left_join_employment_dependents():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT eq.questionnaire_id, eq.PersonalInformation, eq.job_requested, d.full_name, d.relationship, d.gender
            FROM EmploymentQuestionnaire eq
            LEFT JOIN Dependents d ON eq.questionnaire_id = d.questionnaire_id
            WHERE d.gender = 'female' 
        ''')
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('left_join_employment_dependents.html', records=records)
    except Exception as error:
        return f"Error performing LEFT JOIN: {error}"

if __name__ == '__main__':
    app.run()