from django.contrib import admin
from .models import Cv, DetailCv, DetailSection, Section
# Register your models here.

# class CvAdmin(admin.ModelAdmin):
#     fieldsets = [
#         "user", "file"
#     ]
# class DetailCvAdmin(admin.ModelAdmin):
#     fieldsets = [
#         "cv", "detail_section", "konten"
#     ]   
    
# class SectionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         "nama","deskripsi", "active"
#     ]

# class DetailSectionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         "section", "nama", "deskripsi"
#     ]





admin.site.register(Cv)
admin.site.register(DetailCv)
admin.site.register(Section)
admin.site.register(DetailSection)
