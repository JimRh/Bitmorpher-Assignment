from rest_framework import serializers
from .models import User

class UserSerialziers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email','user_type']