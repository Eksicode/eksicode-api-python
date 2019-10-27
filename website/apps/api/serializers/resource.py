from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from apps.core.models import Resource, ResourceComment


class ResourceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceComment
        fields = [
            'id',
            'created_at',
            'last_updated_at',
            'commenter',
            'title',
            'content',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'last_updated_at',
        ]


class ResourceSerializer(TaggitSerializer, serializers.ModelSerializer):
    comments = ResourceCommentSerializer(read_only=True, many=True)
    tags = TagListSerializerField()

    class Meta:
        model = Resource
        fields = [
            'id',
            'created_at',
            'last_updated_at',
            'name',
            'link',
            'creator',
            'approved',
            'comments',
            'tags',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'last_updated_at',
        ]
