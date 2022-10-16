from reply_insta_classifier import __version__
from unittest import TestCase
from fastapi.testclient import TestClient
from reply_insta_classifier.main import app

from reply_insta_classifier.dummy_model import Dummy_text_classifier


class insta_classifier_test(TestCase):
    def test_model(self):
        model = Dummy_text_classifier()
        result = model.classify_text("test")
        expected = {"label": "LABEL_1", "score": 0.7012348771095276}
        self.assertAlmostEqual(result[0]["score"], expected["score"], 4)
        self.assertEqual(result[0]["label"], expected["label"])

    def test_api(self):
        client = TestClient(app)
        response = client.post("/insta/classification", json={"textBody": "test"})
        assert response.status_code == 200

    def test_version(self):
        assert __version__ == "0.1.0"
