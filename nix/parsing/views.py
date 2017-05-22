from rest_framework.generics import ListAPIView
from parsing.serializers import *


class PostList(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        if self.kwargs.get('site', None):
            return Article.objects.filter(site=self.kwargs['site']).order_by('-id')
        else:
            return Article.objects.all().order_by('-id')
