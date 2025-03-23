from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser, BaseUserManager
from taggit.managers import TaggableManager
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profilre')
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True)
    
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    


# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("email is required")
#         email = self.normalize_email(email=email)
#         user = self.model(email=email)
#         if not password :
#             raise ValueError("password is required")
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
        
#     def create_superuser(self, email,password=None):
        
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
    
    
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(unique=False, max_length=10)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     objects = CustomUserManager()
    

