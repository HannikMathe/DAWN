# Generated by Django 5.0.3 on 2024-03-07 22:39

import encrypted_model_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matsecom", "0012_alter_session_duration_alter_subscriber_imsi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscriber",
            name="imsi",
            field=encrypted_model_fields.fields.EncryptedCharField(unique=True),
        ),
    ]
