# Generated by Django 2.1.7 on 2019-03-18 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, '普通用户'), (2, '会员')], default=1),
        ),
    ]
