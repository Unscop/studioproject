from django.db import models

class TeamList(models.Model):
    name = models.CharField("Имя", max_length=150)
    secname = models.CharField("Фамилия", max_length=150)
    position = models.CharField("Должность", max_length=150)
    avatar = models.ImageField("", upload_to='movies/') 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"


class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    poster = models.ImageField("", upload_to='movies/')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class CallBack(models.Model):
    email = models.EmailField(unique=True)
    name = models.TextField("Имя", max_length=500)
    message = models.TextField("Сообщение", max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратный связь"
        verbose_name_plural = "Обратные связи"
