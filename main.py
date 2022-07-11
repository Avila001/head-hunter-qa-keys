import imp
from urllib import response

import requests
import operator


print('Hello!')

class Vacancy:
    pass

response = requests.get("https://api.hh.ru/vacancies?text=тестировщик&area=113&employer_id=1178447")

#print(response.content.decode('utf-8'))
data = response.json()['items']

selected_vacancies = []
dict_unique_vacancies = []

for i in range(len(data)):
    temp_list = [data[i]['employer']['name'], data[i]['name']]
    print(temp_list, type(temp_list))
    if temp_list not in dict_unique_vacancies:
        selected_vacancies.append(data[i])
        dict_unique_vacancies.append(temp_list)

print('Словарь уникальных работодателей с уникальными вакансиями:', dict_unique_vacancies)

key_skills = []
dict_key_skills = {}

for vaсancy in selected_vacancies:
    url = vaсancy['url']
    response_vacancy =  requests.get(url)
    data_vacancy = response_vacancy.json()
    key_skills_one_vacancy = data_vacancy['key_skills']
    print(data_vacancy['key_skills'])
    print(key_skills_one_vacancy)
    for i in key_skills_one_vacancy:
        key_skill = i['name']
        dict_key_skills[key_skill] = dict_key_skills.get(key_skill, 0) + 1
        #key_skills.append((key_skill['name'],1))

print(key_skills)
print(dict_key_skills)
print(type(data))

sorted_dict_key_skills = sorted(dict_key_skills.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_dict_key_skills)



