#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

import cgi, cgitb

cgitb.enable()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

form_data = cgi.FieldStorage()
funo_values = form_data.getvalue("funo")
sub=form_data.getvalue("sub")
print(funo_values)

if sub!=None:

    cur.execute("""UPDATE userdetails SET Status='%s' WHERE uno=%s"""%("Approved",funo_values))
    connection.commit()

    cur.execute("SELECT Name, Email FROM userdetails WHERE uno=%s", (funo_values,))
    user_data = cur.fetchone()
    # Send email to the user
    if user_data:
        user_name = user_data[0]
        user_email = user_data[1]

        subject = "Registration verified"
        message = f"Dear {user_name},\n\nYour registration details are verified! You can come and join from today onwards.\n\nBest regards,\nWEIN SOFT"

        sender_email = "rose2010mary2000@gmail.com"  # password RoseMarry@2000
        sender_password = "dhba btkv cytg elyi"
        receiver_email = user_email

        # Configure the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Quit the server
        server.quit()

        print("""
                    <script>
                        alert("Success: Status updated, mail sent to user");
                        location.href="dashboard-admin.py";
                    </script>
                """)
    else:
        print("""
                    <script>
                        alert("Error: User details not found");
                        location.href="dashboard-admin.py";
                    </script>
                """)