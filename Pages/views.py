from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review_post
from .models import Game


def reviewlist(request):
    review_list = Review_post.objects.filter(status=1).order_by('-created_on')
    context = {'review_list': review_list}
    paginate_by = 6
    return render(request, 'index.html', context)
