#coding:utf-8

import unittest
import urlsplitter


class urlsplitterTest(unittest.TestCase):

    def test_should_complete_function(self):
        self.assertDictContainsSubset({"protocol": "http"}, urlsplitter.url_split("http://www.baidu.com"))
        self.assertDictContainsSubset({"domain": "www.baidu.com"}, urlsplitter.url_split("http://www.baidu.com"))
        self.assertDictContainsSubset({"path": ""}, urlsplitter.url_split("http://www.baidu.com"))
        self.assertDictContainsSubset({"protocol": "ftp"}, urlsplitter.url_split("ftp://a.large.site/userlist/[侯勇-陆毅]"))
        self.assertDictContainsSubset(
            {"domain": "a.large.site"},
            urlsplitter.url_split("ftp://a.large.site/userlist/[侯勇-陆毅]"))
        self.assertDictContainsSubset(
            {"path": "userlist/[侯勇-陆毅]"},
            urlsplitter.url_split("ftp://a.large.site/userlist/[侯勇-陆毅]"))

    def test_should_return_False_when_input_http(self):
        self.assertFalse(urlsplitter.is_url("http://"))

    def test_should_return_True_when_input_real_url(self):
        self.assertTrue(urlsplitter.is_url("wddd://www.baidu.com"))


