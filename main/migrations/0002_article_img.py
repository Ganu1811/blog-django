# Generated by Django 4.2.5 on 2023-09-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='images/'),
        ),
    ]