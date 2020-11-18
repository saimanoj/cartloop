from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.conf import settings

import os
import pytz
import json
from faker import Faker
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from random import randint
from dateutil.relativedelta import relativedelta
from django.db import connection

from user.models import User
from .serializers import *
from .decorators import is_valid
from .models import *

class MyConversation(APIView):
    def get(self, request, id, format=None):
        conversation = Conversation.objects.get( id = id, status=1 )
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)

class MyChat(APIView):
    @is_valid('')
    def post(self, request, format=None):
        body = json.loads(request.body)
        conversation = Conversation.objects.get(id = body['conversationId'])
        message = body['chat']['payload'].replace('{{ username }}', conversation.client.name)
        message = message.replace('{{ operator }}', conversation.operator.name)
        message = message.replace('{{ discountCode }}', conversation.discount_code)

        print(self.get_send_time(body).replace(tzinfo=pytz.UTC))
        chat, created_at= Chat.objects.get_or_create(message= message, user_id = body['chat']['userId'], conversation_id = body['conversationId'], status = 1)
        Schedule.objects.create(
            chat_id = chat.id,
            message_status = 'New',
            send_at = self.get_send_time(body)
            )
        chat.save()
        
        return JsonResponse({'chatId':chat.id}, safe=False)
        #return JsonResponse({'chatId':123124}, safe=False)

    def get_send_time(self, body):
        c = Conversation.objects.get(id = body['conversationId'])
        tz = c.client.timezone
        if not tz:    
            tz = c.store.timezone
        
        dt = datetime.now()
        cdt = dt+timedelta(seconds = tz)
        
        cst = cdt.replace(hour=settings.START_TIME.hour, minute=settings.START_TIME.minute, second=0, microsecond=0)
        cet = cdt.replace(hour=settings.END_TIME.hour, minute=settings.END_TIME.minute, second=0, microsecond=0)
        if cst <= cdt <= cet:
            return cdt
        elif cdt < cst:
            return cst
        elif cdt > cet:
            return cst+timedelta(days = 1)

        

class ImportData(APIView):
    def get(self, request, format=None):
        '''x = pytz.all_timezones

        fake = Faker()
        operator = 5
        for _ in range(20):  
            zone = x[randint(0,len(x))]
            utcnow = timezone('utc').localize(datetime.utcnow())
            client_time = utcnow.astimezone(timezone(zone)).replace(tzinfo=None)
            utcnow = utcnow.replace(tzinfo=None)
            sec = int((utcnow-client_time).total_seconds())
            User.objects.create(
                name = fake.name(),
                email = fake.email(),
                timezone = sec, 
                user_type = 'operator' if operator else 'client',
                status = 1
            )

            if operator: operator -= 1'''

        cursor = connection.cursor()
        sql_file = open(os.path.join(settings.BASE_DIR, 'initial_data.sql'))
        for l in sql_file.readlines():
            if len(l):
                try:
                    cursor.execute( l )
                except Exception as e:
                    print(e)
        connection.commit()

        return HttpResponse('Sucess')