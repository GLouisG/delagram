from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.db.models.base import ObjectDoesNotExist
from delaapp.forms import NewCommentForm, NewImageForm
from django.contrib.auth.models import User

from delaapp.models import Comment, Image
# Create your views here.
def landing(request):
  explore = Image.objects.all()
  current_user = request.user.profile
  feed = Image.objects.get(owner = current_user.following).all()
  return render(request, 'index.html', {"feed": feed,"explore": explore})
def new_post(request):
    current_user = request.user.profile
    if request.method == "POST":
      form = NewImageForm(request.POST, request.FILES)
      if form.is_valid():
        post = form.save(commit=False)
        post.owner = current_user
        post.save()
        return redirect('landing')
    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})

def comment(request, id):
    current_user = request.user
    current_image = Image.objects.filter(id=id)
    form = NewCommentForm(request.POST)
    if form.is_valid():
      comm = form.save(commit=False)
      comm.owner = current_user
      comm.postde = current_image        
      comm.save()
      return redirect('comment')      
    else:
        form = NewCommentForm()
    the_comments  = Comment.objects.get(postde = id)
    return render(request, 'comment.html', {"form": form, "comments": the_comments})      

def you (request):
    current_user = request.user
    pics  =   Image.objects.get(owner = current_user).all()
    return render(request, 'you.html', {"pics": pics,})     

def profile(request, id):
    user = User.objects.get(id=id)
    pics = Image.objects.get(owner = id).all()
    return render(request, 'profile.html', {"pics": pics, "user":user})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_imgs = Image.img_searcher(search_term)
        title = f"For {search_term}"

        return render(request, 'search.html', {"title":title, "imgs":searched_imgs})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def like(request, post_id):
    current_user = request.user
    img = Image.objects.get(id=post_id)
    if img.likes.filter(id = current_user.id).exists():
       img.likes.remove(current_user)   
    else:
       img.likes.add(current_user)
    return redirect('landing')              

      