from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    shortDis = models.TextField()
    slug = models.SlugField()
    readMin = models.CharField(max_length=255)
    firstPara = models.TextField()
    secondPara = models.TextField()
    thirdPara = models.TextField()
    imageFirst = models.ImageField(null=True)
    fourthPara = models.TextField(blank=True)
    fifthPara = models.TextField(blank=True)
    sixthPara = models.TextField(blank=True)
    imageSecond = models.ImageField(null=True, blank=True)
    seventhPara = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title



