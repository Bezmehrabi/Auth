# Generated by Django 3.0.2 on 2020-01-30 19:29

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200130_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='code',
            field=models.IntegerField(default=68046922, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rec_code',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(11, message=''), users.validators.validate_phonenumber], verbose_name='Recommender code'),
        ),
    ]
