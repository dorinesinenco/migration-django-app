









## Pyhon / Django / mini social 

  
  +------------- App -------------------+  
  |                                     |
  |         import                      |
  |         custom                      |
  |         override                    |
  |                                     |
  +------------- App -------------------+  
                  ^
                  |
  +------------- FRAMEWORK -------------+
  |                                     |
  |        tools                        | tools: django-admin, manage.py
  |        functions/classes/methods    |
  |        configurations               |
  |        tests                        |
  |        magic                        |
  |                                     |
  +-------------------------------------+









## Patterns / arch : 

   web projects: MVC / [MVT]




              +--- router ---+                   <VIEW>
 --- req ---> |              |            
              |    ""  ------------------> homePage (request)
              |              |                |
              +--------------+                |                      <TEMPLATE>
                                              v                        
                                             loader.get_template(...) ------> 
                                                                            home.html ... {{q}}
                                                          template    <------
                                                             |
                                                           .render(context, request)
                                                             |        ^
                                                             v        |
                                        return HttpResponse(...)     dict  { 'q': ... }
                                              |                       |
                                              |                        
                                              |
<--- res -------------------------------------+  













## Python / Django / mini social / Templating




                                                    render
                                                    /
                                                   /
                       +--------------- TEMPLATE ----------------+
                       |                                         |
                       |                                         |
                       |     {{ variable }}                      |
RESPONSE <--- string < |     {% tag %}{% endtag %}               | <---- view load template < VIEW
                       |     {{ value|filter }}                  |        
                       |                                         |
                       |         ^                               |
                       +---------|-------------------------------+
                                 |
                                 |
                                 |
                             evaluated     

                                      














## HW4: creat the sign in page
##      draw the inheritance diagram with blocks

+----------- parent template ---------+
|                                     |----------------------+
|      ...                            |                      |
|      ...                            |                      v
|                                     |      +--------- child template ----------+
|   {% block A %}                     |      |  {% extends 'parent template'% }  |
|      ...                            |      |                                   |
|      ...                            |      |                                   |
|      ...                            |    / |  {% block B %}                    |
|      ...                 +--------------<  |     ...                           |
|   {% endblock %}         |          |    \ |  {% endblock %}                   |
|                          |          |      +-----------------------------------+
|      ...                 |          |
|                          |          |
|   {% block B %}          |          |
|      ...         <-------+          |
|   {% endblock %}                    |
|                                     |
|      ...                            |
|      ...                            |
|                                     |
+-------------------------------------+


















------ settings --------------------------------+
  INSTALLED_APPS ---> which modules to turn on  |
------------------------------------------------+  














## Python / Django / mini social / MODEL (database, migrations)
```

        +------- CustomModelClass -----+
        |                              |  
        |        ...                   | <---------------- migration (sync) ---------- DDL --------------+
        |                              |                                                                 |
        +------------------------------+                                                                 | 
                      |                                                                                  | 
                      |                                                                                  |
+~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~ Django ORM ~~~~~~~~~~~~~~~~~~~~~~+                                       |
|                     v                                          |                                       |
|       +---------- Model ------------+                          |                                       v 
|       |                             |                          .                            +------- database -------+
|       |        model logic          | <----------> [ db engine / driver ] <------------->   |                        |
|       .                             .                                                       .                        . 
.                   DML                                   ^
                                                          | 
                                                        settings 









```














## Python / Django / mini social / MODEL (database, migrations)
  > developing Post CRUD






























                           [routes/urls]         [VIEWS]          [TEMPLATE] +----- extends 'layout.html'
                                                                             V
                      req > 'add-post' ------->  addPost ------>   'add-post.html'
                                                      |             
                                                      |             
                                                      |             
                                                      |             
                                                      |             
                      res < ---------------- render --+
                       |
                       v
                      HTML DOCUMENT
                       |
                       v
                     <form>                   <------- USER data
                       + action="/save-post"     |
                       + name="title"            |
                       + name="body"             |
                                                 |
                        BUTTON (save) <----------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                       BROWSER 
                           v                                                                     data  
                          form data -----> req        [routes/urls]                  [VIEWS]      V     
                                            |              /save-post  --------->    savePost (request)
                                            |                                                     .GET
                                            |                                                   QueryDict {"title":['title1'], ...}
                                            v                                                      |
                                            /save-post?title=title1&body=body1                     V
                                                                                                post<Post> {title: ....}
                                                                                                   V
                                                                                               post.save() -> SQL -> database     
                                                                                                   v  
                        res <----------------------------------------------------------------------+                       








      [routes/urls]         [VIEWS]          [TEMPLATE] +----- extends 'layout.html'
                                                        V
