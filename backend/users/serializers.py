import re
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    invited = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ('name', 'code', 'invited')
    
    def get_invited(self, obj):
        return get_user_model().objects.filter(rec_code=obj.code).count()


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, label=_('password confirm'))


    class Meta:
        model = get_user_model()
        fields = ('telnum', 'name', 'rec_code', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True}}
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': _('Passwords do not match')})
        rec_code = data['rec_code']
        if rec_code and not get_user_model().objects.filter(code=rec_code).exists():
            raise serializers.ValidationError({'rec_code': _('User with this code is not found.')})

        return data

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            validated_data['telnum'],
            validated_data['name'],
            validated_data['password'],
            rec_code=validated_data['rec_code'],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    telnum = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(_('wrong username or password.')) 