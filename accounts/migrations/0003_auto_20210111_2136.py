# Generated by Django 3.1.5 on 2021-01-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customaccount',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Endereço de email'),
        ),
    ]
