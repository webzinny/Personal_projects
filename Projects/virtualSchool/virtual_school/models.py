from django.db import models

class student_list (models.Model):
    school_id = models.IntegerField()
    roll_no = models.CharField(max_length=15)
    name = models.CharField(max_length=25)
    Class = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)

class teacher_list (models.Model):
    school_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)


class school_list (models.Model):
    school_name = models.CharField(max_length=30)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)


class homework (models.Model):
    school_id = models.IntegerField()
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=30,default='Name')
    name = models.CharField(max_length=100)
    Class = models.IntegerField()
    subject = models.CharField(max_length=15)
    date = models.DateField()
    file = models.FileField(upload_to='student_homework')

class chat (models.Model):
    school_id = models.IntegerField(default=1)
    Class = models.IntegerField(default=1)
    person_id = models.CharField(max_length=6)
    name = models.CharField(max_length=30)
    date = models.DateField()
    message = models.CharField(max_length=250)

class teacher_hw(models.Model):
    school_id = models.IntegerField()
    Class = models.IntegerField()
    subject = models.CharField(max_length=15)
    date = models.DateField()
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='teacher_hw')

class notes(models.Model):
    school_id = models.IntegerField()
    teacher_id = models.IntegerField()
    Class = models.IntegerField()
    subject = models.CharField(max_length=15)
    date = models.DateField()
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='notes')

class notice(models.Model):
    school_id = models.IntegerField()
    teacher_id = models.IntegerField()
    date = models.DateField()
    notice_msg = models.CharField(max_length=300)

class lectures(models.Model):
    school_id = models.IntegerField()
    teacher_id = models.IntegerField()
    Class = models.IntegerField()
    subject = models.CharField(max_length=15)
    link = models.CharField(max_length=300)

class info(models.Model):
    school_id = models.IntegerField()
    teacher_id = models.IntegerField()
    Class = models.IntegerField()
    type = models.CharField(max_length=10)
    file = models.FileField(upload_to='info')
