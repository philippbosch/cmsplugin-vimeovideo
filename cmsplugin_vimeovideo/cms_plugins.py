from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import VimeoVideo

class VimeoVideoPlugin(CMSPluginBase):
    model = VimeoVideo
    name = _("vimeo video")
    render_template = "plugins/vimeovideo/vimeovideo.html"
    text_enabled = True
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'vimeovideo': instance,
            'placeholder': placeholder
        })
        return context 

plugin_pool.register_plugin(VimeoVideoPlugin)
