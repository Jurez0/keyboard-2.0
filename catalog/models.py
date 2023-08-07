from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


# # Create your models here.
# class Product(models.Model):
#     '''
#     описание
#     ''' 
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
#                                      limit_choices_to={'model__in': ('pcb', 'switch', 'keyboard', 'keycap')})
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type', 'object_id')



# class Base(models.Model): 
#     '''
#     описание
#     ''' 
#     class Meta:
#         abstract = True

#     name = models.CharField(max_length=20)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     color = models.CharField(max_length=20) 
#     # product_type = models.CharField(max_length=20, default='keyboard')
#     def __str__(self):
#         return self.name
    
    
# kb_format_choise = (('100','Fullsize'), ('80', 'TKL'), ('75', '75%'), ('65', '65%'), ('60', '60%'), ('40', '40%'))
# kb_connect_choise = (('WR','Wire'), ('BT', 'Bluetooth'), ('WF', '2.4 GHz'), ('Al', 'All 3'))
# kb_material_choise = (('PL','Plastic'), ('AL', 'Aluminum'))
# kb_light_choise = (('R','Red'), ('B', 'Blue'), ('W', 'White'), ('RGB', 'RGB'))

# class PCB(Base): 
#     '''
#     описание
#     ''' 
#     kb_format = models.CharField(choices=kb_format_choise, max_length=3)
#     hot_swap = models.BooleanField(default=False) 
#     kb_connect = models.CharField(choices=kb_connect_choise, max_length=2)
#     kb_material = models.CharField(choices=kb_material_choise, max_length=2)
#     kb_light = models.CharField(choices=kb_light_choise, max_length=3)
#     perem_for_relete = models.ManyToManyField(
#         Product,
#         related_name = "catalog_pcb_related",
#         related_query_name = "pcb"
#     )

# switch_type_choise = (('LN','Linear'), ('TС', 'Tactile'), ('CL', 'Clicky'))

# class Switch(Base): 
#     '''
#     описание
#     ''' 
#     switch_type = models.CharField(choices=switch_type_choise, max_length=2)
#     strength = models.IntegerField() 
#     resource = models.IntegerField()
#     perem_for_relete = models.ManyToManyField(
#         Product,
#         related_name = "catalog_switch_related",
#         related_query_name = "switch"
#     )

# class Keyboard(Base): 
#     '''
#     описание
#     ''' 
#     kb_format = models.CharField(choices=kb_format_choise, max_length=3)
#     Hot_Swap = models.BooleanField(default=False) 
#     kb_connect = models.CharField(choices=kb_connect_choise, max_length=2)
#     kb_material = models.CharField(choices=kb_material_choise, max_length=2)
#     kb_light = models.CharField(choices=kb_light_choise, max_length=3)
#     switch_type = models.CharField(choices=switch_type_choise, max_length=2)
#     strength = models.IntegerField() 
#     resource = models.IntegerField()
#     perem_for_relete = models.ManyToManyField(
#         Product,
#         related_name = "catalog_keyboard_related",
#         related_query_name = "keyboard"
#     )

# kc_material_choise = (('PBT', 'PBT'), ('ABS', 'ABS'))
# kc_profile_choise = (('SA', 'SA'), ('TAI', 'TAI'), ('KAT', 'KAT'), ('OEM', 'OEM'), ('CHR', 'CHR'), ('XDA', 'XDA'))

# class KeyCap(Base):
#     '''
#     описание
#     ''' 
#     kc_material = models.CharField(choices=kc_material_choise, max_length=3)
#     kc_profile = models.CharField(choices=kc_profile_choise, max_length=3)
#     double_Shot = models.BooleanField(default=False) 
#     rus_layout = models.BooleanField(default=False) 
#     perem_for_relete = models.ManyToManyField(
#         Product,
#         related_name = "catalog_keycap_related",
#         related_query_name = "keycap"
#     )


#     '''
#     “Заказ” (Order) - информация сделанном пользователем заказе. 
#     Поля: Покупатель, Дата заказа, Статус заказа, Сумма заказа, Список товаров.
#     '''