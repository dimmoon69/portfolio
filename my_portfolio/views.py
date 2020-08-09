from django.views.generic import ListView, DetailView

from .models import Profile, Work, Recommendation, Article, Category


class DetailProfileView(ListView):
    """Детальное отображение профиля"""
    model = Profile
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(DetailProfileView, self).get_context_data()
        context["testimonials_list"] = Recommendation.objects.all().order_by("sequence")
        context["article_list"] = Article.objects.filter(draft=True)[:3]
        context["work_list"] = Work.objects.filter(draft=True)
        # context["category_list"] = Category.objects.all()
        return context


class DetailArticlesView(DetailView):
    """Детальное отображение статьи"""
    model = Article
    slug_field = "url"
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super(DetailArticlesView, self).get_context_data()
        # context["article_list"] = Article.objects.filter(draft=True)
        context["profile_list"] = Profile.objects.all()
        context["categories"] = Category.objects.all()
        return context