# Generated by Django 5.0.4 on 2024-09-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_rename_nome_da_trasacao_transacao_nome_da_transacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacao',
            old_name='autor_da_transacao',
            new_name='autor_transacao',
        ),
        migrations.RenameField(
            model_name='transacao',
            old_name='data_da_transacao',
            new_name='data_transacao',
        ),
        migrations.RenameField(
            model_name='transacao',
            old_name='descricao_da_transacao',
            new_name='descricao_transacao',
        ),
        migrations.RenameField(
            model_name='transacao',
            old_name='nome_da_transacao',
            new_name='nome_transacao',
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='valor_da_transacao',
        ),
        migrations.AddField(
            model_name='transacao',
            name='valor_transacao',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
