# Generated by Django 4.1 on 2022-11-15 09:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_profile_other_exemptions_profile_passport_number_and_more'),
        ('advertisement', '0009_alter_advertisement_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilitaryServiceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
            options={
                'verbose_name': 'MilitaryServiceStatus',
                'verbose_name_plural': 'MilitaryServiceStatus',
            },
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='exemption_or_complete_military_service',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='get_intern',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='is_show_salary',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='is_unknown',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='remote',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='province',
            field=models.CharField(blank=True, choices=[('آذربایجان شرقی', 'آذربایجان شرقی'), ('آذربایجان غربی', 'آذربایجان غربی'), ('اردبیل', 'اردبیل'), ('اصفهان', 'اصفهان'), ('البرز', 'البرز'), ('ایلام', 'ایلام'), ('بوشهر', 'بوشهر'), ('تهران', 'تهران'), ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'), ('خراسان جنوبی', 'خراسان جنوبی'), ('خراسان رضوی', 'خراسان رضوی'), ('خراسان شمالی', 'خراسان شمالی'), ('خوزستان', 'خوزستان'), ('زنجان', 'زنجان'), ('سمنان', 'سمنان'), ('سیستان و بلوچستان', 'سیستان و بلوچستان'), ('فارس', 'فارس'), ('قزوین', 'قزوین'), ('قم', 'قم'), ('کردستان', 'کردستان'), ('کرمان', 'کرمان'), ('کرمانشاه', 'کرمانشاه'), ('کهگیلویه و بویراحمد', 'کهگیلویه و بویراحمد'), ('گلستان', 'گلستان'), ('گیلان', 'گیلان'), ('لرستان', 'لرستان'), ('مازندران', 'مازندران'), ('مرکزی', 'مرکزی'), ('هرمزگان', 'هرمزگان'), ('همدان', 'همدان'), ('یزد', 'یزد')], max_length=200, null=True, verbose_name='province'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='type_of_salary',
            field=models.CharField(blank=True, choices=[('پیشنهادی', 'پیشنهادی'), ('توافقی', 'توافقی')], max_length=75, null=True, verbose_name='salary'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='country',
            field=models.CharField(default='Iran', max_length=100, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='job_description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='job description'),
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='languages',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='maximum_age',
            field=models.PositiveIntegerField(default='there is no limit', validators=[django.core.validators.MaxValueValidator(50)], verbose_name='maximum age'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='minimum_age',
            field=models.PositiveIntegerField(default='there is no limit', validators=[django.core.validators.MinValueValidator(18)], verbose_name='minimum age'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='organizational_category',
            field=models.CharField(max_length=75, verbose_name='organizational category'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='salary',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='salary'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='type_of_cooperation',
            field=models.CharField(choices=[('full-time', 'full-time'), ('per time', 'per time'), ('remote', 'remote')], max_length=75, verbose_name='type of cooperation'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='work_time',
            field=models.TimeField(blank=True, max_length=250, null=True, verbose_name='work time'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='military_service_status',
            field=models.ManyToManyField(to='advertisement.militaryservicestatus', verbose_name='Military Service Status'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='languages',
            field=models.ManyToManyField(to='accounts.language', verbose_name='languages'),
        ),
    ]
