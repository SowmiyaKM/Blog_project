from django.contrib import admin
from .models import Post, Category, Aboutus, Submission  # Add Submission

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')

# Admin for Submission model
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # Columns to show
    search_fields = ('name', 'email', 'message')      # Searchable fields
    list_filter = ('submitted_at',)                   # Filter by date

# Register models
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Aboutus)
admin.site.register(Submission, SubmissionAdmin)  # Register Submission



