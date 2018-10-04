# Generated by Django 2.0 on 2018-10-04 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_remove_transaction_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='Inventory.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='val', to='Inventory.Value'),
        ),
    ]
