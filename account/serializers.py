from rest_framework import serializers

from account.models import MyUser

#TODO: register serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_')

#TODO: Login serializer