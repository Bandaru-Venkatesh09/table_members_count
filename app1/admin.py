from django.contrib import admin


from app1.models import HOD,Facality

class hod_admin(admin.ModelAdmin):
    list_display=['Name','Pin','PH']
admin.site.register(HOD,hod_admin)

class facality_admin(admin.ModelAdmin):
    list_display=['Name','Pin','PH']
admin.site.register(Facality,facality_admin)
