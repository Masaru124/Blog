# Generated by Django 5.1.4 on 2024-12-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0008_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
