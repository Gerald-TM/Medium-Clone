# Generated by Django 4.1.5 on 2023-02-17 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="publish",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="article", name="updated", field=models.DateField(auto_now=True),
        ),
    ]
