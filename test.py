import random
import math
import sys

data = """1;electrical engineer;0;90
2;mechanic;0;77
3;scientist;1;71
4;computers specialist;1;90
5;electrical engineer;1;40
6;manager;1;44
7;scientist;1;74
8;scientist;1;74
9;mechanic;0;50
10;mechanic;1;69
11;cook;1;68
12;computers specialist;1;100
13;cook;1;40
14;doctor;1;79
15;doctor;0;71
16;doctor;0;75
17;doctor;0;97
18;doctor;0;81
19;scientist;1;92
20;mechanic;0;68
21;cook;0;43
22;scientist;0;79
23;manager;1;65
24;mechanic;1;41
25;mechanic;0;93
26;mechanic;0;76
27;cook;1;91
28;electrical engineer;1;62
29;mechanic;1;48
30;electrical engineer;1;70
31;scientist;0;100
32;doctor;0;42
33;scientist;1;47
34;mechanic;0;63
35;scientist;0;92
36;scientist;1;60
37;manager;0;50
38;electrical engineer;1;44
39;scientist;0;81
40;computers specialist;0;62
41;doctor;0;84
42;mechanic;1;57
43;scientist;0;57
44;cook;1;41
45;scientist;0;75
46;mechanic;1;60
47;electrical engineer;1;81
48;doctor;0;88
49;mechanic;1;90
50;cook;0;68
51;doctor;1;54
52;manager;1;50
53;doctor;1;41
54;cook;0;89
55;electrical engineer;1;88
56;electrical engineer;1;93
57;electrical engineer;0;79
58;electrical engineer;0;75
59;scientist;0;92
60;doctor;1;59
61;cook;0;79
62;cook;0;75
63;scientist;0;42
64;electrical engineer;0;71
65;doctor;0;68
66;mechanic;1;53
67;mechanic;1;47
68;scientist;1;61
69;mechanic;0;53
70;doctor;1;52
71;cook;1;44
72;scientist;1;71
73;doctor;0;44
74;cook;1;62
75;scientist;0;63
76;scientist;0;84
77;electrical engineer;1;77
78;cook;0;79
79;mechanic;0;63
80;mechanic;0;81
81;scientist;0;97
82;doctor;0;99
83;scientist;1;60
84;cook;1;79
85;computers specialist;1;93
86;cook;1;79
87;scientist;0;70
88;computers specialist;0;80
89;mechanic;1;58
90;scientist;0;75
91;computers specialist;0;98
92;electrical engineer;1;88
93;doctor;0;54
94;mechanic;1;66
95;computers specialist;1;52
96;computers specialist;1;71
97;scientist;1;74
98;scientist;0;96
99;computers specialist;0;40
100;computers specialist;0;99
101;computers specialist;0;93
102;computers specialist;1;66
103;doctor;0;65
104;scientist;1;77
105;scientist;1;85
106;electrical engineer;1;100
107;computers specialist;1;68
108;manager;0;82
109;mechanic;0;70
110;cook;0;67
111;mechanic;1;64
112;scientist;0;66
113;electrical engineer;1;82
114;computers specialist;0;93
115;manager;1;60
116;cook;1;77
117;doctor;0;100
118;electrical engineer;1;97
119;computers specialist;0;54
120;mechanic;1;60"""

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

unsorted_list = data.split('\n')

sorted_list = list()
for i in unsorted_list:
    sorted_list.append(i.split(';'))

for item in sorted_list:
    if int(item[3]) >= 60:
        colonists_list.append(item)

counter = 0

for item in colonists_list:
    if int(item[2]) == 0:
        new_colonists_list_female.append(item)
    elif int(item[2]) == 1:
        new_colonists_list_male.append(item)

for item in new_colonists_list_female:
    if item[1] == 'manager':
        manager_fem_list.append(item)
    elif item[1] == 'cook':
        cook_fem_list.append(item)
    elif item[1] == 'electrical engineer':
        elen_fem_list.append(item)
    elif item[1] == 'computers specialist':
        compspec_fem_list.append(item)
    elif item[1] == 'doctor':
        doc_fem_list.append(item)
    elif item[1] == 'mechanic':
        mech_fem_list.append(item)
    elif item[1] == 'scientist':
        sci_fem_list.append(item)

for item in new_colonists_list_male:
    if item[1] == 'manager':
        manager_mal_list.append(item)
    elif item[1] == 'cook':
        cook_mal_list.append(item)
    elif item[1] == 'electrical engineer':
        elen_mal_list.append(item)
    elif item[1] == 'computers specialist':
        compspec_mal_list.append(item)
    elif item[1] == 'doctor':
        doc_mal_list.append(item)
    elif item[1] == 'mechanic':
        mech_mal_list.append(item)
    elif item[1] == 'scientist':
        sci_mal_list.append(item)


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
                    female.remove(colonist_choice)
                elif len(female) == 0:
                    colonist_choice = random.choice(male)
                    resulting_list.append(colonist_choice)
                    male.remove(colonist_choice)


sex = random.choice([manager_fem_list, manager_mal_list])
choice = random.choice(sex)
lucky_colonists.append(choice)

choose_colonists(cook_fem_list, cook_mal_list, cooks, lucky_colonists)
choose_colonists(elen_fem_list, elen_mal_list, electrical_engineers, lucky_colonists)
choose_colonists(compspec_fem_list, compspec_mal_list, computer_system_specialists, lucky_colonists)
choose_colonists(doc_fem_list, doc_mal_list, medics, lucky_colonists)
choose_colonists(mech_fem_list, mech_mal_list, mechanics, lucky_colonists)
choose_colonists(sci_fem_list, sci_mal_list, scientists, lucky_colonists)

colonists_string = ''

for item in lucky_colonists:
    colonists_string = colonists_string + item[0] + ';'
colonists_string = colonists_string[0:len(colonists_string)-1]

sys.stdout.write(colonists_string)
