# Generated by Django 4.2.1 on 2023-05-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_remove_comprarmodel_comp_quanteidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprarmodel',
            name='comp_quanteidade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]