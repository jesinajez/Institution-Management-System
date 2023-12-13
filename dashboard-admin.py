#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()

import footer

connection = pymysql.connect(host="localhost", user="root", password="", database="weinsoft")
cur = connection.cursor()
cur.execute(""" select * from admin""")
f = cur.fetchone()
# print(f[1])

# Get the count of records with a "Pending" status
cur.execute("""SELECT COUNT(*) FROM userdetails WHERE Status='Pending'""")
pending_status_count = cur.fetchone()[0]

cur.execute("""select * from userdetails where Status='Pending'""")
g = cur.fetchall()


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
      *{
            box-sizing: border-box;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
        }
        body{
            font-family: Helvetica;
            -webkit-font-smoothing: antialiased;
            margin: 0;
        }
        h2{
            text-align: center;
            font-size: 18px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: white;
            padding: 30px 0;
        }
        
        /* Table Styles */
        
        .table-wrapper{
            margin: 10px 70px 70px;
            box-shadow: 0px 35px 50px rgba( 0, 0, 0, 0.2 );
        }
        
        .fl-table {
            border-radius: 5px;
            font-size: 12px;
            font-weight: normal;
            border: none;
            border-collapse: collapse;
            width: 100%;
            max-width: 100%;
            white-space: nowrap;
            background-color: white;
        }
        
        .fl-table td, .fl-table th {
            text-align: center;
            padding: 8px;
        }
        
        .fl-table td {
            border-right: 1px solid #f8f8f8;
            font-size: 12px;
        }
        
        .fl-table thead th {
            color: #ffffff;
            background: #4FC3A1;
        }
        
        
        .fl-table thead th:nth-child(odd) {
            color: #ffffff;
            background: #324960;
        }
        
        .fl-table tr:nth-child(even) {
            background: #F8F8F8;
        }
        
        /* Responsive */
        
        @media (max-width: 767px) {
            .fl-table {
                display: block;
                width: 100%;
            }
            .table-wrapper:before{
                content: "Scroll horizontally >";
                display: block;
                text-align: right;
                font-size: 11px;
                color: white;
                padding: 0 0 10px;
            }
            .fl-table thead, .fl-table tbody, .fl-table thead th {
                display: block;
            }
            .fl-table thead th:last-child{
                border-bottom: none;
            }
            .fl-table thead {
                float: left;
            }
            .fl-table tbody {
                width: auto;
                position: relative;
                overflow-x: auto;
            }
            .fl-table td, .fl-table th {
                padding: 20px .625em .625em .625em;
                height: 60px;
                vertical-align: middle;
                box-sizing: border-box;
                overflow-x: hidden;
                overflow-y: auto;
                width: 120px;
                font-size: 13px;
                text-overflow: ellipsis;
            }
            .fl-table thead th {
                text-align: left;
                border-bottom: 1px solid #f7f7f9;
            }
            .fl-table tbody tr {
                display: table-cell;
            }
            .fl-table tbody tr:nth-child(odd) {
                background: none;
            }
            .fl-table tr:nth-child(even) {
                background: transparent;
            }
            .fl-table tr td:nth-child(odd) {
                background: #F8F8F8;
                border-right: 1px solid #E6E4E4;
            }
            .fl-table tr td:nth-child(even) {
                border-right: 1px solid #E6E4E4;
            }
            .fl-table tbody td {
                display: block;
                text-align: center;
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
                      <li><a href="admin-trainer-details.py">Existing</a></li>
                    </ul>
                  </li>
                  <li class="dropdown"><a href="#"><span>Office Staff</span> <i class="bi bi-chevron-right"></i></a>
                    <ul>
                      <li><a href="admin-staff.py">New</a></li>
                      <li><a href="admin-staff-details.py">Existing</a></li>
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
                  <li><a href="admin-online-details.py">Existing</a></li>
                </ul>
              </li>
              <li class="dropdown"><a href="#"><span>Offline</span> <i class="bi bi-chevron-right"></i></a>
                <ul>
                  <li><a href="admin-offline.py">New</a></li>
                  <li><a href="admin-offline-details.py">Existing</a></li>
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
     """)
print(f"""
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
            <button type="button" class="btn btn-primary" onclick="toggleTable()">
              Notifications <span class="badge text-bg-danger">{pending_status_count}</span>
            </button>
      </div>
    </nav>

    <div class="home-content">
      <div class="overview-boxes">
        <div class="box">
          <div class="right-side">
            <div class="box-topic">Students</div>
            <div class="number">200</div>
            <div class="indicator">
              <i class='bx bx-up-arrow-alt'></i>
              <span class="text">Up to yesterday</span>
            </div>
          </div>
          <i class='bx bx-user-circle cart'></i>
        </div>
        <div class="box">
          <div class="right-side">
            <div class="box-topic">Staffs</div>
            <div class="number">50</div>
            <div class="indicator">
              <i class='bx bx-up-arrow-alt'></i>
              <span class="text">Up to yesterday</span>
            </div>
          </div>
          <i class='bx bxs-group cart two' ></i>
        </div>
        <div class="box">
          <div class="right-side">
            <div class="box-topic">Cources</div>
            <div class="number">50</div>
            <div class="indicator">
              <i class='bx bx-up-arrow-alt'></i>
              <span class="text">Up to yesterday</span>
            </div>
          </div>
          <i class='bx bx-code cart three' ></i>
        </div>
        <div class="box">
          <div class="right-side">
            <div class="box-topic">Placements Tie-up</div>
            <div class="number">150</div>
            <div class="indicator">
              <i class='bx bx-up-arrow-alt down'></i>
              <span class="text">Till Today</span>
            </div>
          </div>
          <i class='bx bxs-doughnut-chart cart four' ></i>
        </div>
      </div>

      <div class="sales-boxes">
        <div class="recent-sales box">
          <div class="title">Recently Placed Candidates</div>
          <div class="sales-details">
            <ul class="details">
              <li class="topic">Company</li>
              <li><a href="#" style="">Microsoft Corporation</a></li>
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
          <div class="title">Top Rating Cources</div>
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
            </div>""")
print(f"""
        <!-- ... (your existing Main and Section content) ... -->
    <!-- Table structure initially hidden -->
    <div id="pendingTable" class="table-wrapper" style="display: none;">
    <table class="fl-table">
        <thead>
          <tr>
            <th>EID</th>
            <th>Name</th>
            <th>Qualification</th>
            <th>DOB</th>
            <th>Phone</th>
            <th>Place</th>
            <th>Language Known</th>
            <th>Gender</th>
            <th>Status</th>
            <th>Approve</th>
          </tr>
        </thead>
""")
for r in g:
    print("""
        <tbody>
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <form method="post" action="admin-Approve.py">
                    <input type="hidden" name="funo" value="%s">
                    <input type="submit" name="sub" value="Approve">
                </form>
            </td>
        </tr>
    """ % (r[1], r[2], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[0]))
print("""
    </table>
    </div>
    </div>
    </section>
    </main>
    <script>
        function toggleTable() { 
            var pendingTable = document.getElementById("pendingTable");
            if (pendingTable.style.display === "none") {
                pendingTable.style.display = "block";
                location.href="#pendingTable";
            } else {
                pendingTable.style.display = "none";
            }
        }
    </script>
    </body>
    </html>
""")

foot = footer.funfooter()