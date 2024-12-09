import json #Библиотека
num = str(input("Введите номер квалификации: ")) #Ввод искомой класификации
file = 'dump.json' #Переменная с названием файла
skills = False #Переменная для проверки
with open(file, 'r', encoding='utf-8') as file: #Открываем файл 
    data = json.load(file) #Сохраняем файл в переменную 
    for skill in data: #Перебор
        if skill.get("model") == "data.skill":
            if skill["fields"].get("code") == num: #Условие
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")
                skills = True
                for profession in data: #Перебор
                    if profession.get("model") == "data.specialty": #Условие
                        specialty_code = profession["fields"].get("code")
                        if specialty_code in num:  #Условие
                            specialty_title = profession["fields"].get("title")
                            specialty_educational = profession["fields"].get("c_type")
                            break #Выход
                break
if not skills: 
    print("=============== Не Найдено ===============") 
else:
    print("=============== Найдено ===============") 
    print(f"{specialty_code} >> Специальность {specialty_title} , {specialty_educational}")
    print(f"{skill_code} >> Квалификация {skill_title}")
