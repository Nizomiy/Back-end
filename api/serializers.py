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


class DepartmentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ["id", "title", "row", "order", "parent", "children"]

    def get_children(self, obj):
        children = obj.children.all().order_by("row", "order")
        return DepartmentSerializer(children, many=True).data


class CouncilSerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField()

    class Meta:
        model = Council
        fields = ["id", "title", "departments"]

    def get_departments(self, obj):
        departments = obj.departments.filter(parent__isnull=True).order_by("row", "order")
        return DepartmentSerializer(departments, many=True).data


class GenealogySerializer(serializers.ModelSerializer):
    councils = CouncilSerializer(many=True, read_only=True)

    class Meta:
        model = Genealogy
        fields = ["id", "title_name", "councils"]
