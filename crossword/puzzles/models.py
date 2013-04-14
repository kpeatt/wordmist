# puzzles/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
from model_utils.models import TimeStampedModel
import puz

class Source(TimeStampedModel):
    # Source Slug
    slug = models.SlugField()
    
    # Source Name
    name = models.CharField(max_length=255)

    # Source Update Frequency
    DAILY = 'd'
    WEEKLY = 'w'
    MONTHLY = 'm'
    UPDATE_FREQUENCY = (
        ('d', 'daily'),
        ('w', 'weekly'),
        ('m', 'monthly')
    )
    frequency = models.CharField(max_length=255,
                                 choices=UPDATE_FREQUENCY,
                                 default=WEEKLY)

    # Day on which it updates
    DAYS_OF_WEEK = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    day = models.CharField(max_length=3,
                           choices=DAYS_OF_WEEK,
                           blank=True)

    # Source URL
    url = models.URLField()

    # Filename structure
    # name[ymd] where [ymd] is in PHP date format
    filename = models.CharField(max_length=50)

    # Filetype (JPZ or PUZ)
    FILETYPES = (
        ('puz', 'puz'),
        ('jpz', 'jpz')
    )
    filetype = models.CharField(max_length=3,
                                choices=FILETYPES,
                                default='puz')

    # Whether or not this source is active
    active = models.BooleanField()

    def __unicode__(self):
        return self.name

class Puzzle(TimeStampedModel):
    source = models.ForeignKey(Source)
    title = models.CharField(max_length=255, default='Title')
    author = models.CharField(max_length=255, default='Author')
    copyright = models.CharField(max_length=100, default='Copyright')
    puzzle = models.FileField(upload_to=lambda self, fname:self.save_path(fname))

    def __unicode__(self):
        return self.title

    def save_path(self, filename):
        return 'puzzles/' + self.source.slug + '/' + filename

    def read_puzzle(self):
        contents = puz.read(self.puzzle.path)
        return contents

    def save(self, *args, **kwargs):
        """Save crossword metadata"""
        super(Puzzle, self).save(*args, **kwargs)
        puzzledata = self.read_puzzle()

        self.title = puzzledata.title.strip()
        self.author = puzzledata.author.strip()
        self.copyright = puzzledata.copyright.strip()

        super(Puzzle, self).save(*args, **kwargs)

