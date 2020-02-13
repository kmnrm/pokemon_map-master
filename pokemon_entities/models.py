from django.db import models

class Pokemon(models.Model):
    pokemon_id = models.AutoField(auto_created=True, primary_key=True)
    title_ru = models.CharField('Название покемона на русском', max_length=200, default='Неизвестное имя')
    title_en = models.CharField('Название покемона на английском', max_length=200, default='Unknown name')
    title_jp = models.CharField('Название покемона на японском', max_length=200, default='不明な名前')
    previous_evolution = models.ForeignKey('self', verbose_name='Эволюционировал из', related_name='next_evolutions', null=True, blank=True, on_delete=models.SET_NULL)
    img_url = models.ImageField('Изображение покемона', blank=True)
    description = models.TextField('Описание покемона', blank=True)
    
    def __str__(self):
        return f"{self.title_ru}"

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    lat = models.FloatField('Положение на карте(широта)')
    lon = models.FloatField('Положение на карте(долгота)')
    appeared_at = models.DateField('Появится', blank=True, null=True)
    disappeared_at = models.DateField('Исчезнет', blank=True, null=True)
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Выносливость', blank=True, null=True)