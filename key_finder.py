from urllib import response

import requests
import operator


url = f"https://api.hh.ru/vacancies?search_field=name&text='Machine learning' OR 'ML'&area=113&items_on_page=1999&per_page=100"

response = requests.get(url)

key_skills = []
dict_key_skills = {}

#print(response.content.decode('utf-8'))
pages = response.json()['pages']
for i in range(pages):
    response_for_page = requests.get(f"{url}&page={i}")
    print(f"{url}&page={i}")
    data = response_for_page.json()['items']

    selected_vacancies = []
    dict_unique_vacancies = []

    for i in range(len(data)):
        temp_list = [data[i]['employer']['name'], data[i]['name']]

        if temp_list not in dict_unique_vacancies:
            selected_vacancies.append(data[i])
            dict_unique_vacancies.append(temp_list)

    #print('Словарь уникальных работодателей с уникальными вакансиями:', dict_unique_vacancies)

    for vaсancy in selected_vacancies:
        url_vacancy = vaсancy['url']
        response_vacancy =  requests.get(url_vacancy)
        data_vacancy = response_vacancy.json()
        key_skills_one_vacancy = data_vacancy['key_skills']
        for i in key_skills_one_vacancy:
            key_skill = i['name']
            dict_key_skills[key_skill] = dict_key_skills.get(key_skill, 0) + 1
            #key_skills.append((key_skill['name'],1))

    # print(key_skills)
    # print(dict_key_skills)
    # print(type(data))

sorted_dict_key_skills = sorted(dict_key_skills.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_dict_key_skills)
for item in sorted_dict_key_skills:
    print(f"{item[0]}: {item[1]}", end='\n')





