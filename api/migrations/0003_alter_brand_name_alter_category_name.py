# Generated by Django 5.1.1 on 2024-11-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_category_level_category_lft_category_rght_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]