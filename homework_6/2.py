# num = input("n = ")
# summ = 0
# for i in num:
#     summ += int(i)
# print(int(num) % summ ==0 )
# str = " the sky is blue "
# str2= "".join(reversed(str))
# print(str2)
# def f(name,number):
#     match number:
#         case 0:
#             print(f"hello,{name}")
#         case 1:
#             print(f"bye, {name}")
#         case _:
#             print("not valid number insert 0 or 1")
# f(name=input("insert name "),number=int(input("insert numbr ")))
# f(name=input("Insert your name "),number = int(input("insert number ")))


# d={
#     "name":"jon",
#     "name2":"Tigranuhi",
#     "name3":"Ani"
# }
# print(sorted(d.values()))
# d = {
#     'D':1,
#     'C':3,
#     'A':9
# }
# print(list(d.items()))
# d = {
#     'class': {
#         'student': {
#             'name': 'Mike',
#             'marks': {
#                 'physics': 70,
#                 'history': 80
#             }
#         }
#     }
# }
# print(d['class']['student']['marks']['history'])
# profit={
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }
# print(round(profit["sell_price"]-profit["cost_price"])*profit["inventory"])
# str1 = "apple"
# str2 = "play"
# print(len(set(str1+str2)))
# lst1 = [1,2,3]
# lst2 = [3,5,2]
# lst3 = [7,3,2]
# s1 = set(lst1)
# s2 = set(lst2)
# s3 = set(lst3)
# print(sum(s1&s2&s3))
lst = [1,2,3,4,5,6]

sum_odd = sum(i for i in lst if i%2 ==1)
sum_even =sum(i for i in lst if i%2 ==0)
print([sum_odd,sum_even])
