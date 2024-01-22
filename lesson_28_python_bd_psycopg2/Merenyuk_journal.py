# Journal

import psycopg2

conn = psycopg2.connect(dbname='students', host='localhost', user='postgres', password='1', port='5432')
cursor = conn.cursor()


def add_student(firstname, lastname):
    cursor.execute(f'''INSERT INTO students(firstname, lastname) VALUES('{firstname}', '{lastname}');''')
    conn.commit()


def add_grade(student_id, subject, grade):
    cursor.execute(f'''INSERT INTO grades(studentid, subject, grade) VALUES('{student_id}', '{subject}', '{grade}');''')
    conn.commit()


def menu():
    flag = True
    while flag:
        try:
            choice = int(input('\n1-Set student\'s firstname and lastname;'
                               '\n2-Give a grade from id;'
                               '\n3-Exit from program. -> '))
            if choice == 1:
                firstname = str(input('Enter student\'s firsname: '))
                lastname = str(input('Enter student\'s lastname: '))
                add_student(firstname, lastname)
                print('\nStudent added!')
            elif choice == 2:
                student_id = int(input('Enter student\'s id: '))
                subject = str(input('Enter subject: '))
                grade = int(input('Enter student\'s grade: '))
                add_grade(student_id, subject, grade)
                print('\nGrade given!')
            elif choice == 3:
                print('\nProgram work is finished.')
                flag = False
            else:
                print('\nInvalid input! Try again.')
        except ValueError:
            print('\nInvalid input! Try again.')


menu()

conn.close()
cursor.close()