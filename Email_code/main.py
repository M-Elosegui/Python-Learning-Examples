import smtplib

my_email = "multi.santiago@yahoo.com"
# my_pass="multi947211aa"
my_pass = "xocmxdtiifnweoce"


def send_email(message):

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        # this server is for yahoo only, check other providers
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mateuselosegui@gmail.com",
                            msg=f"subject:Warning! Intruder\n\n {message}")


send_email("Hello there! \n There is one intruder entering")