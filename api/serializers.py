from rest_framework import serializers
from .models import PagesModel, TitleModel, SectionsModel, LinksModel, NewsModel, FooterModel, NewsLinkModel, Council, \
    Department, Genealogy


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagesModel
        fields = [
            "logo_name",
            "logo",
            "img",
            "text1",
            "text2",
        ]


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleModel
        fields = [
            "name",
        ]


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionsModel
        fields = [
            "title_name",
            "main_paragraph",
            "university_name",
            "text1",
            "text2",
            "img",
            "phone_number",
            "date_time",
            "years"
        ]


class LinksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksModel
        fields = [
            "id",
            "name",
            "logo",
            "url_link",
        ]


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = [
            "id",
            "title",
            "image",
            "date_time",
            "text1",
            "text2",
        ]


class FooterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = [
            "id",
            "logo_name",
            "logo",
            "text",
            "phone_number1",
            "phone_number2",
            "phone_number3",
            "phone_number4",
        ]


class NewsLinkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLinkModel
        fields = [
            "id",
            "news",
            "text",
            "url",
        ]


class DepartmentFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "title", "row", "order", "parent"]

class CouncilFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Council
        fields = ["id", "title"]

class GenealogyFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genealogy
        fields = ["id", "title_name"]