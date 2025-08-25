from rest_framework import serializers
from .models import PagesModel, TitleModel, SectionsModel, LinksModel, NewsModel, FooterModel, NewsLinkModel


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagesModel
        fields = "__all__"


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleModel
        fields = "__all__"


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionsModel
        fields = "__all__"

        
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
