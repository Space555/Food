from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, DeleteView
from app_recipes.models import Category, Dishes, Comments
from app_recipes.forms import DishesForm, StepsForm, CommentForm
from app_users.models import Profile


class Index(TemplateView):
    template_name = 'food_tube/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context


class CategoryList(ListView):
    model = Category
    template_name = 'food_tube/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = Category.objects.all()
        title = self.request.GET.get('title')
        if title:
            queryset = Category.objects.filter(title__icontains=title)
        return queryset


class DishesByCategory(ListView):
    model = Dishes
    template_name = 'food_tube/category_list.html'
    context_object_name = 'dishes_c'
    paginate_by = 10

    def get_queryset(self):
        return Dishes.objects.filter(cat_id_id=self.kwargs['pk'])


class DishesList(ListView):
    model = Dishes
    template_name = 'food_tube/dishes_all.html'
    context_object_name = 'dishes'
    paginate_by = 10

    def get_queryset(self):
        queryset = Dishes.objects.all()
        title = self.request.GET.get('title')
        if title:
            queryset = Dishes.objects.filter(title__icontains=title)
        return queryset


class DishesDetail(DetailView):
    model = Dishes
    template_name = 'food_tube/dish_detail.html'
    context_object_name = 'dishes_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.get_object()
        related_video = Dishes.objects.filter(cat_id=dish.cat_id).exclude(id=dish.id)
        context['related_video'] = related_video
        context['user_likes'] = dish.like.filter(pk=self.request.user.pk).exists()
        context['comments'] = Comments.objects.prefetch_related('user').filter(
            dish_id=self.get_object()).order_by('-created')
        return context

    def post(self, request, **kwargs):
        dish_id = self.get_object()
        com_form = CommentForm(request.POST)
        if 'like' in request.POST:
            if dish_id.like.filter(pk=request.user.pk).exists():
                dish_id.like.remove(request.user)
                # like_cnt = dish_id.like.count()
                # return HttpResponse(like_cnt)
            else:
                dish_id.like.add(request.user)
                # like_cnt = dish_id.like.count()
                # return HttpResponse(like_cnt)

        if 'comment_text' in request.POST:
            text = request.POST['comment_text']
            Comments.objects.create(dish_id=dish_id, author=request.user, comment=text)

        return redirect('detail_i', pk=dish_id.id)


class RecipesAdd(CreateView):
    model = Dishes
    form_class = DishesForm
    template_name = 'food_tube/recipes_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        profile = Profile.objects.get(user=self.request.user)
        profile.dish_count += 1
        profile.save()
        return super().form_valid(form)

    # def form_valid(self, form):
        # context = self.get_context_data()
        # step_formset = context['step']
        # if step_formset.is_valid():
            # self.object = form.save()
            # step_instance = step_formset.save(commit=False)
            # step_instance.dish = self.object
            # step_instance.save()
            # return super().form_valid(form)
        # else:
            # return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class DishDel(DeleteView):
    model = Dishes
    template_name = 'food_tube/recipes_del.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        profile = Profile.objects.get(user=self.request.user)
        profile.dish_count -= 1
        profile.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        project = self.get_object()
        profile_id = self.request.user.id
        return reverse_lazy('profile', kwargs={'pk': profile_id})

