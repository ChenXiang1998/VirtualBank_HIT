# Generated by Django 2.0.5 on 2018-06-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_drawdeposit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawdeposit',
            name='datafrom',
            field=models.CharField(default='自动存取款机', max_length=64, null=True),
        ),
    ]
