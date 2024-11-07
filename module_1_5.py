immutable_var = (1,3,'Hello',True,[45,14])
print(immutable_var)
immutable_var[4][1] = 46 # в кортеже можно менять только элементы списка
print(immutable_var)

mutable_list = [1,2,3,'Python']
print(mutable_list)
mutable_list[0] = 0
mutable_list[1] = 8
mutable_list[2] = 9
mutable_list[3] = 'Java'
print(mutable_list)

