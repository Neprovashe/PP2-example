class string2:
    def __init__(self, a = ""):
        self.string = a
    
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())

a = string2("hello")
a.printString()


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

a = Square(5)
print(a.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, point2):
        return ((self.x - point2.x)**2 + (self.y - point2.y)**2) ** 0.5
    
a = Point()
b = Point(4,3)
print(b.dist(a))


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return 1
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
            return 0
        else:
            self.balance -= amount
            return 1
        


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = list(range(1,100))
prime_numbers = list(filter(lambda x: prime(x), numbers))
print(prime_numbers)
    

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solver(heads, legs):
    
    left, right = 0, heads

    while left <= right:
        mid = (left + right) // 2  
        if mid * 4 + (heads-mid) * 2 == legs:
            return (mid, heads-mid)   
        elif mid * 4 + (heads-mid) * 2 < legs:
            left = mid + 1  
        else:
            right = mid - 1 
    return -1  


print(solver(35,94))


def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        permute(left + right, answer + ch)

permute("abc")



def reverse(sentence):
    words = sentence.split()
    return (words[::-1])

print(reverse("Machine you will die"))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False


def sphere_volume(radius):
    return (4/3) * 3.14 * (radius ** 3)


def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


def is_palindrome(s):
    return s == s[::-1]


def histogram(lst):
    for num in lst:
        print('*' * num)


def guess_the_number(num):
    name = input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    number = num
    guesses = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


guess_the_number(9)






# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def is_high_rated(movie):
    return movie["imdb"] > 5.5


def get_high_rated_movies(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]


def get_movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie["category"].lower() == category.lower()]


def average_imdb(movies_list):
    if not movies_list:
        return 0
    return sum(movie["imdb"] for movie in movies_list) / len(movies_list)


def average_imdb_by_category(movies_list, category):
    category_movies = get_movies_by_category(movies_list, category)
    return average_imdb(category_movies)