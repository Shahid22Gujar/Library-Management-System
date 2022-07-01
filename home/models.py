
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.
ROLE=(
    ("Admin","Admin"),
    ("Student","Student"),
)


class User(AbstractUser):
    role=models.CharField(choices=ROLE,max_length=50)

class Books(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    cover_page=models.ImageField(upload_to='cover_page')
    book_issued=models.DateTimeField(default=now)

    """Overiding delete method"""
    def delete(self, *args, **kwargs):
        self.cover_page.delete()
        self.pdf.delete()
        super(Books, self).delete(*args, **kwargs) # Call the "real" save() method.
       

    class Meta:
        verbose_name="Book"

    def __str__(self) -> str:
    
        return self.title

