import unittest
from unittest.mock import patch
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch('emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):

        # Mock API response
        mock_response = '''
        {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.1,
                        "disgust": 0.05,
                        "fear": 0.02,
                        "joy": 0.8,
                        "sadness": 0.03
                    }
                }
            ]
        }
        '''

        # Configure mock object
        mock_post.return_value.text = mock_response

        # Call function
        result = emotion_detector("I am very happy today!")

        # Expected output
        expected_result = {
            'anger': 0.1,
            'disgust': 0.05,
            'fear': 0.02,
            'joy': 0.8,
            'sadness': 0.03,
            'dominant_emotion': 'joy'
        }

        # Assertions
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()