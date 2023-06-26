from django import forms
from FruitipediaApp.fruitipedia.models import Profile, Fruit


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }
        labels = {
            'first_name': "",
            'last_name': "",
            'email': "",
            'password': ""
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['password']
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'email': "Email",
        }


class ProfileDeleteForm(ProfileEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if self.instance:
            Fruit.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for name, field in self.fields.items():
            field.widget = forms.HiddenInput()


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'})
        }
        labels = {
            'name': "",
            'image_url': "",
            'description': "",
            'nutrition': ""
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': "Name",
            'image_url': "Image URL",
            'description': "Description",
            'nutrition': "Nutrition"
        }


class FruitDeleteForm(FruitEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for name, field in self.fields.items():
            if name == 'nutrition':
                field.widget = forms.HiddenInput()
            field.widget.attrs['readonly'] = 'readonly'
