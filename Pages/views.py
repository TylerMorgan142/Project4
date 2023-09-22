from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review_post


# class ReviewList(generic.ListView):
#     model = Review_post
#     queryset = Review_post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#     paginate_by = 6

def reviewlist(request):
    review_list = Review_post.objects.filter(status=1).order_by('-created_on')
    context = {'review_list': review_list}
    return render(request, 'index.html', context)