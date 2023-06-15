from django import forms


class MusicForm(forms.Form):
    file = forms.FileField()
    upload_file_as = forms.ChoiceField(choices=[("private","Private"),("public","Public"),("protected","Protected")])
    share_with_emails = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'eg. abc1@gmail.com,abc2@gmail'}))
    