"""Book Model"""

#django
from django.db import models



class Book(models.Model):
    title = models.CharField('book title' , blank=False , null=False , max_length=100)
    author = models.CharField('author' , blank=False , null=False , max_length=100)
    publication_date = models.DateField('publication date')
    cover = models.ImageField(
        'cover image',
        upload_to='books/cover/',
        blank=False,
        null=False
    )
    edition = models.CharField('edition' , blank=True , null=True , max_length=255)
    quantity = models.IntegerField(blank=False , null=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return book's str representation."""
        return str(self.title)
