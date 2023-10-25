from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.    

# Candidate Table:   
class Candidate(models.Model):
    candidate_id = models.IntegerField(primary_key=True)
    first_name      = models.CharField(max_length= 50,default=" ")
    last_name       = models.CharField(max_length= 50, default= " ")
    sex             = models.CharField(max_length=15, default= " ")
    date_of_birth   = models.DateField
    marital_status  = models.CharField(max_length=25, default=" ")
    email           = models.EmailField(unique=True, default=" ")
    phone_number    = PhoneNumberField(default='+41', blank = True,null=True)
    photo           = models.ImageField(upload_to='photos/', default=" ")
    disability      = models.CharField(max_length= 50,default=" ")
    street          = models.CharField(max_length=50, null=False, default=" ")
    city            = models.CharField(max_length=50, null=False, default=" ")
    postal_code     = models.CharField(max_length=10, null=False, default=" ")
    country         = models.CharField(max_length=50, null=False, default=" ")
    self_desc       = models.TextField(max_length=255, default=" ")
 
 # Candidate_account Table:   
class Candidate_account(models.Model):
    account_id          = models.IntegerField(primary_key=True)
    account_sts         = models.CharField(max_length=50, default=" ")
    account_hibernate   = models.BooleanField(default=False)
    candidate_id        = models.ForeignKey(Candidate, on_delete=models.CASCADE)   

#Candidate_certification Table:
class Candidate_certification(models.Model):
    certification_id    = models.IntegerField(primary_key=True)
    org_name            = models.CharField(max_length=100, default= " ")
    issuing_date        = models.DateField(null = True)
    expiry_date         = models.DateField(null = True)
    credential_id       = models.CharField(max_length=100, default= " ")
    credential_url      = models.CharField(max_length=100, default=" ")
    skillset            = models.TextField(max_length=255, default=" ")
    candidate_id        = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    
#Candidate_experience Table
class Candidate_exp(models.Model):
    exp_id              = models.IntegerField(primary_key=True)
    curr_comp           = models.CharField(max_length=50, default=" ")
    job_title           = models.CharField(max_length=50, default=" ")
    no_of_exp           = models.FloatField
    skills              = models.CharField(max_length=50, default=" ")
    work_desc           = models.TextField(max_length=100)
    date_of_joining     = models.DateField(null=True)
    date_of_termination = models.DateField(null=True)
    permit              = models.CharField(max_length=50, default=" ")
    notice_period_mon   = models.IntegerField
    sal_expec           = models.IntegerField
    language            = models.CharField(max_length=50, default=" ")
    level               = models.CharField(max_length=50, default=" ")
    candidate_id        = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    
# Candidate_EDucation table
class Candidate_edu(models.Model):
    edu_id              = models.IntegerField(primary_key=True)
    univ                = models.CharField(max_length=50, default=" ")
    course              = models.CharField(max_length=50, default=" ")
    degree              = models.CharField(max_length=50, default=" ")
    start_date          = models.DateField(null=True)
    end_date            = models.DateField(null=True)
    percentage          = models.IntegerField
    candidate_id        = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    
# Reference table
class Candidate_reference(models.Model):
    ref_id              = models.IntegerField(primary_key=True)
    ref_name            = models.CharField(max_length=50, default=" ")
    ref_Comp            = models.CharField(max_length=50, default=" ")
    ref_role            = models.CharField(max_length=50, default=" ")
    ref_Date            = models.DateField(null=True)
    ref_desc            = models.TextField(max_length=100)
    candidate_id        = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    
# Job table
class job(models.Model):
    job_id              = models.IntegerField(primary_key=True)
    job_title           = models.CharField(max_length=50, default=" ")
    job_position        = models.CharField(max_length=50, default=" ")
    company             = models.CharField(max_length=50, default=" ")
    job_location        = models.CharField(max_length=50, default=" ")
    job_type            = models.CharField(max_length=50, default=" ")
    job_desc            = models.TextField(max_length=100, default=" ")
    job_role            = models.CharField(max_length=50, default=" ")
    job_options         = models.CharField(max_length=50, default=" ")
    job_expiry_date     = models.DateField(null=True)
    job_exp_of_emp      = models.IntegerField(default=0)
    job_sal_expect      = models.CharField(max_length=50, default=" ")

# Application table
class Candidate_application(models.Model):
    app_id              = models.IntegerField(primary_key=True)
    app_status          = models.CharField(max_length=50, default=" ")
    candidate_id        = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_id              = models.ForeignKey(job, on_delete=models.CASCADE)
    
# Candidate_docs table:
class Candidate_Docs(models.Model):
    doc_id      = models.IntegerField(primary_key=True)
    doc_name    = models.CharField(max_length=50, default=" ")
    doc_data    = models.FileField(upload_to='resumes/', default=" ")
    candidate_id= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    