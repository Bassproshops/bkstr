# Generated by Django 3.2.5 on 2021-07-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-created_at',), 'verbose_name': 'usuario'},
        ),
        migrations.AlterField(
            model_name='user',
            name='postalcode',
            field=models.PositiveSmallIntegerField(verbose_name='Zip'),
        ),
    ]
