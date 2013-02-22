"""
.. module:: models
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>

"""

from django.db import models

# Create your models here.
class Project(models.Model):
    """Fetches rows from a Bigtable.
    
    ::
    
        def session(self):
            retorn False

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    """Docstring for class attribute date.baz."""
    
    client = models.ForeignKey('Client', blank=True, null=True)
    media = models.ManyToManyField('Media', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('name', )
        
    def __unicode__(self):
        return '%s' % self.name


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
    
    
    
    