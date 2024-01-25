# Type the given
list1 = [10, 20, 25, 30, 35]
list2 = [25, 35, 40, 60, 90]
# If Function and Odd or Even Function
result_list = [num for num in list1 if num % 2 !=0] + [num for num in list2 if num % 2 ==0]
# Print result list: [ result ]
print("result list: ", result_list)
