from django.db import models


# Create your models here.


class Customer(models.Model):
    slno = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)
    rmn = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    slno = models.IntegerField(null=True)
    name = models.CharField(max_length=200, null=True)
    # rpic=models.ImageField
    rmn = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Resttab(models.Model):
    rname = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    tnum = models.IntegerField(null=True)

    def __str__(self):
        rest=str(self.rname)
        return str(self.tnum) +" "+ rest


class Dishes(models.Model):
    rname = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    dname = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.dname


class OrdersDish(models.Model):
    STATUS = (
        ('Order Confirmed', 'Order Confirmed'),
        ('Order Pending', 'Order Pending'),
        ('Order Cancelled', 'Order Cancelled'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    dish = models.ForeignKey(Dishes, null=True, on_delete=models.SET_NULL)
    orderby = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        cust=str(self.customer)
        rest=str(self.restaurant)
        dish=str(self.dish)
        return cust + rest + dish


class BookTable(models.Model):
    STATUS = (
        ('Booked', 'Booked'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    tables = models.ForeignKey(Resttab, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100,null=True,choices=STATUS)

    def __str__(self):
        cust=str(self.customer)
        tab=str(self.tables)
        return cust +" "+ tab