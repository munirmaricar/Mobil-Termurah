# Generated by Django 3.0.2 on 2020-03-05 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0007_review_articlecontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='articleContent',
            new_name='carReview',
        ),
    ]
