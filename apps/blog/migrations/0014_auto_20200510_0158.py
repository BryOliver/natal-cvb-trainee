# Generated by Django 3.0.3 on 2020-05-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200510_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, null=True, verbose_name='de um titulo para a etiqueta')),
                ('descricao', models.TextField(max_length=100, null=True, verbose_name='descrição do evento')),
                ('imagem', models.ImageField(null=True, upload_to='eventos/', verbose_name='imagem do evento')),
                ('pagina', models.TextField(null=True, verbose_name='descrição na página do evento')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.AlterModelOptions(
            name='cards',
            options={'verbose_name': 'Cardoo', 'verbose_name_plural': 'Cardsoo'},
        ),
    ]
