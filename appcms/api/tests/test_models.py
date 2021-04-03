from django.test import TestCase
from django.contrib.auth.models import User
from appcms.models import Content
from appuser.models import Profile
import re


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testUser1", email="Test12User@gmail.com", password="Testuser"
        )
        self.user1 = User.objects.create(
            username="testUser2", email="Test12User@gmail.com", password="Test12User"
        )

    # testing user creation using id of the user and then also validating the password
    def validate_password(self, obj):

        password = obj.password
        if len(password) < 8:
            return False

        if not re.match(r"^(?=.{8,}$)(?=.*?[a-z])(?=.*?[A-Z])", password):
            return False
        return True

    # testing user creation using id of the user and then also validating the password
    def test_user_is_created_or_not(self):
        self.assertTrue(self.validate_password(self.user))
        self.assertEquals(self.user.id, 1)

    # testing content model
    def test_content_model(self):
        content1 = Content.objects.create(
            author=self.user,
            title="my post",
            body="body of the post",
            summary="this is summary",
            category="Science",
        )
        content2 = Content.objects.create(
            author=self.user,
            title="my post2",
            body="body of the post2",
            summary="this is summary2",
            category="Science",
        )
        self.assertEquals(content1.author, self.user)
        self.assertEquals(content2.title, "my post2")

    def validate_phone(self, obj):
        if len(obj.phone) < 10:
            return False
        if not re.match(r"^[0-9]*$", obj.phone):
            return False
        return True

    def validate_pincode(self, obj):
        if len(obj.pincode) < 6:
            return False
        if not re.match(r"^[0-9]*$", obj.pincode):
            return False
        return True

    # this test_profile_model will test all the fields filled by the user test case will passonly if the user is entering data in the correct format
    def test_profile_model(self):
        profile1 = Profile.objects.create(
            user_author=self.user, phone="9036158371", pincode="123456"
        )
        isValidPhone = self.validate_phone(profile1)
        isValidPincode = self.validate_pincode(profile1)
        """ this will fail if we use same user id as user_author is one to one field"""
        # profile1 = Profile.objects.create(
        #     user_author=self.user, phone="9036158371", pincode="123456"
        # )

        profile2 = Profile.objects.create(
            user_author=self.user1, phone="9901549071", pincode="123456"
        )
        isValidPincode1 = self.validate_pincode(profile2)
        isValidPincode2 = self.validate_pincode(profile2)
        isValidPhone2 = self.validate_phone(profile2)
        self.assertTrue(isValidPincode1)
        self.assertTrue(isValidPincode2)
        self.assertTrue(isValidPhone2)
        self.assertTrue(isValidPhone)
        self.assertEquals(profile1.user_author, self.user)
        self.assertEquals(profile2.user_author, self.user1)
