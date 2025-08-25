from rest_framework import viewsets
from .models import LinksModel, NewsModel, FooterModel, NewsLinkModel
from .serializers import (
    LinksModelSerializer,
    NewsModelSerializer,
    FooterModelSerializer,
    NewsLinkModelSerializer,
)


class LinksModelViewSet(viewsets.ModelViewSet):
    queryset = LinksModel.objects.all()
    serializer_class = LinksModelSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer


class FooterModelViewSet(viewsets.ModelViewSet):
    queryset = FooterModel.objects.all()
    serializer_class = FooterModelSerializer


class NewsLinkModelViewSet(viewsets.ModelViewSet):
    queryset = NewsLinkModel.objects.all()
    serializer_class = NewsLinkModelSerializer
