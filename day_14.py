# print("never give up!!")
# l=[1,2,3,4,5,6,7,8,9,9]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# l=["idli","vada","dosa"]              # list comprehension
# m=[i.upper() for i in l]      
# print(m)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# D={"pen":5, "book":20,"laptop":50000,"computer":60000}
# total=0
# for key,value in D.items():
#     total=total+value
#     print(total)
#     print(key,"----", value)
# print(f"The total price is : {total}")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# l=[ i**2 for i in range(1,101)]             # list comprehension to generate a list of their squares.
# print(l)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# c_p= {                                        # Dictionary Comprehension:
#     "Bengaluru": 8400000,
#     "Mysuru": 1100000,
#     "Hubballi": 900000,
#     "Mangaluru": 500000
# }
# population={city:pop for city,pop in c_p.items() if pop < 1000000}
# print(population)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# sum=0
# for i in matrix:           #  To Prints the entire matrix row by row.
#     print(i)
# sum=[str(i) for index ,i in enumerate(matrix)]

# print(sum)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# names=["ullas","Whatsapp","Facebook","Youtube","Amazon","play store","apps"]
# d={name:len(name) for name in names if len(name)>=4}
# print(d)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# s="this is naruto uzamaki !!"   # to split the sentence
# l=s.split(" ",2)
# print(l)
# data="apple,banana,mango"
# fruits=data.split(",")
# print(fruits)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
x=input("Enter the list of integers : ").split()
m=[int(i) for i in x]
print(m)

