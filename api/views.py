from rest_framework import viewsets
from .models import PagesModel, TitleModel, SectionsModel
from .serializers import PagesSerializer, TitleSerializer, SectionsSerializer


class PagesViewSet(viewsets.ModelViewSet):
    queryset = PagesModel.objects.all()
    serializer_class = PagesSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = TitleModel.objects.all()
    serializer_class = TitleSerializer


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = SectionsModel.objects.all()
    serializer_class = SectionsSerializer