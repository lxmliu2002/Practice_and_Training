# Generated by Django 4.2.3 on 2023-07-08 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_authordetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learn.author'),
        ),
    ]
