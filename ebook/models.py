from django.db import models



class Admin(models.Model):
    Nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100,primary_key=True)
    Password = models.CharField(max_length=20)


    def __str__(self):
        return f" Bonjour {self.Nom} {self.prenom}"
class contact(models.Model):
    Nom = models.CharField(max_length=60)
    Email = models.EmailField(max_length=100)
    TEL = models.IntegerField()
    Contenu = models.TextField(max_length=300)


    def __str__(self):
        return f" Bonjour {self.Nom} "

class Utilisateur(models.Model):
    Nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100,primary_key=True)
    Password = models.CharField(max_length=20)
    def __str__(self):
        return f" Bonjour {self.Nom} {self.prenom} "
class Categorie(models.Model):
    Id_categorie = models.IntegerField(primary_key=True)
    name_categorie = models.CharField(max_length=40)
    image = models.ImageField(upload_to='covers')


    def __str__(self):
        return f"{self.name_categorie}"

class Livre(models.Model):
    Titre= models.CharField(max_length=50)
    Auteur= models.CharField(max_length=50)
    Description=models.CharField(max_length=500)
    Date_publication=models.DateTimeField()
    Date_Edition=models.DateTimeField()
    Id_categorie= models.ForeignKey(Categorie,on_delete=models.CASCADE)
    image = models.ImageField()
    Pdf= models.FileField()
    def __str__(self):
        return f" Le livre est : {self.Titre}  de {self.Auteur} "



# Create your models here.
