# Generated by Django 4.2.2 on 2023-07-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toluport', '0002_project_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
