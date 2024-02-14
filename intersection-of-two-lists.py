def intersection(list1, list2):
    return list(filter(lambda x: x in list2, list1))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = intersection(list1, list2)
print("Intersection of list1 and list2:", result)
