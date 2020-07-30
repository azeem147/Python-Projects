import smtplib  # the module for handling emails (simple mail transfer prog)
conn = smtplib.SMTP('smtp.gmail.com', 587)  # standard settings
conn.ehlo()  # responsible for starting the connection
conn.starttls()  # responsible for encrypting your password
# you need to see this https://support.google.com/accounts/answer/185833?hl=en
# to generate app specific password to make the script work
conn.login(Your Email, Your Password)  # (email, password)
# (from address, to address) I am sending email to myself for testing
# you need to format the body as per Python format
body = 'Subject: Testing..\n\nDear Azeem, \nTesting.\n\nRegards'
conn.sendmail('azm2006@gmail.com', 'azm2006@gmail.com', body)
conn.quit()
