list1 = ["hello ", "take "]

list2 = ["dear ", "sir "]

result = []

for list1 in list1:
    for list2 in list2:
        result.append(list1 + list2)

print(result)
