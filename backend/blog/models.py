from django.db import models


class PublicationCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField(upload_to='publication_images')
    category = models.ForeignKey(to=PublicationCategory, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return f'Публикация:  {self.name} | Категория {self.category.name}'