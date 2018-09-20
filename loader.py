from operator import itemgetter

data = """0;18;33;66
1;52;33;90
2;33;30;71
3;56;2;90
4;100;51;47
5;88;53;68
6;97;39;92
7;35;45;96
8;22;5;92
9;33;31;13
10;99;49;59
11;83;48;94
12;23;40;8
13;81;37;3
14;61;15;3
15;41;4;64
16;42;38;7
17;96;25;22
18;38;57;79
19;17;57;32
20;94;49;79
21;8;10;73
22;85;20;99
23;48;47;57
24;29;30;9
25;79;8;26
26;23;35;45
27;45;44;31
28;80;29;77
29;31;22;100
30;26;34;38
31;8;46;98
32;99;44;86
33;38;23;16
34;50;44;32
35;10;6;71
36;29;22;37
37;14;45;71
38;19;53;89
39;16;28;20
40;68;23;52
41;70;4;18
42;32;26;67
43;15;35;48
44;38;29;55
45;20;4;83
46;41;50;30
47;67;11;46
48;62;49;1
49;17;14;60
50;26;33;5
51;79;56;85
52;66;40;92
53;68;56;64
54;69;49;17
55;87;16;28
56;12;17;45
57;91;44;100
58;4;34;4
59;81;47;88
60;19;30;39
61;34;38;91
62;30;60;50
63;25;32;60
64;86;17;24
65;80;45;83
66;9;57;78
67;8;34;11
68;34;20;82
69;45;34;15
70;44;37;76
71;44;36;97
72;99;43;70
73;33;13;83
74;95;37;66
75;62;22;51
76;37;9;100
77;22;41;88
78;76;22;93
79;44;24;76
80;28;23;83
81;80;9;29
82;75;5;87
83;14;34;51
84;6;60;95
85;5;51;31
86;86;27;85
87;6;29;37
88;36;17;59
89;75;18;26
90;6;25;89
91;95;18;33
92;20;40;66
93;46;20;16
94;28;33;67
95;7;52;91
96;14;26;44
97;7;57;13
98;64;50;87
99;70;38;93"""

data = data.split('\n')

unsorted_list = list()
while 1:
    try:
        line = input()
        unsorted_list.append(line)
    except EOFError:
        break

data_list = []
for item in unsorted_list:
    data_list.append(item.split(';'))
for item in data_list:
    for i in range(4):
        item[i] = int(item[i])
data_list_sorted_time = sorted(data_list, key=itemgetter(2))
data_list_sorted_weight = sorted(data_list, key=itemgetter(1))
data_list_sorted_rating = sorted(data_list, key=itemgetter(3), reverse=True)

time_left = 60
kg_left = 1000

things_we_need = []

for item in data_list_sorted_time:
    time_left = time_left - int(item[2])
    kg_left = kg_left - int(item[1])
    if time_left >= 0 and kg_left >= 0:
        things_we_need.append(item)
    else:
        time_left = time_left + int(item[2])
        kg_left = kg_left + int(item[1])

time = 0
kg = 0

for item in things_we_need:
    time = time + item[2]
    kg = kg + item[1]

id_str = ''

for item in things_we_need:
    id_str = id_str + str(item[0]) + ';'
id_str = id_str[0:len(id_str)-1]
print(id_str)
