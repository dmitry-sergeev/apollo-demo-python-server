from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .types import TodoNoteType


class TodoQueries():
    todo_note = relay.Node.Field(TodoNoteType)
    todo_notes = DjangoFilterConnectionField(TodoNoteType)
