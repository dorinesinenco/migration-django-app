# views module
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.shortcuts import redirect
from django.db import connection
from random import randint

from .models import Post

# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout, get_user

from django.contrib import messages
from django.contrib.sessions.models import Session


# AKA DATABASE
users = [
    { "username": "johny", "created":   "2000-01-01" },
    { "username": "marry", "created":   "2000-01-02" },
    { "username": "pete", "created":    "2000-01-03" },
    { "username": "pier", "created":    "2000-01-04" },
    { "username": "vasilyi", "created": "2000-01-05" },
    { "username": "masha", "created":   "2000-01-06" },
    { "username": "lily", "created":    "2000-01-07" },
]


posts = [
    { "title": "First title", "created": "2001-01-01"},
    { "title": "Second title", "created": "2001-01-02"},
    # simple XSS example
    { "title": "Third title <script>alert('You\"ve been hacked!!!')</script>", "created": "2001-01-03"},
    { "title": "Fourth title", "created": "2001-01-04"},
    { "title": "Fifth title", "created": "2001-01-05"},
]


def homePage(request):
    template = loader.get_template("home.html")
    # HW2: sort users by date descending list.sort()
    #      sort posts by date
    show_notifications =  request.session.get('show_notifications', None)
    return HttpResponse( template.render({
       "last_users": users[:5],
       "last_posts": posts[:3],
       "user": request.user,
       "show_notifications" : show_notifications
    }, request))











def signupPage(request):
    template = loader.get_template("signup.html")
  
    return HttpResponse( template.render({
    }, request))










def postsPage(request):
    return HttpResponse("Post's page")






# POST VIEWS
def addPost(request):
    template = loader.get_template("add-post.html")
  
    return HttpResponse( template.render({
    }, request))




def savePost(request): # HttpRequest

    # HW1: check if user is authenticated
    visitingUser = get_user(request) # User
    visitingUser = CustomUser.objects.get(pk=visitingUser.id)

    title = request.POST['title']    
    body  = request.POST['body']    
                           

    post = Post(title=title,body=body, author=visitingUser)
    post.save()
    
    # HW2: redirect to it's profile
    return redirect('/get-posts')













def getPosts(request):
    template = loader.get_template("get-posts.html")
    
    posts = Post.objects.all()

    print(type(Post.objects))  # Manager
    print(type(posts))         # QuerySet

    return HttpResponse( template.render({
        'posts': posts
    }, request))











def updatePost(request):
    template = loader.get_template("update-post.html")
    
    id = request.GET['id']
    
    # 1. find the post by id
    post = Post.objects.get(pk=id)  # Post

    print(type(post))

    return HttpResponse( template.render({
        'post': post
    }, request))
















def changePost(request):

    
    id = request.GET['id']
    new_title = request.GET['title']
    new_body = request.GET['body']
    
    # 1. find the post by id
    post = Post.objects.get(pk=id)  # Post

    post.title = new_title
    post.body = new_body
    
    post.save()

    return HttpResponse('Post updated successfully!')


















def deletePost(request): 

    id = request.GET['id']
    
    # 1. find the post by id
    post = Post.objects.get(pk=id)

    # 2. delete
    post.delete()

    return HttpResponse('Post deleted successfully')






# USER VIEWS
def registerUser(request):
    if request.method == 'GET':
        template = loader.get_template("user/register.html")
        return HttpResponse( template.render({}, request))
    
    elif request.method == 'POST':    
        username = request.POST['username']
        email = request.POST['email']        # regex
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # HW1: 
        #   validate password confirmation
        if password == confirm_password:

            CustomUser.objects.create_user(username, email, password)
            return redirect( '/')
        else:    
            return redirect( '/user/register')
        # redirect
       
    





def f():
    a = 1
    b = 2
    a + b



def loginUser(request):
 
    # req ------> FORM
    if request.method == 'GET':
        f()
        template = loader.get_template("user/login.html")
        # message = request.session.get('error_message', None)
        return HttpResponse( template.render({}, request))
    
    elif request.method == 'POST':    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

    # req -------> AUTH        
        if user is None:
            # request.session['error_message'] = 'Wrong credentials!'
            messages.error(request, 'Wrong credentials!')
            return redirect("/user/login")
        
        login(request, user)
       
        visitingUser = CustomUser.objects.get(pk=user.id)
        
        # 1. load the backup data
        session_data_backup = visitingUser.session_data_backup
        session_data = json.loads(session_data_backup if session_data_backup else '{}')
      
        # 2. put the data in current session
        request.session.update(session_data)
        
      

        messages.success(request, 'Login successful!')
        return redirect("/")








