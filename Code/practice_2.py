# 不改变原列表的情况下，在列表每个元素后增加字符
magicians = ['David Copperfield', 'Harry Houdini', 'Derren Brown', 'Penn Jillette', 'Teller']
print(magicians)
modified_list = list(magicians) # magicians[:]等效，magicians的话会改变原列表（why？
for i in range(len(modified_list)):
    modified_list[i] += ' the great'
print(modified_list)

# 字典传参
def build_profile(first, last, **user_profile):
    profile ={}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_profile.items():
        profile[key] = value
    return print(profile)

user_profile = build_profile('albert', 'einstein',   # 字典传参，要用等号？
location='princeton',
field='physics')

# class
from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(f"Rolling a {self.sides}-sided die: {result}")

six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(sides=10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    ten_sided_die.roll_die()


# 读取文件 异常
file_name = 'digits.txt'
with open(file_name) as file_object:  
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())  # print有换行，文件里面也有换行符，需要rstrip去掉
print(lines)
string = ''
for line in lines:
    string += line.strip()
print(string)

# 计算文件大致包含多少个单词
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +" words.")
filename = 'digits.txt'
count_words(filename)


# json
import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
        print("Welcome back, " + username + "!")
except:
    with open(filename, 'w') as f_obj:
        username = input("What is your name? ")
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")



