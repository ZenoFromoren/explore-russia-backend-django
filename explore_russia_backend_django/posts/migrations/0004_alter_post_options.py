# Generated by Django 5.1.4 on 2024-12-21 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["createdAt"],
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
