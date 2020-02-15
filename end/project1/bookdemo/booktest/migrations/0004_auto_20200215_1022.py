# Generated by Django 3.0.3 on 2020-02-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20200215_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.CharField(blank=True, db_column='description', help_text='请输入书籍备注信息', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=20, verbose_name='图书名'),
        ),
    ]
