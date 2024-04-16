lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)
lst.remove(40) #find 40 and remove 
print(lst)
lst.pop(2) #remove value at given index 
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)
lst[0]=500
print(lst)
lst=lst[1:]
print(lst)

index3 = lst.index(7) #index function
print(index3)

lst.append(20)
lst.append(20)
lst.append(20)
print(lst)

num20 = lst.count(20)
print(num20)
lst_copy = lst #changing a value in lst_copy does change original lsy 
print(lst_copy)
lst_copy[1]=99
print(lst_copy)
print("original list: ",lst)

new_copy = lst.copy() #changing a value in new copy does not change the original lst
print(new_copy)
new_copy[0]=1000
print(lst)
print(new_copy)

new_copy=lst[:] #changing a value in new copy does not change the original lst

empty_lst =[]
for val in new_copy:
    empty_lst.append(val)
print(empty_lst)

empty_lst=[0]*10
print(empty_lst)
empty_lst[1]=100
print(empty_lst)

squares=[]
for i in range (1,10):
    squares.append(i**2) # OR squares=[i*i for i in range(1,10)]
print(squares)

plus_5=[]
plus_5=[5+val for val in lst] #list comprehension
print(plus_5)

small_vals= [val for val in lst if val < 20]
print(small_vals)

fav_foods={"kathleen" : "pizza", "maya" : "ice cream", "Tom" : "ice cream", "Eric" : "Steak"}
print(fav_foods)

mff= fav_foods["maya"]
print(mff)

for key in fav_foods: 
    print(f"{key}'s favorite food is {fav_foods[key]}")

for person, food in fav_foods:
    print(f"{person}'s favorite food is {food}")

    if "Bob" in fav_foods:
        print(fav_foods["Bob"])
    else:
        fav_foods["Bob"]="wings"
    print(fav_foods)