# Generated by Django 4.2.3 on 2023-08-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboard',
            name='product_type',
            field=models.CharField(default='keyboard', max_length=20),
        ),
        migrations.AddField(
            model_name='keycap',
            name='product_type',
            field=models.CharField(default='keyboard', max_length=20),
        ),
        migrations.AddField(
            model_name='pcb',
            name='product_type',
            field=models.CharField(default='keyboard', max_length=20),
        ),
        migrations.AddField(
            model_name='switch',
            name='product_type',
            field=models.CharField(default='keyboard', max_length=20),
        ),
    ]