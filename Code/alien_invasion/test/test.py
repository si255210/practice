import requests
import matplotlib.pyplot as plt

def get_github_repositories(username):
    url = f"https://api.github.com/users/si255210/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")
        return None

def visualize_repository_languages(repositories):
    if not repositories:
        return

    # 提取每个仓库的语言信息
    languages = [repo.get("language", "Unknown") for repo in repositories]

    # 统计每种语言的数量
    language_counts = {lang: languages.count(lang) for lang in set(languages)}

    # 生成柱状图
    plt.bar(language_counts.keys(), language_counts.values())
    plt.xlabel("Programming Languages")
    plt.ylabel("Number of Repositories")
    plt.title("GitHub Repository Languages")
    plt.show()

if __name__ == "__main__":
    github_username = "your_github_username"
    
    repositories = get_github_repositories(github_username)
    if repositories:
        visualize_repository_languages(repositories)
