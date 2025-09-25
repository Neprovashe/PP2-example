#Boolean


print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

print(bool("Hello"))
print(bool(15))



x = "Hello"
y = 15

print(bool(x))
print(bool(y))



bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])



bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 



class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 



def myFunction() :
  return True

print(myFunction()) 



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 



x = 200
print(isinstance(x, int)) 




#Operators



print(10 + 5)



print((6 + 3) - (6 + 3)) 




print(100 + 5 * 3) 



#lists



thislist = ["apple", "banana", "cherry"]
print(thislist)



thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
print(len(thislist))



list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]



list1 = ["abc", 34, True, 40, "male"]



mylist = ["apple", "banana", "cherry"]
print(type(mylist))



thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



#list items



thislist = ["apple", "banana", "cherry"]
print(thislist[1])



thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])



thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 



thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)




thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)




thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



thislist = ["apple", "banana", "cherry"]
del thislist



thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



