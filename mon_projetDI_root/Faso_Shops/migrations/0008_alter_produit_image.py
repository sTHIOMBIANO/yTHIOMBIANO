# Generated by Django 4.2 on 2023-05-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faso_Shops', '0007_pagne_pretporter_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='../static/album'),
        ),
    ]
