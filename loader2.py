from operator import itemgetter

data = list()
while 1:
    try:
        line = input()
        data.append(line)
    except EOFError:
        break


loader1 = []
loader2 = []
kg_left_1 = 200
kg_left_2 = 200


def contains(item1, item2): #item2 in item1
    for i in range(len(item1)):
        for j in range(len(item2)):
            if item1[i] == item2[j]:
                return True
                break
    return False


unsorted_list = list()

for item in data:
    unsorted_list.append(item.split(';'))

for item in unsorted_list:
    for i in range(2):
        item[i] = int(item[i])
    item[2] = item[2].split(',')
    for i in range(3):
        item[2][i] = int(item[2][i])
    item[3] = int(item[3])

data_list_sorted_rating = sorted(unsorted_list, key=itemgetter(3), reverse=True)

loader1.append(data_list_sorted_rating[0][0])

loader2.append(data_list_sorted_rating[1][0])

for i in range(len(data_list_sorted_rating)):
    if i > 1:
        if contains(loader1, data_list_sorted_rating[i][2]) == False:
            loader1.append(data_list_sorted_rating[i][0])
        elif contains(loader2, data_list_sorted_rating[i][2]) == False:
            loader2.append(data_list_sorted_rating[i][0])

loader1str = ''
loader2str = ''

for item in loader1:
    loader1str = loader1str + str(item) + ';'
loader1str = loader1str + '\n'

for item in loader2:
    loader2str = loader2str + str(item) + ';'

loaderstr = loader1str + loader2str
loaderstr = loaderstr[0:len(loaderstr)-1]
print(loaderstr)