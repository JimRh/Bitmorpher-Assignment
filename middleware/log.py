import json
from apps.usermanager.models import User,APILog
from apps.usermanager.serializers import UserSerialziers
from django.utils import timezone

class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
   

    def __call__(self, request):
        
        body = request.body
        token = None

        if body:
            try:
                
                if request.content_type == 'application/json':
                    data = json.loads(body)
                    token = data.get('token')
                    user=User.objects.filter(authentication_token=token)
                    time=timezone.localtime(timezone.now())
                    localtime = time.strftime('%Y-%m-%d %H:%M:%S')
                    if not user:
                       username="anynomous"
                       APILog.objects.update_or_create(username=username,timestamp=localtime)
                    else:
                        serializeddata=UserSerialziers(user,many=True)
                        data=serializeddata.data
                        username=data[0]['username']
                        APILog.objects.update_or_create(username=username,timestamp=localtime)

                        

                       

                 
            except Exception as e:
                print(f"Error parsing request body: {e}")

       
        
        
        
        
        response = self.get_response(request)

        return response