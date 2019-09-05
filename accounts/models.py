from django.db import models

class info(models.Model):
    flight_name = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=50, unique = True)
    invoice_date = models.CharField(max_length=30)
    type_of_invo = models.CharField(max_length=5)
    pnr =models.CharField(max_length=20)
    gstin_of_supplier = models.CharField(max_length=50)
    gstin_of_customer = models.CharField(max_length=50)
    organisation_name = models.CharField(max_length=80)
    origin = models.CharField(max_length= 15)
    destination =models.CharField(max_length=20)
    
    igst_transport_rate = models.CharField(max_length=15)
    igst_transport_amount = models.CharField(max_length=15)
    igst_airport_rate = models.CharField(max_length=15)
    igst_airport_amount = models.CharField(max_length=15) 
    
    cgst_transport_rate = models.CharField(max_length=15)
    cgst_transport_amount = models.CharField(max_length=15)
    cgst_airport_rate = models.CharField(max_length=15)
    cgst_airport_amount = models.CharField(max_length=15)

    sgst_transport_rate = models.CharField(max_length=15)
    sgst_transport_amount = models.CharField(max_length=15)
    sgst_airport_rate = models.CharField(max_length=15)
    sgst_airport_amount = models.CharField(max_length=15)

    total_gst = models.CharField(max_length=15)
    grand_total = models.CharField(max_length=15)