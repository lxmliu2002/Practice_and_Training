# Generated by Django 4.2.3 on 2023-07-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.BooleanField(null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=64, verbose_name='名字'),
        ),
    ]
