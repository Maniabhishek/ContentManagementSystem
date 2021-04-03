from django.http import request, response
from django.test import TestCase, Client
from django.urls import reverse, resolve
from appcms.models import Content
from rest_framework.test import APIRequestFactory, APITestCase
from django.contrib.auth.models import User
from appcms.models import Content
from appcms.api.views import ContentCreateView
from django.contrib.auth import login

# we can also use request factory this is not only the way
class Test(APITestCase, TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse("apiHome")
        self.registerUrl = reverse("apisregister")
        self.contentDetailUrl = reverse("contentDetail", kwargs={"pk": 1})
        self.contentCreateUrl = reverse("contentCreate")
        self.loginUrl = reverse("loggin")
        self.factory = APIRequestFactory()
        self.password = "TestUser12"
        self.user = User.objects.create(
            username="testUser1", email="Test12User@gmail.com"
        )
        self.user.set_password(self.password)
        self.user.save()
        self.content = Content.objects.create(
            author=self.user,
            title="my post",
            body="body of the post",
            summary="this is summary",
            category="Science",
        )

    def test_appcms_list_GET(self):
        # my setup code
        # all test code
        response = self.client.get(self.home_url)

        # then assertion
        self.assertEquals(response.status_code, 200)

    def test_appcms_detail(self):
        # all test code
        response = self.client.get(self.contentDetailUrl)
        self.assertEquals(response.data["title"], "my post")
        self.assertEquals(response.status_code, 200)


# this test will verify whether or not if user is able to login and register
class LoginTest(Test):
    def test_login(self):
        response = self.client.get(self.loginUrl)
        self.assertEqual(response.status_code, 200)

    def test_register_sccess(self):
        response = self.client.post(
            self.registerUrl,
            {
                "username": "Test3",
                "first_name": "test3",
                "last_name": "user",
                "email": "test3@gmail.com",
                "password": "TestUser12",
                "password2": "TestUser12",
                "phone": "9036158371",
                "pincode": "123456",
            },
            format="application/json",
        )
        self.assertEqual(response.status_code, 400)
