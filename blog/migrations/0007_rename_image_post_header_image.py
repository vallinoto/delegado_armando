# Generated by Django 4.2.6 on 2023-11-12 23:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_post_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="image",
            new_name="header_image",
        ),
    ]
