from rest_framework import serializers
from .models import LinksModel, NewsModel, FooterModel, NewsLinkModel


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
            "text",
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
            "text",
            "url",
        ]
