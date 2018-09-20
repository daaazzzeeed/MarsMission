import random
import math
import sys

colonists_list = list()
new_colonists_list_male = list()
new_colonists_list_female = list()
manager_fem_list = list()
manager_mal_list = list()
cook_fem_list = list()
cook_mal_list = list()
elen_fem_list = list()
elen_mal_list = list()
compspec_fem_list = list()
compspec_mal_list = list()
doc_fem_list = list()
doc_mal_list = list()
mech_fem_list = list()
mech_mal_list = list()
sci_fem_list = list()
sci_mal_list = list()
lucky_colonists = list()

luck_list = [random.randint(0, 100) for i in range(100)]

managers = 1
cooks = 3
electrical_engineers = 4
computer_system_specialists = 5
medics = 5
mechanics = 8
scientists = 14

def pick_percentage(low, high):
    return random.randint(low, high)/100

perc_male = pick_percentage(30, 49)
perc_female = pick_percentage(51, 69)

quantity_required = 40
quantity_of_women_required = math.ceil(quantity_required * perc_female)
min_percentage_fem = quantity_of_women_required/quantity_required
quantity_of_men_required = quantity_required * perc_male
min_percentage_mal = quantity_of_men_required/quantity_required

unsorted_list = list()
while 1:
    try:
        line = input()
    except EOFError:
        break
        unsorted_list.append(line)

sorted_list = list()
for i in unsorted_list:
    sorted_list.append(i.split(';'))

# сортировка по рейтингу
for item in sorted_list:
    if int(item[3]) >= 60:
        colonists_list.append(item)

counter = 0

conditions = "1. Crew must include all specialists essential for the colony: 1 manager, 3 cooks," \
             " 4 electrical engineers, 5 computer system specialists, 5 medics, 8 mechanics, 14 " \
             "scientists. 2. The colony have to exist for several generations, so at least 51% " \
             "of selected colonists must be female. Don't forget about men, at least 30% of colonists must be male."\
             "3. Colonists will face all kinds of harsh conditions. Only the most resilient people should colonize " \
             "the planet. Select people with resilience rating 60 and more on scale from 1 to 100."

# отсортируем женщин
for item in colonists_list:
    if int(item[2]) == 0:
        new_colonists_list_female.append(item)

# отсортируем мужчин
for item in colonists_list:
    if int(item[2]) == 1:
        new_colonists_list_male.append(item)

# отсортируем по профессиям женщин
for item in new_colonists_list_female:
    if item[1] == 'manager':
        manager_fem_list.append(item)

for item in new_colonists_list_female:
    if item[1] == 'cook':
        cook_fem_list.append(item)

for item in new_colonists_list_female:
    if item[1] == 'electrical engineer':
        elen_fem_list.append(item)

for item in new_colonists_list_female:
    if item[1] == 'computers specialist':
        compspec_fem_list.append(item)

for item in new_colonists_list_female:
    if item[1] == 'doctor':
        doc_fem_list.append(item)

for item in new_colonists_list_female:
    if item[1] == 'mechanic':
        mech_fem_list.append(item)

for item in new_colonists_list_female:
    if item[1] == 'scientist':
        sci_fem_list.append(item)

# отсортируем по профессиям мужчин
for item in new_colonists_list_male:
    if item[1] == 'manager':
        manager_mal_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'cook':
        cook_mal_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'electrical engineer':
        elen_mal_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'computers specialist':
        compspec_mal_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'doctor':
        doc_mal_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'mechanic':
        mech_mal_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'scientist':
        sci_mal_list.append(item)

# Подберем колонистов


def percentage_is_ok(colonists):
    female_quantity = 0
    female_is_ok = 1
    male_is_ok = 1
    for i in colonists:
        if int(i[2]) == 0:
            female_quantity = female_quantity + 1
    percentage_female = female_quantity/int(len(colonists))
    percentage_male = 1 - percentage_female
    if percentage_female < min_percentage_fem:
        female_is_ok = 0
    elif percentage_male < min_percentage_mal:
        male_is_ok = 0
    return [female_is_ok, male_is_ok, percentage_female, percentage_male, female_quantity]


def choose_colonists(female, male, quantity, resulting_list):
    for i in range(quantity):
        if int(percentage_is_ok(resulting_list)[0]) == 0 and len(female) > 0:
            colonist_choice = random.choice(female)
            resulting_list.append(colonist_choice)
            female.remove(colonist_choice)
        elif int(percentage_is_ok(resulting_list)[1]) == 0 and len(male) > 0:
            colonist_choice = random.choice(male)
            resulting_list.append(colonist_choice)
            male.remove(colonist_choice)
        else:
            if len(male) > 0 and len(female) > 0:
                sex_choice = random.choice([female, male])
                colonist_choice = random.choice(sex_choice)
                resulting_list.append(colonist_choice)
                sex_choice.remove(colonist_choice)
            else:
                if len(male) == 0:
                    colonist_choice = random.choice(female)
                    resulting_list.append(colonist_choice)
                    sex_choice.remove(colonist_choice)
                elif len(female) == 0:
                    colonist_choice = random.choice(male)
                    resulting_list.append(colonist_choice)
                    sex_choice.remove(colonist_choice)


# управляющих
if int(random.choice(luck_list)) >= 50:
    choice = random.choice(manager_fem_list)
    lucky_colonists.append(choice)
else:
    choice = random.choice(manager_mal_list)
    lucky_colonists.append(choice)

# поваров
choose_colonists(cook_fem_list, cook_mal_list, cooks, lucky_colonists)

# электроинженеров
choose_colonists(elen_fem_list, elen_mal_list, electrical_engineers, lucky_colonists)

# компьютерных инженеров
choose_colonists(compspec_fem_list, compspec_mal_list, computer_system_specialists, lucky_colonists)

# медиков - частный случай
doctors_left = 1
for i in range(medics):
    if int(percentage_is_ok(lucky_colonists)[0]) == 0:
        choice = random.choice(doc_fem_list)
        lucky_colonists.append(choice)
        doc_fem_list.remove(choice)
    elif doctors_left > 0:
        choice = random.choice(doc_mal_list)
        lucky_colonists.append(choice)
        doc_mal_list.remove(choice)
        doctors_left = 0
    else:
        choice = random.choice(doc_fem_list)
        lucky_colonists.append(choice)
        doc_fem_list.remove(choice)

# механиков - частный случай
mechanics_male_left = 6
for i in range(mechanics):
    if int(percentage_is_ok(lucky_colonists)[0]) == 0:
        choice = random.choice(mech_fem_list)
        lucky_colonists.append(choice)
        mech_fem_list.remove(choice)
    elif mechanics_male_left > 0:
        choice = random.choice(mech_mal_list)
        lucky_colonists.append(choice)
        mech_mal_list.remove(choice)
        mechanics_male_left = mechanics_male_left - 1
    else:
        choice = random.choice(mech_fem_list)
        lucky_colonists.append(choice)

# ученых
choose_colonists(sci_fem_list, sci_mal_list, scientists, lucky_colonists)

colonists_string = ''

for item in lucky_colonists:
    colonists_string = colonists_string + item[0] + ';'
colonists_string = colonists_string[0:len(colonists_string)-1]

sys.stdout.write(colonists_string)
