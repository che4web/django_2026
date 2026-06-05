from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, StudentProfile, TeacherProfile


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "email", "password"),
            },
        ),
    )

@admin.register(StudentProfile)
class StudetProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user_full_name","expertise")
    ordering = ("-created_at",)

    @admin.display(description="ФИО")
    def user_full_name(self, obj):
        return obj.user.get_full_name()
