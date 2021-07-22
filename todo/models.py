from django.db import models
from django.utils.timezone import now

# Create your models here.
CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))


class TodoModel(models.Model):
    # fieldを定義
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE,
        null=True
    )
    duedate = models.DateField(default=now)

    def __str__(self):
        return "Title: {}, Memo: {}".format(self.title,
                                            self.memo)

# makemigrations　--> 実際にフィールドを作成する, 0001.py, 0002.py
# migrate --> モデルの設計図を作成し、データベースと統合する
