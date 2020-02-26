import unittest
from Github_Repo_List import get_Github_API,get_repo_list
from unittest.mock import Mock, patch
import json


class Testgithubapi(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_Github_API(self,mock_get):
        with open('response.json') as fopen:
            data = json.load(fopen)
        mock_get.return_value = data
        response = get_Github_API('cylee820621')
        self.assertEqual(response, data)

if __name__ == '__main__':
    unittest.main()
