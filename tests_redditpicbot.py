import unittest
import redditapi

class Testredditapi(unittest.TestCase):
    def setUp(self) -> None:
        self.reddit_1 = redditapi.redditAPI("japanpics")
        pass

    def tearDown(self) -> None:
        pass

    def test_getOutputPath(self) -> None:
        self.assertIsInstance(self.reddit_1.outputPath,str, f"Type is {type(self.reddit_1.outputPath)}")


if __name__ == "__main__":
    unittest.main()