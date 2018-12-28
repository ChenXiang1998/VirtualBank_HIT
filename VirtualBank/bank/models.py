from django.db import models

# Create your models here.
class Users(models.Model):
  #  id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=32)
    uidcard = models.CharField(max_length=32)
    uphone = models.CharField(max_length=32)
    uemail = models.CharField(max_length=32)
    upasswd = models.CharField(max_length=128)
    paypasswd = models.CharField(max_length=128,null=True)
    time = models.DateTimeField()
    status = models.CharField(max_length=32, default="正常")

class Admins(models.Model):
   # id = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=32)
    apasswd = models.CharField(max_length=128)

class CrashCard(models.Model):
   # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
#    balance = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    balance = models.FloatField(default=0)
    time = models.DateTimeField(null=True)
    status = models.CharField(max_length=32, default="正常")

class Transfer(models.Model):
   # id = models.AutoField(primary_key=True)
    time = models.DateTimeField(default="1970-10-10 08:00:00")
    suser = models.ForeignKey(Users,on_delete=models.DO_NOTHING,related_name="sid")
    duser = models.ForeignKey(Users,on_delete=models.DO_NOTHING,related_name="did")
    scard = models.ForeignKey(CrashCard, on_delete=models.DO_NOTHING,related_name="scard")
    dcard = models.ForeignKey(CrashCard, on_delete=models.DO_NOTHING,related_name="dcard")
  #  amount = models.DecimalField(max_digits=16,decimal_places=2)
    amount = models.FloatField(default=0)
   # scbalance = models.IntegerField()
   # dcbalance = models.IntegerField()
    scbalance = models.FloatField(default=0)
    dcbalance = models.FloatField(default=0)
    remark = models.CharField(max_length=128,null=True,default="无")

class DrawDeposit(models.Model):
   # id = models.AutoField(primary_key=True)
    card = models.ForeignKey(CrashCard, on_delete=models.DO_NOTHING)
  #  amount = models.DecimalField(max_digits=16,decimal_places=2)
    amount = models.FloatField(default=0)
  #  balance = models.DecimalField(max_digits=16,decimal_places=2)
    type = models.CharField(max_length=32,default="存款")
    balance = models.FloatField(default=0)
    datafrom = models.CharField(max_length=64,null=True,default="自动存取款机")
    time = models.DateTimeField()

