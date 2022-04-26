from tortoise.models import Model
from tortoise import fields

class Jokes(Model):
    """
    The Joke model
    """
    id = fields.IntField(pk=True)
    setup = fields.TextField()
    punchline = fields.TextField()
    type = fields.CharField(max_length=15)

    def __str__(self):
        return f"{self.setup} ==> {self.punchline}"