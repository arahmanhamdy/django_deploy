# Generated by Django 4.0.6 on 2022-07-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='salary',
            field=models.FloatField(default=1000),
            preserve_default=False,
        ),
    ]
