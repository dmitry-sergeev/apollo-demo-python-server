from graphene import Field
from .types import TodoNoteType


class TodoQueries():
    # todo_notes = relay.Node.Field(CategoryNode)
    todo_notes = Field(TodoNoteType)
