from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.db.models.base import ObjectDoesNotExist
from delaapp.forms import NewCommentForm, NewImageForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from delaapp.models import Comment, Image, Profile
# Create your views here.

@login_required(login_url='/accounts/login/')
def landing(request):
  explore = Image.objects.all()
  current_user = request.user.profile
  following = current_user.followers.all()
  the_feed = None
  for item in following:
      feed = Image.objects.filter(owner = item).all()
      the_feed = feed
  print ('feed', the_feed)
  return render(request, 'index.html', {"feed": the_feed,"explore": explore})
@login_required(login_url='/accounts/login/')  
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
@login_required(login_url='/accounts/login/')
def comment(request, id):
    current_user = request.user.profile
    current_image = Image.objects.get(id=id)
    image_id = id
    if request.method == "POST":
       form = NewCommentForm(request.POST)
       if form.is_valid():
        comm = form.save(commit=False)
        comm.owner = current_user
        comm.postde = current_image        
        comm.save()
        return redirect('landing')      
    else:
        form = NewCommentForm()
    try:    
        the_comments  = Comment.objects.filter(postde = id)
    except Comment.DoesNotExist:
        the_comments = None    
    return render(request, 'comment.html', {"form": form, "comments": the_comments, "image_id": image_id})      

@login_required(login_url='/accounts/login/')
def you (request):
    current_user = request.user.profile
    profile_pic = request.user.profile.picture
    print("profile", profile_pic )
    if profile_pic == "SOME STRING":
        print("profile", profile_pic )
        profile_pic= "https://thumbs.dreamstime.com/b/print-216776620.jpg" 
    elif profile_pic == "profile.jpg":
        print("profile", profile_pic )
        profile_pic= "https://thumbs.dreamstime.com/b/print-216776620.jpg"          
    else:
        profile_pic = None      
    print("profile", profile_pic)    
    pics  =   Image.objects.filter(owner = current_user).all()
    return render(request, 'you.html', {"pics": pics, "profile_pic": profile_pic})   
      

def profile(request, id):
    user = User.objects.get(id=id)
    profile_pic = user.profile.picture    
    if profile_pic == "SOME STRING":
        print("profile", profile_pic )
        profile_pic= "https://thumbs.dreamstime.com/b/print-216776620.jpg" 
    elif profile_pic == "profile.jpg":
        print("profile", profile_pic )
        profile_pic= "https://thumbs.dreamstime.com/b/print-216776620.jpg"          
    else:
        profile_pic = None      
    print("here", profile_pic, id)      
    pics = Image.objects.filter(owner = user.profile).all()
    print(pics)
    return render(request, 'profile.html', {"pics": pics, "user":user,"profile_pic": profile_pic})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_imgs = Image.img_searcher(search_term)
        title = f"For {search_term}"

        return render(request, 'search.html', {"title":title, "imgs":searched_imgs})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')        
def like(request, post_id):
    current_user = request.user
    img = Image.objects.get(id=post_id)
    if img.likes.filter(id = current_user.id).exists():
       img.likes.remove(current_user)   
    else:
       img.likes.add(current_user)
    return redirect('landing')            

@login_required(login_url='/accounts/login/')      
def followToggle(request, name):
    userObj = User.objects.get(username=name)
    profileObj = userObj.profile
    current_user = User.objects.get(username=request.user.username)
    currentObj = current_user.profile
    following = profileObj.following.all()

    if name != current_user.username:
        if currentObj in following:
            profileObj.following.remove(currentObj.id)
        else:
            profileObj.following.add(currentObj.id)
    return redirect('landing')         

@login_required(login_url='/accounts/login/')
def bio(request):
    if 'bio' in request.GET and request.GET["bio"]:
        current_profile = request.user.profile
        bio_new = request.GET.get("bio")
        current_profile.bio_updater(bio_new)

        return redirect('you')
    else:
        message = "You haven't changed anything"
        return redirect('you')      

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_profile = request.user.profile
    current_user = request.user
    if request.method == "POST":
      form = UpdateProfileForm(request.POST, request.FILES,instance=request.user.profile)
      if form.is_valid():
        # prof = form.save(commit=False)
        # prof.user = current_user
        # prof.bio = current_profile.bio  
#         prof.following = current_profile.following  
#         prof.save()       
        image = form.cleaned_data['picture']
        current_profile.picture = image
        current_profile.save()
        print("image", image)
        return redirect('you')
    else:
        form = UpdateProfileForm()
    return render(request, 'update_prof.html', {"form": form})    