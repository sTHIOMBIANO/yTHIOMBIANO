# Generated by Django 4.2 on 2023-05-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faso_Shops', '0005_alter_commande_produit'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default=2000, max_length=300),
            preserve_default=False,
        ),
    ]
