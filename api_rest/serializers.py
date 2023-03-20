from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User                                        ## Qual modelo vamos serializar e quais campos.
        fields ='__all__'


