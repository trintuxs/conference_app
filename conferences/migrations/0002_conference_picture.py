# Generated by Django 4.2.2 on 2023-06-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
