from django.db import models

# Create your models here.
class Notes(models.Model):
    unitcode=models.CharField(max_length=50)
    unitname=models.CharField(max_length=50)
    
    pdf=models.FileField(upload_to="pdf",blank=False)
    def __str__(self) :
        return '{} {}'.format(self.unitcode,self.unitname)


class Exams(models.Model):
    unitcode=models.CharField(max_length=50)
    unitname=models.CharField(max_length=50)
    yeardone=models.IntegerField()
    image=models.ImageField(upload_to ="img",blank=False)
    def __str__(self) :
        return '{} {}'.format(self.unitcode,self.unitname)
        

class Cats(models.Model):
    unitcode=models.CharField(max_length=50)
    unitname=models.CharField(max_length=50)
    yeardone=models.IntegerField()
    image=models.ImageField(upload_to ="img",blank=False)
    def __str__(self) :
        return '{}{}'.format(self.unitcode,self.unitname)
        