req > 'get-posts' ------->  getPosts ------>   'get-posts.html'
                                |  
                                +-----> Post.objects.all() 
                                
                                +-----< posts<QuerySet>
                                |             
                                |             
                                |             
res < ---------------- render --+
  |
  v
HTML DOCUMENT


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 BROWSER 
    v                                                                  data  
form data -----> req        [routes/urls]                  [VIEWS]      V     
                  |              /change-post  --------->  changePost (request)
                  |                                                     .GET
                  |                                                   QueryDict {"title":['title1'], ...}
                  v                                                      |
                  /change-post?id=...&title=...&body=...                 V
                                                                         +-----> Post.objects.get(pk=...)
                                                                         v
                                                                      post<Post> {title: ....}
                                                                         v
                                                                        post.save() -> SQL -> database     
                                                                         v  
res <--------------------------------------------------------------------+                   






















      [routes/urls]                  [VIEWS]             [TEMPLATE] +----- extends 'layout.html'
                                                            V
req > 'update-post?id=...' ------->  updatePost ------> 'update-post.html'
                                  
                                       id <--- request.GET

                                        ----> Post.objects.get(pk=id)

                                                          
                                        +-----< post<???>
                                        |             
                                        |             
                                        |             
res < ---------------- render ----------+
  |
  v
HTML DOCUMENT
  |
  v
 <form> 




```











## Python / Django / mini social / User (builtin model/auth) 

    * User model
    * account creation
    * authentication
     

    - GET / POST
    - csrf 
    - urls 




  1. urls 

    /user/register 
    /user/login
    /user/logout







BROWSER ---> req (GET) ----> urls /user/register
                             |
                             v
                          registerUser(request)   
                             |
                            req.method == 'GET' ? 
                                |
                                True
                                |
                                + load ('user/register.html')
                                |
                                render() 
                                |
       <-------- res -----------+                      
<html>
  |
 FORM
  |
  + action = '/user/register'
  + method = 'POST'
  + {% csrf_token %}
  ...
  inputs         
  ...
               csrf_token
                   v
BROWSER ---> req (POST) ----> urls /user/register  
                              |
       <--------- res ------ CSRF protection  < MIDDLEWARE
                              |
                              v
                             registerUser(request)    





             +--------- authenticate() ---------+
             |                                  |
 username    |                                  |
------------->                                  |
             |                                  ----->
 password    |                                  |      DB
------------->    --->hash() ----->             <-----
             |                                  |  
             |                                  |
             +----------------v-----------------+  
               user           | 
     <------------------------+        






```
















## Python / Django / mini social / session & messages 


engines using SESSION:
   - auth
   - messages
   - custom



HTTP(S) request lifecycle
 ! stateless

                    data 
                      x --------------------------------------------------> x

                              A                                              B
                  req start -------------- end                req start -------------- end        
                    v                      v                    v                      v
>-x-----------------*----------------------*--------------------*----------------------*---------x-->
  ^                   ^   ^   ^   ^                                                              ^
 app started         mid url view db ...                                                     app ended 








            session data x-----------------------------------------....>
                    ^ 
s                   |      e
x--------- request -|------>
              |     ^
              .session












#  HW1:
#     draw the diagram as you see it, login -> message & session
#  HW2:
#     using django messages -> show messages wherever is needed
#  HW3:
#     when creating new user account:
#      1. show message
#      2. redirect to /
#      3. login the user automatically













## Let's use session to store a user preference !
   
    > notifications










## User Avatar 

  * profile
  * file uploads
  * alter user model 









