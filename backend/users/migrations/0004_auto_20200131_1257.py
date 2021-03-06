# Generated by Django 3.0.2 on 2020-01-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200130_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='code',
            field=models.IntegerField(default=94372990, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rec_code',
            field=models.CharField(blank=True, max_length=24, null=True, verbose_name='Recommender code'),
        ),
    ]
