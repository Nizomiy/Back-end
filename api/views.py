from rest_framework import viewsets
from .models import PagesModel, TitleModel, SectionsModel, LinksModel, NewsModel, FooterModel, NewsLinkModel
from .serializers import PagesSerializer, TitleSerializer, SectionsSerializer, LinksModelSerializer, NewsModelSerializer, FooterModelSerializer, NewsLinkModelSerializer


class PagesViewSet(viewsets.ModelViewSet):
    queryset = PagesModel.objects.all()
    serializer_class = PagesSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = TitleModel.objects.all()
    serializer_class = TitleSerializer


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = SectionsModel.objects.all()
    serializer_class = SectionsSerializer


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
