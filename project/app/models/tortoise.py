from tortoise.models import Model
from tortoise import fields

class Jokes(Model):
    """
    The Joke model
    """
    id = fields.IntField(pk=True,null=False)
    setup = fields.TextField(null=False)
    punchline = fields.TextField(null=False)
    type = fields.CharField(null=False,max_length=15)

    def __str__(self):
        return f"{self.setup} ==> {self.punchline}"