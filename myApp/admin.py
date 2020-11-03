from django.contrib import admin
from myApp.models import Post


class PostAdmin(admin.ModelAdmin):
    fields = [
        'title', 'author', 'post', 'post_type', 'created_date', 'modified_date', 'completion_status'
    ]

    list_display = [
        'title', 'author', 'post_type', 'created_date', 'modified_date', 'completion_status'
    ]

    search_fields = [
        'title', 'author__email'
    ]

    list_filter = [
        'title', 'created_date'
    ]

    readonly_fields = [
        'created_date', 'modified_date', 'completion_status',
    ]


admin.site.register(Post, PostAdmin)
