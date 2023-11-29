from django import forms


class fonttimes(forms.Form):
    n = forms.IntegerField()
    term = forms.CharField(required=True)


class teen_sum(forms.Form):
    X = forms.IntegerField(required=True)
    Y = forms.IntegerField(required=True)
    Z = forms.IntegerField(required=True)


class xyz(forms.Form):
    term = forms.CharField(required=True)


class centeredsavage(forms.Form):
    X = forms.IntegerField(required=True)
    Y = forms.IntegerField(required=True)
    Z = forms.IntegerField(required=True)
