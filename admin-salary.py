#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()

import footer

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

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
        height:calc(100vh - 220px);
        width:100%;
        }
      .container1{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        overflow: hidden;
        width: 100%;
        background-color: #fff;
        padding: 25px 30px;
        border-radius: 5px;
        box-shadow: 0 5px 10px rgba(0,0,0,0.15);
        display:flex;
        flex-direction:column;
        justify-content:center;
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
        display: grid;
        grid-template-columns:repeat(4,1fr);
        margin: 20px 0 12px 120px;
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
      .user-details .input-box input{
        height: 45px;
        width: 120%;
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
        width: 120%;
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
      form .category{
        display: flex;
        width: 40%;
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
      form .button{
        height: 45px;
        margin: 35px 200px;
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
          margin-bottom: 20px;
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
              <li class="dropdown"><a href="#"><span>Faculty</span> <i class="bi bi-chevron-down"></i></a>
                <ul>
                  <li class="dropdown"><a href="#"><span>Trainer</span> <i class="bi bi-chevron-right"></i></a>
                    <ul>
                      <li><a href="admin-trainers.py">New</a></li>
                      <li><a href="#">Existing</a></li>
                    </ul>
                  </li>
                  <li class="dropdown"><a href="#"><span>Office Staff</span> <i class="bi bi-chevron-right"></i></a>
                    <ul>
                      <li><a href="admin-staff.py">New</a></li>
                      <li><a href="#">Existing</a></li>
                    </ul>
                  </li>
                  <li><a href="admin-salary.py">Salary</a></li>
                </ul>
              </li>
              <li class="dropdown"><a href="#"><span>Student</span> <i class="bi bi-chevron-down"></i></a>
            <ul>
              <li class="dropdown"><a href="#"><span>Online</span> <i class="bi bi-chevron-right"></i></a>
                <ul>
                  <li><a href="admin-online.py">New</a></li>
                  <li><a href="#">Existing</a></li>
                </ul>
              </li>
              <li class="dropdown"><a href="#"><span>Offline</span> <i class="bi bi-chevron-right"></i></a>
                <ul>
                  <li><a href="admin-offline.py">New</a></li>
                  <li><a href="#">Existing</a></li>
                </ul>
              </li>
            </ul>
          </li>
              <li><a href="index.html" style="text-decoration:none;">Signout</a></li>
            </ul>
            <i class="bi bi-list mobile-nav-toggle"></i>
          </nav><!-- .navbar -->
        </div>
        </header><!-- End Header -->
        
         <!-- ======= Main ======= -->
        <main id="main">
          <section id="admin-main" class="admin-main">
    <div class="containersss">
      <div class="container1">
        <div class="title">Salary</div>
        <div class="content">
          <form action="#" method="post">
            <div class="user-details">
              <div class="input-box">
                <span class="details">Enrollment ID</span>
                <input type="text" placeholder="Enter staff ID" name="eid" required>
              </div>
              <div class="select-box">
                <span class="details">Department</span>
                <select id="dept" name="dept">
                  <option>Select</option>
                  <option value="Reception">Reception</option>
                  <option value="Administration">Administration</option>
                  <option value="Accounts">Accounts</option>
                  <option value="HR">HR</option>
                  <option value="Office Assistant">Office Assistant</option>
                  <option value="Manager">Manager</option>
                  <option value="Trainers">Trainers</option>
              </select>
              </div>
              <div class="select-box">
                <span class="details">Month</span>
                <select id="month" name="month">
                  <option>Select</option>
                  <option value="January">January</option>
                  <option value="February">February</option>
                  <option value="March">March</option>
                  <option value="April">April</option>
                  <option value="May">May</option>
                  <option value="June">June</option>
                  <option value="July">July</option>
                  <option value="August">August</option>
                  <option value="September">September</option>
                  <option value="October">October</option>
                  <option value="November">November</option>
                  <option value="December">December</option>
              </select>
              </div>
              <div class="input-box">
                <span class="details">Working Days</span>
                <input type="text" placeholder="No of working days" name="working" required>
              </div>
               <div class="input-box">
                <span class="details">Leave Days</span>
                <input type="text" placeholder="No of leave days" name="leave" required>
              </div>
              <div class="input-box">
                <span class="details">Basic Pay</span>
                <input type="text" placeholder="Basic Salary" name="basic" id="basic" required>
              </div>
              <div class="input-box">
                <span class="details">HR Allowance</span>
                <input type="text" placeholder="HR Allowance" name="house-rent" id="house-rent" required>
              </div>
              <div class="input-box">
                <span class="details">Special Allowance</span>
                <input type="text" placeholder="Special Allowance" name="special" id="special" required>
              </div>
              <div class="input-box">
                <span class="details">Conveyance Allowance</span>
                <input type="text" placeholder="Conveyance Allowance" name="conveyance" id="conveyance" required>
              </div>
              <div class="input-box">
                <span class="details">Medical Allowance</span>
                <input type="text" placeholder="Medical Allowance" name="medical" id="medical" onchange="funSalary()">
              </div>
              <div class="input-box">
                <span class="details">Gross Salary</span>
                <input type="text" placeholder="Gross Salary" name="gross" id="gross" readonly>
              </div>
              <div class="input-box">
                <span class="details">EPF</span>
                <input type="text" placeholder="EPF" name="epf" id="epf" required>
              </div>
              <div class="input-box">
                <span class="details">Health Insurance</span>
                <input type="text" placeholder="Health Insurance" name="health" id="health" required>
              </div>
              <div class="input-box">
                <span class="details">Professional Tax</span>
                <input type="text" placeholder="Professional Tax" name="tax" id="tax" onchange="netsalary()">
              </div>
              <div class="input-box">
                <span class="details">Total Deduction</span>
                 <input type="text" placeholder="Total Deduction" name="total" id="total" readonly>
              </div>
              <div class="input-box">
                <span class="details">Salary</span>
                <input type="text" placeholder="Salary" name="net-pay" id="net-pay" readonly>
              </div>
            </div>
            <div class="button">
              <input type="submit" value="Submit" name="sub">
            </div>
          </form>
        </div>
      </div>
      </div>
     <script>
        function funSalary(){
          let a,b,c,d,e,f;

            a=parseInt(document.getElementById("basic").value);
            b=parseInt(document.getElementById("house-rent").value);
            c=parseInt(document.getElementById("special").value);
            d=parseInt(document.getElementById("conveyance").value);
            e=parseInt(document.getElementById("medical").value);
            f=a+b+c+d+e;
            document.getElementById("gross").value=f;
        }
        function netsalary(){
          let g,h,i,f,t,n;

            g=parseInt(document.getElementById("epf").value);
            h=parseInt(document.getElementById("health").value);
            i=parseInt(document.getElementById("tax").value);
            f=parseInt(document.getElementById("gross").value);
            t=g+h+i;
            
            n=f-t;
            document.getElementById("total").value=t;
            document.getElementById("net-pay").value=n;
        }
      </script>
      </section>
      </main>
    </body>
    </html>
""")
f = cgi.FieldStorage()
peid = f.getvalue("eid")
pdept = f.getvalue("dept")
pmonth = f.getvalue("month")
pwork = f.getvalue("working")
pleave = f.getvalue("leave")
pbasic = f.getvalue("basic")
phr = f.getvalue("house-rent")
pspecial = f.getvalue("special")
pconveyance = f.getvalue("conveyance")
pmedical = f.getvalue("medical")
pgross = f.getvalue("gross")
pepf = f.getvalue("epf")
phealth = f.getvalue("health")
ptax = f.getvalue("tax")
ptotal = f.getvalue("total")
pnet = f.getvalue("net-pay")
psub = f.getvalue("sub")

if psub != None:
    cur.execute("""insert into salary(EID, Department, Sal_Month, Working, Absent, Basic, HR_Allowance, Sp_Allowance, 
    Con_Allowance, Med_Allowance, Gross, EPF, Insurance, Tax, Tot_Deduction, Salary) 
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                %(peid, pdept, pmonth, pwork, pleave, pbasic, phr, pspecial, pconveyance, pmedical, pgross, pepf, phealth, ptax, ptotal, pnet))
    connection.commit()
    print("""
        <script>
            alert("Success");
        </script>
        """)

c = footer.funfooter()

