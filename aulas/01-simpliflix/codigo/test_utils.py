import utils

import unittest
import json
from unittest.mock import patch, mock_open
from pathlib import Path


REQUEST_TEMPLATE = '''{method} {route} HTTP/1.1
Host: 192.168.15.14:8080
Connection: keep-alive
Save-Data: on
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'''


def target_function(function_name):
    def decorate(clazz):
        if hasattr(utils, function_name):
            return clazz
        print(f'\033[91mA função {function_name} não foi implementada, portanto não é possível testá-la.\033[0m')
        return None
    return decorate


@target_function('extract_route')
class ExtractRouteTestCase(unittest.TestCase):
    def test_has_method(self):
        if not hasattr(utils, 'extract_route'):
            self.skipTest('Função não implementada')

    def test_extract_root(self):
        request = REQUEST_TEMPLATE.format(method='GET', route='/')
        self.assertEqual('', utils.extract_route(request))


@target_function('read_file')
class ReadFileTestCase(unittest.TestCase):
    def assert_read(self, filename, read_data):
        filename = Path() / 'subdir' / 'textfile.txt'

        m = mock_open(read_data=read_data)
        with patch('utils.open', m):
            received = utils.read_file(filename)

        self.assertEqual(received, read_data)

    def test_read_txt_file(self):
        filename = Path() / 'subdir' / 'textfile.txt'
        self.assert_read(filename, 'Some text')

    def test_read_html_file(self):
        filename = Path() / 'subdir' / 'textfile.html'
        self.assert_read(filename, '<html></html>')

    def test_read_css_file(self):
        filename = Path() / 'subdir' / 'textfile.css'
        self.assert_read(filename, 'p {color: "red"}')

    def test_read_js_file(self):
        filename = Path() / 'subdir' / 'textfile.js'
        self.assert_read(filename, 'console.log("OK");')

    def test_read_jpg_file(self):
        filename = Path() / 'subdir' / 'textfile.jpg'
        self.assert_read(filename, bytes([1,3,2,5,234,23,123,23,2,255]))

    def test_read_png_file(self):
        filename = Path() / 'subdir' / 'textfile.png'
        self.assert_read(filename, bytes([1,3,2,5,234,23,123,23,2,255]))


@target_function('load_data')
class LoadDataTestCase(unittest.TestCase):
    def test_load_data_from_file(self):
        expected = [
            {
                "titulo": "Breaking Bad",
                "slug": "breakingbad",
                "imagem": "/img/breakingbad/breaking-bad.jpg"
            },
            {
                "titulo": "Friends",
                "slug": "friends",
                "imagem": "/img/friends/friends.jpg"
            },
        ]
        m = mock_open(read_data=json.dumps(expected))
        with patch('utils.open', m):
            received = utils.load_data('data.json')
        self.assertEqual(expected, received)
        self.assertEqual(Path(m.call_args[0][0]), Path('data/data.json'))


@target_function('load_template')
class LoadTemplateTestCase(unittest.TestCase):
    def assert_template_loaded(self, filename, expected):
        m = mock_open(read_data=expected)
        with patch('utils.open', m):
            received = utils.load_template(filename)
        self.assertEqual(expected, received)
        self.assertEqual(Path(m.call_args[0][0]), Path('templates') / filename)

    def test_load_template_from_file(self):
        expected = '<h1>{title}</h1>'
        self.assert_template_loaded('template.html', expected)

    def test_load_component_template(self):
        expected = '<p>{text}</p>'
        self.assert_template_loaded('components/component.html', expected)

@target_function('load_episodes')
class LoadEpisodes(unittest.TestCase):
    def setUp(self):
        self.all_episodes = [
            {
                "numero": 1,
                "titulo": "Titulo 1",
                "descricao": "Descrição 1",
                "thumbnail": "/img/img1.jpg",
                "slug-serie": "serie2"
            },
            {
                "numero": 3,
                "titulo": "Titulo 3",
                "descricao": "Descrição 3",
                "thumbnail": "/img/img3.jpg",
                "slug-serie": "serie2"
            },
            {
                "numero": 2,
                "titulo": "TITULO 2",
                "descricao": "DESCRICAO 2",
                "thumbnail": "/img/img2.png",
                "slug-serie": "serie1"
            },
            {
                "numero": 2,
                "titulo": "Titulo 2",
                "descricao": "Descrição 2",
                "thumbnail": "/img/img2.jpg",
                "slug-serie": "serie2"
            },
            {
                "numero": 1,
                "titulo": "TITULO 1",
                "descricao": "DESCRICAO 1",
                "thumbnail": "/img/img1.png",
                "slug-serie": "serie1"
            },
        ]

    def assert_episodes_loaded(self, series, expected):
        filename = 'episodes.json'
        m = mock_open(read_data=json.dumps(self.all_episodes))
        with patch('utils.open', m):
            received = utils.load_episodes(series, filename)
        self.assertListEqual(expected, received)
        self.assertEqual(Path(m.call_args[0][0]), Path('data') / filename)

    def test_serie1(self):
        eps = self.all_episodes
        self.assert_episodes_loaded('serie1', [eps[4], eps[2]])

    def test_serie2(self):
        eps = self.all_episodes
        self.assert_episodes_loaded('serie2', [eps[0], eps[3], eps[1]])


if __name__ == '__main__':
    unittest.main()
