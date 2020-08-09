from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Profile, Work, Tag, Recommendation, Article, SocialNetwork, Skill, Category

admin.site.site_header = "My skill site"
admin.site.site_title = "My skill site"
admin.site.index_title = "Административная панель"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
    prepopulated_fields = {'url': ('name',)}


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label="Текст", widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = "__all__"


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    extra = 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SocialNetworkInline, SkillInline]
    save_on_top = True

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)

    def has_module_permission(self, request):
        return False


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    inlines = [RecommendationInline]
    list_display = ("title", "publish", "get_image", "draft")
    list_display_links = ("title",)
    prepopulated_fields = {"url": ("title",)}
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_image", "draft")
    list_display_links = ("title",)
    form = ArticleAdminForm
    prepopulated_fields = {"url": ("title",)}
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

    get_image.short_description = "Изображение"