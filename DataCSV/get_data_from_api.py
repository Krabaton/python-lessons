import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print(r.status_code)

res_dict = r.json()

repo_dicts = res_dict['items']
for repo_dict in repo_dicts:
    print('Name: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repo: ', repo_dict['html_url'])
    print('Created: ', repo_dict['created_at'])
    print('Update: ', repo_dict['updated_at'])
    print('Description: ', repo_dict['description'])