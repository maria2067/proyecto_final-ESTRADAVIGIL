# Generated by Django 4.0.5 on 2022-07-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_link',
            field=models.CharField(default='', max_length=256),
        ),
    ]
