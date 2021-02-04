# Generated by Django 3.1.4 on 2021-01-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210125_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seasonproduct',
            name='all',
        ),
        migrations.RemoveField(
            model_name='seasonproduct',
            name='rainy',
        ),
        migrations.RemoveField(
            model_name='seasonproduct',
            name='summer',
        ),
        migrations.RemoveField(
            model_name='seasonproduct',
            name='winter',
        ),
        migrations.AddField(
            model_name='seasonproduct',
            name='seasonName',
            field=models.CharField(default='Summer', max_length=100),
        ),
    ]
