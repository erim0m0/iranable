# Generated by Django 4.1 on 2022-12-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_companyprofile_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='logo'),
        ),
    ]
