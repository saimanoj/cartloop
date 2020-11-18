from django.db import models
from store.models import Store
from user.models import User


class Conversation(models.Model):
    store =  models.ForeignKey( Store, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey( User, related_name='operator', on_delete=models.SET_NULL, null=True)
    discount_code = models.CharField(max_length=50, null=True)
    client = models.ForeignKey( User, related_name='client', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField( default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_chats(self):
        chats = Chat.objects.filter(conversation_id = self.id).order_by('id')
        result = []
        for chat in chats:
            s = Schedule.objects.get(chat_id = chat.id)
            result.append({
                "chatId":chat.id,
                "payload":chat.message,
                "userId":chat.user.id,
                "utc-date":chat.created_at,
                "status":s.message_status})
        return result

class Chat(models.Model):
    message = models.TextField()
    user = models.ForeignKey( User, on_delete=models.SET_NULL, null=True)
    conversation = models.ForeignKey( Conversation, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField( default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Schedule(models.Model):
    chat =  models.ForeignKey( Chat, on_delete=models.SET_NULL, null=True)
    message_status = models.CharField(max_length=50, null=True)
    send_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
