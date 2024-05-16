from django.contrib import admin
from app_recipes.models import Category, Dishes, StepDishes, Comments


class StepAdmin(admin.StackedInline):
    model = StepDishes
    extra = 3


class CommentAdmin(admin.StackedInline):
    model = Comments
    extra = 0


class DishesAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'like_count', 'user'
    list_display_links = 'id', 'title'
    search_fields = 'id', 'title'
    inlines = [StepAdmin, CommentAdmin]


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    list_display_links = 'id', 'title'
    search_fields = 'id', 'title'


admin.site.register(Dishes, DishesAdmin)
admin.site.register(Category, CategoryAdmin)
