# Generated by Django 2.1.7 on 2019-03-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190321_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[(1, '男'), (2, '女')], default='男', max_length=32),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.CharField(choices=[(1, '普通会员'), (2, 'VIP'), (3, 'SVIP')], default='普通会员~', max_length=32),
        ),
    ]
