import os
import traceback
from  django.core.exceptions import ValidationError
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
from django import setup
setup()

from newapp.models import Person
try:
    p = Person(
        first_name='Taro', last_name='Sato1',
        birthday='2000-01-01', email='a@a.co.jp',
        salary=10000.0, memo='memo taro', web_site='http://www.aaa.co.jp'
    )
    print("aaaa_1")
    #Person.clean_fields(Person,exclude=['id','birthday','create_at','update_at','first_name','last_name','salary','memo','email','web_site'])
    Person.clean_fields(Person,exclude=['id','birthday','create_at','update_at','last_name','salary','memo','email','web_site'])
    print("aaaa_2")
    p.save()

except ValidationError as e:
    print("err")
    t = traceback.format_exc()
    print(t)
except:
    print("save err")
    t = traceback.format_exc()
    print(t)
