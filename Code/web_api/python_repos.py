import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 转化为json字典
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# items是一个列表嵌套字典
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

'''
取items的第一个列表,获取其key
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
遍历所以有的items
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])  # owner 是个字典所以需要再次取值
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
'''

repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')