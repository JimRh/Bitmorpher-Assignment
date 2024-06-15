from ..models import User

def createuser(username,email,password):

        user=User()
        user.username=username
        user.email=email
        user.set_password(raw_password=password)
        user.user_type='customer'
        user.save()
    
        authentication_token=user.authentication_token
        return authentication_token
 