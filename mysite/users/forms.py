from django import forms
from .models import *


class SignInForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                "placeholder": "name@company.com",
                "required": "required",
            }
        ),
    )
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                "placeholder": "••••••••",
                "required": "required",
            }
        ),
    )
    remember = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "aria-describedby": "remember",
                "class": "w-4 h-4 cursor-pointer border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600",
            }
        ),
    )


class AddUserForm(forms.ModelForm):
    class Meta:
        model = BackendUser
        fields = "__all__"
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                    "placeholder": "example@company.com",
                    "required": "required",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                    "placeholder": "Bonnie",
                    "required": "required",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                    "placeholder": "Green",
                    "required": "required",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                }
            ),
            "date_of_birth": forms.DateTimeInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                    "placeholder": "Select date",
                    "datepicker": "datepicker",
                    "format": "yyyy-mm-dd",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",
                    "rows": "4",
                    "placeholder": "Bonnie",
                }
            ),
        }
