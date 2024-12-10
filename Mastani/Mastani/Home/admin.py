from django.contrib import admin
from .models import literasi

# Register your models here.

class literasi_admin (admin.ModelAdmin):
    list_display = ('title','deskripsi','author','created_date','link_literasi','img')

    def img_preview(self, obj):
        if obj.img:
            return f'<img src="{obj.gambar.url}" style="max-width: 100px;"/>'
        return "tidak ada gambar"
    
    img_preview.allow_tags = True
    img_preview.short_description = "Preview gambar"

admin.site.register(literasi,literasi_admin)