# Generated by Django 2.0.2 on 2018-02-11 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Risks', '0005_auto_20180210_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risktype',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risks_type', to='Risks.Risk'),
        ),
    ]
