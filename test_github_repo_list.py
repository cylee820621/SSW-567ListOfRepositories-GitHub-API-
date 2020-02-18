import unittest
import requests
from Github_Repo_List import get_repo_commits_number, get_repo_list, get_Github_API, get_output_list

class TestGithub_Repo_list(unittest.TestCase):

    def test_get_Github_API(self):
        userID = 'cylee820621'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):    
            self.assertEqual(get_Github_API('cylee820621'), response)
            self.assertEqual(get_Github_API('users'), None)
        else:
            self.assertEqual(get_Github_API('cylee820621'), None)
        
    def test_get_repo_list(self):
        userID = 'cylee820621'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        print(response)
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            list1 = get_repo_list(response)
            self.assertEqual(get_repo_list(response),list1)

    def test_get_repo_commits_number(self):
        userID = 'cylee820621'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            list1 = get_repo_list(response)
            list2 = get_repo_commits_number(userID,list1)
            self.assertEqual(get_repo_commits_number(userID,list1),list2)

    def test_get_output_list(self):
        userID = 'cylee820621'
        response = requests.get("https://api.github.com/users/{}/repos".format(userID))
        response = response.json()
        if not "message" in response or not response["message"].startswith("API rate limit exceeded"):
            list1 = get_repo_list(response)
            list2 = get_repo_commits_number(userID,list1)
            list3 = get_output_list(list1,list2)
            self.assertAlmostEqual(get_output_list(list1,list2),list3)

if __name__ == "__main__":
    unittest.main()