from django.db import models

# Create your models here.
class Author(models.Model):
    #relations
    GENDERS = ((1, 'Kişi'), (2, 'Qadın'), )
    #information
    fullname = models.CharField('Adı',max_length=255)
    author_image = models.ImageField('Şekili',upload_to='images/authors')
    gender = models.IntegerField('Cinsiyyeti',choices=GENDERS, default=1)
    date_of_birth = models.DateField('Doğum Tarixi',)
    nationality = models.CharField('Milliyeti',max_length=255)
    info = models.TextField('Haqqında',)

    #moderator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Yazar'
        verbose_name_plural= 'Yazarlar'
        ordering = ('fullname',)

    def __str__(self):
        return f"{self.fullname}"

class Book(models.Model):
    #relations
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name="books")
    category = models.ManyToManyField('Category')
    #information
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    page_count = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='images/books')

    #moderator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Kitab'
        verbose_name_plural= 'Kitablar'
        ordering = ('title',)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    #relations
    
    #information
    title = models.CharField(max_length=255)
    #moderator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= 'Kateqoriya'
        verbose_name_plural= 'Kateqoriyalar'
        ordering = ('title',)

    def __str__(self):
        return f"{self.title}"
