from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import re
from django import forms
# from tinymce import TinyMCE


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


class Portfolio(models.Model):

    class EducationList(models.Model):
        universities = [
            ("UC", "University of Canberra")
        ]
        name = models.CharField(max_length=200, default=1)
        institution = models.CharField(
            max_length=10, choices=universities, default="UC")
        date_from = models.CharField(max_length=50, default=1)
        date_to = models.CharField(max_length=50, default=1)

    class JobList(models.Model):
        name = models.CharField(max_length=200, default=1)
        company = models.CharField(max_length=200, default=1)
        description = models.TextField(max_length=1000, blank=True)
        date_from = models.CharField(max_length=50, default=1)
        date_to = models.CharField(max_length=50, default=1)


class AchievementTags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "AchievementTags"

    def __str__(self):
        return self.name


class AchievementList(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(
        AchievementTags, related_name="AchievementTags")
    upload = models.ImageField(blank=True,
                               null=True, upload_to='frontend/static/frontend/img/uploads/')
    slug = models.SlugField(null=True, blank=True)

    def save(self, **kwargs):
        slug_str = "%s" % (self.name)
        unique_slugify(self, slug_str)
        super(ProjectList, self).save(**kwargs)

    def __str__(self):
        return self.name


class ProjectTags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "ProjectTags"

    def __str__(self):
        return self.name


class ProjectList(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(ProjectTags, related_name="Project_List")
    upload = models.ImageField(blank=True,
                               null=True, upload_to='frontend/static/frontend/img/uploads/')
    slug = models.SlugField(null=True, blank=True)
    # content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

    def __str__(self):
        return f"{self.name}, {self.tag}"

    def save(self, **kwargs):
        slug_str = "%s" % (self.name)
        unique_slugify(self, slug_str)
        super(ProjectList, self).save(**kwargs)


class BlogTags(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "BlogTags"

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(BlogTags, related_name="Project_List")
    upload = models.ImageField(blank=True,
                               null=True, upload_to='frontend/static/frontend/img/uploads/')
    slug = models.SlugField(null=True, blank=True)
    # content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

    def __str__(self):
        return f"{self.name}"

    def save(self, **kwargs):
        slug_str = "%s" % (self.name)
        unique_slugify(self, slug_str)
        super(Blog, self).save(**kwargs)
