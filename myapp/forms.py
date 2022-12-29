from .models import Resume
from django import forms

GENDER_OPTIONS = [
            ('Male', 'Male'),
            ('Female', 'Female'),
        ]

CITY_OPTIONS = [
    ('New York', 'New York'),
    ('New Jersey', 'New Jersey'),
    ('San Francisco', 'San Francisco'),
    ('Atlanta', 'Atlanta'),
    ('Boston', 'Boston'),
    ('Houston', 'Houston'),
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_OPTIONS, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job City', choices=CITY_OPTIONS,
                                         widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Resume
        fields = '__all__'

        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'mobile_num': 'Mobile Number',
            # 'job_city': 'Preferred Job City',
            'email': 'Email ID',
            'profile_image': 'Profile Image',
            'my_file': 'Document/PDF',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # 'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'gender': forms.RadioSelect(choices=gender_options),
            # 'job_city': forms.CheckboxSelectMultiple(choices=city_options),
}
