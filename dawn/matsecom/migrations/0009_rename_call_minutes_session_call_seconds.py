# Generated by Django 5.0.3 on 2024-03-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matsecom", "0008_rename_duration_invoice_charges_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="session",
            old_name="call_minutes",
            new_name="call_seconds",
        ),
    ]
