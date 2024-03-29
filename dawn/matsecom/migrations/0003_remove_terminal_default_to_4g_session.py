# Generated by Django 5.0.3 on 2024-03-06 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "matsecom",
            "0002_service_subscription_technology_throughputpercentage_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="terminal",
            name="default_to_4g",
        ),
        migrations.CreateModel(
            name="Session",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("duration", models.PositiveIntegerField()),
                ("data_volume", models.PositiveIntegerField()),
                ("call_minutes", models.PositiveIntegerField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matsecom.service",
                    ),
                ),
                (
                    "subscriber",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="matsecom.subscriber",
                    ),
                ),
            ],
        ),
    ]
