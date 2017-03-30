
import unittest

import url_parser


class UrlSplitterTest(unittest.TestCase):
    def test_should_return_protocol_domain_path(self):
        self.assertDictEqual({"protocol": "http", "domain": "www.baidu.com", "path": "v1"},
                             url_parser.url_parser("http://www.baidu.com/v1"))

        self.assertDictEqual({"protocol": "http", "domain": "www.baidu.com", "path": ""},
                             url_parser.url_parser("http://www.baidu.com/"))

        self.assertDictEqual({"protocol": "ftp", "domain": "www.baidu.com", "path": "v1"},
                             url_parser.url_parser("ftp://www.baidu.com/v1"))

    def test_should_return_protocol_if_input_valid_url(self):
        self.assertEqual("http", url_parser.get_protocol("http://www.baidu.com/v1"))

    def test_should_return_protocol_if_input_url(self):
        self.assertEqual("www.baidu.com", url_parser.get_domain("http://www.baidu.com/v1"))

    def test_should_return_path_if_input_url(self):
        self.assertEqual("v1", url_parser.get_path("http://www.baidu.com/v1"))