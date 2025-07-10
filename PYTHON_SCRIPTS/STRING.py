user_name = "Tarun"
country_code = "+91"
mobile_number = "1234567890"
City = "CH"

def mask_data():
    num = mobile_number[:2]+"******"+mobile_number[-2:]
    return num
print(mask_data())

message = "Your id : 132DSXCFED is been booked.Thank you so much for booking!"
extract = message.split(":")[1].split("is")[0].strip()
print("Extracted booking id : ",extract)

name = "jona sharon"
# for i in name.split():
#     v = i[0].upper()
#     print(v)

ext = " ".join([word[0].upper() for word in name.split()])
print(ext)

message_data = "Your id : 132DSXCFED  : been booked.Thank you so much for booking!"
ext2 = message_data.split(":")[1].split(":")[0].strip()
print(ext2)

class user_Data:
    def __init__(self,id,name,city,phNO):
        self.id = id
        self.name = name
        self.city = city
        self.phNO = phNO

    def print_all(self):
        print("-------user data---------")
        print(self.id,self.name,self.city,self.phNO)

    def masking(self):
        hide = self.phNO[:2]+"******"+self.phNO[-2:]
        return hide

    @staticmethod
    def common_welcom():
        print("welcome to dataGuy!")


user1 = user_Data("ZXCSDE","john","CH","1234567890")
user1.print_all()
print(user1.masking())
user1.common_welcom()
