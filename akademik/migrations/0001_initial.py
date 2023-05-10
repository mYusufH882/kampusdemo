# Generated by Django 4.2.1 on 2023-05-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fakultas",
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
                ("nama_fakultas", models.CharField(max_length=150, null=True)),
                ("prodi", models.CharField(max_length=150, null=True)),
            ],
            options={
                "db_table": "fakultas",
            },
        ),
    ]
