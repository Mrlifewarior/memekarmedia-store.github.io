# Generated by Django 2.2.14 on 2020-10-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201026_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2),
        ),
    ]
