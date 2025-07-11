# Generated by Django 4.2.19 on 2025-06-17 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notatki', '0005_alter_notatka_options_notatka_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='notatka',
            name='data_modyfikacji',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='notatka',
            name='data_utworzenia',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
