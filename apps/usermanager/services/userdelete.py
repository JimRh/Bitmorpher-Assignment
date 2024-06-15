from ..models import User

def userdelete(name):
    
    userdata=User.objects.filter(username=name)
    if userdata:
        userdata.delete()
        return "user has been deleted"
    else:
        return "user doesn't exists"
    