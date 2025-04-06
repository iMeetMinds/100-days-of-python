import smtplib
import Dummy

my_email = Dummy.MY_EMAIL
my_pass = Dummy.MY_PASS

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user = my_email, password=my_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=Dummy.TO_EMAIL,
        msg='Subject:Hello\n\nThis is email from Python code')
