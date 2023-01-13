from collections import defaultdict


def add_data(data, new_data):
    for x in new_data:
        data["some_key"].append(x)


data = defaultdict(list)
for x in [5, 6]:
    data["some_key"].append(x)

add_data(data, [1, 2])
add_data(data, [3, 4])

for i in data:
    print(data[i])
