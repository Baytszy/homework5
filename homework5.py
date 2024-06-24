

immutable_var = 1,2, "text", True, "text2"
print(immutable_var)
immutable_var[0] = 5   #кортеж не поддерживает обращение по элементам, выдает ошибку
print(immutable_var)
mutable_list = [1,3,5,"text3", True]
mutable_list[3] = 10
print(mutable_list)