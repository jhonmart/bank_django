from rest_framework import serializers
from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    def validate(self, data):  # pylint: disable=W0221
        if UserModel.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({'email': 'Email já existe'})
        return data

    class Meta:
        model = UserModel
        fields = ('__all__')


class UserListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = UserModel
        exclude = ('password',)
