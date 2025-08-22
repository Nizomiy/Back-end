from rest_framework import serializers
from .models import PagesModel, TitleModel, SectionsModel


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