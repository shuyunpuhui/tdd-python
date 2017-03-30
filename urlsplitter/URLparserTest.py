import unittest
import urlsplitter


class URLsplitter(unittest.TestCase):

    def test_should_return_dict_if_input_url(self):
        self.assertEqual({"protocol": "http","domain": "www.google.se","path": ""},
                         urlsplitter.urlparser("http://www.google.se"))
        self.assertEqual({"protocol": "http","domain": "www.baidu.com","path": "123"},
                         urlsplitter.urlparser("http://www.baidu.com/123"))
        self.assertEqual({"protocol": "ftp","domain": "www.baidu.com","path": "123"},
                         urlsplitter.urlparser("ftp://www.baidu.com/123"))
        self.assertEqual({"protocol": "http","domain": "www.baidu.com","path": "123/456"},
                         urlsplitter.urlparser("http://www.baidu.com/123/456"))

    def test_should_return_protocol_if_input_url(self):
        self.assertEqual("http", urlsplitter.get_protocol("http://www.google.se"))

    def test_should_return_domain_if_input_url(self):
        self.assertEqual("www.baidu.com", urlsplitter.get_domain("http://www.baidu.com/123"))

    def test_should_return_full_path_if_input_url(self):
        self.assertEqual("123/456", urlsplitter.get_path("http://www.baidu.com/123/456"))
