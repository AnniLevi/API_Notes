from django.db import models


class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    name = models.CharField(max_length=50, verbose_name='Город')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    name = models.CharField(max_length=50, verbose_name='Специальность')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    class Meta:
        verbose_name = 'Сайт для поиска'
        verbose_name_plural = 'Сайты для поиска'

    name = models.CharField(max_length=50, verbose_name='Сайт для поиска')
    url = models.URLField(unique=True, verbose_name='Адрес сайта')

    def __str__(self):
        return self.name


# class Vacancy(models.Model):
#     class Meta:
#         verbose_name = 'Вакансия'
#         verbose_name_plural = 'Вакансии'
#
#     url = models.URLField(unique=True, verbose_name='Адрес вакансии')
#     title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
#     description = models.TextField(blank=True, verbose_name='Описание вакансии')
#     company = models.CharField(max_length=250, blank=True, verbose_name='Название компании')
#     city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
#     specialty = models.ForeignKey(Specialty, verbose_name='Специальность', on_delete=models.CASCADE)
#     site = models.ForeignKey(Site, verbose_name='Сайт', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
