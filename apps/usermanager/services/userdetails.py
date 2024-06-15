from ..models import User
from ..serializers import UserSerialziers
def userdetails(name):

    userdata=User.objects.filter(username=name)
    if not userdata:
        return "User doesn't exist"
    res=UserSerialziers(userdata,many=True)
    return res.data
    