# Generated by Django 3.0.3 on 2020-02-15 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name': '用户模型类a', 'verbose_name_plural': '用户模型类s'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='用户类',
        ),
    ]
