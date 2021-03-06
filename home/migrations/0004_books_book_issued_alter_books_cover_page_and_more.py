# Generated by Django 4.0.5 on 2022-07-01 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_student_books_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_issued',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='books',
            name='cover_page',
            field=models.ImageField(upload_to='cover_page'),
        ),
        migrations.AlterField(
            model_name='books',
            name='pdf',
            field=models.FileField(upload_to='pdf'),
        ),
    ]
