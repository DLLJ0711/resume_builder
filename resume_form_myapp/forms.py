from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'.transparentField'}))
    job_title = forms.CharField(label = 'Job Title')
    email = forms.EmailField(label = 'E-Mail')
    website = forms.URLField()
    phone = forms.CharField()
    personal_profile = forms.CharField(label = 'Personal Profile', widget = forms.Textarea)
    category = forms.ChoiceField(choices= [('questions', 'Questions'), ('other', 'Other')])
    position_at_company = forms.CharField(label = 'Job Title at Company')
    work_experience = forms.CharField(label= 'Work Experience', widget= forms.Textarea)
    start_end = forms.CharField(label= 'Start to End Date')
    skills = forms.CharField(label= 'Key Skills')
    education = forms.CharField(label= 'Education', widget= forms.Textarea)