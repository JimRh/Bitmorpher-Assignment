from ..models import User
from ..serializers import UserSerialziers
def userlist():

    userdata=User.objects.all()
    if not userdata:
        return "No user is found"
    res=UserSerialziers(userdata,many=True)
    return res.data
    