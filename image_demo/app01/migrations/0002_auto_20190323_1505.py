# Generated by Django 2.1.7 on 2019-03-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usericon',
            name='username',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
