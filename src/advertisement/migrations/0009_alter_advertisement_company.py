# Generated by Django 4.1 on 2022-11-05 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_companyprofile_organizational_interface'),
        ('advertisement', '0008_alter_advertisement_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='company',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='accounts.companyprofile'),
        ),
    ]
