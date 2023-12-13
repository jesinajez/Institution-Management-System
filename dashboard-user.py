#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()

import footer

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()
h = cgi.FieldStorage()
id = h.getvalue("uno")
peid = h.getvalue("EID")
# print(id)
# print(peid)

a = """select * from userdetails where EID='%s'"""%(peid)
cur.execute(a)
f = cur.fetchall()
print(f, peid)

b = """select * from student where EID='%s'"""%(peid)
cur.execute(b)
g = cur.fetchall()
print(g)


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
""")
print("""
          <nav id="navbar" class="navbar order-last order-lg-0">
            <ul>
              <li><a class="active" href="dashboard-user.py" style="text-decoration:none;">Home</a></li>
              <li><a href="#" style="text-decoration:none;">Course Details</a></li>
              <li><a href="user-leave.py?EID=%s" style="text-decoration:none;">Leave</a></li>
              <li><a href="user-fees-payment.py?EID=%s" style="text-decoration:none;">Fees</a></li>
              <li><a href="#" style="text-decoration:none;">Assessments</a></li>
              <li><a href="index.html" style="text-decoration:none;">Signout</a></li>
            </ul>
"""%(peid,peid))
print("""
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
      <div class="d-flex justify-content-end">
        <button type="button" class="btn btn-primary">
            Notifications <span class="badge text-bg-danger">4</span>
        </button>
      </div>
    </nav>
""")
for r in f:
    print("""
        <div class="home-content">
          <div class="overview-boxes">
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Name</div>
                <div class="number">%s</div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Enrolment ID</div>
                <div class="number">%s</div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
            """%(r[2],r[1]))
for s in g:
    print("""
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Cource</div>
                <div style="font-size: 17px;"><b>%s</b></div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
            <div class="box">
              <div class="right-side">
                <div class="box-topic">Department</div>
                <div style="font-size: 17px;"><b>%s</b></div>
                <div class="indicator">
                  <span class="text">&nbsp;</span>
                </div>
              </div>
            </div>
          </div>
    """%(s[4],s[3]))
print("""
      <div class="sales-boxes">
        <div class="recent-sales box">
          <div class="title">Attendance</div>
          <div class="sales-details">
            <ul class="details">
              <li class="topic">Company</li>
              <li><a href="#">Microsoft Corporation</a></li>
              <li><a href="#">Accenture</a></li>
              <li><a href="#">Cognizant</a></li>
              <li><a href="#">Infosys</a></li>
              <li><a href="#">TCS</a></li>
              <li><a href="#">SAP</a></li>
              <li><a href="#">Capgemini</a></li>
              <li><a href="#">IBM</a></li>
              <li><a href="#">Oracle</a></li>
            </ul>
            <ul class="details">
            <li class="topic">Student</li>
            <li><a href="#">Alex Doe</a></li>
            <li><a href="#">David Mart</a></li>
            <li><a href="#">Roe Parter</a></li>
            <li><a href="#">Diana Penty</a></li>
            <li><a href="#">Martin Paw</a></li>
            <li><a href="#">Doe Alex</a></li>
            <li><a href="#">Aiana Lexa</a></li>
            <li><a href="#">Rexel Mags</a></li>
             <li><a href="#">Tiana Loths</a></li>
          </ul>
          <ul class="details">
            <li class="topic">Designation</li>
            <li><a href="#">Network architect</a></li>
            <li><a href="#">Systems analyst</a></li>
            <li><a href="#">IT coordinator</a></li>
            <li><a href="#">Network administrator</a></li>
            <li><a href="#">Network engineer</a></li>
            <li><a href="#">Service desk analyst</a></li>
            <li><a href="#">Sysadmin</a></li>
             <li><a href="#">Solutions architect</a></li>
            <li><a href="#">Technical architect</a></li>
          </ul>
          <ul class="details">
            <li class="topic">Package</li>
            <li><a href="#">$204.98</a></li>
            <li><a href="#">$244.55</a></li>
            <li><a href="#">$225.88</a></li>
            <li><a href="#">$170.66</a></li>
            <li><a href="#">$256.56</a></li>
            <li><a href="#">$144.95</a></li>
            <li><a href="#">$167.33</a></li>
             <li><a href="#">$223.53</a></li>
             <li><a href="#">$246.52</a></li>
          </ul>
          </div>
          <div class="button">
            <a href="#">See All</a>
          </div>
        </div>
        <div class="top-sales box">
          <div class="title">Performance</div>
          <ul class="top-sales-details">
            <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bxl-html5'></i>
              <span class="product">HTML 5</span>
            </a>
            <span class="price">1107</span>
          </li>
          <li>
            <a href="#">
               <i style="font-size: 32px;" class='bx bxl-python'></i>
              <span class="product">Python</span>
            </a>
            <span class="price">1567</span>
          </li>
          <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bxl-react'></i>
              <span class="product">React</span>
            </a>
            <span class="price">1234</span>
          </li>
          <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bxl-kubernetes'></i>
              <span class="product">Tailwind CSS</span>
            </a>
            <span class="price">2312</span>
          </li>
          <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bxl-bootstrap'></i>
              <span class="product">bootstrap</span>
            </a>
            <span class="price">1456</span>
          </li>
          <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bx-data'></i>
              <span class="product">Database</span>
            </a>
            <span class="price">2345</span>
          <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bxl-javascript' ></i>
              <span class="product">Javascript</span>
            </a>
            <span class="price">2345</span>
          </li>
          <li>
            <a href="#">
                <i style="font-size: 32px;" class='bx bxl-firebase'></i>
              <span class="product">Firebase</span>
            </a>
            <span class="price">1245</span>
          </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
            </main>
        </body>
        </html>
    """)

c = footer.funfooter()