# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BusinessOrder(models.Model):
    field_id = models.CharField(db_column='\ufeffID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    billno = models.CharField(db_column='BillNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billdate1 = models.CharField(db_column='Billdate1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shopcode = models.CharField(db_column='Shopcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodscode = models.CharField(max_length=255, blank=True, null=True)
    qty = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    vipcardno = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    holiday = models.CharField(max_length=255, blank=True, null=True)
    orderamount = models.CharField(max_length=255, blank=True, null=True)
    orderqty = models.CharField(max_length=255, blank=True, null=True)
    amounttag = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BusinessOrder'
