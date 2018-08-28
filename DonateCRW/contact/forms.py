from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Name", required= True, widget = forms.TextInput(
        attrs = {"class":"form-control", "placeholder":"Write you name"}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label = "Email", required= True, widget = forms.EmailInput(
        attrs = {"class":"form-control", "placeholder":"Write you email"}
    ), min_length=3, max_length=100)
    content = forms.CharField(label = "Content", required= True, widget = forms.Textarea(
        attrs = {"class":"form-control", "rows":4, "placeholder":"Write the message"}
    ))