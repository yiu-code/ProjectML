from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django import forms

from django.contrib.auth.models import AbstractBaseUser
from rest_framework import serializers

# Create your models here.
#Models + __str__ dat ervoor zorgt dat hij bij een call de naam laat zien.
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  def __str__(self):
      return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=120)
    brand = models.CharField(max_length=30)
    image = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class ProductList(models.Model):
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name='orders', on_delete=models.CASCADE)
    amount = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey('User', related_name='user', on_delete=models.CASCADE)
    def __str__(self):
      return self.user

"""
Associate multiple products to a cart. products verwijst naar de class Product
null an blank: you don't always need to have products in the cart, but the cart
has to exist.
"""
class Cart(models.Model):
    #id = models.IntegerField(primary_key=True)
    product_id = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    #timestamp = models.DateTimeField(auto_now_add=True)
    #timestamp = models.DateField(auto_now=False, default="")
    #updated = models.DateField(auto_now=True)
    #active = models.BooleanField(default=True)

    #def __unicode__(self):
    #    return "Cart id: %s" %(self.id)


class CartItem(models.Model):
    quantity = models.IntegerField()
    product_id = models.ManyToManyField(Product, null=True, blank=True)


class Cart_Items(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cartitem_id = models.ForeignKey(CartItem, on_delete=models.CASCADE)


"""
class CartItem(models.Model):
    # This class is going to handle all the new items in the cart
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    # The number of individual items for that product
    quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.product.title

class Cart(models.Model):
    # Info from class Product
    # Info from class User
    # Info from class Order (when user finished ordering, added OrderId is Max(OrderId) + 1
    # The amount of items in the cart (add the number to the cart image in .html
    # Ervoor zorgen dat de nieuwe order in de database wordt toegevoegd
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete_cascade)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.ForeignKey(ProductList, on_delete=models.CASCADE)

    def get_amount(self):
        return self.amount.amount()

    def get_cart_items(self):
        return self.product.all()

    def get_total_price(self):
        return sum(product.price for item in self.product.all())
"""
    
 


#---------------------------------- USER MODEL ---------------------------------------------
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff= False, is_admin=False, **extra_fields):
        if not email :
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(email = self.normalize_email(email), **extra_fields)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using= self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user
    
    

class User(AbstractBaseUser):
    Job_title_choices = [('Developer', 'Developer'),
                         ('Designer', 'Designer'),
                         ('Office', 'Office')
                        ]

    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    jobtitle = models.CharField(max_length=255, choices=Job_title_choices)
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    #This replaces the username field(which normally is used bij default) with email

    REQUIRED_FIELDS = []

    def get_mail(self):
        return self.email
    
    def get_full_name(self):
        return '%s %s' % (self.firstname, self.lastname)

    def get_first_name(self):
        return self.firstname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

    objects = UserManager()


    


    
