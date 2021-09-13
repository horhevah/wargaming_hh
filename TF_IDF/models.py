from django.db import models

class Words(models.Model):
    word = models.CharField(null=True,max_length=50)
    file = models.ForeignKey('Files', null=True, on_delete=models.PROTECT)
    tf = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    idf = models.FloatField(null=True, blank=True)

class Files(models.Model):
    # pass
    file = models.FileField(null=True,upload_to='files/%Y/%m/%d')
    file_name = models.CharField(null=True, max_length=50)

# class Filesdsd(models.Model):
#     # pass
#     # file = models.FileField()
#     file_name = models.CharField(null=True, max_length=50)
