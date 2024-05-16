from django.contrib import admin
from voyage.models import Duree, Pays, Category, Voyage, FormContact, StatusContact, ImageVoyage,VoyageHasImage

@admin.register(Duree)
class DureeAdmin(admin.ModelAdmin):
    model = Duree
    
@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    model = Pays
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    
@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    model = Voyage

@admin.register(FormContact)
class FormContactAdmin(admin.ModelAdmin):
    model = FormContact
    
@admin.register(StatusContact)
class StatusContactAdmin(admin.ModelAdmin):
    model = StatusContact
    
@admin.register(ImageVoyage)
class ImageVoyageAdmin(admin.ModelAdmin):
    model = ImageVoyage
    
@admin.register(VoyageHasImage)
class VoyageHasImageAdmin(admin.ModelAdmin):
    model = VoyageHasImage