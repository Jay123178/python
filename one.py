def intersection(list1, list2):
    # Create an empty list to store the intersection elements
    intersection_list = []
    
    # Iterate through each element in list1
    for item in list1:
        # Check if the element is also in list2 and not already in the intersection_list
        if item in list2 and item not in intersection_list:
            intersection_list.append(item)
    
    return intersection_list


# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Finding intersection
result = intersection(list1, list2)
print("Intersection of list1 and list2:", result)  # Output: [3, 4, 5]

