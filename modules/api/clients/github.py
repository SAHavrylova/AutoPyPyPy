import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", 
            params={"q": name}
        )
        body = r.json()

        return body

    def list_branches(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches")
        body = r.json()

        return body
    
    def emojis(self):
        r = requests.get(f"https://api.github.com/emojis")
        body = r.json()

        return body
    
    def labels(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/labels")
        body = r.json()
        print(body)

        return body
