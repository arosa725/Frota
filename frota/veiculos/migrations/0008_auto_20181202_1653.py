# Generated by Django 2.1.3 on 2018-12-02 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0007_auto_20181111_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 16, 53, 27, 995141)),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='cnh',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]