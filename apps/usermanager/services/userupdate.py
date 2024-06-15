from ..models import User
from django.shortcuts import get_object_or_404

def userupdate(username, data):
  
    user = get_object_or_404(User, username=username)

    for key, value in data.items():
        if key == 'password':
            user.set_password(value)  
        else:
            setattr(user, key, value) 

    user.save()
    return {"status": "success", "message": "User updated successfully"}
    

    