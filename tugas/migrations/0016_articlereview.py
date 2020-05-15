# Generated by Django 2.1.5 on 2020-05-08 08:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0015_article_articlerating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleRating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('articleTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tugas.Article')),
            ],
        ),
    ]
