import pywhatkit

L=[]


def whatsapp_message():
    i = int(input("Enter the total number of contacts you want to send message : "))
    for i in range(0,i):
       count_code = input("Enter the country code (Start with +) : ")
       number = input("Enter the number you want to send message : ")
       m_no = count_code + number
       L.append(m_no)
    
    message = input("Enter the message you want to send : ")
    hour = int(input("Enter the time in hour : "))
    minute = int(input("Enter the time in minute : "))
    
    for k in range(0,len(L)):
        pywhatkit.sendwhatmsg(L[k],message,)
        print("Message Sent")
    

while True:
 whatsapp_message()
