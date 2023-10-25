from django.contrib import admin

from learning_log.models import Candidate, Candidate_account,Candidate_certification,Candidate_exp
from learning_log.models import Candidate_edu, Candidate_reference, job, Candidate_application,Candidate_Docs

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Candidate_account)
admin.site.register(Candidate_certification)
admin.site.register(Candidate_exp)
admin.site.register(Candidate_edu)
admin.site.register(Candidate_reference)
admin.site.register(job)
admin.site.register(Candidate_application)
admin.site.register(Candidate_Docs)