def userProfile(request, id):
    # HW3:
    #   update user profile - so it shows all of it's posts

    # req ------> FORM
    if request.method == 'GET':
        profileUser = CustomUser.objects.get(pk=id)
        show_notifications =  request.session.get('show_notifications', None)
        print(profileUser)
        # print(profileUser.friends.all())
        visitingUser = get_user(request) # User
        visitingUser = CustomUser.objects.get(pk=visitingUser.id)
        # print(visitingUser)
        template = loader.get_template("user/profile.html")
        userFriends = profileUser.friends.all()
        profileUserIsNotVisitingUserFriend = visitingUser.friends.all().contains(profileUser)
        # print(profileUserIsNotVisitingUserFriend)
    
        # message = request.session.get('error_message', None)
        return HttpResponse( template.render({
            'profileUser':profileUser, 
            'visitingUser': visitingUser,
            'userFriends': userFriends,
            'profileUserIsNotVisitingUserFriend': profileUserIsNotVisitingUserFriend,
            "show_notifications" : show_notifications
        }, request))




def addUserFriend(request, id):
 
    # req ------> FORM
    if request.method == 'GET':
        profileUser  = CustomUser.objects.get(pk=id)
        visitingUser = get_user(request) # User
        visitingUser = CustomUser.objects.get(pk=visitingUser.id)
     

        visitingUser.friends.add(profileUser)
        visitingUser.save()



        return redirect(f"/user/profile/{profileUser.id}")
    
    
    
def editUserProfile(request, id):
 
    # req ------> FORM
    if request.method == 'GET':
        profileUser = CustomUser.objects.get(pk=id)
        visitingUser = get_user(request)
        if profileUser.id == visitingUser.id: 
            template = loader.get_template("user/edit-profile.html")
            # message = request.session.get('error_message', None)
            return HttpResponse( template.render({
                'profileUser':profileUser, 
            }, request))
        else:
            return HttpResponseForbidden('Access Denied!')

    elif request.method == 'POST':
        profileUser = CustomUser.objects.get(pk=id)
        visitingUser = get_user(request)
        if profileUser.id == visitingUser.id: 
            avatar = request.FILES['avatar']  # this file is still in MEMORY!!!
            avatar_file = open(f"app/public/uploads/{avatar}","wb+")
            for chunk in avatar.chunks():
                avatar_file.write(chunk)

            avatar_file.close()    
            profileUser.avatar = f"uploads/{avatar}"
            profileUser.save()
            return redirect(f'/user/profile/{profileUser.id}')
        else:
           return HttpResponseForbidden('Access Denied!')
        

    # User <model>
    # + avatar <---- avatar file url 

 

    # # req -------> AUTH        
    #     if user is None:
    #         # request.session['error_message'] = 'Wrong credentials!'
    #         messages.error(request, 'Wrong credentials!')
    #         return redirect("/user/login")
        
    #     login(request, user)
    #     # request.session.pop('error_message')
    #     messages.success(request, 'Login successful!')
    #     return redirect("/")








def toggleUserNotification(request):
    visitingUser = get_user(request)
    toggle = request.GET.get('toggle', None)
    # .POST.get()
    print("TOGGLE", not toggle)
    if not toggle:
        request.session['show_notifications'] = False 
    else:  
        request.session['show_notifications'] = True   
    
    return redirect(f"/user/profile/{visitingUser.id}")




import json

def logoutUser(request):
    # show_notifications = request.session.get('show_notifications',None)
    visitingUser = get_user(request)
    visitingUser = CustomUser.objects.get(pk=visitingUser.id)
    
    # 1. get all the current session data
    session = Session.objects.get(pk=request.session.session_key)
    session_data = session.get_decoded()

    # 2. serialize data in json
    session_data_json = json.dumps(session_data)

    # 3. save to backup column in visiting user
    visitingUser.session_data_backup = session_data_json
    visitingUser.save()

    logout(request) 
    
    return redirect("/")
  
    
   