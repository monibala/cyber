# Generated by Django 4.1.5 on 2023-04-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default=True, null=True, upload_to='knowledge')),
            ],
        ),
    ]