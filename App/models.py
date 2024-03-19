from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)


class AgrOff(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)



class Farmer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Notification(models.Model):
    notification = models.CharField(max_length=240)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    filename = models.CharField(max_length=240)


class Feedback(models.Model):
    feedback = models.CharField(max_length=240)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    FARMER = models.ForeignKey(Farmer, on_delete=models.CASCADE)


class Cfp(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo = models.CharField(max_length=240)
    type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)



class Policy(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)


class Stock(models.Model):
    count = models.CharField(max_length=100)
    CFP = models.ForeignKey(Cfp, on_delete=models.CASCADE)
    AGROFF = models.ForeignKey(AgrOff, on_delete=models.CASCADE)


class CfpCart(models.Model):
    count = models.CharField(max_length=100)
    STOCK = models.ForeignKey(Stock, on_delete=models.CASCADE)
    FARMER = models.ForeignKey(Farmer, on_delete=models.CASCADE)


class CfpReqMain(models.Model):
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=150)
    time = models.CharField(max_length=100)
    FARMER = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    AGROFF = models.ForeignKey(AgrOff, on_delete=models.CASCADE)


class CfpReqSub(models.Model):
    count = models.CharField(max_length=100)
    CFP = models.ForeignKey(Cfp, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    CFPREQMAIN = models.ForeignKey(CfpReqMain, on_delete=models.CASCADE)


class Stories(models.Model):
    image = models.CharField(max_length=150)
    description = models.TextField()
    date = models.CharField(max_length=150)
    time = models.CharField(max_length=100)
    FARMER = models.ForeignKey(Farmer, on_delete=models.CASCADE)


class Chat(models.Model):
    OFFICER = models.ForeignKey(AgrOff, on_delete=models.CASCADE)
    FARMER = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    message = models.CharField(max_length=245)
    mdate = models.CharField(max_length=150)
    mtime = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Complaints(models.Model):
    complaint_date = models.CharField(max_length=100)
    complaint= models.CharField(max_length=100)
    reply= models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    FARMER = models.ForeignKey(Farmer, default=1, on_delete=models.CASCADE)
