from rest_framework import serializers
from .models import *

class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    chats = serializers.SerializerMethodField('get_chats')
    operatorGroup = serializers.SerializerMethodField('get_operatorgroup')
    
    def get_chats(self, obj):
        return obj.get_chats()
    
    def get_operatorgroup(self, obj):
        return obj.operator.group.name
    
    class Meta:
        model = Conversation
        fields = [ 'id', 'store_id', 'operator_id', 'client_id', 'operatorGroup', 'chats']
