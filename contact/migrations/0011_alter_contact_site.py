# Generated by Django 4.1.2 on 2022-10-12 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_alter_contact_clave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='site',
            field=models.BooleanField(default=False),
        ),
    ]