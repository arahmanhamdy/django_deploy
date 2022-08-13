# Generated by Django 4.0.6 on 2022-07-31 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_track_student_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='create_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='update_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
