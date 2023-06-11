# Generated by Django 4.2.2 on 2023-06-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="arduino",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("langitude", models.FloatField(default=0)),
                ("longitude", models.FloatField(default=0)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
    ]