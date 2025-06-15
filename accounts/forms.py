from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False  

    def save(self, request):
        user = super().save(request)
        user.email = ""  
        user.save()
        return user