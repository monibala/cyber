# Generated by Django 4.1.5 on 2023-04-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.TextField(blank=True, null=True),
        ),
    ]