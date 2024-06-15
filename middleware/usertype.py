import json
from apps.usermanager.models import User

class UsertypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
   

    def __call__(self, request):
        
        body = request.body
        token = None
        usertype=None
        if body:
            try:
                
                if request.content_type == 'application/json':
                    data = json.loads(body)
                    token = data.get('token')
                    user=User.objects.filter(authentication_token=token)
                    if not user:
                       usertype=None 
                    else:
                        usertype=user[0].user_type
            except Exception as e:
                print(f"Error parsing request body: {e}")

        print(token)
        
        request.usertype = usertype
        
        
        response = self.get_response(request)

        return response