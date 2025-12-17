from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, Category, Aboutus
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import Submission

blog_title = "Latest Posts"
# Create your views here.
#Static demo data
#posts=[
#       {'id':1,'title':'Post 1','content':'Content of post 1'}, 
 #       {'id':2,'title':'Post 2','content':'Content of post 2'}, 
  #      {'id':3,'title':'Post 3','content':'Content of post 3'}, 
   #     {'id':4,'title':'Post 4','content':'Content of post 4'}, 
   # ]

def index(request):
    all_posts=Post.objects.all()
    #paginate
    paginator=Paginator(all_posts, 5)
    page_number=request.GET.get('page') 
    page_obj=paginator.get_page(page_number)

    return render(request,'blog/index.html',{'blog_title':blog_title, 'page_obj':page_obj})

def detail(request, slug):
    #logger = logging.getLogger("TESTING")
    #Getting static data
    #post = next((item for item in posts if item['id'] == int(post_id)),None)
    #getting data from model by post id
    try:
        post=Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    #logger.debug(f'Post variable is {post}')
    return render(request, 'blog/detail.html', {'post': post, 'related_posts': related_posts})
 

def old_url_redirect(request):
    return redirect(reverse('Blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_view(request):
    logger = logging.getLogger("TESTING")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if form.is_valid():
            # Log submission
            logger.debug(
                f"Post data is "
                f"Name: {form.cleaned_data['name']}, "
                f"Email: {form.cleaned_data['email']}, "
                f"Message: {form.cleaned_data['message']}"
            )

            # Save to database
            Submission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            success_message = 'Your email has been sent!'
            return render(request, 'blog/contact.html', {'form': form, 'success_message': success_message})
        else:
            logger.debug('Form validation failure')
            return render(request, 'blog/contact.html', {'form': form, 'name': name, 'email': email, 'message': message})

    # If GET request
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def about_view(request):
    about_content= Aboutus.objects.first().content
    return render(request, 'blog/about.html',{'about_content':about_content})

