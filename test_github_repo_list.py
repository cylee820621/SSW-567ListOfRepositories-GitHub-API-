import unittest
import Github_Repo_List

class TestGithub_Repo_list(unittest.TestCase):

    def test_get_Github_API(self):
        self.assertEqual(get_Github_API('APIRateLimitExceeded'), None) 

    def test_get_repo_list(self):
        self.assertEqual(get_repo_list("cylee820621"),)
if __name__ == "__main__":
    unittest.main()