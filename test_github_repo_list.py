import unittest
import requests
from Github_Repo_List import get_repo_commits_number, get_repo_list, get_Github_API, get_output_list

class TestGithub_Repo_list(unittest.TestCase):
    userID = 'cylee820621'
    response = requests.get("https://api.github.com/users/{}/repos".format(userID))
    response = response.json()

    def test_get_Github_API(self):
        #self.assertEqual(get_Github_API('APIRateLimitExceeded'), None) 
        self.assertEqual(get_Github_API('cylee820621'), response)
        
    def test_get_repo_list(self):
        list1 = ['SSW-533-project', 'SSW-567', 'SSW-567HW02a-Triangle', 'SSW-567ListOfRepositories-GitHub-API-', 'SSW690Project', 'Univerity', 'Xcodetesting']
        self.assertEqual(get_repo_list(response),list1)

    def test_get_repo_commits_number(self):
        userID = 'cylee820621'
        list_repo = ['SSW-533-project', 'SSW-567', 'SSW-567HW02a-Triangle', 'SSW-567ListOfRepositories-GitHub-API-', 'SSW690Project', 'Univerity', 'Xcodetesting']
        list1 = [30, 6, 12, 7, 14, 3, 2]
        self.assertEqual(get_repo_commits_number(userID,list_repo),list1)

    def test_get_output_list(self):
        list_repo = ['SSW-533-project', 'SSW-567', 'SSW-567HW02a-Triangle', 'SSW-567ListOfRepositories-GitHub-API-', 'SSW690Project', 'Univerity', 'Xcodetesting']
        list_commits = [30, 6, 12, 7, 14, 3, 2]
        list1 = ['Repo: SSW-533-project Number of commits: 30', 'Repo: SSW-567 Number of commits: 6', 'Repo: SSW-567HW02a-Triangle Number of commits: 12', 'Repo: SSW-567ListOfRepositories-GitHub-API- Number of commits: 7', 'Repo: SSW690Project Number of commits: 14', 'Repo: Univerity Number of commits: 3', 'Repo: Xcodetesting Number of commits: 2']
        self.assertAlmostEqual(get_output_list(list_repo,list_commits),list1)

if __name__ == "__main__":
    unittest.main()