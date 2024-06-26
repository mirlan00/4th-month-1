# Generated by Django 4.2.10 on 2024-03-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_rename_nubers_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Нумерация')),
                ('title', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('descriptions', models.TextField(verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
