# Generated by Django 4.0.5 on 2022-06-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='Email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='Nom',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='admin',
            name='Password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='admin',
            name='prenom',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='image',
            field=models.ImageField(upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name_categorie',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Contenu',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Nom',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='livre',
            name='Auteur',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='livre',
            name='Description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='livre',
            name='Titre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Nom',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(max_length=30),
        ),
    ]
