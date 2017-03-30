import unittest
import urlsplitter


class UrlSplitterTest(unittest.TestCase):
    def test_should_split_correctly_baidu_url(self):
        result = urlsplitter.resolve("http://baidu.com")
        self.assertEqual("http", result.protocol)
        self.assertEqual("baidu.com", result.domain)
        self.assertEqual("", result.path)

    def test_should_return_url_obj(self):
        self.assertIsInstance(urlsplitter.resolve("http://baidu.com"), urlsplitter.URL)

    def test_should_return_protocol(self):
        self.assertEqual("http", urlsplitter.resolve_protocol("http://baidu.com"))
        self.assertEqual("ftp", urlsplitter.resolve_protocol("ftp://baidu.cn/"))

    def test_should_return_domain(self):
        self.assertEqual("baidu.com", urlsplitter.resolve_domain("http://baidu.com"))

    def test_should_return_path(self):
        self.assertEqual("path/to/something", urlsplitter.resolve_path("http://baidu.com/path/to/something"))
