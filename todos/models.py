from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    pub_date = models.DateTimeField('date published')
    STATUS = (
        (1, 'todo'),
        (2, 'progress'),
        (3, 'onhold'),
        (4, 'done')
    )
    status = models.IntegerField(choices=STATUS, default=1)

    def __str__(self):
        return self.title + ' - ' + self.desc

    class Meta:
        verbose_name_plural = "Todo List"
