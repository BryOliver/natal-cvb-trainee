# Generated by Django 3.0.3 on 2020-05-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_missao_valores_visao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='titulo')),
                ('descricao', models.TextField(verbose_name='descrição de quem somos')),
            ],
        ),
    ]
