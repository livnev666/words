from django.db import models

# Create your models here.


class Text(models.Model):

    file_name = models.FileField(upload_to='gallery/%y/%m/%d/',
                                 default='', blank=True, null=False, verbose_name='Название файла')

    def __str__(self):
        return f'{self.file_name}'

    class Meta:
        verbose_name = 'Имя файла'
        verbose_name_plural = 'Имя файлов'
