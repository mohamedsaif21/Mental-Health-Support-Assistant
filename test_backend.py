import unittest
from app import app, analyze_sentiment, is_crisis

class TestMindCare(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_sentiment_stress(self):
        self.assertEqual(analyze_sentiment("I am so stressed with exams"), "stress")
        self.assertEqual(analyze_sentiment("work is overwhelming"), "stress")

    def test_sentiment_sad(self):
        self.assertEqual(analyze_sentiment("I feel sad and lonely"), "sad")
        self.assertEqual(analyze_sentiment("I've been crying all day"), "sad")

    def test_sentiment_anxiety(self):
        self.assertEqual(analyze_sentiment("I am anxious about my future"), "anxiety")
        self.assertEqual(analyze_sentiment("I'm having a panic attack"), "anxiety")

    def test_sentiment_general(self):
        self.assertEqual(analyze_sentiment("Hello, how are you?"), "general")

    def test_crisis_detection(self):
        self.assertTrue(is_crisis("I want to kill myself"))
        self.assertTrue(is_crisis("I'm thinking of suicide"))
        self.assertFalse(is_crisis("I'm just feeling a bit down"))

    def test_chat_api(self):
        response = self.app.post('/chat', json={'message': 'I am stressed'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', data)
        self.assertEqual(data['category'], 'stress')

    def test_crisis_api(self):
        response = self.app.post('/chat', json={'message': 'suicide'})
        data = response.get_json()
        self.assertTrue(data.get('is_crisis'))
        self.assertTrue(data.get('emergency'))
        self.assertIn('helplines', data)
        self.assertTrue(any('988' in (h.get('phone', '') if isinstance(h, dict) else '') for h in data['helplines']))

if __name__ == '__main__':
    unittest.main()
