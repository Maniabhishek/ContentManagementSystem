from rest_framework.serializers import ModelSerializer, ValidationError
from appuser.models import Profile
import re
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# this serializer class will validate all the users phone and pincode


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'pincode']

    def validate_phone(self, value):
        phone = value

        if len(phone) < 10:
            raise ValidationError(
                {'Please Check your phone number': 'check your phone number'})
        if not re.match(r"^[0-9]*$", phone):
            raise ValidationError(
                {'Please Check your phone number abc': 'check your phone number'})
        return value

    def validate_pincode(self, value):
        pincode = value
        if len(pincode) < 6:
            raise ValidationError(
                {'Please Check your picode': 'check your pincode'})
        if not re.match(r"^[0-9]*$", pincode):
            raise ValidationError(
                {'Please Check your phone number abc': 'check your pincode'})
        return value

# UserSerializer is for registraion purpose that will valiate the password (atleast one uppercase and one lowercase)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, required=True, label='Confirm Password')
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, required=True, label='Password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password', 'password2', 'profile']
        extra_kwargs = {"password": {
            "write_only": True
        }}

    def validate_email(self, value):
        email = value.lower()
        emailqs = User.objects.filter(email=email)
        if emailqs.exists():
            raise serializers.ValidationError(
                {'email already registered': "This email is already registered"})
        return value

    def validate_password(self, value):
        data = self.get_initial()
        password2 = data['password2']
        password = value

        if len(password) < 8:
            raise ValidationError(
                {'Password length atleast 8 characters': 'Please check the length of the password'})

        if password != password2:
            raise serializers.ValidationError(
                {'Password does not match': 'password should be the same at both input fields'})
        if not re.match(r"^(?=.{8,}$)(?=.*?[a-z])(?=.*?[A-Z])", password):
            raise ValidationError(
                {
                    'Password must contain at least 1 lowercase and 1 uppercase'
                })
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )

        profile_data = validated_data.pop('profile')

        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(
            user_author=user,
            phone=profile_data['phone'],
            pincode=profile_data['pincode']
        )

        return user
