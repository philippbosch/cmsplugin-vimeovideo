# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cmsplugin_filer_image.models import ThumbnailOption

class VimeoVideo(CMSPlugin):
    url = models.URLField(_("vimeo URL"))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True, null=True, help_text=_("textual description of the image"))
    thumbnail_option = models.ForeignKey(ThumbnailOption, verbose_name=_("thumbnail option"))
    
    def __unicode__(self):
        return u"%s" % self.url
    
    @property
    def vimeo_id(self):
        return self.url[self.url.rfind('/')+1:]
    
    @property
    def dimensions(self):
        if not self.thumbnail_option:
            return [None, None]
        return [self.thumbnail_option.width, self.thumbnail_option.height]
    
    @property
    def width(self):
        return self.dimensions[0]
    
    @property
    def height(self):
        return self.dimensions[1]
    
    class Meta:
        verbose_name=_("vimeo video")
        verbose_name_plural=_("vimeo videos")
