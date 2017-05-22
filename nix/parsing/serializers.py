from rest_framework import serializers
from parsing.models import *
from rest_framework.utils.serializer_helpers import ReturnDict


class CustomListSerializer(serializers.ListSerializer):
    @property
    def data(self):
        return ReturnDict([('posts', super(serializers.ListSerializer, self).data)], serializer=self)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'url', 'site')
        list_serializer_class = CustomListSerializer
