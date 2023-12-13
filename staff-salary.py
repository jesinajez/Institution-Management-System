#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()

import footer

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

f = cgi.FieldStorage()
peid = f.getvalue("EID")

q = """select * from salary where EID='%s'""" %peid
cur.execute(q)
r = cur.fetchall()

for i in r:
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
            * {
                box-sizing:border-box;
            }
            body {
                background-color:rgba(207, 211, 211, 0.5);
                font-family: Arial, Helvetica, sans-serif;
                color: rgb(114, 115, 115);
            }
            .salary{
                height: 700px;
                width: 100%;
            }
            form .container {
                border: 2px solid white;
                width: 500px;
                position: absolute;
                top: 90px;
                margin-left: 100px;
                padding: 16px;
                background-color: white;
                box-shadow: 10px;
                border-radius: 10px;
            }
            input[type=text] {
                width: 100%;
                padding: 15px;
                margin: 5px 0 22px 0;
                display: inline-block;
                border: none;
                background: #ebedf1;
                border-radius: 4px;
            }
            input[type=number] {
                width: 100%;
                padding: 15px;
                margin: 5px 0 22px 0;
                display: inline-block;
                border: none;
                background: #ebedf1;
                border-radius: 4px;
            }
            form .container2{
                position: absolute;
                margin-left: 750px;
                top: 100px;
            }
            .container2 input[type=number]{
              border-style: none;
              background-color: rgba(207, 211, 211, 0.1);
            }
            h1{
              color:black;
              text-align: center;
              font-family: "Poppins", sans-serif;
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
""")
print("""
              <li><a href="dashboard-staff.py?EID=%s" style="text-decoration:none;">Home</a></li>
              """%peid)
print("""
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
        <div class="salary">
            <form action="#" method="post" name="form-1">
              <div class="container">
    
                <label for="emp-id"><b>EMP ID &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department</b></label><br>
                <input type="text" value="{i[1]}" name="emp_id" id="emp_id" placeholder="EMP ID" style="width: 30%;" readonly>
                <input type="text" value="{i[2]}" placeholder="Department" name="dept" id="dept" style="width: 66%;" readonly><br>
                
                <label for="emp-id"><b>Working Days &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave Days</b></label><br>
                <input type="text" value="{i[4]}" name="working_days" id="working_days" placeholder="Working Days" style="width: 46%;" readonly>
                <input type="text" value="{i[5]}" placeholder="Leave Days" name="leave_days" id="leave_days" style="width: 50%;" readonly><br>
    
                <label for="basic"><b>Salary Month&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Basic Pay</b></label>
                <input type="text" value="{i[3]}" placeholder="Month" name="month" id="month" style="width: 46%;" readonly>
                
                <input type="number" value="{i[6]}" placeholder="Basic Salary" name="basic_salary" id="basic_salary" style="width: 50%;" readonly><br>
                
                
                <label for="house-rent"><b>House Rent Allowance&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Special Allowance</b></label>
                <input type="number" value="{i[7]}" placeholder="HR Allowance" name="hr_allowance" id="hr_allowance" style="width: 45%;" readonly>
                <input type="number" value="{i[8]}" placeholder="Special Allowance" name="special_allowance" id="special_allowance" style="width: 51%;" readonly><br>
    
                <label for="conveyance"><b>Conveyance Allowance&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Medical Allowance</b></label>
                <input type="number" value="{i[9]}" placeholder="Conveyance Allowance" name="conveyance_allowance" id="conveyance_allowance" style="width: 45%;" readonly>
                <input type="number" value="{i[10]}" placeholder="Medical Allowance" name="medical_allowance" id="medical_allowance" style="width: 51%;" readonly><br>
    
                <label for="gross"><b>Gross Salary</b></label>
                <input type="number" value="{i[11]}" placeholder="Gross Salary" name="gross_salary" id="gross_salary" readonly><br>
    
              </div>
             <div class="container2">
                <h1>Deductions</h1>
    
                <label for="epf"><b>EPF</b></label>
                <input type="number" value="{i[12]}" placeholder="EPF" name="epf" id="epf" readonly><br>
    
                <label for="health"><b>Health Insurance</b></label>
                <input type="number" value="{i[13]}" placeholder="Health Insurance" name="health_insurance" id="health_insurance" readonly><br>
    
                <label for="tax"><b>Professional Tax</b></label>
                <input type="number" value="{i[14]}" placeholder="Professional Tax" name="professional_tax" id="professional_tax" readonly><br>
    
                <label for="deduction"><b>Total Deduction</b></label>
                <input type="number" value="{i[15]}" placeholder="Total Deduction" name="total_deduction" id="total_deduction" readonly><br>
    
                <label for="net-pay" style="font-size: 30px; color:black;"><b>Net Pay</b></label>
                <input type="text" value="{i[16]}" name="net_pay" id="net_pay" style="font-size: 35px; text-align: center; font-family: 'Poppins', sans-serif;" readonly>
             </div>
            </form>
          </div>
          </section>
          </main>
    </body>
    </html>
""")

c = footer.funfooter()