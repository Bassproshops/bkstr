# Generated by Django 3.2 on 2021-07-26 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_postalcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nombre',
            field=models.CharField(default='Nombre por defecto', max_length=300),
            preserve_default=False,
        ),
    ]