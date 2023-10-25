from django.db import models

# Create your models here.
class company(models.Model):
    company_id      = models.IntegerField(primary_key=True)
    comp_name       = models.CharField(max_length=50,default=" ")
    comp_sector     = models.CharField(max_length=50,default=" ")
    comp_desc       = models.TextField(default=" ")
    comp_values     = models.TextField(default=" ")
    comp_street     = models.CharField(max_length=50, null=False, default=" ")
    city            = models.CharField(max_length=50, null=False, default=" ")
    postal_code     = models.CharField(max_length=10, null=False, default=" ")
    country         = models.CharField(max_length=50, null=False, default=" ")
    comp_linkedin   = models.CharField(max_length=100, default=" ")
    comp_instagram  = models.CharField(max_length=100, default=" ")
    
class company_contact(models.Model):
    comp_contactid  = models.IntegerField(primary_key=True)
    contact_name    = models.CharField(max_length=50, default=" ")
    contact_role    = models.CharField(max_length=100, default=" ")
    contact_emailid = models.CharField(max_length=100, default=" ")
    company_id      = models.ForeignKey(company, on_delete=models.CASCADE)
    
class company_stats(models.Model):
    stats_id        = models.IntegerField(primary_key=True)
    active_jobs     = models.IntegerField(default=0)
    app_received    = models.IntegerField(default=0)
    candidates_match= models.IntegerField(default=0)
    company_id      = models.ForeignKey(company, on_delete=models.CASCADE)    
    
   
