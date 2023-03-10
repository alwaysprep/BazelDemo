import time
import unittest

from src.preprocessing.stop_words import remove_stop_words


class TestStopWordsInputOutput(unittest.TestCase):

    def test_remove_stop_words(self):
        time.sleep(1)
        string = open("data/ThePhilosophersStone.txt").read()
        expected = open("data/ThePhilosophersStoneStopWordsRemoved.txt").read()
        
        res = remove_stop_words(string)

        self.assertEqual(res, expected)

        
if __name__ == "__main__":
    unittest.main()
