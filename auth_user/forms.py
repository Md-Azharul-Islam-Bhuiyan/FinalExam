from django import forms
from django.contrib.auth.models import User
from .models import ShopUserAccount, UserAddress
from .constants import GENDER_TYPE
from django.contrib.auth.forms import UserCreationForm




class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    profile_picture = forms.ImageField()
    phone_no = forms.CharField(max_length=11)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'phone_no', 'email', 'gender', 'profile_picture','street_address', 'city', 'postal_code', 'country']

    def save(self, commit=True):
        user = super().save(commit=False) # ami database a data save korbo na ekhn
        if commit == True:
            user.save()
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            profile_picture = self.cleaned_data.get('profile_picture')
            phone_no = self.cleaned_data.get('phone_no')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')

            UserAddress.objects.create(
                user = user,
                postal_code = postal_code,
                city = city,
                country = country,
                street_address = street_address
            )

            ShopUserAccount.objects.create(
                user = user,
                birth_date = birth_date,
                gender = gender,
                profile_picture = profile_picture,
                phone_no = phone_no,
                account_no = 10000+user.id
            )
        return user
    
class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    profile_picture = forms.ImageField()
    phone_no = forms.CharField(max_length=11)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except ShopUserAccount.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                
                self.fields['phone_no'].initial = user_account.phone_no
                self.fields['profile_picture'].initial = user_account.profile_picture
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = ShopUserAccount.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_address, created = UserAddress.objects.get_or_create(user=user) 

            user_account.phone_no = self.cleaned_data['phone_no']
            user_account.profile_picture = self.cleaned_data['profile_picture']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user
   

       



