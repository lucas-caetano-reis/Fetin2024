# Generated by Django 5.0.4 on 2024-05-31 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listagem', '0002_alter_livro_livro_serie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['autor_nome']},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'ordering': ['livro_id']},
        ),
        migrations.AddField(
            model_name='livro',
            name='livro_sinopse',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='livro_autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='listagem.autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='livro_serie',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
