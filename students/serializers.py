from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Student, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class StudentSerializer(serializers.ModelSerializer):
    track = TrackSerializer(read_only=True)
    create_by = UserSerializer(read_only=True)
    track_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'salary', 'email', 'track', 'track_id', 'create_by')

    def create(self, validated_data):
        validated_data['create_by'] = self.context['request'].user
        return Student.objects.create(**validated_data)
