# Generated by Django 5.1.4 on 2024-12-18 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]