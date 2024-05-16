# Generated by Django 5.0.4 on 2024-05-02 13:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Duree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('nbrsJours', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ImageVoyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pays', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatusContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Nom')),
                ('prenom', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Prenom')),
                ('email', models.EmailField(max_length=50, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Email')),
                ('text', models.TextField(blank=True, max_length=350, verbose_name='Message')),
                ('dateCreate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voyage.statuscontact')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=400)),
                ('prix', models.IntegerField()),
                ('dateCreate', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('Duree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.duree')),
                ('Pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.pays')),
            ],
        ),
        migrations.CreateModel(
            name='ContactHasVoyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idContact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.formcontact')),
                ('idVoyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='VoyageHasCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.category')),
                ('idVoyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.voyage')),
            ],
        ),
        migrations.CreateModel(
            name='VoyageHasImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idImageVoyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.imagevoyage')),
                ('idVoyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.voyage')),
            ],
        ),
    ]
