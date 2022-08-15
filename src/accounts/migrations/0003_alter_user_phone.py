# Generated by Django 4.1 on 2022-08-15 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_email_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number.', regex='^989\\d{2}\\d{3}\\d{4}$')], verbose_name='phone'),
        ),
    ]
