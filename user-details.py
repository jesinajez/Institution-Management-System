#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import design
a = design.funheader()
b = design.funmain()

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

print("""
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <link rel="stylesheet" href="design.html">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <style>
     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
      *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Poppins',sans-serif;
      }
      .containersss{
        height:calc(100vh - 220px);
        width:100%;
        }
      .container1{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        overflow: hidden;
        max-width: 1500px;
        width: 100%;
        background-color: #fff;
        padding: 25px 30px;
        border-radius: 5px;
        box-shadow: 0 5px 10px rgba(0,0,0,0.15);
      }
      .container1 .title{
        font-size: 25px;
        font-weight: 500;
        position: relative;
      }
      .container1 .title::before{
        content: "";
        position: absolute;
        left: 0;
        bottom: 0;
        height: 3px;
        width: 30px;
        border-radius: 5px;
        background: linear-gradient(135deg, #4db277, rgb(7, 88, 57));
      }
      .content form .user-details{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        margin: 20px 0 12px 0;
      }
      form .user-details .input-box{
        margin-bottom: 15px;
        width: calc(100% / 2 - 20px);
      }
      form .user-details .select-box{
        margin-bottom: 15px;
        width: calc(100% / 2 - 20px);
      }
      form .user-details .date-box{
        margin-bottom: 15px;
        width: calc(100% / 2 - 20px);
      }
      form .input-box span.details{
        display: block;
        font-weight: 500;
        margin-bottom: 5px;
      }
      form .select-box span.details{
        display: block;
        font-weight: 500;
        margin-bottom: 5px;
      }
      form .date-box span.details{
        display: block;
        font-weight: 500;
        margin-bottom: 5px;
      }
      .user-details .input-box input{
        height: 45px;
        width: 100%;
        outline: none;
        font-size: 16px;
        border-radius: 5px;
        padding-left: 15px;
        border: 1px solid #ccc;
        border-bottom-width: 2px;
        transition: all 0.3s ease;
      }
      .user-details .select-box select{
        height: 45px;
        width: 100%;
        outline: none;
        font-size: 16px;
        border-radius: 5px;
        padding-left: 15px;
        border: 1px solid #ccc;
        border-bottom-width: 2px;
        transition: all 0.3s ease;
      }
      .user-details .date-box input{
        height: 45px;
        width: 100%;
        outline: none;
        font-size: 16px;
        border-radius: 5px;
        padding-left: 15px;
        border: 1px solid #ccc;
        border-bottom-width: 2px;
        transition: all 0.3s ease;
      }

      .user-details .input-box input:focus,
      .user-details .input-box input:valid{
        border-color: rgb(103, 182, 89);
      }
      form .gender-details .gender-title{
        font-size: 20px;
        font-weight: 500;
      }
      form .category{
        display: flex;
        width: 80%;
        margin: 14px 0 ;
        justify-content: space-between;
      }
      form .category label{
        display: flex;
        align-items: center;
        cursor: pointer;
      }
      form .category label .dot{
        height: 18px;
        width: 18px;
        border-radius: 50%;
        margin-right: 10px;
        background: #d9d9d9;
        border: 5px solid transparent;
        transition: all 0.3s ease;
      }
      #dot-1:checked ~ .category label .one,
      #dot-2:checked ~ .category label .two,
      #dot-3:checked ~ .category label .three{
        background: #9b59b6;
        border-color: #d9d9d9;
      }
      form input[type="radio"]{
        display: none;
      }
      form .button{
        height: 45px;
        margin: 35px 0
      }
      form .button input{
        height: 100%;
        width: 100%;
        border-radius: 5px;
        border: none;
        color: #fff;
        font-size: 18px;
        font-weight: 500;
        letter-spacing: 1px;
        cursor: pointer;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #4db277, rgb(7, 88, 57));
      }
      form .button input:hover{
        /* transform: scale(0.99); */
        background: linear-gradient(-135deg, #63c98d, rgb(9, 143, 92));
        }
      @media(max-width: 584px){
      .container{
        max-width: 100%;
      }
      form .user-details .input-box{
          margin-bottom: 15px;
          width: 100%;
        }
        form .category{
          width: 100%;
        }
        .content form .user-details{
          max-height: 300px;
          overflow-y: scroll;
        }
        .user-details::-webkit-scrollbar{
          width: 5px;
        }
        }
        @media(max-width: 459px){
        .container .content .category{
          flex-direction: column;
        }
      }
     </style>
     </head>
    <body>
    <div class="containersss">
      <div class="container1">
        <div class="title">More Details</div>
        <div class="content">
          <form action="#" method="post">
            <div class="user-details">
              <div class="input-box">
                <span class="details">Full Name</span>
                <input type="text" placeholder="Enter your name" name="fname" required>
              </div>
              <div class="select-box">
                <span class="details">Qualification</span>
                <select id="qual" name="qual">
                  <option>Select</option>
                  <option value="Btech-IT">Btech IT</option>
                  <option value="Btech-CS">Btech CS</option>
                  <option value="Bsc-CS">BSc CS</option>
                  <option value="BCA">BCA</option>
                  <option value="Mtech-IT">Mtech IT</option>
                  <option value="Mtech-CS">Mtech CS</option>
                  <option value="MSc CS">MSc CS</option>
                  <option value="MCA">MCA</option>
              </select>
              </div>
              <div class="date-box">
                <span class="details">DOB</span>
                <input type="date" name="dob" required>
              </div>
              <div class="input-box">
                <span class="details">Phone Number</span>
                <input type="text" placeholder="Enter your number" name="phno" required>
              </div>
              <div class="input-box">
                <span class="details">Place</span>
                <input type="text" placeholder="Enter your place" name="place" required>
              </div>
              <div class="select-box">
                <span class="details">Programing Languages Known</span>
                <select id="language" name="language[]" multiple>
                  <option value="php">PHP</option>
                  <option value="java">Java</option>
                  <option value="ruby">Ruby</option>
                  <option value="c#">C#</option>
                  <option value="python">Python</option>
              </select>
              </div>
            </div>
            <div class="gender-details">
              <input type="radio" name="gender" id="dot-1" value="Male">
              <input type="radio" name="gender" id="dot-2" value="Female">
              <input type="radio" name="gender" id="dot-3" value="NotS">
              <span class="gender-title">Gender</span>
              <div class="category">
                <label for="dot-1">
                <span class="dot one"></span>
                <span class="gender">Male</span>
              </label>
              <label for="dot-2">
                <span class="dot two"></span>
                <span class="gender">Female</span>
              </label>
              <label for="dot-3">
                <span class="dot three"></span>
                <span class="gender">Prefer not to say</span>
                </label>
              </div>
              <input type="checkbox" name="check" id="agreeCheckbox">Please confirm that you are agreed to our <a href="#" style="text-decoration: none;">Tearms and Conditions</a>
            </div>
            <div class="button">
              <input type="submit" value="Register" name="sub">
            </div>
          </form>
        </div>
      </div>
      </div>
    </body>
    </html>
""")
f = cgi.FieldStorage()
pname = f.getvalue("fname")
pqual = f.getvalue("qual")
pdob = f.getvalue("dob")
ppno = f.getvalue("phno")
pplace = f.getvalue("place")
planguage = f.getlist("language[]")  # Use f.getlist() to get multiple selected values
if planguage:
    languages = ', '.join(planguage)
