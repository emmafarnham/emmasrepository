
counter = 0
while counter <10:
    print(counter)
    counter += 1

nums = [10,20,30,40,50]
for i in range (2,len(nums)):
    print(nums[i])

for num in nums:
    num+=5
    print(num)

for i, val, in enumerate (nums):
    print ("i is " , i, " and the val is ", val)

dogs = ["boomer", "rocky", "daisy"]

#use three types of loops to iterate through the dog array 
#in range loop
for i in range (3):
    print(dogs[i])

#for each 
for dog in dogs:
    print(dog)

#list of numbers 
nums = [1,2,3,4,5]
sum_nums=0
for value in nums:
    sum_nums += value
print(f"The sum of the values is {sum_nums}")

#functions
def hello (name="friend"):
    print("hello!", name)
hello("bob")
hello()

#Strings
Fname = "Emma"
Lname = "Farnham"
print ("She's a great dancer")

fullName = Fname + " " + Lname
print(fullName)
f_initial = fullName[0]
l_initial = fullName[len(fullName)-1]
print(l_initial)
print(f_initial)

print("Emma" * 3)

#comparing strings
magician = "Harry Houdini"
if magician == 'Harry Houdini':
    print("World's greatest magician!")

course = "Platform Computing"
platform = course [0:8]
computing = course [9:18]
print (platform + computing)

# excersise 
swap = [0,3,8,5,4]
print(swap)
temp = swap[4]
swap[4]= swap[2]
swap[2]=temp
print(swap)
