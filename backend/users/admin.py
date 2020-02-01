from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ('telnum', 'name', 'rec_code')
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            msg = "password don't match"
            raise forms.ValidationError(msg)
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('telnum', 'password', 'name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('telnum', 'name', 'code', 'is_active', 'is_admin')
    list_filter = ('is_admin', 'is_active')
    readonly_fields = ('rec_code', 'code')
    fieldsets = (
        (None, {'fields': ('telnum', 'password', 'code', 'rec_code')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telnum', 'name', 'rec_code', 'password1', 'password2')}
        ),
    )
    search_fields = ('telnum',)
    ordering = ('name',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)