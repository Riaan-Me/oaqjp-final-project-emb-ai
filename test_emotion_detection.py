from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        test_result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(test_result_1["dominant_emotion"], 'joy')
        test_result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(test_result_2["dominant_emotion"], 'anger')
        test_result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_result_3["dominant_emotion"], 'disgust')
        test_result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(test_result_4["dominant_emotion"], 'sadness')
        test_result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_result_5["dominant_emotion"], 'fear')

unittest.main()