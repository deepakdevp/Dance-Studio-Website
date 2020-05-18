from rest_framework import serializers
from .models import userDetails

class messageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = userDetails
		fields ='__all__'

