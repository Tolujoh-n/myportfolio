# Generated by Django 4.2.2 on 2023-07-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toluport', '0005_remove_certificate_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='course',
            field=models.CharField(default='coursera', max_length=255),
            preserve_default=False,
        ),
    ]
