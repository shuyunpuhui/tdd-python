# -*- coding: utf-8 -*-
import unittest
import urlsplitter


class urlsplitter_test(unittest.TestCase):

    def test_should_return_list_input_url(self):
        self.assertEqual(['http', 'www.baidu.com', ''],  urlsplitter.get_protocol('http://www.baidu.com'))
        self.assertEqual(['http', 'www.baidu.com', 'abc'],  urlsplitter.get_protocol('http://www.baidu.com/abc'))
        self.assertEqual(['http', 'www.baidu.com', 'abc/ef'],  urlsplitter.get_protocol('http://www.baidu.com/abc/ef'))
    # def test_should_return_http_if_input_is_http(self):
    #     self.assertEqual("http", urlsplitter.get_protocol('http://'))
    #     self.assertEqual("https", urlsplitter.get_protocol('https://'))
    #
    # def test_should_return_http_if_protocol_is_http(self):
    #     self.assertEqual("http", urlsplitter.get_protocol('http://some.thing'))
    #
    # def test_should_return_domain_of_url(self):
    #     self.assertEqual('some.thing', urlsplitter.get_domain('http://some.thing'))
    #     self.assertEqual('some.thing', urlsplitter.get_domain('http://some.thing/abc'))
    # def test_should_return_path_of_url(self):
    #     self.assertEqual('abc', urlsplitter.get_path('http://some.thing/abc'))
    #     self.assertEqual('abc/ef', urlsplitter.get_path('http://some.thing/abc/ef'))
