#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()

import footer

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()

g = cgi.FieldStorage()
peid = g.getvalue("EID")

a = """ select * from staff where EID='%s'"""%peid
cur.execute(a)
f = cur.fetchall()

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
      <link href="assets/css/adminstyle.css" rel="stylesheet">
      
      <style>
       .main{
            height: 500px;
            width: 1000px;
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
              
              <li><a class="active" href="dashboard-staff.py" style="text-decoration:none;">Home</a></li>
              """)
print("""
              <li><a href="staff-leave.py?EID=%s" style="text-decoration:none;">Leave</a></li> 
              <li><a href="staff-salary.py?EID=%s" style="text-decoration:none;">Salary</a></li>
              
            """%(peid, peid))
print("""
              <li><a href="index.html" style="text-decoration:none;">Signout</a></li>
            </ul>
            <i class="bi bi-list mobile-nav-toggle"></i>
          </nav><!-- .navbar -->
        </div>
        </header><!-- End Header -->
        
         <!-- ======= Main ======= -->
        <main id="main">
         <section class="home-section">
    <nav>
      <div class="sidebar-button">
        <i class='bx bx-menu sidebarBtn'></i>
        <span class="dashboard">Dashboard</span>
      </div>
      <div class="search-box">
        <input type="text" placeholder="Search...">
        <i class='bx bx-search' ></i>
      </div>
      
      </div>
    </nav>
    """)
for r in f:
    print(f"""
        <div class="home-content">
          <div class="overview-boxes">
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Name</div>
                <div class="number">{r[3]}</div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Enrolment ID</div>
                <div class="number">{r[1]}</div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Section</div>
                <div class="number">{r[2]}</div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Department</div>
                <div class="number">{r[10]}</div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
          </div>
            """)
print("""
      <div class="sales-boxes">
        <div class="recent-sales box">
          <div class="title">Schedule</div>
          <div class="sales-details">
            <ul class="details">
              <li class="topic">Day</li>
              <li><a href="#">Monday</a></li>
              <li><a href="#">Tuesday</a></li>
              <li><a href="#">Wednesday</a></li>
              <li><a href="#">Thursday</a></li>
              <li><a href="#">Friday</a></li>
              <li><a href="#">Saturday</a></li>
            </ul>
            <ul class="details">
            <li class="topic">Class</li>
            <li><a href="#">Blockchain</a></li>
            <li><a href="#">DevOps</a></li>
            <li><a href="#">Cybersecurity</a></li>
            <li><a href="#">AI</a></li>
            <li><a href="#">Machine Learning</a></li>
            <li><a href="#">Mobile SEO</a></li>
          </ul>
          <ul class="details">
            <li class="topic">Hour</li>
            <li><a href="#">5th Hour</a></li>
            <li><a href="#">4th Hour</a></li>
            <li><a href="#">1st Hour</a></li>
            <li><a href="#">2nd Hour</a></li>
            <li><a href="#">6th Hour</a></li>
            <li><a href="#">3rd Hour</a></li>
          </ul>
          <ul class="details">
            <li class="topic">Mode</li>
            <li><a href="#">Online</a></li>
            <li><a href="#">Online</a></li>
            <li><a href="#">Offline</a></li>
            <li><a href="#">Online</a></li>
            <li><a href="#">Offline</a></li>
            <li><a href="#">Offline</a></li>
          </ul>
          </div>
        </div>
""")
print("""
        <div class="top-sales box">
          <div class="title">Extras</div>
          <ul class="top-sales-details">
            <li>
            <a href="staff-assessment.py?EID=%s">
              <button type="button" class="btn">Assessment</button>
            </a>
          </li>
          <li>
           <a href="staff-student-attendance.py?EID=%s">
            <button type="button" class="btn">Attendance</button>
            </a>
          </li>
          """%(peid,peid))
print("""
          <li>
          <a href="staff-student-leave.py">
            <button type="button" class="btn">
                Leave Notifications <span class="badge text-bg-danger">4</span>
            </button>
            </a>
          </li>
          <li>
          <a href="#">
            <button type="button" class="btn">Class Activities</button>
            </a>
          </li>
          <li>
          <a href="#">
           <button type="button" class="btn">Lab Availability</button>
           </a>
          </li>
          
          </ul>
        </div>
      </div>
    </div>
  </section>
    </div>
    </main>
    </body>
    </html>
""")
c = footer.funfooter()