from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(db_column='NAME', primary_key=True, blank=True, max_length=30)  # Field name made lowercase.
    membersince = models.DateField(db_column='MEMBERSINCE', blank=True, null=True)  # Field name made lowercase.
    numsightings = models.IntegerField(db_column='NUMSIGHTINGS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MEMBERS'

class Features(models.Model):
    location = models.CharField(db_column='LOCATION', primary_key=True, blank=True, max_length=30)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', blank=True, null=True, max_length=30)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    latitude = models.IntegerField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitude = models.IntegerField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maps = models.CharField(db_column='MAP', blank=True, null=True, max_length=30)  # Field name made lowercase.
    elev = models.IntegerField(db_column='ELEV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'FEATURES'

class Flowers(models.Model):
    genus = models.CharField(db_column='GENUS', blank=True, max_length=30)  # Field name made lowercase.
    species = models.CharField(db_column='SPECIES', blank=True, null=True, max_length=30)  # Field name made lowercase.
    comname = models.CharField(db_column='COMNAME', blank=True, primary_key=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FLOWERS'

class Sightings(models.Model):
    name = models.ForeignKey(Flowers, to_field = 'comname', db_column='NAME', on_delete=models.CASCADE)  # Field name made lowercase.
    person = models.CharField(db_column='PERSON', blank=True, max_length=30)  # Field name made lowercase.
    location = models.ForeignKey(Features, to_field = 'location', db_column='LOCATION', on_delete=models.CASCADE)  # Field name made lowercase.
    sighted = models.DateField(db_column='SIGHTED', blank=True)  # Field name made lowercase.

    class Meta:
        managed = True
        unique_together = (('name', 'person', 'location',  'sighted'), ) 
        db_table = 'SIGHTINGS'
