# БД - структурированный набор данных
# СУБД - инструмент для работы с базами данных
# Реляционные бд - бд, в которых есть связи между данными
# Постреляционная бд - расширенная реляционная
# Многомерная
# Всегда должен быть Primary key (Лучше это будет ID) (не повторяются) - первичный ключ
# Super key - состоит из нескольких Primary key
# Foreign key - внешние ключи
# CREATE DATABASE sample;    # писать заглавными буквами, в конце всегда точка с запятой
# ALTER DATABASE sample RENAME TO example;
# CREATE TABLE "StudentGrades" (
# "StudentName" VARCHAR(255),
# "BirthDate" DATE,
# "AverageGrade" decimal
# );
# SELECT * FROM "StudentGrades";    # Вывод всех полей
# SELECT "StudentName", "BirthDate" FROM "StudentGrades";    # Вывод конкретных полей
# SELECT DISTINCT "City" FROM "StudentGrades";    # Вывод уникальных городов
# INSERT INTO "StudentGrades" ("StudentName") VALUES ('Ivan Ivanov');    # Добавить строку
# DELETE FROM "StudentGrades" WHERE "StudenName" = 'Ivan Ivanov';    # Удаление значения
# UPDATE "StudentGrades" set "PhoneNumber" = '79999999999' "City" = 'Moscow' WHERE "StudentName" = 'Ivan Ivanov';
# SELECT "StudentName" FROM "StudentGrades" WHERE "AverageGrade" BETWEEN 3 AND 4.5;    # Сравнение
# FOREIGN KEY(BOOK_REF) REFERENCES BOOKINGS (BOOK_REF)

# SERIAL - Инт, который автоматически увеличивается на 1 (всегда уникальный)
# DELETE - удаление данных (атрибутов)
# DROP - удаление всего остального

# Аномалия модификации -
# Аномалия удаления -
# Аномалия добавления -

# DDL - Data Definition Lang - drop, create, alter (работа с таблицами)
# DML - Data Manipulation Lang - select, delete, update, insert (работа с данными в таблице)
# DCL - Data Control Lang - grant, revoke, deny (управление правами пользователя, доступ)
# TCL - Transaction Control Lang - begin, commit, rollback (чтобы не появлялись аномалии)

# Первая нормальная форма - если все атрибуты являются простыми (данные атомарны)
# Вторая норм форма - если находится в первой норм форме и если
# Третья - деление на таблицы и взаимосвязаны

# Связи: один к одному, один к многим, многие к многим

# INSERT INTO BOOKINGS (BOOK_REF, BOOK_DATE, TOTAL_AMOUNT)
# VALUES
# ('AK768D', '2023-03-14', 7890.2),
# ('BV543D', '2023-03-16', 5670, 4);



