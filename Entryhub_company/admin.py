from django.contrib import admin
from Entryhub_company.models import company, company_contact, company_stats

# Register your models here.
admin.site.register(company)
admin.site.register(company_contact)
admin.site.register(company_stats)
