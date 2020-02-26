import unittest
from Github_Repo_List import get_Github_API,get_repo_list
from unittest.mock import Mock, patch
import json


class Testgithubapi(unittest.TestCase):
    
    @patch('Github_Repo_List.requests.get')
    def test_get_Github_API(self,mock_get):
        with open('response.json') as fopen:
            data = json.load(fopen)
        mock_get.return_value = data
        response = get_Github_API('cylee820621')
        self.assertEqual(response, data)

    @patch('Github_Repo_List.requests.get')
    def test_get_repo_list(self, mock_get):
        with open('response.json') as fopen:
            data = json.load(fopen)
        mock_get.return_value = data
        response = get_Github_API('cylee820621')
        response = get_repo_list(response)
        repo_list = ['GitHubApi', 'SSW-533-project', 'SSW-567', 'SSW-567HW02a-Triangle', 'SSW-567ListOfRepositories-GitHub-API-', 'SSW690Project', 'Univerity', 'Xcodetesting']
        self.assertEqual(response, repo_list)
    
    @patch('Github_Repo_List.get_repo_list')
    def get_repo_commits_number(self,mock_list_repo):
        repo_list = ['SSW-533-project',
                    'SSW-567',
                    'SSW-567HW02a-Triangle',
                    'SSW-567ListOfRepositories-GitHub-API-',
                    'SSW690Project',
                    'Univerity',
                    'Xcodetesting']
        mock_list_repo.return_value = repo_list
        response = get_repo_commits_number("cylee820621",repo_list)
        commits_number = [22, 30, 6, 18, 22, 14, 3, 2]
        self.assertEqual(response,commits_number)

    

if __name__ == '__main__':
    unittest.main()
