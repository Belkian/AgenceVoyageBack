import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from voyage import models

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class VoyageType(DjangoObjectType):
    class Meta:
        model = models.Voyage

class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category
        
class VoyageHasImageType(DjangoObjectType):
    class Meta:
        model = models.VoyageHasImage

class ImageVoyageType(DjangoObjectType):
    class Meta:
        model = models.ImageVoyage
        
class PaysType(DjangoObjectType):
    class Meta:
        model = models.Pays        

class Query(graphene.ObjectType):
    Voyage = graphene.List(VoyageType)
    Voyage_by_destination = graphene.Field(VoyageType, destination=graphene.String())
    
    def resolve_Voyage(self,info):
        return models.Voyage.objects.select_related().all()
    
    def resolve_Voyage_by_destination(self, info, destination):
        return (
            models.Voyage.objects.get(destination=destination)
        )        
schema = graphene.Schema(query=Query)