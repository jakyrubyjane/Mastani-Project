# Generated by Django 4.2.16 on 2024-12-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer_app', '0005_isipulsa_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='is_sender',
            field=models.BooleanField(default=True),
        ),
    ]