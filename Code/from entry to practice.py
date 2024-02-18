# 遍历列表 for
for i in range(1,10):
    for x in range(1,i+1):
        print(x,'*',i,'=',i*x,'\t\n')
# 浮点数，lower，upper方法 
name = 'hello python world'
print(name.upper())
nick_name = 'hell'
full_name = name + ' ' + nick_name
print(0.2 + 0.1, 5/2) 

# the use of list
number = list(range(4))
del number[0]
print(number)
number.insert(0,0)
print(number)
number[0] = 9
print(number)
number.sort(reverse=True)
print(len(number))
# list（range）
print(list(range(1,12,2)))

# 列表解析
squres = [value**2 for value in range(1,9)]
print(squres)

# 字典 如果要修改字典特定的内容可以遍历加if
alien_0 = {}
alien_0['point'] = 5
alien_0['color'] = 'green'
alien_0['color'] = 'red'
alien_0['speed'] = 'fast'
alien_0['x_position'] = 0
if alien_0['speed'] == 'medium':
    x_position = 2
elif alien_0['speed'] == 'low':
    x_position = 1
else:
    x_position = 3
alien_0['x_position'] += x_position
print('alien_0 x_position is',alien_0['x_position'])

# 遍历字典
for key, value in alien_0.items():
    print('\nkey:', key, value)

# 字典嵌套列表 
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
    if len(languages) != 1:
        print(name, "'s favorate languages are:")
        for language in languages:
            print('\t',language)
    else:
        print(name, "'s favorate language is:")
        for language in languages:
            print('\t',language)

# 用户输入和wihle循环
"""
while True:
    message = input("enter")
    if message == 'quit':
        break
    else:
        print(message)
"""

# 打小于10的奇数
count_num = 0
while count_num < 10:
    count_num += 1
    if count_num % 2 == 0:
        continue
    print(count_num)
"""
while True:
    age = input('your age')
    if int(age) < 3:
        print("pay for 6")
    elif  int(age) >3 and int(age) < 15:
        print('pay for 8')
    else:
        print("10")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
for cat in pets:
    if cat == "cat":
        pets.remove('cat')
    print(pets)
"""
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    modle = unprinted_designs.pop()
    print(modle)