from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator


class Duree(models.Model):
    dateDebut = models.DateField()
    dateFin = models.DateField()
    nbrsJours = models.CharField(max_length=5)
    def __str__(self):
        return self.nbrsJours
        
    
class Pays(models.Model):
    pays = models.CharField(max_length=50)
    def __str__(self):
        return self.pays
    
    
class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category
    
class ImageVoyage(models.Model):
    url = models.TextField(max_length=500)

    
class Voyage(models.Model):
    destination = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    prix = models.IntegerField()
    dateCreate = models.DateTimeField(auto_now_add= True)
    dateModified = models.DateTimeField(auto_now= True)
    
    Duree = models.ForeignKey(Duree, on_delete=models.CASCADE)
    Pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.destination} {self.prix}"

class VoyageHasCategory(models.Model):
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idVoyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    
class StatusContact(models.Model):
    Status = models.CharField( max_length=50)
    def __str__(self):
        return self.Status
            
class FormContact(models.Model):
    nom = models.CharField(max_length=50, validators=[MinLengthValidator(2)], verbose_name='Nom')
    prenom = models.CharField(max_length=50,validators=[MinLengthValidator(2)], verbose_name='Prenom')
    email = models.EmailField(max_length=50, unique=True,validators=[EmailValidator()], verbose_name='Email')
    text = models.TextField(max_length=350, blank=True, verbose_name='Message')
    dateCreate = models.DateTimeField(auto_now_add= True)
    status = StatusContact.objects.get(pk=4)
    Status = models.ForeignKey(StatusContact, on_delete=models.DO_NOTHING, default=status)
    def __str__(self):
        return f"{self.nom} {self.prenom} {self.email} {self.dateCreate} {self.Status}"
    
class ContactHasVoyage(models.Model):
    idVoyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    idContact = models.ForeignKey(FormContact, on_delete=models.CASCADE)
            
class VoyageHasImage(models.Model):
    idVoyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    idImageVoyage = models.ForeignKey(ImageVoyage, on_delete=models.CASCADE)