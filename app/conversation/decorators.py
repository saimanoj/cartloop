from django.http import JsonResponse, HttpResponse
from django.conf import settings

import re
import json


def is_valid(permission):
    def _function(func):
        def _function1(request, *args, **kwargs):
            body = json.loads(request.request.body)
            reg=re.compile('[^'+settings.STRING_MATCH+'\s]+')
            sm = reg.findall(body['chat']['payload'])
            print(sm)
            match = True if sm else False
            if (match):
                return JsonResponse({'message':'in valid input'}, status=403)
            elif (not(len(body['chat']['payload']) < settings.MESSAGE_LENGTH)):
                return JsonResponse({'message':'in valid input'}, status=403)
            return func(request, *args, **kwargs)
        return _function1        
    return _function