# Generated by Django 2.0.5 on 2018-06-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20180617_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashcard',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='drawdeposit',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='drawdeposit',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='dcbalance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='scbalance',
            field=models.FloatField(default=0),
        ),
    ]
