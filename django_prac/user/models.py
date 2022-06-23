from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,username,password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    #password 는 hasing 해야하기 때문에 최대 128로 맞춰줌 
    fullname = models.CharField(max_length=50)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}/{self.email}/{self.fullname}"

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = []
    is_active =models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True


    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label):
        return True

    #admin 권한설정    
    @property
    def is_staff(self):
        return self.is_admin