#To retrieve a user's list of repositories you can use this GitHub API:
#https://api.github.com/users/<ID>/repos
"""
author: Chih-Yu Lee

output example:
Repo: Triangle567 Number of commits: 10
Repo: Square567 Number of commits: 27
"""
import requests
import json

def get_repo_list(github_api_response):
    repo_list = [repo['name'] for repo in github_api_response]
    return repo_list

def get_repo_commits_number(userID,repo_name):
    number = requests.get("https://api.github.com/repos/{}/{}/commits".format(userID,repo_name))
    number = len((number.json()))
    return number

def get_output_list(list_repo,list_repo_commits_number):
    list_output = ["Repo: {} Number of commits: {}".format(name, commits) for name, commits in zip(list_repo,list_repo_commits_number)]
    return list_output

if __name__ == "__main__":
    userID = input("enter a user ID: ")
    response = requests.get("https://api.github.com/users/{}/repos".format(userID))
    response = response.json()
    list_repo = get_repo_list(response)
    list_repo_commits_number = [get_repo_commits_number(userID,repo) for repo in list_repo]
    list_output = get_output_list(list_repo,list_repo_commits_number)    
    print(list_output)