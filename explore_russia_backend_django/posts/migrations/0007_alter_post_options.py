# Generated by Django 5.1.4 on 2024-12-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["id"],
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
