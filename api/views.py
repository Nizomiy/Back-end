from rest_framework import viewsets
from .models import PagesModel, TitleModel, SectionsModel, LinksModel, NewsModel, FooterModel, NewsLinkModel, Genealogy, \
    Council, Department
from .serializers import PagesSerializer, TitleSerializer, SectionsSerializer, LinksModelSerializer, \
    NewsModelSerializer, FooterModelSerializer, NewsLinkModelSerializer, GenealogyFlatSerializer, CouncilFlatSerializer, \
    DepartmentFlatSerializer
from rest_framework.response import Response
from collections import defaultdict


class GenealogyTreeViewSet(viewsets.ViewSet):

    def list(self, request):
        genealogies = Genealogy.objects.all()
        data = []

        for genealogy in genealogies:
            genealogy_item = GenealogyFlatSerializer(genealogy).data
            genealogy_item["councils"] = []

            for council in genealogy.councils.all():
                council_item = CouncilFlatSerializer(council).data

                grouped = defaultdict(list)
                for dept in council.departments.all().order_by("row", "order"):
                    dept_data = DepartmentFlatSerializer(dept).data
                    grouped[dept.row].append(dept_data)

                council_item["departments"] = []
                for row, depts in grouped.items():
                    council_item["departments"].append({
                        "row": row,
                        "items": depts
                    })

                genealogy_item["councils"].append(council_item)

            data.append(genealogy_item)

        return Response(data)


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
