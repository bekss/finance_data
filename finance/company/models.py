from django.db import models


class ReceivedFile(models.Model):
    url_file = models.FileField(upload_to='media/received_csv')

    class Meta:
        verbose_name = 'Received File'
        verbose_name_plural = 'Received Files'

    def __str__(self):
        return self.url_file


class Url_File(models.Model):
    url_file = models.FileField()
    csv = models.FileField(upload_to='received_csv/')
    json_file = models.FileField(upload_to='media/json_file/')

    class Meta:
        verbose_name = 'URL FILE'
        verbose_name_plural = 'URL FILES'

    def __str__(self):
        return self.url_file
