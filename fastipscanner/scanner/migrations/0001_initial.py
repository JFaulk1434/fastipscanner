# Generated by Django 5.0.4 on 2024-09-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ScanResult",
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
                ("ip_address", models.GenericIPAddressField()),
                ("mac_address", models.CharField(max_length=17)),
                ("manufacturer", models.CharField(blank=True, max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
