from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from nests.views import index


class IndexTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_index_returns_proper_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endwith(b'</html>'))
