# Generated by Django 5.0.2 on 2024-08-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=255)),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                ("preco", models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
            ],
        ),
    ]
