from django.db import models


class Client(models.Model):
    fio = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)


class Cashier(models.Model):
    fio = models.CharField(max_length=200)


class NormalDocument(models.Model):
    document = models.CharField(max_length=200)


class PartsInfo(models.Model):
    name = models.CharField(max_length=200)
    supplier_alligment = \
        models.ForeignKey(NormalDocument, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class ServiceApplication(models.Model):
    id_cashier = \
        models.ForeignKey(Cashier, on_delete=models.CASCADE)
    id_client = \
        models.ForeignKey(Client, on_delete=models.CASCADE)
    id_part = \
        models.ForeignKey(PartsInfo, on_delete=models.CASCADE)
    id_document = \
        models.ForeignKey(NormalDocument, on_delete=models.CASCADE)
