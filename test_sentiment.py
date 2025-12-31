import unittest
from SentimentAnalysis.sentiment import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_positive_sentiment(self):
        result = sentiment_analyzer("I love this amazing product")
        self.assertEqual(result["sentiment"], "Positive")

    def test_negative_sentiment(self):
        result = sentiment_analyzer("This is the worst experience")
        self.assertEqual(result["sentiment"],"Negative")

    def test_neutral_sentiment(self):
        result = sentiment_analyzer("This product is available in the market")
        self.assertEqual(result["sentiment"], "Neutral")

    def test_empty_input(self):
        result = sentiment_analyzer("")
        self.assertEqual(result["sentiment"], "Neutral")

if __name__ == "__main__":
    unittest.main()
