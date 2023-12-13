#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi

import design
a = design.funheader()
b = design.funmain()

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

f = cgi.FieldStorage()
potp = f.getvalue("otp")
id = f.getvalue("uno")
pemail = f.getvalue("email")
print(potp)
print(id)
print(pemail)


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
        
        .button1 {
            background: -webkit-linear-gradient(right, #5d7d61, #43e097);
            color: white;
            padding: 14px 20px;
            margin: 8px 10px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            width: 50%;
        }
        
        .button1:hover {
            opacity: 0.8;
        }
    </style>
    </head>
    <body>
    <div class="containersss">
    <div class="wrapper">
        <div class="title-text">
          <div class="title login">
            Enter OTP
          </div>
        </div>
        <div class="form-container">
          
          <div class="form-inner">
            <form action="#" class="login" method="post">
              <div class="field">
                <input type="text" placeholder="Enter your OTP" name="otp" required>
              </div>
              
                <div style="display: flex; justify-content: center;">
                    <input type="submit" value="Validate" name="sub" class="button1">
              </div>
            </form>
          </div>
        </div>
      </div>
      </div>
</body>
</html>
""")
qotp=f.getvalue("otp")
psub=f.getvalue("sub")
if psub != None:
    if potp==qotp:
        print("""
            <script>
                alert("otp is correct");
                location.href="new-password.py?uno=%s&email=%s";
            </script>
        """ %(id,pemail))
    else:
        print("""
            <script>
                alert("Entered OTP is not correct....!");
            </script>
        """)
c = design.funfooter()
