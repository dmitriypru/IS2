from tortoise import fields, models


class Memo(models.Model):
    id: int = fields.IntField(pk=True)
    text: str = fields.CharField(max_length=100)

    class Meta:
        table = "memos"
        ordering = ["-id"]