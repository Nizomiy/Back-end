from django.db import models

# Create your models here.

class LinksModel(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='links_logos/')
    url_link = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    date_time = models.DateTimeField()
    text = models.TextField()
    text2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class FooterModel(models.Model):
    logo_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='footer_logos/')
    text = models.TextField()
    phone_number1 = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    phone_number3 = models.CharField(max_length=20, blank=True, null=True)
    phone_number4 = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.logo_name


class NewsLinkModel(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.text
