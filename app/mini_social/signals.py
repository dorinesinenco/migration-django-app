from .models import Post
from django.core.mail import send_mail
from django.conf import settings


def postPublishedCallback(sender,instance, **kwargs):
    if isinstance(instance,  Post):
    
        print("!!!! Post publshed !!!!")
        host = settings.SITE_URL
        print(f"you can read it <a href='{host}/post/{instance.id}'>here</a>")
        send_mail(
            "MINI SOCIAL: A new post was published ",
            "",
            settings.SITE_MAIL,
            ["dorin.e.art@gmail.com"],
            fail_silently=False,
            html_message = f"you can read it <a href='{host}/post/{instance.id}'>here</a>",
        )
      
# HW1: when a post is created - notify all the users      
# HW2: when a new comment is added to a post -> notify the author