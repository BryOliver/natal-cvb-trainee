# Generated by Django 3.0.3 on 2020-05-06 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_descricao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Descricao',
        ),
        migrations.DeleteModel(
            name='Natal',
        ),
    ]