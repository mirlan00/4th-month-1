from django.db import models

class InfoUser(models.Model):
    name = models.CharField(
        max_length=255 ,
        verbose_name="Имя пользователя"
    )
    job = models.CharField(
        max_length=100,  
        verbose_name="Профессия"
    )
    image = models.ImageField(
        upload_to="infouser_images", 
        verbose_name="Фотография"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=20,  
        verbose_name="Телефонный номер"
    )
    youtube = models.URLField(
        verbose_name="YOUTUBE"
    )
    instagram = models.URLField(
        verbose_name="Instagram"
    )
    whatsapp = models.URLField(
        verbose_name="Whatsapp"
    )
    facebook = models.URLField(
        verbose_name="Facebook"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация пользователя"
        verbose_name_plural = "Информация пользователей"


class Numbers(models.Model):
    experience = models.IntegerField(
        verbose_name="Годы опыта"
    )
    project=models.IntegerField(
        verbose_name="Завершенные проекты"
    )
    clients =models.IntegerField(
        verbose_name="Доволные клиенты"
    )

    def __str__(self):
        return f"Опыт: {self.experience}, Проекты: {self.project}, Клиенты: {self.clients}"
    
    class Meta:
        verbose_name = "Я в числе"
        verbose_name_plural = "Я в числах"
    
class Service(models.Model):
    number = models.IntegerField(
        verbose_name= "Нумерация"
    )
    title= models.CharField(
        max_length= 255,
        verbose_name= "Название услуги"
    )
    descriptions = models.TextField(
        verbose_name= "Описание услуги"
    ) 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
