# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Features(models.Model):
    location = models.CharField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    latitude = models.TextField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitude = models.TextField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    map = models.CharField(db_column='MAP', blank=True, null=True)  # Field name made lowercase.
    elev = models.TextField(db_column='ELEV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'FEATURES'


class Flowers(models.Model):
    genus = models.CharField(db_column='GENUS', blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='SPECIES', blank=True, null=True)  # Field name made lowercase.
    comname = models.CharField(db_column='COMNAME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FLOWERS'


class Members(models.Model):
    name = models.CharField(db_column='NAME', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    membersince = models.DateField(db_column='MEMBERSINCE', blank=True, null=True)  # Field name made lowercase.
    numsightings = models.IntegerField(db_column='NUMSIGHTINGS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEMBERS'


class Sightings(models.Model):
    name = models.CharField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    person = models.CharField(db_column='PERSON', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    sighted = models.DateField(db_column='SIGHTED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIGHTINGS'
