from django.contrib import admin
from .models import User, StudentProfile, TeacherProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

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
