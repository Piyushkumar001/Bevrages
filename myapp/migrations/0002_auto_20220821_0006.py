# Generated by Django 3.0 on 2022-08-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='uom_id',
            field=models.IntegerField(null=True),
        ),
    ]