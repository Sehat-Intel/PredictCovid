# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('tumin.sheth102987@marwadiuniversity.ac.in', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("tumin.sheth102987@marwadiuniversity.ac.in", "Koaw@2265GU") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("tumin.sheth102987@marwadiuniversity.ac.in", "t.sheth33@gmail.com", message) 
  
# terminating the session 
s.quit() 