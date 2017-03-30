# -*- coding: utf-8 -*-

import unittest

import urlsplitter


class UrlsplitterTest(unittest.TestCase):
    def test_should_return_protocol_domain_path_if_input_is_url(self):
        self.assertEqual(['http', 'some.thing', ''], urlsplitter.url_parse('http://some.thing'))
        self.assertEqual(['ftp', 'a.large.site', ''], urlsplitter.url_parse('ftp://a.large.site'))
        self.assertEqual(['http', 'a.site.with', 'a-path'], urlsplitter.url_parse('http://a.site.with/a-path'))
        self.assertEqual(['http', 'a.site.with', 'a-path/gyf'], urlsplitter.url_parse('http://a.site.with/a-path/gyf'))
        self.assertEqual(['http', 'a.site.with', 'a-path/gyf?a=1'], urlsplitter.url_parse('http://a.site.with/a-path/gyf?a=1'))

    def test_should_return_protocol_if_input_is_url(self):
        self.assertEqual('http', urlsplitter.url_parse('http://some.thing')[0])

    def test_should_return_domain_if_input_is_url(self):
        self.assertEqual('some.thing', urlsplitter.url_parse('http://some.thing')[1])

    def test_should_return_path_if_input_is_url(self):
        self.assertEqual('', urlsplitter.url_parse('http://some.thing')[2])
        self.assertEqual('a-path', urlsplitter.url_parse('http://a.site.with/a-path')[2])
        self.assertEqual('a-path/gyf', urlsplitter.url_parse('http://a.site.with/a-path/gyf')[2])
        self.assertEqual('a-path/gyf?a=1', urlsplitter.url_parse('http://a.site.with/a-path/gyf?a=1')[2])