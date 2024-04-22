from django.db import models

class State(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Program(models.Model):
    name = models.CharField(max_length=150, unique=True)
    state = models.ManyToManyField(State)
    district = models.ManyToManyField(District)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    state = models.ManyToManyField(State)
    district = models.ManyToManyField(District)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


