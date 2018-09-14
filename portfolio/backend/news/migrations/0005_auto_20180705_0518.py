# Generated by Django 2.0.6 on 2018-07-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subject',
            field=models.CharField(choices=[('business', 'Business'), ('arts', 'Arts'), ('tech', 'Tech'), ('sports', 'Sports'), ('lifestyle', 'Lifestyle'), ('culture', 'Culture'), ('travel', 'Travel'), ('opinion', 'Opinion'), ('politics', 'Politics'), ('national', 'National'), ('world', 'World')], default='arts', max_length=9),
        ),
    ]