num=input("Enter a number")
print(num)
num=int(num)
num+=10
print(num)
sum=0

try:
    num=int(input("Enter a number: "))
    sum=sum+10
except:
    print("You did not enter a number.")
print("continue")

with open("movies.txt") as file:
        for line in file:
             line=line.strip()
             print(line)

with open("heights.txt") as file:
     for line in file:
          line=line.strip()
          tokens=line.split()
          print(tokens)