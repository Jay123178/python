def intersection(list1, list2):
   
    intersection_list = []
    
   
    for item in list1:
      
        if item in list2 and item not in intersection_list:
            intersection_list.append(item)
    
    return intersection_list


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


result = intersection(list1, list2)
print("Intersection of list1 and list2:", result)  # Output: [3, 4, 5]

