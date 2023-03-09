from fastapi import FastAPI
from typing import Dict
from github import Github
from gitoken import access_token

app = FastAPI()

access_token = access_token

class User:
    def __init__(self, name: str, url: str, public_repos: int, followers: int,
                                                              following: int):
        self.name = name
        self.url = url
        self.public_repos = public_repos
        self.followers = followers
        self.following = following


def get_user(username: str) -> User:
    g = Github(access_token)
    user = g.get_user(username)
    return User(user.name, user.html_url, user.public_repos, user.followers, 
                                                             user.following)

def get_user_repos(username: str) -> Dict[str, str]:
    g = Github(access_token)
    repos = g.get_user(username).get_repos()
    return {repo.name: repo.html_url for repo in repos}

def user_report(username: str) -> str:
    user = get_user(username)
    repos = get_user_repos(username)
    report = f"Nome: {user.name}\nPerfil: {user.url}\
            Número de repositórios publicos: {user.public_repos}\
            Número de seguidores: {user.followers}\
            Número de usuários seguidos: {user.following}\nRepositórios:"
    for name, url in repos.items():
        report += f"{name}: {url}"         
    with open(f"{username}.txt", "w") as f:
        f.write(report)
        print(report)
    return report


@app.get("/user/{username}")
def generate_user(username: str):
    return get_user(username)

@app.get("/user/{username}/repos")
def generate_user_repos(username: str):
    return get_user_repos(username)

# @app.get("/user/report/{username}")
# def generate_user_report(username: str):
#     return user_report(username)



import unittest


class TestMethods(unittest.TestCase):
    """ Classe de testes unitários. """
    def test_user_class_has_minimal_parameters(self):

        """
        Teste unitário relativo ao primeiro passo do desafio, esse cenário
        deve ser mantido na sua resolução.
        """

        parameters = [
            'name', 'url', 'public_repos', 'followers', 'following'
        ] 

        user = get_user('londoncomputadores')
        # print(user)
        # user = str(user)

        for param in parameters:
            self.assertEqual(hasattr(user, param))

    """ Escreva seus testes unitários a partir daqui. """

    # def setUp(self):
    #     self.user = User()
    #     self.test = TestMethods()

    def test_get_user(self):
        user = User('name', 'url', 'public_repos', 'followers', 'following')
        self.assertIsNotNone(user.name)
        self.assertIsNotNone(user.url)
        self.assertIsNotNone(user.public_repos)
        self.assertIsNotNone(user.followers)
        self.assertIsNotNone(user.following)
        # self.user.test_user_class_has_minimal_parameters.user()
        # self.assertEqual('user', 'param' == str)

    def test_get_user_repos(self):
        pass

    def test_user_report(self):
        pass


if __name__ == "__main__":
    unittest.main()

@app.get("/user/report/{username}")
def generate_user_report(username: str):
    return user_report(username)
    
