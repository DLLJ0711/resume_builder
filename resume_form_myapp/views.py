from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientForm


# Create your views here.
def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
        
        # name = forms.CharField()
        # email = forms.EmailField(label = 'E-Mail')
        # job_title = forms.CharField(lable = 'Job Title')
        # website = forms.URLField()
        # phone = forms.NumberInput()
        # category = forms.ChoiceField(choices= [('questions', 'Questions'), ('other', 'Other')])
        # work_experience = forms.CharField(required=False)
        # personal_profile = forms.CharField(widget = forms.Textarea)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            job_title = form.cleaned_data['job_title']
            website = form.cleaned_data['website']
            phone = form.cleaned_data['phone']
            category = form.cleaned_data['category']
            personal_profile = form.cleaned_data['personal_profile']
            work_experience = form.cleaned_data['work_experience']
            position_at_company = form.cleaned_data['position_at_company']
            start_end = form.cleaned_data['start_end']
            skills = form.cleaned_data['skills']
            education = form.cleaned_data['skills']
            request.session['name']= form.cleaned_data['name']
            request.session['email']= form.cleaned_data['email']
            request.session['job_title']= form.cleaned_data['job_title']
            request.session['website']= form.cleaned_data['website']
            request.session['phone']= form.cleaned_data['phone']
            request.session['category']= form.cleaned_data['category']
            request.session['personal_profile']= form.cleaned_data['personal_profile']
            request.session['work_experience']= form.cleaned_data['work_experience']
            request.session['position_at_company']= form.cleaned_data['position_at_company']
            request.session['start_end']= form.cleaned_data['start_end']
            request.session['skills']= form.cleaned_data['skills']
            request.session['education']= form.cleaned_data['education']

            print(name, email, job_title, website, phone, category, work_experience, personal_profile, position_at_company, start_end, skills, education)
            return redirect('/resume')
    else:
        form = ClientForm()
    return render(request, 'form.html', {'form': form})
    

    #This is the index.html code for the resume_template

def index(request):
    return render(request, 'index.html', {'index': index, 'name': request.session.get('name'), 'email': request.session.get('email')
    , 'job_title': request.session.get('job_title'), 'website': request.session.get('website'), 'phone': request.session.get('phone'), 'category': request.session.get('category')
    , 'work_experience': request.session.get('work_experience'), 'personal_profile': request.session.get('personal_profile'), 'position_at_company': request.session.get('position_at_company')
    , 'start_end': request.session.get('start_end'), 'skills': request.session.get('skills'), 'education': request.session.get('education')})