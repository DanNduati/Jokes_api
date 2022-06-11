from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Jokes(Model):
    """
    The Joke model
    """

    id = fields.IntField(pk=True, null=False)
    setup = fields.TextField(null=False)
    punchline = fields.TextField(null=False)
    type = fields.CharField(null=False, max_length=15)

    def __str__(self) -> str:
        return f"{self.setup} ==> {self.punchline}"


# Really cool way to generate pydantic schemas from orm model
Joke_pydantic = pydantic_model_creator(Jokes, name="Joke")
