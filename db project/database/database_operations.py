import psycopg2

def connect_db():
    return psycopg2.connect(
        host="78.38.35.219",
        database="401463151",
        user="401463151",
        password="123456",
        port="5432"
    )

def select_employment_questionnaires():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM EmploymentQuestionnaire')
        records = cursor.fetchall()
        for row in records:
            print(f"questionnaire_id: {row[0]}, PersonalInformation: {row[2]}, job_requested: {row[8]}")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error retrieving Employment Questionnaires: {error}")

def insert_employment_questionnaire():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        questionnaire_id = input("questionnaire_id: ")
        PersonalInformation = input("PersonalInformation: ")
        medical_history_code = input("medical_history_code: ")
        detention_code = input("detention_code: ")
        EducationalBackground = input("EducationalBackground: ")
        TechnicalCourses = input("TechnicalCourses: ")
        salary_code = input("salary_code: ")
        job_requested = input("job_requested: ")
        WorkExperience = input("WorkExperience: ")
        insurance_and_benefits = input("insurance_and_benefits: ")
        RelativesInformation = input("RelativesInformation: ")
        reason_for_leaving_previous_job = input("reason_for_leaving_previous_job: ")
        ResidentialAddress = input("ResidentialAddress: ")
        cooperation_number = input("cooperation_number: ")
        Dependents = input("Dependents: ")
        
        cursor.execute('''
            INSERT INTO EmploymentQuestionnaire (questionnaire_id, PersonalInformation, medical_history_code, detention_code, 
            EducationalBackground, TechnicalCourses, salary_code, job_requested, WorkExperience, 
            insurance_and_benefits, RelativesInformation, reason_for_leaving_previous_job, 
            ResidentialAddress, cooperation_number, Dependents)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (questionnaire_id, PersonalInformation, medical_history_code, detention_code, 
              EducationalBackground, TechnicalCourses, salary_code, job_requested, WorkExperience, 
              insurance_and_benefits, RelativesInformation, reason_for_leaving_previous_job, 
              ResidentialAddress, cooperation_number, Dependents))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Employment Questionnaire added successfully.")
    except Exception as error:
        print(f"Error adding Employment Questionnaire: {error}")

def update_employment_questionnaire():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        questionnaire_id = input("questionnaire_id: ")
        PersonalInformation = input("New PersonalInformation: ")
        job_requested = input("New job_requested: ")
        
        cursor.execute('''
            UPDATE EmploymentQuestionnaire 
            SET PersonalInformation = %s, job_requested = %s
            WHERE questionnaire_id = %s
        ''', (PersonalInformation, job_requested, questionnaire_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Employment Questionnaire updated successfully.")
    except Exception as error:
        print(f"Error updating Employment Questionnaire: {error}")

def delete_employment_questionnaire():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        questionnaire_id = input("Enter questionnaire_id to delete: ")
        
        cursor.execute('''
            DELETE FROM EmploymentQuestionnaire WHERE questionnaire_id = %s
        ''', (questionnaire_id,))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Employment Questionnaire deleted successfully.")
    except Exception as error:
        print(f"Error deleting Employment Questionnaire: {error}")

def select_dependents():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Dependents')
        records = cursor.fetchall()
        for row in records:
            print(f"questionnaire_id: {row[0]}, full_name: {row[1]}, gender: {row[2]}, relationship: {row[3]}, birth_date: {row[4]}, education_level: {row[5]}, job: {row[6]}")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error retrieving Dependents: {error}")

def insert_dependent():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        questionnaire_id = input("questionnaire_id: ")
        full_name = input("full_name: ")
        gender = input("gender: ")
        relationship = input("relationship: ")
        birth_date = input("birth_date: ")
        education_level = input("education_level: ")
        job = input("job: ")
        
        cursor.execute('''
            INSERT INTO Dependents (questionnaire_id, full_name, gender, relationship, birth_date, education_level, job)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (questionnaire_id, full_name, gender, relationship, birth_date, education_level, job))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Dependent added successfully.")
    except Exception as error:
        print(f"Error adding Dependent: {error}")

def update_dependent():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        questionnaire_id = input("questionnaire_id: ")
        full_name = input("New full_name: ")
        gender = input("New gender: ")
        relationship = input("New relationship: ")
        birth_date = input("New birth_date: ")
        education_level = input("New education_level: ")
        job = input("New job: ")
        
        cursor.execute('''
            UPDATE Dependents 
            SET full_name = %s, gender = %s, relationship = %s, birth_date = %s, education_level = %s, job = %s
            WHERE questionnaire_id = %s
        ''', (full_name, gender, relationship, birth_date, education_level, job, questionnaire_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Dependent updated successfully.")
    except Exception as error:
        print(f"Error updating Dependent: {error}")

def delete_dependent():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        questionnaire_id = input("Enter questionnaire_id to delete: ")
        
        cursor.execute('''
            DELETE FROM Dependents WHERE questionnaire_id = %s
        ''', (questionnaire_id,))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Dependent deleted successfully.")
    except Exception as error:
        print(f"Error deleting Dependent: {error}")
        
        
 #شرط ON eq.questionnaire_id = d.questionnaire_id مشخص می‌کند که این دو جدول بر اساس 
#questionnaire_id مرتبط هستند.
#این عملیات به شما اجازه می‌دهد تا اطلاعات مربوط به 
#پرسش‌نامه‌ها و وابستگان را در یک مجموعه داده ترکیبی مشاهده کنید.                
        
def select_join_employment_dependents():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT e.questionnaire_id, e.PersonalInformation, e.job_requested, d.full_name, d.gender, d.relationship 
            FROM EmploymentQuestionnaire e
            JOIN Dependents d ON e.questionnaire_id = d.questionnaire_id
        ''')
        records = cursor.fetchall()
        for row in records:
            print(f"questionnaire_id: {row[0]}, PersonalInformation: {row[1]}, job_requested: {row[2]}, full_name: {row[3]}, gender: {row[4]}, relationship: {row[5]}")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error retrieving Employment Questionnaires with Dependents: {error}")

def select_left_join_employment_dependents():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT e.questionnaire_id, e.PersonalInformation, e.job_requested, d.full_name, d.gender, d.relationship 
            FROM EmploymentQuestionnaire e
            LEFT JOIN Dependents d ON e.questionnaire_id = d.questionnaire_id
            WHERE d.gender = 'male' 
        ''')
        records = cursor.fetchall()
        for row in records:
            print(f"questionnaire_id: {row[0]}, PersonalInformation: {row[1]}, job_requested: {row[2]}, full_name: {row[3]}, gender: {row[4]}, relationship: {row[5]}")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error retrieving Employment Questionnaires with Male Dependents: {error}")

def select_aggregated_employment_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT 
                COUNT(*) as total_entries,
                AVG(salary_code) as avg_salary,
                MAX(salary_code) as max_salary,
                MIN(salary_code) as min_salary
            FROM EmploymentQuestionnaire
        ''')
        result = cursor.fetchone()
        print(f"Total Entries: {result[0]}, Average Salary Code: {result[1]}, Maximum Salary Code: {result[2]}, Minimum Salary Code: {result[3]}")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Error retrieving aggregated Employment Questionnaire data: {error}")



        
  
        