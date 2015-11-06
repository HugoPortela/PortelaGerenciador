from django.contrib import admin

from .models import UserProfile, ProdutoProfiles
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

class ProdutoProfilesAdmin(admin.ModelAdmin):
    list_display = ('nome','referencia','quantidade','categoria','preco')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProdutoProfiles, ProdutoProfilesAdmin)
