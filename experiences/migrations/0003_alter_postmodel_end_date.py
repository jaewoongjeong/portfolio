# Generated by Django 3.2.6 on 2021-12-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_remove_postmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
