import random
import smtplib

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = "1234567890"
symbol = '-'
message = 'Your Plate Number'
p_number = "".join(random.sample(upper, 3 )) + "-" + "".join(random.sample(number, 3)) + "".join(random.sample(upper, 2))

upper = smtplib.SMTP('smtp.gmail.com', 587)
upper.starttls()

emailid = input("Enter your email: ")
upper.login("pjnumberreg@gmail.com", "yefwvxfmkadrhrdh")
upper.sendmail('&&&&&&',emailid, message)
emailid = input("Plate Number sent to your email")
print(p_number)