# Generated by Django 4.2.6 on 2023-11-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_employee_mob_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=25000),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
