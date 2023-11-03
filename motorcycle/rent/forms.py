from django import forms

from motorcycle.accessory.models import Accessory
from motorcycle.motor.models import Motorcycle
from motorcycle.rent.models import Rental, ContactUs
from motorcycle.tour.models import Tour


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email',
            'message',
        ]

        widgets={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                    'placeholder': 'Message...',
                    'style': 'color: gray',
                }
            )
        }


class MotorcycleRentForm(forms.ModelForm):
    motorcycle = forms.ModelChoiceField(
        queryset=Motorcycle.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    tour = forms.ModelChoiceField(
        queryset=Tour.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    accessory = forms.ModelMultipleChoiceField(
        queryset=Accessory.objects.all(),
        required=False,  # Allow no selection
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Rental
        fields = ('motorcycle',
                  'tour',
                  'pickup_location',
                  'dropoff_location',
                  'pickup_date',
                  'dropoff_date',
                  'name',
                  'email',
                  'phone_number',
                  'message'
                  )

        widgets = {
            'pickup_location': forms.Select(
                choices=[
                    ('option-1', 'Option 1'),
                    ('option-2', 'Option 2'),
                    ('option-3', 'Option 3'),
                ],
                attrs={
                    'class': 'form-control',
                }
            ),

            'dropoff_location': forms.Select(
                choices=[
                    ('option-1', 'Option 1'),
                    ('option-2', 'Option 2'),
                    ('option-3', 'Option 3'),
                ],
                attrs={
                    'class': 'form-control',
                }
            ),

            'pickup_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),

            'dropoff_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'John Doe',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'john.doe@company.com',
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '+359 888 111 333',
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 10,
                    'placeholder': 'Message...',
                    'style': 'color: gray',
                }
            )
        }
