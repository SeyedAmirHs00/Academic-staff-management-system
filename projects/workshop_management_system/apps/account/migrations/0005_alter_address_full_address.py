# Generated by Django 5.0.1 on 2024-02-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_roles_user_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='full_address',
            field=models.TextField(unique=True, verbose_name='Full Address'),
        ),
    ]
