# Generated by Django 4.2 on 2023-04-04 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Faso_Shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date_ajout', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=500)),
                ('prix', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=5000)),
                ('date_ajout', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faso_Shops.categorys')),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
    ]
