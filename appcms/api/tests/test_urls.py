from django.test import SimpleTestCase
from django.urls import reverse , resolve
from appcms.api.views import ContentListAPIView,ContentDetailAPIView,ContentUpdateAPIView,ContentDeleteAPIView,ContentCreateView


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('apiHome')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,ContentListAPIView)

    def test_post_detail(self):
        url = reverse('contentDetail',kwargs={"pk": 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,ContentDetailAPIView)
    
    def test_post_update(self):
        url = reverse('contentUpdate',kwargs={"pk": 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,ContentUpdateAPIView)
    
    def test_post_delete(self):
        url = reverse('contentDelete',kwargs={"pk": 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,ContentDeleteAPIView)

    def test_post_create(self):
        url = reverse('contentCreate')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,ContentCreateView)
    

