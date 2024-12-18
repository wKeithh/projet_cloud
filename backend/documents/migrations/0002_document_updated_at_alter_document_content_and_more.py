# Generated by Django 5.1.4 on 2024-12-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
