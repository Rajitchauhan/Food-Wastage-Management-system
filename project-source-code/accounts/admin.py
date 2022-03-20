from django.contrib import admin

# Register your models here.

from .models import Donate_Food

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'amount', 'Address', 'Donate_time' , 'status' , 'message')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'Info'



admin.site.register(Donate_Food , UserProfileAdmin
)
#admin.site.site_header = "Admin"
