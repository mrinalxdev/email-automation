import smtplib

def send_mail():
    server = smtplib.SMTP('smt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Set a Password in seperate txt file 
    with open('password.txt', 'r') as x:
        password = x.read()
    server.login('mrinalbitsat@gmail.com', password)
    subject = "Good morning from Mrinal!"
    with open('body.txt', 'r') as b:
        body = b.read()

    msg = f"subject:{subject} \n\n\n {body}"

    server.sendmail(
        'mrinalbitsat@gmail.com',
        'mrinaltennis005@gmail.com',
        msg
    )
    print('Message sent suceesfully')

if __name__ == "__main__":
    send_mail()