from django.db import models


class PagesModel(models.Model):
    logo_name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="pages_img")
    img = models.ImageField(upload_to="pages_img")
    text1 = models.TextField()
    text2 = models.TextField()

    def __str__(self):
        return self.text1


class TitleModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SectionsModel(models.Model):
    title_name = models.ForeignKey(TitleModel, on_delete=models.CASCADE)
    main_paragraph = models.TextField()
    university_name = models.CharField(max_length=64)
    text1 = models.TextField()
    text2 = models.TextField()
    img = models.ImageField(upload_to="sections_img")
    phone_number = models.CharField(max_length=16, default='+998')
    date_time = models.DateTimeField(auto_now=True)
    years = models.CharField(max_length=4)
