import re

# text = 'milk how dogs python'

# match = re.search(r'\w{4}', text)
# print(match.group())


# matches = re.findall(r'\b\w{4,}\b', text)
# print(matches)


# text = '1234 124 748 78 5 147'
#
# match = re.findall(r'\b\d{3}\b', text)
#
# print(match)


# dates = '10.12.2001 15/01/2004 14.02.14 18-05-2024'
#
# matches = re.findall(r'\d{2}\.\d\d\.\d{4}', dates)
# matches_sub = re.sub(r'\d{2}-\d\d-\d{4}', r'dd.mm.yyyy', dates)
#
# print(matches_sub)


# text = 'Ivan, Bob; Maria: Petr'
#
# names = re.split(r'[,;:]', ''.join(text.split()))
# print(names)

# tels = '+79999999998 +7 (999)9999998 +7 (999)-999-9998 +7 (999)-99-999-78'
#
# correct_num = re.findall(r'\+7\s\(\d{3}\)-\d{2}-\d{3}-\d{2}', tels)
# print(correct_num)


# email = 'testmail.ru test@mail.ru test123@mail.com test@mail!com'
# correct_emails = re.findall(r'\w+@\w{2,20}\.[a-z]{2,3}', email)
# print(correct_emails)


# lorem = 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Accusantium velit corrupti sunt et dolorum minima sed iure est soluta praesentium blanditiis molestiae explicabo, dolores ducimus reprehenderit cumque expedita eveniet debitis.'

# matches = re.findall(r'\b\w{4}\b', lorem)
# print(matches)

# matches = re.findall(r'\w+,', lorem)
# print(matches)

# nomer = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П7777 666АМР666'
#
# private = re.findall(r'\w\d{3}\w{2}\d{3}', nomer)
# taxi = re.findall(r'\w{2}\d{3}\d{2,3}', nomer)
# print(private)
# print(taxi)