+----- CustomUser  (proxy)
          |
          |
          +--- avatar 
          |                                     +---------- User
          +--- user_ptr_id ----------------->   | id
                                                |







  User
    ^
    |
CustomUser
   + avatar
   + friends --- relationship --- [CustomUser,CustomUser,CustomUser,...]
   
   


# HW1: 
#    finish "remove from friends"   










  ------------- ? -----------+ 
  v
anonymous <-------------> signedin
                             ^
  +---------------------------










CustomUser
   + session_data_backup: text 
+



user ---------------> logout
          ^             ^
        backup data   clear all data     


user ---------------> login
                        ^
                       new session <   backup data










User ------ cascading ---+
  ^                      |
  |                      |
 rel                     |
  |                      v
  +------ author ------ Post















## QUERIES / Django ORM

  * creation 
   
    obj = new Model(...)
    obj.save()

    obj = Model.objects.create(...)




  * read ONE!!! by id
    obj = Model.objects.get(pk= ...)
    obj = Model.objects.get(field= ...)

  * read MANY|ONE!!! by any field or relation field
    obj = Model.objects.filter(field= ...)
    obj = Model.objects.filter(field_id= ...)

  * read by any field with operator (exact, inexact, contains, startswith, endswith, ...)
    obj = Model.objects.get(field__operator= ...)
    obj = Model.objects.filter(field__operator= ...)

  * read by span relationships   
    obj = Model.objects.filter(relation__field__operator= ...)

  * read by  multiple conditions
    obj = Model.objects.filter(field_1= ..., field_2= ...)

  * read all 
    obj = Model.objects.all()

  * read all ordering
    obj = Model.objects.order_by('field_name').all()

  * read all except
    obj = Model.objects.exclude(field=...)




  * update

    obj.attribute = new_value
    obj.save()

    

  * update multiple

    Model.objects.update(field=F('field') + ...)  





  * delete

    obj.delete()    









+--------------------- Model<class> ----------------+
|                                                   |
|                                                   |
|            +----- .objects<Manager> -----+        | <--------------------> DB
|            |                             |        |
|            |                             |        |
|            |                             |        |
|            |                             |        |
|            +-----------------------------+        |
|                                                   |
+---------------------------------------------------+
         ^            ^      ...        ^      
         |            |                 |       
     obj1<Model>  obj2<Model>       objn<Model>














   
   
   
 +----------  <QuerySet>  --------------+
 |                                      |
 |                                      |
 |         .query                       |   
 |                                      |
 |                                      |
 +--------------------------------------+










author = CustomUser.objects.get(pk=8)
                         |
                       <QuerySet>  
                         |
                         v
                        "SELECT * FROM mini_social_customuser JOIN .... WHERE id = 8 " 


author 









## Django / Debugging

   

    USER :)
     |
    click url 
     |
     v                                   HTTPS
+------------- BROWSER --------------+              +----------------- APP --------------+       +-- DB ---+
|                                    |    req       |                                    |       |         |
|   --------------------------------------------------> middle > urls                    |       |         |
|                                    |              |              v                     |       |         |
|                                    |    res       |  template < views                  |       |         |
|    <----------------------------------------------------+        +--------> model ------> SQL >|         |
|                                    |              |              ^                     |       |         |
|                                    |              |              +--------  model  <---| < raw |         |
+---------------^--------------------+              +------------------------------------+       +---------+
                |
             dev console / inspector / network   











             django <--- INSTALLED_APPS <------------- mini_social 
                                                            ^
                                                            |
                                                          apps.py  
                                                            ^
                                                            |
                                                          SignalConfig(AppConfig)
                                                            ^
                                                            |  
                                                           ... 


AOP



                           model
                            |
                    pre     v     post 
   x-----------------x------x------x------------->                                 
                           save    ^
                                   |
                                   +---- callback                     


# HW1: 
    notify by email the post author when a new comment was added to its post                                  

    hint: post_save (comment) ---> post ---> author -> email










      http://127.0.0.1:8000/path/to/some/page



      https://gmail.com/path/to/some/page











      django
      send_mail() ---------> connect -----> MAIL server ----> ...
                                ^               ^
                                |               |
                              settings        gmail 