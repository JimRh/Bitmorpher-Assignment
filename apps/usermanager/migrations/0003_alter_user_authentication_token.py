# Generated by Django 5.0.6 on 2024-06-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0002_alter_user_authentication_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='authentication_token',
            field=models.CharField(editable=False, max_length=16),
        ),
    ]