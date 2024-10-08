# Generated by Django 4.1.5 on 2023-03-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0004_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                help_text="Please enter the category name.", max_length=128, unique=True
            ),
        ),
    ]
