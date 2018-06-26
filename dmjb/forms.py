from django import forms
from dmjb.models import Job


class JobForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label="Job title")
    url = forms.URLField(label="Job's URL")
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}),
                                  max_length=256,
                                  label="Job description",
                                  )
    company_name = forms.CharField(max_length=128, label="Company name")
    contact_email = forms.EmailField(label="Contact email")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Job
        fields = ('title', 'url', 'description', 'company_name', 'contact_email')


# class RegistrationForm(forms.registration):
#
#
#
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#
#         try:
#             user = User.objects.get(username=username)
#         except user.DoesNotExist:
#             return username
#         raise forms.ValidationError