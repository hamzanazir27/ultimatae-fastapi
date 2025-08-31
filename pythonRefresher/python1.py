# hi=12
# print(hi)



"""
####################### STRING FORMATING ###################
"""
print("####################### STRING FORMATING ###########################")


firstName="hamza"
lastName="nazir"

print(firstName+" "+lastName)
print()

print(f"firstName {firstName}")

print()

kuchb="lastname {}"

print(kuchb.format(lastName))




"""
####################### User Input ###################
"""
print("####################### User Input ###########################")


# age=input("what is your age ")
# print(f"your age is: {age}")




"""
####################### String  assignment ###################

String Assignment
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.

"""
print("####################### string assignment ###########################")
# type operater
intg=32
flt=.32
stg="s"
stg2=''
print(type(intg))
print(type(flt))
print(type(stg))
print(type(stg2))

days=int(input("how many days until Your birthday : "));
print(f"{days} is approx to {days // 7}")

