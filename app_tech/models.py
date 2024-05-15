from django.db import models


class Leadership(models.Model):
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    number = models.IntegerField()
    email = models.EmailField()
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name


class Structural(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Standard(models.Model):
    decision_name = models.CharField(max_length=250)
    decision_number = models.IntegerField()
    decision_text = models.CharField(max_length=250)

    def __str__(self):
        return self


class Electronic_Standard(models.Model):
    keyword = models.CharField(max_length=250)
    document_number = models.IntegerField()
    document_category = models.CharField(max_length=250)
    conditional_symbol = models.CharField(max_length=250)
    document_year = models.IntegerField()

    def __str__(self):
        return self.keyword


class Connection(models.Model):
    adress = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    email2 = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    FIO = models.CharField(max_length=250)
    e_mail = models.CharField(max_length=250)
    leadership = models.ForeignKey(Leadership, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)

    def __str__(self):
        return self.email


class Building(models.Model):
    number = models.IntegerField()
    characters = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.characters


class Dictionary(models.Model):
    standard_number = models.IntegerField()
    language_code = models.CharField(max_length=15)
    language_ru = models.CharField(max_length=250)
    language_uz = models.CharField(max_length=250)
    language_turk = models.CharField(max_length=250)
    language_en = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.standard_number} - {self.language_code} - {self.language_uz}'

    class Meta:
        db_table = 'dictionary'
        verbose_name = 'Dictionary'