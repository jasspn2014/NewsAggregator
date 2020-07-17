from django.db import models

class IndiaTodayNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title

class DainikJagranNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title

class HindustanTimesNews(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title

