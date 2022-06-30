# name = ["g","a","m","v","i","r"]
# # # print(dir(name))
# # # print(help(name.sort))
# # name.append("is ,"+ "don")
# # print(name)
# a = [1,2,3,4,5]
# c = list()
# for i in a:
#     c.append(i**2)
# print(c)
n = "1 2 3 4 5"

my_list = n.split()
for i in range(0,len(my_list),2):
    print(my_list[i],end=" ")