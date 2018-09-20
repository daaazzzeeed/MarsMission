unsorted_list = list()
while 1:
    try:
        line = input()
        unsorted_list.append(line)
    except EOFError:
        break

data_list = []

for item in unsorted_list:
    data_list.append(item.split(':'))

ids = []
time = []

for item in data_list:
    ids.append(item[0])
    time.append(int(item[1]))

times = []
m = 0
n = 10
ids_list = []

for i in range(10):
    if m < 91:
        times.append(time[m:n])
        ids_list.append(ids[m:n])
        m = m + 10
        n = n + 10

times_sorted = []

for item in times:
    times_sorted.append(sorted(item)[0])

counter = []

for i in range(10):
    for j in range(10):
        if int(times[i][j]) == int(times_sorted[i]):
            counter.append([i, j])
            break
        continue
resulting_list = []

for i in range(10):
    resulting_list.append(ids_list[i][counter[i][1]])

final_string = ''

for item in resulting_list:
    item = item.replace('/',':')
    item = item + ';\n'
    final_string = final_string + item
print(final_string)

