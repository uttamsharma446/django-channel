import threading
from .models import *
from faker import Faker
fake = Faker()
import time
import random
from asgiref.sync import async_to_sync

class CreateStudentThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            channel_layer=get_channel_layer()
            current_total=0
            for i in range(self.total):
                current_total+=1
                print(f'We are inside first thread {i}')
                student_instance=Student.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    address=fake.address(),
                    age=random.randint(10,50)
                )
                data={"current_total":current_total,"total":self.total,'student_name':student_instance.name,'email':student_instance.email,"age":student_instance.age}
                print(data)
                async_to_sync(channel_layer.group_send)('new_consumer_group',{
                        'type':'send_notification',
                        'value':json.dumps(data)
                    })
                time.sleep(1)
        except Exception as e:
            print(e)
            
            
class AnotherThread(threading.Thread):
    
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)
    
    def run(self):
        try:
            for i in range(self.total):
                print(f'We are inside second thread {i}')
                time.sleep(1)

        except Exception as e:
            print(e)
        
        
    