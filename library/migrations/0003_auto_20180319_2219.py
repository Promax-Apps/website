# Generated by Django 2.0.3 on 2018-03-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20180319_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Publication Date'),
        ),
    ]
