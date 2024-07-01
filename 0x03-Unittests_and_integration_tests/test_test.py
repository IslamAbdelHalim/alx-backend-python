import unittest
from unittest.mock import patch, Mock
from test import get_dog

class Test_get_user(unittest.TestCase):

    @patch("requests.get")
    def test_get_data(self, dog_data):
        mock_response = Mock()
        response_dict = {'message': ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'], 'status': 'success'}

        mock_response.json.return_value = response_dict

        dog_data.return_value = mock_response
        data = get_dog("https://dog.ceo/api/breed/hound/list")
        dog_data.assert_called_with("https://dog.ceo/api/breed/hound/list")
        self.assertEqual(data, response_dict)