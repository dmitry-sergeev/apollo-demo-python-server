from graphene import relay
from graphene_django import DjangoObjectType

from .models import TodoNote


class TodoNoteType(DjangoObjectType):
    class Meta:
        model = TodoNote
        filter_fields = ('note', )
        interfaces = (relay.Node, )
