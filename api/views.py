from rest_framework import viewsets
from .models import PagesModel, TitleModel, SectionsModel, LinksModel, NewsModel, FooterModel, NewsLinkModel, Genealogy, \
    Council, Department
from .serializers import PagesSerializer, TitleSerializer, SectionsSerializer, LinksModelSerializer, \
    NewsModelSerializer, FooterModelSerializer, NewsLinkModelSerializer, GenealogySerializer, CouncilSerializer, \
    DepartmentSerializer
from rest_framework.response import Response


class GenealogyTreeViewSet(viewsets.ViewSet):

    def list(self, request):
        genealogies = Genealogy.objects.all()
        serializer = GenealogySerializer(genealogies, many=True)
        return Response(serializer.data)


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
