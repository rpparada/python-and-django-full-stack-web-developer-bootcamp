# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView
from blog.models import Post,Comment

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostlistView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post
