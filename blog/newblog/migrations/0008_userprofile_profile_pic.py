# Generated by Django 5.1.4 on 2024-12-31 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
