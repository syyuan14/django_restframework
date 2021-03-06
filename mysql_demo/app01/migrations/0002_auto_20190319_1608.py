# Generated by Django 2.1.7 on 2019-03-19 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TailNumber', models.CharField(max_length=64)),
                ('LineNumber', models.CharField(max_length=64)),
                ('AC_ASN', models.CharField(max_length=64)),
                ('AC_Variable', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Scar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField()),
                ('scar_type', models.SmallIntegerField(choices=[(1, 'crack'), (2, 'perforation'), (3, 'rivets'), (4, 'scartch'), (5, 'flake')], default=1)),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Airplane')),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
