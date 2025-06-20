from django.db import models

from django.db import models
from django.utils.timezone import now
from hello.models import UserAccount

class Book(models.Model):
    bookid = models.AutoField(db_column='bookid', primary_key=True)
    title = models.CharField(db_column='title', max_length=255)
    description = models.TextField(db_column='description', blank=True, null=True)
    stockquantity = models.IntegerField(db_column='stockquantity', default=0)
    language = models.CharField(db_column='language', max_length=100)
    pagecount = models.IntegerField(db_column='pagecount', blank=True, null=True)
    authorid = models.IntegerField(db_column='authorid', blank=True, null=True) 
    publisherid = models.IntegerField(db_column='publisherid', blank=True, null=True)  
    price = models.DecimalField(db_column='price', max_digits=10, decimal_places=2)
    publicationdate = models.DateField(db_column='publicationdate')
    agerestriction = models.CharField(db_column='agerestriction', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'book'  
        managed = False  

    def __str__(self):
        return self.title

class Role(models.Model):
    roleid = models.AutoField(db_column='roleid', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)

    class Meta:
        db_table = 'role'
        managed = False

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    cartid = models.AutoField(db_column='cartid', primary_key=True)
    user = models.OneToOneField(UserAccount, db_column='useraccountid', on_delete=models.CASCADE, related_name='api_shop_cart')

    class Meta:
        db_table = 'cart'
        managed = False

class CartItem(models.Model):
    cartitemid = models.AutoField(db_column='cartitemid', primary_key=True)
    cart = models.ForeignKey(Cart, db_column='cartid', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, db_column='bookid', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(db_column='quantity', default=1)

    class Meta:
        db_table = 'cartitem'
        managed = False

class OrderStatus(models.Model):
    orderstatusid = models.AutoField(db_column='orderstatusid', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description')

    class Meta:
        db_table = 'orderstatus'
        managed = False

    def __str__(self):
        return self.name


class DeliveryMethod(models.Model):
    deliverymethodid = models.AutoField(db_column='deliverymethodid', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description')
    address = models.TextField(db_column='address')

    class Meta:
        db_table = 'deliverymethod'
        managed = False

    def __str__(self):
        return self.name


class Publisher(models.Model):
    publisherid = models.AutoField(db_column='publisherid', primary_key=True)
    name = models.CharField(db_column='name', max_length=255)
    country = models.CharField(db_column='country', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='description')

    class Meta:
        db_table = 'publisher'
        managed = False

    def __str__(self):
        return self.name


class Format(models.Model):
    formatid = models.AutoField(db_column='formatid', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description')

    class Meta:
        db_table = 'format'
        managed = False

    def __str__(self):
        return self.name


class Author(models.Model):
    authorid = models.AutoField(db_column='authorid', primary_key=True)
    firstname = models.CharField(db_column='firstname', max_length=100)
    lastname = models.CharField(db_column='lastname', max_length=100)
    middlename = models.CharField(db_column='middlename', max_length=100, blank=True, null=True)
    country = models.CharField(db_column='country', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='description')

    class Meta:
        db_table = 'author'
        managed = False

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Genre(models.Model):
    genreid = models.AutoField(db_column='genreid', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description')

    class Meta:
        db_table = 'genre'
        managed = False

    def __str__(self):
        return self.name


class BookGenres(models.Model):
    bookgenresid = models.AutoField(db_column='bookgenresid', primary_key=True)
    genre = models.ForeignKey(Genre, db_column='genreid', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, db_column='bookid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookgenres'
        managed = False


class OrderTable(models.Model):
    orderid = models.AutoField(db_column='orderid', primary_key=True)
    user = models.ForeignKey(UserAccount, db_column='useraccountid', on_delete=models.CASCADE, related_name='api_shop_orders')
    totalamount = models.DecimalField(db_column='totalamount', max_digits=10, decimal_places=2)
    orderdate = models.DateField(db_column='orderdate')
    orderstatus = models.ForeignKey(OrderStatus, db_column='orderstatusid', on_delete=models.SET_NULL, null=True)
    deliverymethod = models.ForeignKey(DeliveryMethod, db_column='deliverymethodid', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ordertable'
        managed = False


class OrderItem(models.Model):
    orderitemid = models.AutoField(db_column='orderitemid', primary_key=True)
    order = models.ForeignKey(OrderTable, db_column='orderid', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, db_column='bookid', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(db_column='quantity')

    class Meta:
        db_table = 'orderitem'
        managed = False