else:
    languages = ''

pgender = f.getvalue("gender")
pcheck = f.getvalue("check")
psub = f.getvalue("sub")
if psub != None:
    if pcheck != None:
        mail_id = cgi.FieldStorage()
        pmail = mail_id.getvalue("mail")
        # print(pmail)

        cur.execute("""insert into userdetails(Name, Email, Qualification, DOB, Phone, Place, Language_known, Gender, Status) values(
       '%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (pname, pmail, pqual, pdob, ppno, pplace, languages, pgender,"Pending"))

        # After inserting staff data, retrieve the last inserted EID
        cur.execute("SELECT LAST_INSERT_ID()")
        last_inserted_id = cur.fetchone()[0]

        # Generate the EID
        z = ""
        if last_inserted_id < 10:
            z = "000"
        elif last_inserted_id < 100:
            z = "00"
        elif last_inserted_id < 1000:
            z = "0"
        else:
            z = ""
        eid = "SWEIN" + z + str(last_inserted_id)

        # Update the row with the generated EID
        cur.execute("UPDATE userdetails SET EID = %s WHERE uno = %s", (eid, last_inserted_id))

        # Commit the changes to the database
        connection.commit()

        # Send email to the user
        g = cgi.FieldStorage()
        rmail = g.getvalue("mail")

        subject = "Your Registration Details"
        message = f"Dear {pname},\n\nThank you for registering! Your EID is: {eid}\n\nBest regards,\nYour Application Team"

        sender_email = "rose2010mary2000@gmail.com"  # password RoseMarry@2000
        sender_password = "dhba btkv cytg elyi"
        receiver_email = rmail

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
                alert("Success! Registration details sent to your email.");
                location.href="login.py";
            </script>
        """)
    else:
        print("""
            <script>
                    alert("please check the terms and conditions");
            </script>
        """)

connection.rollback()
c = design.funfooter()
