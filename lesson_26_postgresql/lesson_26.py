# БД - структурированный набор данных
# Реляционные бд - бд, в которых есть связи между данными
# Всегда должен быть Primary key (Лучше это будет ID) (не повторяются)
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

