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
        repo_list = ['SSW-533-project',
                      'SSW-567',
                      'SSW-567HW02a-Triangle',
                      'SSW-567ListOfRepositories-GitHub-API-',
                      'SSW690Project',
                      'Univerity',
                      'Xcodetesting']
        self.assertEqual(response, repo_list)


if __name__ == '__main__':
    unittest.main()
