# Generated by Django 2.2.6 on 2019-11-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191123_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='telegram_username',
            field=models.TextField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_username',
            field=models.TextField(max_length=50, unique=True),
        ),
    ]