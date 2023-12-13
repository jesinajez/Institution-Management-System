#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()

import footer

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

q1 = """select max(uno) from staff"""
cur.execute(q1)
r = cur.fetchone()
print(r[0])
if r[0] != None:
    n = r[0]
else:
    n = 0
z = ""
if n < 10:
    z = "000"
elif n < 100:
    z = "00"
elif n < 1000:
    z = "0"
else:
    z = ""
aid = "FWEIN"+z+str(n+1)
# print(aid)

print("""
<!DOCTYPE html>
    <html lang="en">

    <head>
      <meta charset="utf-8">
      <meta content="width=device-width, initial-scale=1.0" name="viewport">

      <title>WEIN SOFT</title>
      <meta content="" name="description">
      <meta content="" name="keywords">

      <!-- Favicons -->
      <link href="assets/img/wein.png" rel="icon">
      <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

      <!-- Google Fonts -->
      <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

      <!-- Vendor CSS Files -->
      <link href="assets/vendor/animate.css/animate.min.css" rel="stylesheet">
      <link href="assets/vendor/aos/aos.css" rel="stylesheet">
      <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
      <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
      <link href="assets/vendor/remixicon/remixicon.css" rel="stylesheet">
      <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

      <!-- Template Main CSS File -->
      <link href="assets/css/style.css" rel="stylesheet">
      
      <style>
     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
      *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Poppins',sans-serif;
      }
      .containersss{
        height:calc(100vh - 60px);
        width:100%;
        }
      .container1{
        position: absolute;
        top: 60%;
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
        width: 70%;
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
      #dot-2:checked ~ .category label .two{
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
    <!-- ======= Header ======= -->
      <header id="header" class="fixed-top">
        <div class="container d-flex align-items-center">

          <h1 class="logo me-auto"><a href="index1.html" style="text-decoration:none;">WEIN SOFT</a></h1>
          <!-- Uncomment below if you prefer to use an image logo -->
          <!-- <a href="index1.html" class="logo me-auto"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>-->

          <nav id="navbar" class="navbar order-last order-lg-0">
            <ul>
              <li><a class="active" href="dashboard-admin.py" style="text-decoration:none;">Home</a></li>
              <li><a href="index.html" style="text-decoration:none;">Signout</a></li>
            </ul>
            <i class="bi bi-list mobile-nav-toggle"></i>
          </nav><!-- .navbar -->
        </div>
        </header><!-- End Header -->
        """)
print(f"""
         <!-- ======= Main ======= -->
        <main id="main">
          <section id="admin-main" class="admin-main">
    <div class="containersss">
      <div class="container1">
        <div class="title">Teaching Staff</div>
        <div class="content">
          <form action="#" method="post">
            <div class="user-details">
            <div class="input-box">
                <span class="details">EID</span>
                <input type="text"  name="eid" value="{aid}" readonly>
              </div>
              <div class="input-box">
                <span class="details">Section</span>
                <input type="text" value="Trainer" name="trainer" readonly>
              </div>
              <div class="input-box">
                <span class="details">Full Name</span>
                <input type="text" placeholder="Enter your name" name="fname" required>
              </div>
              <div class="select-box">
                <span class="details">Qualification</span>
                <select id="qual" name="qual">
                  <option>Select</option>
                  <option value="Btech IT">Btech IT</option>
                  <option value="Btech CS">Btech CS</option>
                  <option value="Mtech IT">Mtech IT</option>
                  <option value="Mtech CS">Mtech CS</option>
                  <option value="MSc CS">MSc CS</option>
                  <option value="MSc IT">MSc IT</option>
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
              <div class="input-box">
                <span class="details">Email</span>
                <input type="text" placeholder="Enter your email" name="mail" required>
              </div>
              <div class="input-box">
                <span class="details">Password</span>
                <input type="password" placeholder="Enter password" name="pwd" required>
              </div>
              <div class="input-box">
                <span class="details">Conform Password</span>
                <input type="text" placeholder="Re-enter Password" name="cpwd" required>
              </div>
              <div class="select-box">
                <span class="details">Domain</span>
                <select id="domain" name="domain">
                  <option>Select</option>
                  <option value="web design">Website Design</option>
                  <option value="SEO">Search Engine Optimization</option>
                  <option value="Programming Language">Programming Languages</option>
              </select>
              </div>
              <div class="input-box">
                <span class="details">Salary(In Hours)</span>
                <input type="text" placeholder="Salary in hours" name="salary" required>
              </div>
            </div>
               <div class="button">
              <input type="submit" value="Submit" name="sub">
            </div>
          </form>
        </div>
      </div>
      </div>
      </section>
      </main>
    </body>
    </html>
""")
f = cgi.FieldStorage()
peid = f.getvalue("eid")
psection = "Trainer"
pname = f.getvalue("fname")
pqual = f.getvalue("qual")
pdob = f.getvalue("dob")
ppno = f.getvalue("phno")
pplace = f.getvalue("place")
pmail = f.getvalue("mail")
ppwd = f.getvalue("pwd")
pcpwd = f.getvalue("cpwd")
pdomain = f.getvalue("domain")
psalary = f.getvalue("salary")
pcheck = f.getvalue("check")
psub = f.getvalue("sub")
if psub != None:
        if ppwd == pcpwd:
                cur.execute("""insert into staff(EID, Section, Name, Qualification, DOB, Phone, Email, Password, Place, Department, Salary) values(
               '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %
                            (peid, psection, pname, pqual, pdob, ppno, pmail, ppwd, pplace, pdomain, psalary))

                cur.execute("""insert into faculty(EID, Section, Email, Password) values('%s','%s','%s','%s')""" % (peid, psection, pmail, ppwd))
                # Commit the changes to the database
                connection.commit()
                print("""
                <script>
                    alert("Success");
                    location.href="dashboard-admin.py";
                </script>
                """)
c = footer.funfooter()
