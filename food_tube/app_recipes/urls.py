from django.urls import path
from app_recipes.views import Index, DishesByCategory, DishesList, DishesDetail, CategoryList, RecipesAdd


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('categories', CategoryList.as_view(), name='categories'),
    path('category/<int:pk>/', DishesByCategory.as_view(), name='dishes_cats'),
    path('dishes/', DishesList.as_view(), name='dishes'),
    path('dishes_info/<int:pk>/', DishesDetail.as_view(), name='detail_i'),
    path('add_dish/', RecipesAdd.as_view(), name='add_dish'),
]
