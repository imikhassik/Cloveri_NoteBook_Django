from django.db import models


class Form(models.Model):
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    number_1 = models.CharField(max_length=12)
    number_2 = models.CharField(max_length=12)
    email_1 = models.EmailField
    email_2 = models.EmailField
    
    
class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)


class Organization(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    head = models.ForeignKey(Form, on_delete=models.CASCADE)
    
    
class Position(models.Model):
    name = models.CharField(max_length=30)
    workplace = models.CharField(max_length=30)
    
    
class Additional(models.Model):
    name = models.CharField(max_length=30)


class Contact(models.Model):
    info = models.OneToOneField(Form, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    work = models.ForeignKey(Organization, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    additional = models.ForeignKey(Additional, on_delete=models.CASCADE)

