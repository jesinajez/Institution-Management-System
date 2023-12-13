#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()

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
    <title>User Login</title>
    <link rel="stylesheet" href="design.html">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <style>
         @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        ::selection{
            background: #53d965;
            color: #fff;
        }
        .containersss{
            height:calc(100vh - 250px);
            width:100%;
        }
        .wrapper{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            overflow: hidden;
            max-width: 390px;
            background: #fff;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0px 15px 20px rgba(0,0,0,0.1);
        }
        .wrapper .title-text{
            display: flex;
            width: 200%;
        }
        .wrapper .title{
            width: 50%;
            font-size: 35px;
            font-weight: 600;
            text-align: center;
            transition: all 0.6s cubic-bezier(0.68,-0.55,0.265,1.55);
        }
        .wrapper .slide-controls{
            position: relative;
            display: flex;
            height: 50px;
            width: 100%;
            overflow: hidden;
            margin: 30px 0 10px 0;
            justify-content: space-between;
            border: 1px solid lightgrey;
            border-radius: 5px;
        }
        .slide-controls .slide{
            height: 100%;
            width: 100%;
            color: #fff;
            font-size: 18px;
            font-weight: 500;
            text-align: center;
            line-height: 48px;
            cursor: pointer;
            z-index: 1;
            transition: all 0.6s ease;
        }
        .slide-controls label.signup{
            color: #000;
        }
        .slide-controls .slider-tab{
            position: absolute;
            height: 100%;
            width: 50%;
            left: 0;
            z-index: 0;
            border-radius: 5px;
            background: -webkit-linear-gradient(left,  #5d7d61, #43e097);
            transition: all 0.6s cubic-bezier(0.68,-0.55,0.265,1.55);
        }
        input[type="radio"]{
            display: none;
        }
        #signup:checked ~ .slider-tab{
            left: 50%;
        }
        #signup:checked ~ label.signup{
            color: #fff;
            cursor: default;
            user-select: none;
        }
        #signup:checked ~ label.login{
            color: #000;
        }
        #login:checked ~ label.signup{
            color: #000;
        }
        #login:checked ~ label.login{
            cursor: default;
            user-select: none;
        }
        .wrapper .form-container{
            width: 100%;
            overflow: hidden;
        }
        .form-container .form-inner{
            display: flex;
            width: 200%;
        }
        .form-container .form-inner form{
            width: 50%;
            transition: all 0.6s cubic-bezier(0.68,-0.55,0.265,1.55);
        }
        .form-inner form .field{
            height: 50px;
            width: 100%;
            margin-top: 20px;
        }
        .form-inner form .field input{
            height: 100%;
            width: 100%;
            outline: none;
            padding-left: 15px;
            border-radius: 5px;
            border: 1px solid lightgrey;
            border-bottom-width: 2px;
            font-size: 17px;
            transition: all 0.3s ease;
        }
        .form-inner form .field input:focus{
            border-color: #028912;
            /* box-shadow: inset 0 0 3px #fb6aae; */
        }
        .form-inner form .field input::placeholder{
            color: #999;
            transition: all 0.3s ease;
        }
        form .field input:focus::placeholder{
            color: #b3b3b3;
        }
        .form-inner form .pass-link{
            margin-top: 5px;
        }
        .form-inner form .signup-link{
            text-align: center;
            margin-top: 30px;
        }
        .form-inner form .pass-link a,
        .form-inner form .signup-link a{
            color: #16a33e;
            text-decoration: none;
        }
        .form-inner form .pass-link a:hover,
        .form-inner form .signup-link a:hover{
            text-decoration: underline;
        }
        form .btn{
            height: 50px;
            width: 100%;
            border-radius: 5px;
            position: relative;
            overflow: hidden;
        }
        form .btn .btn-layer{
            height: 100%;
            width: 300%;
            position: absolute;
            left: -100%;
            background: -webkit-linear-gradient(right, #5d7d61, #43e097, #5d7d61, #43e097);
            border-radius: 5px;
            transition: all 0.4s ease;;
        }
        form .btn:hover .btn-layer{
            left: 0;
        }
        form .btn input[type="submit"]{
            height: 100%;
            width: 100%;
            z-index: 1;
            position: relative;
            background: none;
            border: none;
            color: #fff;
            padding-left: 0;
            border-radius: 5px;
            font-size: 20px;
            font-weight: 500;
            cursor: pointer;
        }
    </style>
    </head>
    <body>
    <div class="containersss">
         <div class="wrapper">
        <div class="title-text">
          <div class="title login">
            Login
          </div>
          <div class="title signup">
            Signup
          </div>
        </div>
        <div class="form-container">
          <div class="slide-controls">
            <input type="radio" name="slide" id="login" checked>
            <input type="radio" name="slide" id="signup">
            <label for="login" class="slide login">Login</label>
            <label for="signup" class="slide signup">Signup</label>
            <div class="slider-tab"></div>
          </div>
          <div class="form-inner">
            <form action="#" class="login" method="post">
              <div class="field">
                <input type="text" placeholder="Email Address" name="email" required>
              </div>
              <div class="field">
                <input type="password" placeholder="Password" name="pwd" required>
              </div>
              <div class="pass-link">
                <a href="forgot-password.py">Forgot password?</a>
              </div>
              <div class="field btn">
                <div class="btn-layer"></div>
                <input type="submit" value="Login" name="sub">
              </div>
              <div class="signup-link">
                Not a member? <a href="">Signup now</a>
              </div>
            </form>
            <form action="#" class="signup">
              <div class="field">
                <input type="text" placeholder="Email Address" name="smail" required>
              </div>
              <div class="field">
                <input type="password" placeholder="Password" name="spwd" required>
              </div>
              <div class="field">
                <input type="password" placeholder="Confirm password" name="scpwd" required>
              </div>
              <div class="field btn">
                <div class="btn-layer"></div>
                <input type="submit" value="Signup" name="subs">
              </div>
            </form>
          </div>
        </div>
        </div>
      </div>
      <script>
        const loginText = document.querySelector(".title-text .login");
        const loginForm = document.querySelector("form.login");
        const loginBtn = document.querySelector("label.login");
        const signupBtn = document.querySelector("label.signup");
        const signupLink = document.querySelector("form .signup-link a");
        signupBtn.onclick = (()=>{
        loginForm.style.marginLeft = "-50%";
        loginText.style.marginLeft = "-50%";
        });
        loginBtn.onclick = (()=>{
        loginForm.style.marginLeft = "0%";
        loginText.style.marginLeft = "0%";
        });
        signupLink.onclick = (()=>{
        signupBtn.click();
        return false;
        });
    </script>
    </body>
    </html>
""")

f = cgi.FieldStorage()
pmail = f.getvalue("email")
ppwd = f.getvalue("pwd")
psub = f.getvalue("sub")
if psub != None:
    if pmail != None:
        q = """select Email,Password from admin where Email='%s' and Password='%s'"""%(pmail,ppwd)
        cur.execute(q)
        r = cur.fetchone()
        # print(r)
        if r != None:
            print("""
            <script>
                location.href="dashboard-admin.py";
            </script>""")
        else:
            q1 = """SELECT u.uno, ud.EID, ud.Status
                   FROM user u
                   JOIN userdetails ud ON u.uno = ud.uno
                   WHERE u.Email = %s AND u.Password = %s"""
            cur.execute(q1, (pmail, ppwd))
            r1 = cur.fetchone()
            print("User Query Result:", r1)
            if r1!=None:
                if r1[2] == 'Approved':
                    print("""
                            <script>
                                location.href="dashboard-user.py?uno=%s&EID=%s";
                            </script>""" % (r1[0],r1[1]))
                else:
                    print("""
                            <script>
                                alert("Your account is not approved yet. Please wait for admin verification.");
                            </script>""")
            else:
                q2 = """select EID from faculty where Email='%s' and Password='%s'""" % (pmail, ppwd)
                cur.execute(q2)
                r2 = cur.fetchone()
                # print(r2)
                if r2 != None:
                    print("""
                            <script>
                                location.href="dashboard-staff.py?EID=%s";
                            </script>""" % r2[0])
                else:
                    print("""
                            <script>
                                alert("Incorrect login, please try another");
                            </script>""")

g = cgi.FieldStorage()
qmail = g.getvalue("smail")
qpwd = g.getvalue("spwd")
qcpwd = g.getvalue("scpwd")
qsub = g.getvalue("subs")
if qsub != None:
    import random

    otp = random.randint(0000, 9999)
    potp = str(otp)
    print(potp)

    if qpwd == qcpwd:
        # cur.execute("""insert into user(Email, Password) values('%s','%s')""" % (qmail, qpwd))
        # connection.commit()
        import smtplib

        fromaccount = "rose2010mary2000@gmail.com"  # password RoseMarry@2000
        password = "dhba btkv cytg elyi"
        toaccount = qmail
        msg = """
                This is your password reset OTP %s
                """ % (otp)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromaccount, password)
        server.sendmail(fromaccount, toaccount, msg)
        server.quit()
        print("""
                <script>
                alert("OTP send successfully..!");
                location.href="checkmail.py?otp=%s&mail=%s&pwd=%s";
                </script>
                """ % (otp,qmail,qpwd))

connection.commit()
connection.rollback()
c = design.funfooter()