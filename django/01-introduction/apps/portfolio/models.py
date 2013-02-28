"""
.. module:: models
   :platform: Unix, Windows
   :synopsis: Portfolio Models.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>

"""

from django.db import models

# Create your models here.
class Project(models.Model):
    """Project Definition
    
    ::
    
        def whatever(self):
            retorn False
    """
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    """Docstring for class attribute date."""
    
    client = models.ForeignKey('Client', blank=True, null=True)
    media = models.ManyToManyField('Media', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('name', )
        
    def __unicode__(self):
        return '%s' % self.name
    
    
    def get_absolute_url(self):
        return '/portfolio/project/%s/' % self.pk


class Image(models.Model):
    
    file = models.ImageField(upload_to='images')
    
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    project = models.ForeignKey('Project', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        
    def __unicode__(self):
        return '%s - %s' % (self.name, self.file)
    
    
    






class Client(models.Model):
    
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('name', )
        
    def __unicode__(self):
        return '%s' % self.name


class Media(models.Model):
    
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
        ordering = ('name', )
        
    def __unicode__(self):
        return '%s' % self.name
    
    
   
   
class Comment(models.Model):

    username = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    
    project = models.ForeignKey('Project', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created',)
        
    def __unicode__(self):
        return '%s | %s' % (self.username, self.created)


   
    
    