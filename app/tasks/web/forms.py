from django import forms

from ..models import Task


class TaskForm(forms.ModelForm):
    """
    Form for Task model
    """

    class Meta:
        model = Task
        fields = ["title", "description", "email", "due_date"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
