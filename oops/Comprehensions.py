numbers=[13,15,56,23,25]
new_list=[]
for num in numbers:
    new_list.append(num+5)
print(new_list)

#or we can write it as
new_list=[num+5 for num in numbers]#bracket are representing list and inside that it is representing comprehensions. 
print(new_list)

friend_age=[13,15,56,23,25]
age_info=[f"my friend is {age} year old."for age in friend_age]
print(age_info)

#lowercase to uppercase and vice-versa
friend=["Shereya","Riya","Rahul","Puja"]
friend_lower=[name.lower()for name in friend]
print(friend_lower)

friends=["Shereya","Riya","Rahul","Puja"]
friends_lower=[name.upper()for name in friends]
print(friends_lower)

friend=["Shereya","Riya","Rahul","Puja"]
user_input=input("Enter your name:")
if user_input in friend:
    print(f"{user_input} is my friend")

friend=["Shereya","Riya","Rahul","Puja"]
friend_lower=[name.lower()for name in friend]
user_input=input("Enter your name:")
if user_input.lower() in friend_lower:
    print(f"{user_input.title()} is my friend")

friends=["Shreya","Priya","Aman","Rahul"]
guest=["shreya","Raj","aman","Riya"] 

friends_lower=set([f.lower()for f in friends])
guest_lower=set([g.lower()for g in guest])
print(friends_lower.intersection(guest_lower))

#list comprehension
friends=["Shreya","Priya","Aman","Rahul"]
guest=["shreya","Raj","aman","Riya"] 

friends_lower=[f.lower() for f in friends]
present_friend=[
    name.title() 
    for name in guest 
    if name.lower() in friends_lower
    ]
print(present_friend)

#set comprehension
friends=["Shreya","Priya","Aman","Rahul"]
guest=["shreya","Raj","aman","Riya"] 

friends_lower=[f.lower() for f in friends]

