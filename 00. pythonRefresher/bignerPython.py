# hi=12
# print(hi)



"""
####################### STRING FORMATING #######################
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

# days=int(input("how many days until Your birthday : "));
# print(f"{days} is approx to {days // 7}")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hi {name}, you are {age} years old")

# Exercise 2: Simple calculator
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = num1 + num2
# print(f"{num1} + {num2} = {result}")






####################### String  assignment ###################


print("####################### list ###########################")

my_list=[1,24,5,4,4,4,5];
print(my_list);
print(my_list[0]);
print(my_list[-1]); #last element
print(my_list[-4]); #last se start me

my_list[0] = "ss" 

print(my_list);


print("slicing in list");

print(my_list[1:-3])
print("appent 21")
my_list.append(21);

print(my_list);

print("add specific index")
my_list.insert(2,"hamza");
print(my_list)

print("pop 0 index")

print(my_list.pop(0));


print("remove by element")
print(my_list.remove("hamza"));

print(my_list);
print("sorting");

my_list.sort();
print(my_list);
print("find length");

print("length " , len(my_list));
# my_list.sort();


print("clear alll list")

my_list.clear()

print(my_list);



print("******************  SETS  ************************");

my_set={1,2,2,34,5};
print(my_set);
print("length ",len(my_set));

my_set.add("ssssssssssss");
print(my_set);

print("discard 2")
my_set.discard(2)

print(my_set);

for x in my_set:
 print(x)
print("clear the set");

my_set.clear()

print(my_set);







print("******************  tuples   ************************");

mtuple=(1,2,4,4,4,2,23233,3443,353,434,34423,232,342,3232,2332,2323);
print("")
print(mtuple)
print("tuple[5]")
print(mtuple[5])
print("")
# mtuple[]
print(mtuple)
print("")
print(mtuple)
print("")
print(mtuple)
print("")
print(mtuple)


# t = (10, 20, 30, 40, 50)

# print(t[0])   # 10 (first element)
# print(t[-1])  # 50 (last element)
# print(t[1:4]) # (20, 30, 40) (slicing)
# print(mtuple[1])  # Output: 2
# print(len(mtuple))  # Output: 5


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)


# Step 1: Create list
zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]

# Step 2: Delete third index (index 3 = "Lion")
zoo.pop(3)

# Step 3: Append new animal
zoo.append("Lizard")

# Step 4: Delete beginning (index 0 = "Monkey")
zoo.pop(0)

# Step 5: Print all animals
print(zoo)  # Output: ['Zebra', 'Gorilla', 'Tiger', 'Lizard']

# Step 6: Print first three animals
print(zoo[0:3])  # Output: ['Zebra', 'Gorilla', 'Tiger']





print("#######################  -- -----  ###########################")
print("#######################  -- -----  ###########################")
print("#######################  -- -----  ###########################")
print("#######################  -- -----  ###########################")
print("#######################  -- -----  ###########################")
print("#######################  -- -----  ###########################")

"""
####################### Dictionaries ###################
"""
print("####################### Dictionaries ###########################")
dic={
 "name":'hamza',
 "age":121,
 21:"pakistan zindabad"
}
print(dic)

print(dic.get("name"))
print(dic.get(21))
dic["uni"]="numl"

print(dic)

print("----")
print(len(dic))
print("----")
print(dic.pop(21))
print(dic)
# print("----")
# print(dic.clear())
# print(dic)
# print(dic.clear())
# print(dic)
# print("----")
# del dic
# print(dic)

# newDic=dic;
# print(newDic);
# dic["pakistan"]="zindabad"
# print(newDic);
newDic=dic.copy();
print(newDic);
dic["pakistan"]="zindabad"
print(newDic);
print(dic);


for i ,y in dic.items():
   print(i,": ", y)




   
"""
####################### Functions ###################
"""
print("####################### Functions ###########################")

def func():
  print("hello")

func()

# def add(a,b):
#   print(a+b);

# add(1,3)
def add(a,b):
  return a+b;

def mullAdd(a,b,c):
  return add(a,b)*c;

print(mullAdd(1,3,5));
name="hamza"
def method():
  name="hamza nazir ramay"
  return name

print(method())
print(name)
