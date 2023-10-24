from django.shortcuts import render
from django.http import HttpResponse
import supabase
# Create your views here.
def home(request):
    return render(request, "signup.html")

def confirm(request):
    # Supabase project URL and API Key
    supabase_URL = "https://iuyewcdcpqxnbvkjyhtj.supabase.co"
    supabase_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1eWV3Y2RjcHF4bmJ2a2p5aHRqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NjM0NTQ0MywiZXhwIjoyMDExOTIxNDQzfQ._oSgCQ2StUA_dFu2_TIUb7ro_PC92SLN_4685SAgkUU"
    # Creating client for Supabase
    supabase_client = supabase.Client(supabase_URL,supabase_KEY)
    first = request.GET["first_name"]
    last = request.GET["last_name"]
    email = request.GET["email"]
    password = request.GET["password"]
   ## confirmation_token = request.GET.get('token')
    print(first+" ,"+last+" ,"+email+" ,"+password)
    res = supabase_client.auth.sign_up({"email": email,"password": password})
    print(res)
    return render(request, "signedup_confirm.html")