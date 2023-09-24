from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models.cohorteDate import Cohorte
from .models.student import Estudiante

@receiver(pre_save, sender=Estudiante)
def guardar_cohorte_anterior(sender, instance, **kwargs):
    try:
        instance.cohorte_anterior = Estudiante.objects.get(id=instance.id).cohorte
    except Estudiante.DoesNotExist:
        instance.cohorte_anterior = None

@receiver(post_save, sender=Estudiante)
def actualizar_numerodeestudiantes_al_cambiar_cohorte(sender, instance, created, **kwargs):
    if not created and instance.cohorte != instance.cohorte_anterior:
        if instance.cohorte_anterior is not None:
            instance.cohorte_anterior.actualizar_numerodeestudiantes()
        if instance.cohorte is not None:
            instance.cohorte.actualizar_numerodeestudiantes()

@receiver(post_delete, sender=Estudiante)
def actualizar_numerodeestudiantes_al_eliminar_estudiante(sender, instance, **kwargs):
    if instance.cohorte:
        instance.cohorte.actualizar_numerodeestudiantes()