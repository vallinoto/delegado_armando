# Generated by Django 4.2.6 on 2023-10-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="TAG Default", max_length=255),
        ),
    ]
