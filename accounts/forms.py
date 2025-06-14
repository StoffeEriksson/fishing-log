from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False  # Gör fältet valfritt

    def save(self, request):
        user = super().save(request)
        user.email = ""  # Se till att det finns något värde (kan vara tom sträng)
        user.save()
        return user