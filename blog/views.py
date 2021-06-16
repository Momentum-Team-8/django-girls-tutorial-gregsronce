from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

'''  This is where the action happens. 
Views recieve requests and generate responses. 
They can be class-based or function-based. 
Views can process forms, query the database, or simply render HTML responses. 
Views can also generate JSON responses for API endpoints. 
Views are called by a user or part of the Django app itself visiting the url connected to that view in urls.py.'''

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
