from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models import EmailUser
from django.contrib.auth.forms import AuthenticationForm

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = EmailUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    #password = ReadOnlyPasswordHashField()

    class Meta:
        model = EmailUser
        fields = ['email', 'password', 'date_of_birth', 'is_active', 'is_staff', 'is_superuser']

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(UserChangeForm, self).save(commit=False)
        m.set_password(self.cleaned_data["password"])
        if commit:
            m.save()
        return m

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.cleaned_data["password"]


class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super(LoginForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'span12'
    self.fields['username'].widget.attrs['placeholder'] = 'E-mail'
    self.fields['password'].widget.attrs['class'] = 'span12'
    self.fields['password'].widget.attrs['placeholder'] = 'Password'


class SignUpForm(UserCreationForm):

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['email'].widget.attrs['class'] = 'span12'
    self.fields['email'].widget.attrs['placeholder'] = 'E-mail address'
    self.fields['password1'].widget.attrs['class'] = 'span12'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password2'].widget.attrs['class'] = 'span12'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
