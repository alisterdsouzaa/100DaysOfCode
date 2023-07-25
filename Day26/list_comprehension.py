# Square each num in list using list comprehension
num = [1,1,2,3,5,8,13,21,34,55]
new_num_list = [item**2 for item in num]
print(new_num_list)

# Even num from list using list comprehensions
even_num_list = [item for item in num if item%2 == 0]
print(even_num_list)
