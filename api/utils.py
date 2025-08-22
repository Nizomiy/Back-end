from rest_framework import serializers


def validate_phone_number(value: str):
    if len(value) < 8:
        raise serializers.ValidationError("Telefon raqami kamida 8 ta belgidan iborat bo‘lishi kerak.")

    if not value.replace("+", "").isdigit():
        raise serializers.ValidationError("Telefon raqami faqat raqam va '+' belgisidan iborat bo‘lishi kerak.")

    return value
