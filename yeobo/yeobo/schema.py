import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType

from chats.models import Chat

class ChatType(DjangoObjectType):
    class Meta:
        model = Chat
        
class Query(graphene.ObjectType):
    chats = graphene.List(ChatType)

    def resolve_chats(self, info, **kwargs):
        return Chat.objects.all()

schema = graphene.Schema(query=Query)