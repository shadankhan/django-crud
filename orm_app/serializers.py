from rest_framework import serializers
from .models import Profile, Post_ad

class Post_adSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post_ad
		fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
	post_ad = Post_adSerializer(read_only=True, many=True)
	class Meta:
		model=Profile
		fields='__all__'