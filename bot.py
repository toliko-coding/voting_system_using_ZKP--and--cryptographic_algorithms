from twilio.rest import Client 
 

class bot():


    def __init__(self):
        self.account_sid = 'ACa174316e22a6e5596fc4e60a1183eb31' 
        self.auth_token = 'eaf74a6c5b1857e4ed489f23aa4acb7e' 
        self.client = Client(self.account_sid, self.auth_token) 
 
    def send(self,num,key):
        self.message = self.client.messages.create(  
                              messaging_service_sid='MG759c364d99538454e3a6b1a2c723d27d', 
                              body=str(key),      
                              to='+972'+num
                          ) 
 


#SID ACa174316e22a6e5596fc4e60a1183eb31
#eaf74a6c5b1857e4ed489f23aa4acb7e
#my new num : 14103481792