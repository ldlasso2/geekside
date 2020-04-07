from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(_('Título'),max_length= 150)#var char
    text = models.TextField(_('Texto')) #long text
    excerpt = models.CharField(_('Resumen'),max_length=120, blank=True)
    is_active = models.BooleanField(_('Activo'),default=True)
    created_at = models.DateTimeField(_('Feha y hora de creación'),auto_now_add=True)
    update_at = models.DateTimeField(_('fecha y hora de actualización'),auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('autor'))

    class Meta:
        verbose_name = _('Publicación')
        verbose_name_plural =_('Publicaciones')


    def __str__(self):
        return self.title

    