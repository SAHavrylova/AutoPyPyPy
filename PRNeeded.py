import requests

# Замініть ці змінні на власні значення
repository_owner = 'SAHavrylova'
repository_name = 'Course'
github_token = ''
label_name = 'bug'

# Створення заголовку авторизації з токеном GitHub
headers = {
    'Authorization': f'Bearer {github_token}'
}

# URL запиту до API GitHub для отримання пул-реквестів з певним лейблом
url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/pulls?state=all&labels={label_name}'

# Виконання запиту GET до GitHub API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Обробка результатів запиту
    pull_requests = response.json()
    for pr in pull_requests:
        pr_url = pr['html_url']  # URL пул-реквесту
        pr_title = pr['title']  # Назва пул-реквесту
        print(f"{pr_title} ({pr_url})")
else:
    print(f"Не вдалося отримати дані. Код відповіді: {response.status_code}")
