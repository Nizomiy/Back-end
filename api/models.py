from django.db import models


class PagesModel(models.Model):
    logo_name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="pages_img", null=True, blank=True)
    img = models.ImageField(upload_to="pages_img", null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text1


class TitleModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SectionsModel(models.Model):
    title_name = models.ForeignKey(TitleModel, on_delete=models.CASCADE)
    main_paragraph = models.TextField()
    university_name = models.CharField(max_length=64, null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="sections_img", null=True, blank=True)
    phone_number = models.CharField(max_length=16, default='+998', null=True, blank=True)
    date_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    years = models.CharField(max_length=4, null=True, blank=True)


class LinksModel(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='links_logos/', null=True, blank=True)
    url_link = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class FooterModel(models.Model):
    logo_name = models.CharField(max_length=255, )
    logo = models.ImageField(upload_to='footer_logos/', null=True, blank=True)
    text = models.TextField()
    phone_number1 = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    phone_number3 = models.CharField(max_length=20, blank=True, null=True)
    phone_number4 = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.logo_name


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    date_time = models.DateTimeField()
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class NewsLinkModel(models.Model):
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.text
