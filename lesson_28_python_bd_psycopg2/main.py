# import psycopg2
#
# conn = psycopg2.connect(dbname='students', host='localhost', user='postgres', password='1', port='5432')
# cursor = conn.cursor()  # объект для взаимодействия с бд

# cursor.execute(
#     '''CREATE TABLE users(id serial PRIMARY KEY, first_name varchar NOT NULL, nick_name varchar NOT NULL);'''
# )  # complete

# cursor.execute(
#     '''INSERT INTO users(first_name, nick_name) VALUES('Oleg', 'OlegTop');'''
# )  # complete

# cursor.execute(
#     '''SELECT nick_name FROM users WHERE first_name = 'Stepan';'''
# )  # complete
# print(cursor.fetchone())  # вывод в консоль в кортеже

# cursor.execute(
#     ''' DROP TABLE users; '''
# )  # complete


# 1
# cursor.execute(
#     ''' SELECT airport_code, airport_name, city, coordinates FROM airports_data; '''
# )
# print(cursor.fetchall())

# 2
# cursor.execute(
#     ''' SELECT aircraft_code, model FROM aircrafts_data WHERE range > 5000; '''
# )
# print(cursor.fetchall())

# 3
# cursor.execute(
#     ''' SELECT passenger_name, contact_data FROM tickets WHERE passenger_name LIKE 'N%'; '''
# )
# print(cursor.fetchall())

# 4
# cursor.execute(
#     ''' SELECT airport_code, airport_name FROM airports_data WHERE city->>'en' IN ('Moscow'); '''
# )
# print(cursor.fetchall())

# 5
# cursor.execute(
#     ''' SELECT book_ref FROM tickets WHERE passenger_id = '8149 604011'; '''
# )
# print(cursor.fetchall())

# 6
# cursor.execute(
#     ''' SELECT flight_id, flight_no FROM flights WHERE actual_departure > scheduled_departure
#     ORDER BY flight_id LIMIT 5; '''
# )
# print(cursor.fetchall())

# 7
# cursor.execute(
#     ''' SELECT COUNT(*) FROM airports_data; '''
# )
# print(cursor.fetchall())


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
                flag = False
            else:
                print('\nInvalid input! Try again.')
        except ValueError:
            print('\nInvalid input! Try again.')


menu()

conn.close()
cursor.close()
