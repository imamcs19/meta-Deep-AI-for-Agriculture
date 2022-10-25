# 
# By: Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | Filkom UB
# Big Thanks to All Teams :D

from flask import Flask,render_template, Response, redirect,url_for,session,request,jsonify
from flask import json, make_response, render_template_string
import sqlite3
from flask_cors import CORS

from flask import send_file
from flask_qrcode import QRcode

from requests.packages.urllib3.exceptions import ProtocolError
from collections import OrderedDict
from operator import itemgetter
from textblob import TextBlob

from tweepy.streaming import StreamListener

import tweepy
import re
import string
import datetime
import joblib
from flask import send_file
from io import BytesIO

from flask_wtf.file import FileField
from wtforms import SubmitField
from flask_wtf import FlaskForm

# import json
import os

# # untuk CronJob
# from apscheduler.schedulers.background import BackgroundScheduler
from flask_crontab import Crontab

from flask_gtts import gtts

# from flask_app import static

# untuk sqlite admin
# from flask_sqlite_admin.core import sqliteAdminBlueprint, required_roles

app = Flask(__name__, static_folder='static')
crontab = Crontab(app)
gtts(app)
qrcode = QRcode(app)

# sqliteAdminBP = sqliteAdminBlueprint(
#   dbPath = 'data.db',
#   decorator = required_roles('admin', 'user')
# )
# app.register_blueprint(sqliteAdminBP, url_prefix='/sql')

# Ref:
# Big Thanks to,
# https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5
# https://github.com/piinalpin/absent-qrcode-python
# ==============================================================
#

# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "static/qr_app/db/database.db"))

# app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# DB kedua untuk qr_app :D
db_qr = SQLAlchemy(app)
migrate = Migrate(app, db_qr)

# Operasi untuk migrate
# flask db_qr init
# flask db_qr migrate
# flask db_qr upgrade



# from static.qr_app.controller.AppController import *

# from static.qr_app import qr_app
# from static.qr_app import app

# from static.qr_app.model.StudentModel import Student
# from static.qr_app.model.AttendanceModel import Attendance
from static.qr_app.model.StudentModel import Student
from static.qr_app.model.AttendanceModel import Attendance

# static/qr_app/module/Camera.py
# from static.qr_app.module.Camera import Scanner
from static.qr_app.module.Camera import Scanner

import pyqrcode
import uuid


# CORS(app)
CORS(app, resources=r'/api/*')
# CORS(app, resources=r'/*')
# CORS(app)

# app.debug = False
app.secret_key = 'fga^&&*(&^(filkom#BJH#G#VB#Big99nDatakPyICS_ap938255bnUB'

# app.secret_key = secrets.token_bytes(32) # used to cryptographically sign session cookies

# keterangan:
# "#" adalah untuk comment
# <br> adalah new line
# &nbsp; adalah spasi
# <!-- --> atau <!--- ---> adalah untuk comment

# FrameWeb_atas & FrameWeb_bawah untuk dekorasi web
# agar menjadi Web yang Responsif

FrameWeb_atas = """
{% extends "extends/base.html" %}
{% block title %}
    <title>Web App MatKom Dgn Python</title>
{% endblock title %}
{{ self.title() }}
    Home
{{ self.title() }}
<button onclick="window.location.href='/'" class="btn btn-outline btn-rounded btn-info">
    <i class="ti-arrow-left m-l-5"></i>
    <span>Back Home</span>
</button> Project 1

{{ self.title() }}
    Project 1

{% block content %}
"""
A_a = FrameWeb_atas

FrameWeb_bawah = """
{% endblock content %}
"""
Z_z = FrameWeb_bawah

FrameWeb_atas_no_frame = """
{% extends "extends/base_no_frame.html" %}
{% block title %}
    <title>Web App MatKom Dgn Python</title>
{% endblock title %}
{{ self.title() }}
    Home
{{ self.title() }}
<button onclick="window.location.href='/'" class="btn btn-outline btn-rounded btn-info">
    <i class="ti-arrow-left m-l-5"></i>
    <span>Back Home</span>
</button> Project 1

{{ self.title() }}
    Project 1

{% block content %}
"""


A_a_no_frame = FrameWeb_atas_no_frame
Z_z_no_frame = FrameWeb_bawah

@app.route('/tts')
def tts():
    return render_template('gtts.html')

@app.route('/db/<aksi>')
def manipulate_tabel(aksi):
    conn = connect_db()
    db = conn.cursor()

    # buat tabel data_cronjob

    # Tipe Run => menit, jam, harian
    # Date Pembuatan => Date
    # Sintaks Cron Job => python /homw/../iot_api.py
    # Keterangan
    # Date Masa Berlaku
    # Aksi => Edit, Hapus, Play, Extenf Date Berlaku

    # db.execute("DROP TABLE IF EXISTS '" + DATABASE_TABLE + "'");

    if aksi == 'c':
        str_info = 'tabel berhasil dibuat :D'
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS data_cronjob
        (tipe_run TEXT, date_pembuatan DATETIME,
        teks_call_sintaks TEXT,
        keterangan TEXT,
        date_masa_berlaku DATETIME)
        """)
    elif aksi== 'd':
        str_info = 'tabel berhasil dihapus :D'
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS data_cronjob
        """)

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air/<aksi>')
def manipulate_tabel_CloundAI_Air(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air_Rev/<aksi>')
def manipulate_tabel_CloundAI_Air_Rev(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air_Rev (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air_Rev
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/job', methods = ['POST', 'GET'])
def get_time():
    from datetime import datetime
    # from time import strftime
    import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))
    Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%dT%H:%M'))

    # time_req = request.args.get("html_time")
    # format_time = datetime.strptime(time_req, "%Y-%m-%dT%H:%M")

    # minute = format_time.minute
    # hour = format_time.hour
    # day = format_time.day
    # month = format_time.month

    # crontab.job(minute=minute, hour=hour, day=day, month=month)(exe_control)

    # return render_template('myjob.html', time_req=time_req)
    # return str(time_req)

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        time_req = request.form['html_time'] # time data '2022-08-09' does not match format '%Y-%m-%dT%H:%M'
        # format_time = datetime.strptime(time_req, "%Y-%m-%dT%H:%M")

        # ValueError: time data '10-08-2022 08:32:26' does not match format '%Y-%m-%dT%H:%M'

        format_time = datetime.strptime(Date, "%Y-%m-%dT%H:%M")

        minute = format_time.minute
        hour = format_time.hour
        day = format_time.day
        month = format_time.month

        # crontab.job(minute=minute, hour=hour, day=day, month=month)(exe_control)
        crontab.job(minute="1")(exe_control)

        # return str(time_req)
        return render_template('mycronjob.html', time_req=time_req)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add3
        return render_template('mycronjob.html')

# - without decorator -
def exe_control():
    # return 'run job'
    import requests
    from datetime import datetime
    import pytz
    Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    # simpan ke db
    conn = connect_db()
    db = conn.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS data_suhu_dll (date DATETIME, kota TEXT, suhu_dlm_celcius TEXT, precipitation_curah_hujan_dlm_persen TEXT, humidity_kelembaban_dlm_persen TEXT, wind_angin_dlm_km_per_jam TEXT) """)

    list_kota = ['Jakarta','Los Angeles','Chicago','New York City','Toronto','São Paulo', \
                 'Lagos', 'London', 'Johannesburg', 'Kairo', 'Paris', 'Zurich', 'Istanbul', 'Moskwa', 'Dubai', \
                'Mumbai','Hong Kong','Shanghai','Singapura','Tokyo','Sydney']


    for nama_kota in list_kota:

    #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
      each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
      resp=requests.get(each_list_link)

      # print(nama_kota)

      #http_respone 200 means OK status
      if resp.status_code==200:
          resp=resp.json()
          suhu = resp['current']['temp_c']
          curah_hujan = resp['current']['precip_mm']
          lembab = resp['current']['humidity']
          angin = resp['current']['wind_mph']
      else:
          # print("Error")
          suhu = '-'
          curah_hujan = '-'
          lembab = '-'
          angin = '-'

      print(nama_kota, 'dengan suhu = ', round(float(suhu),2),'°C', end='\n')

      db.execute("""INSERT INTO data_suhu_dll (date, kota, suhu_dlm_celcius, precipitation_curah_hujan_dlm_persen, humidity_kelembaban_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?,?,?,?,?,?) """,(Date,nama_kota,suhu,curah_hujan,lembab,angin))


    conn.commit()
    db.close()
    conn.close()

@app.route('/job2', methods = ['POST', 'GET'])
def get_job2():
    from datetime import datetime
    # from time import strftime
    import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))
    Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%dT%H:%M'))

    # time_req = request.args.get("html_time")
    # format_time = datetime.strptime(time_req, "%Y-%m-%dT%H:%M")

    # minute = format_time.minute
    # hour = format_time.hour
    # day = format_time.day
    # month = format_time.month

    # crontab.job(minute=minute, hour=hour, day=day, month=month)(exe_control)

    # return render_template('myjob.html', time_req=time_req)
    # return str(time_req)

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        time_req = request.form['html_time'] # time data '2022-08-09' does not match format '%Y-%m-%dT%H:%M'
        # format_time = datetime.strptime(time_req, "%Y-%m-%dT%H:%M")

        # ValueError: time data '10-08-2022 08:32:26' does not match format '%Y-%m-%dT%H:%M'

        format_time = datetime.strptime(Date, "%Y-%m-%dT%H:%M")

        minute = format_time.minute
        hour = format_time.hour
        day = format_time.day
        month = format_time.month

        # crontab.job(minute=minute, hour=hour, day=day, month=month)(exe_control)
        crontab.job(minute="1")(exe_control)

        # return str(time_req)
        return render_template('mycronjob2.html', time_req=time_req)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add3
        return render_template('mycronjob2.html')

@app.route('/user')
def data_user():
    try:
        conn = connect_db()
        db = conn.cursor()

        rs = db.execute("SELECT * FROM user order by id")
        userslist = rs.fetchall()
        return render_template('data_user.html',userslist=userslist)

    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

@app.route("/update_user",methods=["POST","GET"])
def update_user():
    try:
        conn = connect_db()
        db = conn.cursor()
        if request.method == 'POST':
            field = request.form['field']
            value = request.form['value']
            editid = request.form['id']

            if field == 'mail':
                db.execute("""UPDATE user SET Mail=? WHERE id=?""",(value,editid))
            if field == 'name':
                db.execute("""UPDATE user SET Name=? WHERE id=?""",(value,editid))
            if field == 'pwd':
                db.execute("""UPDATE user SET Password=? WHERE id=?""",(value,editid))
            if field == 'level':
                db.execute("""UPDATE user SET Level=? WHERE id=?""",(value,editid))

            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

# # Inisialisasi variabel scheduler untuk CronJob
# sched = BackgroundScheduler(daemon = True)
# sched.start()

# # Mendefinisikan suatu fungsi cronjob untuk run todo dalam Flask app
# @sched.scheduled_job(trigger = 'cron', minute = '*')
# def print_hello():
#     print('Hello world!')

# # Defining a single API endpoint
# @app.route('/test')
# def test_func():
#     js = json.dumps({'Test': 'Successful!'})
#     return Response(json.dumps(js), status = 200, mimetype = 'application/json')

############ Flask routes general: ############

# ================ awal - dasar ke-2 ===============
#

# buat input dari url, untuk penjumlahan misal 2 bilangan
@app.route('/add/<a>/<b>')
def add_ab(a,b):
    c = int(a) + float(b)
    return 'a + b = ' + str(c)
    # return 'a + b = %s' % c
# https://bigdatafga.pythonanywhere.com/add/1/2.5
# hasil => a + b = 3.5

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return kode html dalam flask python Web App
@app.route('/post_add2', methods=["POST", "GET"])
def inputkan_ab():
    # membuat penjumlahan 2 bilangan

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return '''
        <html>
            <head>
            </head>
            <body>
              <form method="post">
                <input type="text" name="a" value="%s" />
                <input type="text" name="b" value="%s" />
                <input type="submit" value="Hitung a + b"/>

              </form>
              <h2>Hasil a + b = %s + %s = %s </h2>
            </body>
        </html>
        ''' % (a_in, b_in, a_in, b_in, c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add2
        return '''
            <html>
                <head>
                </head>
                <body>
                  <form action="/post_add2" method="post">
                    Masukkan nilai a = <input type="text" name="a" value="" />
                    <br>
                    Masukkan nilai b = <input type="text" name="b" value="" />
                    <input type="submit" value="Hitung a + b"/>
                  </form>
                </body>
            </html>
        '''

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return file "form_add3.html" dalam folder "mysite/templates", flask python Web App
@app.route('/post_add3', methods=["POST", "GET"])
def inputkan_ab3():
    # membuat penjumlahan 2 bilangan
    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return render_template('form_add3.html', a_save = a_in, b_save = b_in, c_save = c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add3
        return render_template('form_add3.html')


# ================================================================================
# Untuk mengakselerasi pengerjaan sebagian FP ke-1 dan FP ke-2, berikut:
#
# Contoh koding dasar operasi CRUD pada tabel CloudAI_Air,
# mulai dari "def dasar2_create_database():" sampai sebelum "# ================ akhir - dasar ke-2 ==============="
#
#
# Contoh koding dasar Run isi kode iot_api.py,
# @app.route('/dasar2_add2')
#
# Jangan lupa menambahkan "from flask import render_template_string" pada bagian atas flask_app.py
#
# ==============================================================
#
# membuat render_template_string sebagai pengganti render_template
# agar semua kodenya hanya dalam 1 file, sehingga lebih mudah untuk membuat dan run kodingnya
#
# Ref: https://stackoverflow.com/questions/67429333/flask-how-to-update-information-on-sqlite-based-on-button-input
# Remodified by Imam Cholissodin
#
# untuk Pengmas 2022 | membuat tabel CloudAI_Air untuk Penentuan Durasi Pengairan / Penyiraman Tanaman
# dengan menggunakan KNN & Fuzzy Mamdani dalam Ekosistem Cloud-AI
#
def dasar2_create_database():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
                """)

    conn.commit()
    conn.close()

def dasar2_generate_data():
    """Generate sintesis atau dummy data untuk percontohan."""
    conn = connect_db()
    cur = conn.cursor()

    # start - insert where tabel CloudAI_Air masih kosong
    # cur.execute('SELECT * FROM CloudAI_Air WHERE (Col1=? AND Col2=? AND Col3=?)', ('a', 'b', 'c'))
    cur.execute('SELECT * FROM CloudAI_Air')
    entry = cur.fetchone()

    # rs = db.execute("SELECT * FROM user order by id")
    # datalist = rs.fetchall()

    # if entry is None:
    #     for i in range(1, 11):
    #     cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
    #                 (f"Suhu {i}", f"Kelembaban {i}", f"Hujan {i}", f"Angin {i}", f"Durasi {i}"))

    if entry is None:
        import numpy as np
        import pandas as pd
        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        # Misal skema dataset-nya seperti berikut: => Silahkan dimodifikasi sesuai case Anda
        kolomFitur_X_plus_Target_Y = ['Suhu (X1)','Kelembaban (X2)', 'Curah Hujan (X3)','Angin (X4)','Durasi Air Dlm Menit (Y)']

        # set bykData = 3*np.power(10,7)
        bykData = 10
        bykFitur = len(kolomFitur_X_plus_Target_Y)-1

        # Interval atau Variasi nilai fitur
        nilaiFitur_Suhu = [17,35]
        nilaiFitur_Kelembaban = [70,90]
        nilaiFitur_Curah_Hujan = [2,95]
        nilaiFitur_Angin = [0,15]
        labelTargetY = [0.0,90.0]

        # generate isi dataset
        content_dataGenerate = np.array([np.arange(bykData)]*(bykFitur+1)).T
        df_gen = pd.DataFrame(content_dataGenerate, columns=kolomFitur_X_plus_Target_Y)

        df_gen ['Suhu (X1)'] = np.random.randint(nilaiFitur_Suhu[0], nilaiFitur_Suhu[1], df_gen.shape[0])
        df_gen ['Kelembaban (X2)'] = np.random.randint(nilaiFitur_Kelembaban[0], nilaiFitur_Kelembaban[1], df_gen.shape[0])
        df_gen ['Curah Hujan (X3)'] = np.random.randint(nilaiFitur_Curah_Hujan[0], nilaiFitur_Curah_Hujan[1], df_gen.shape[0])
        df_gen ['Angin (X4)'] = np.random.randint(nilaiFitur_Angin[0], nilaiFitur_Angin[1], df_gen.shape[0])
        df_gen ['Durasi Air Dlm Menit (Y)'] = np.round(np.random.uniform(labelTargetY[0], labelTargetY[1], df_gen.shape[0]),2)

        # save dataframe generate ke *.csv
        import os
        # print(os.path.expanduser("~"))
        userhome = os.path.expanduser("~").split("/")[-1]
        # print(userhome)

        # file_name_data_generate = '/home/bigdatafga/mysite/static/data_contoh/Data_CloudAI_Air.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)

        path = "/home/"+userhome+"/mysite/static/data_contoh"
        if not os.path.exists(path):
            os.makedirs(path)
        # file_name_data_generate = 'static/data_contoh/Data_CloudAI_Air.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)
        url_file_name_data_generate = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")
        df_gen.to_csv(url_file_name_data_generate, encoding='utf-8', index=False)

        # read file *.csv dan tampilkan
        # data_generate = pd.read_csv(file_name_data_generate)

        url = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")

        # Importing the dataset => ganti sesuai dengan case yg anda usulkan
        dataset = pd.read_csv(url)
        # X = dataset.iloc[:, :-1].values
        # y = dataset.iloc[:, 1].values

        def pushCSVdatasetToDB(x1,x2,x3,x4,y):
            #inserting values inside the created table
            # db = sqlite3.connect("data.db")

            # conn = connect_db()
            # cur = conn.cursor()

            cmd = "INSERT INTO CloudAI_Air(suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES('{}','{}','{}','{}','{}')".format(x1,x2,x3,x4,y)
            cur.execute(cmd)
            conn.commit()

        # CSV_to_SQLite3 dari file dataset
        for i in range(0,len(dataset)):
            pushCSVdatasetToDB(dataset.iloc[i][0],dataset.iloc[i][1],dataset.iloc[i][2],dataset.iloc[i][3],dataset.iloc[i][4])

        # for i in range(1, 11):
        #     cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
        #             (f"Type {i}", f"Receipt {i}", f"Amount {i}", f"Description {i}"))
    else:
        ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'
        print(ket_hasil)

    # end - insert where tabel CloudAI_Air masih kosong

    # # Misal skema dataset-nya seperti berikut: => Silahkan dimodifikasi sesuai case Anda
    # kolomFitur_X_plus_Target_Y = ['Jenis Aktifitas (X1)','Pola Hidup (X2)', 'Olah Raga (08.00-09.30) dalam menit (X3)','Target Rating Imun (Y)']

    # # Interval atau Variasi nilai fitur
    # nilaiFitur_Jenis_Aktifitas = ['Ringan','Sedang']
    # nilaiFitur_Pola_Hidup = ['Cukup Sehat','Sehat','Sangat Sehat']
    # nilaiFitur_Waktu_Olah_Raga = [15,45]
    # labelTargetY = [1.0,5.0]

    # # set bykData = 3*np.power(10,7)
    # bykData = 10
    # bykFitur = len(kolomFitur_X_plus_Target_Y)-1

    # print('Banyak Data = ', bykData)
    # print('Banyak Fitur = ', bykFitur)

    # # generate isi dataset
    # content_dataGenerate = np.array([np.arange(bykData)]*(bykFitur+1)).T
    # df_gen = pd.DataFrame(content_dataGenerate, columns=kolomFitur_X_plus_Target_Y)

    # # set secara random nilai Fitur untuk generate data
    # df_gen ['Jenis Aktifitas (X1)'] = np.random.choice(nilaiFitur_Jenis_Aktifitas, df_gen.shape[0])
    # df_gen ['Pola Hidup (X2)'] = np.random.choice(nilaiFitur_Pola_Hidup, df_gen.shape[0])
    # df_gen ['Olah Raga (08.00-09.30) dalam menit (X3)'] = np.random.randint(nilaiFitur_Waktu_Olah_Raga[0], nilaiFitur_Waktu_Olah_Raga[1], df_gen.shape[0])
    # df_gen ['Target Rating Imun (Y)'] = np.random.uniform(labelTargetY[0], labelTargetY[1], df_gen.shape[0])

    # # save dataframe generate ke *.csv
    # file_name_data_generate = 'Data_Generate_Reg.csv'
    # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)

    # # read file *.csv dan tampilkan
    # data_generate = pd.read_csv(file_name_data_generate)

    # # Menampilkan data
    # print('\nMenampilkan hasil generate dataset:')
    # display(data_generate)


    conn.commit()
    cur.close()
    conn.close()

@app.route('/dasar2_crud')
def dasar2_index():
    return '<a href="/dasar2_list">Demo Menampilkan List dari Tabel + Support => Create, Read, Update, Delete (CRUD)</a>'

@app.route('/dasar2_list')
def dasar2_list():

    # buat tabel dan generate data dummy
    dasar2_create_database()
    dasar2_generate_data()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM CloudAI_Air")
    rows = cur.fetchall()

    conn.close()

    #return render_template("list.html", rows=rows)
    return render_template_string(template_list, rows=rows)


@app.route('/dasar2_edit/<int:number>', methods=['GET', 'POST'])
def dasar2_edit(number):
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        # suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit

        cur.execute("UPDATE CloudAI_Air SET suhu_dlm_celcius = ?, humidity_kelembaban_dlm_persen = ?, precipitation_curah_hujan_dlm_persen = ?, wind_angin_dlm_km_per_jam = ?, durasi_air_dlm_menit = ? WHERE id = ?",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi, item_id))
        conn.commit()

        return redirect('/dasar2_list')

    cur.execute("SELECT * FROM CloudAI_Air WHERE id = ?", (number,))
    item = cur.fetchone()

    conn.close()

    #return render_template("edit.html", item=item)
    return render_template_string(template_edit, item=item)

@app.route('/dasar2_delete/<int:number>')
def dasar2_delete(number):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM CloudAI_Air WHERE id = ?", (number,))

    conn.commit()
    conn.close()

    return redirect('/dasar2_list')

@app.route('/dasar2_add', methods=['GET', 'POST'])
def dasar2_add():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        # item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi))
        conn.commit()

        return redirect('/dasar2_list')

    #return render_template("add.html", item=item)
    return render_template_string(template_add)

@app.route('/dasar2_add2')
def dasar2_add2():
    conn = connect_db()
    cur = conn.cursor()

    # get data dari iot API
    import requests
    # from datetime import datetime
    # import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    # list_kota = ['Jakarta','Los Angeles','Chicago','New York City','Toronto','São Paulo', \
    #              'Lagos', 'London', 'Johannesburg', 'Kairo', 'Paris', 'Zurich', 'Istanbul', 'Moskwa', 'Dubai', \
    #             'Mumbai','Hong Kong','Shanghai','Singapura','Tokyo','Sydney']
    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)

        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error")
            suhu = '-'
            curah_hujan = '-'
            lembab = '-'
            angin = '-'

        # print(nama_kota, 'dengan suhu = ', round(float(suhu),2),'°C', end='\n')

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
                (suhu, lembab, curah_hujan, angin))

        conn.commit()
        cur.close()
        conn.close()

    return redirect('/dasar2_list')

template_list = """
<h2>Menampilkan Data CloudAI Air + Support Create, Read, Update, delete (CRUD)</h2>
<a href="{{ url_for( "dasar2_add" ) }}">Tambah Data</a> |
<a href="{{ url_for( "dasar2_add2" ) }}">Tambah Data dari iot_api (tanpa nilai Durasi Waktu)</a>
{% if rows %}
<table border="1">
    <thead>
        <td>No</td>
        <td>Suhu (°C)</td>
        <td>Kelembaban (%)</td>
        <td>Curah Hujan (%)</td>
        <td>Kecepatan Angin (Km/Jam)</td>
        <td>Durasi Waktu Pengairan / Penyiraman (Menit)</td>
    </thead>

    {% for row in rows %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
        <td>
            <a href="{{ url_for( "dasar2_edit", number=row[0] ) }}">Edit</a> |
            <a href="{{ url_for( "dasar2_delete", number=row[0] ) }}">Hapus</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% else %}
Empty</br>
{% endif %}
"""

template_add = """
<h1>Tambah Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_add" ) }}">
    Suhu: <input name="suhu" value=""/></br>
    Kelembaban: <input name="kelembaban" value=""/></br>
    Curah Hujan: <input name="hujan" value=""/></br>
    Kecepatan Angin: <input name="angin" value=""/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value=""/></br>
    <button>Simpan Data</button></br>
</form>
"""

template_edit = """
<h1>Edit Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_edit", number=item[0] ) }}">
    Suhu: <input name="suhu" value="{{item[1]}}"/></br>
    Kelembaban: <input name="kelembaban" value="{{item[2]}}"/></br>
    Curah Hujan: <input name="hujan" value="{{item[3]}}"/></br>
    Kecepatan Angin: <input name="angin" value="{{item[4]}}"/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value="{{item[5]}}"/></br>
    <button>Simpan Update Data</button></br>
</form>
"""

# ================ akhir - dasar ke-2 ===============

# ================ awal - dasar ke-1 ===============
# #
# @app.route('/')
# def hello_world():
#     return 'Hello Big Data Using Python from Flask - FGA x Cisco Academy 2022 x Filkom UB!'

# @app.route('/add')
# def add():
#     # membuat penjumlahan 2 bilangan
#     a = 10
#     b = 90
#     c = a + b

#     return str(c)

# # buatlah halaman perkalian
# # antara a*b
# @app.route('/kali')
# def kali():
#     # membuat perkalian 2 bilangan
#     a = 10
#     b = 90
#     c = a * b

#     return str(c)

# # buatlah tampilan indeks looping 1..10
# @app.route('/loop')
# def loop():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '  '

#     return str(c)

# # buatlah tampilan indeks looping 1..10 dengan new line (<br> dari tag html)
# @app.route('/loop_new_line')
# def loop_new_line():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '<br>'

#     return str(c)

# # buatlah tampilan indeks looping 1 sampai 10
# # yang ganjil
# @app.route('/ganjil')
# def ganjil():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         if((i+1)%2!=0):
#             c +=str(i+1) + '  '

#     return str(c)
# # ================ akhir - dasar ke-1 ===============

# ========= untuk Project =================

# @app.route("/")
# def index():
#     return render_template("index.html")
#     return 'Hello FGA Big Data Using Python - Filkom UB 2022 :D'

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login",methods=["GET", "POST"])
def login():
  conn = connect_db()
  db = conn.cursor()
  msg = ""
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]

      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")

      conn.commit()

      hasil = []
      for v_login in rs:
          hasil.append(v_login)

      if hasil:
          session['name'] = v_login[3]
          return redirect(url_for("contohfp2_nonspark"))
      else:
          msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  conn = connect_db()
  db = conn.cursor()
  if request.method == "POST":
      mail = request.form['mail']
      uname = request.form['uname']
      passw = request.form['passw']

      cmd = "insert into user(Mail, Password,Name,Level) values('{}','{}','{}','{}')".format(mail,passw,uname,'1')
      conn.execute(cmd)
      conn.commit()

      # conn = db

      return redirect(url_for("login"))
  return render_template("register.html")

@app.route("/bli", methods=["GET", "POST"])
def bli():
  conn = connect_db()
  db = conn.cursor()

  return render_template("bli.html")

@app.route("/biz", methods=["GET", "POST"])
def biz():
  conn = connect_db()
  db = conn.cursor()

  return render_template("biz.html")


@app.route("/contohfp2_nonspark", methods=["GET", "POST"])
def contohfp2_nonspark():
  # Simple Linear Regression / Klasifikasi / Clustering
  # Importing the libraries
  import numpy as np
  # import matplotlib.pyplot as plt
  import pandas as pd
  import os.path

  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  url = os.path.join(BASE_DIR, "static/data_contoh/Salary_Data.csv")

  # Importing the dataset => ganti sesuai dengan case yg anda usulkan
  # a. Min. 30 Data dari case data simulasi dari yg Anda usulkan
  # b. Min. 30 Data dari real case, sesuai dgn yg Anda usulkan dari tugas minggu ke-3 (dari Kaggle/UCI Repository)
  # url = "./Salary_Data.csv"
  dataset = pd.read_csv(url)
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, 1].values

#   Hasil_str_X = ' '.join(str(x_loop) for x_loop in y)

#   return Hasil_str_X

  # Splitting the dataset into the Training set and Test set
  # Lib-nya selain sklearn/ Tensorflow/ Keras/ PyTorch/ etc
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

  # Hitung Mape
  # from sklearn.metrics import mean_absolute_percentage_error

  # Feature Scaling
  """from sklearn.preprocessing import StandardScaler
  sc_X = StandardScaler()
  X_train = sc_X.fit_transform(X_train)
  X_test = sc_X.transform(X_test)
  sc_y = StandardScaler()
  y_train = sc_y.fit_transform(y_train)"""

  # Fitting Simple Linear Regression to the Training set
  from sklearn.linear_model import LinearRegression
  regressor = LinearRegression()
  myModelReg = regressor.fit(X_train, y_train)

  # Simpan hasil model fit
  with open(os.path.join(BASE_DIR, "static/simpan_model_data/myModelReg.joblib.pkl"), 'wb') as f:
    joblib.dump(myModelReg, f, compress=9)

  # Load hasil model fit
  with open(os.path.join(BASE_DIR, "static/simpan_model_data/myModelReg.joblib.pkl"), 'rb') as f:
    myModelReg_load = joblib.load(f)

  # Predicting the Test set results
  #y_pred = regressor.predict(X_test)
  #y_pred2 = regressor.predict(X_train)

  y_pred = myModelReg_load.predict(X_test)
  y_pred2 = myModelReg_load.predict(X_train)

  # Visualising the Training set results
  # plt.scatter(X_train, y_train, color = 'red')
  # plt.plot(X_train, regressor.predict(X_train), color = 'blue')


  # Visualising the Test set results
  # plt.scatter(X_test, y_test, color = 'red')
  # plt.plot(X_train, regressor.predict(X_train), color = 'blue')
  # plt.title('Salary vs Experience (Test set)')
  # plt.xlabel('Years of Experience')
  # plt.ylabel('Salary')
  # plt.show()

  aktual, predict = y_train, y_pred2
  mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)

  # return render_template('MybigdataApps.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)
  return render_template('MybigdataAppsNonPySpark.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)

@app.route("/fp2_regresi", methods=["GET", "POST"])
def fp2_regresi():
  # Importing the libraries
  import numpy as np
  import pandas as pd
  import os.path

  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  url = os.path.join(BASE_DIR, "static/data_contoh/data_suhu_iot_all.csv")

  # Importing the dataset
  dataset = pd.read_csv(url)
  #X = dataset.iloc[:, :-1].values # mengambil data mulai dari date sampai humidity_kelembaban_dlm_persen
  #X = dataset.iloc[:, :-2].values # mengambil data mulai dari date sampai precipitation_curah_hujan_dlm_persen
  #X = dataset.iloc[:, :-3].values # mengambil data mulai dari date sampai suhu_dlm_celcius

  # dhea
  indeks_awal_kolom = 2
  indeks_batas_kolom = -3

  X = dataset.iloc[:, indeks_awal_kolom:indeks_batas_kolom].values # mengambil hanya data suhu_dlm_celcius (x)
  y = np.array(dataset.iloc[:, 4:-1].values).flatten()

#   Hasil_str_X = ' '.join(str(x_loop) for x_loop in y)

#   return Hasil_str_X

  # Splitting the dataset into the Training set and Test set
  # Lib-nya selain sklearn/ Tensorflow/ Keras/ PyTorch/ etc
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


  # Fitting Simple Linear Regression to the Training set
  from sklearn.linear_model import LinearRegression
  regressor = LinearRegression()
  myModelReg = regressor.fit(X_train, y_train)

#   # Simpan hasil model fit
#   with open(os.path.join(BASE_DIR, "static/simpan_model_data/myModelReg.joblib.pkl"), 'wb') as f:
#     joblib.dump(myModelReg, f, compress=9)

#   # Load hasil model fit
#   with open(os.path.join(BASE_DIR, "static/simpan_model_data/myModelReg.joblib.pkl"), 'rb') as f:
#     myModelReg_load = joblib.load(f)

#   y_pred = myModelReg_load.predict(X_test)
#   y_pred2 = myModelReg_load.predict(X_train)

  y_pred = myModelReg.predict(X_test)
  y_pred2 = myModelReg.predict(X_train)

  aktual, predict = y_train, y_pred2
  mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)
  # untuk mape bisa diganti dengan MAE atau dengan RMSE atau MSE atau lainnya

  return render_template('MybigdataAppsReg.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)

@app.route("/contohfp2_spark", methods=["GET", "POST"])
def contohfp2_spark():
  # MLLIB dari Pyspark Simple Linear Regression /Klasifikasi / Clustering
  # Importing the libraries
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import os

  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  url = os.path.join(BASE_DIR, "static/data_contoh/Salary_Data.csv")

  import findspark
  findspark.init()

  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName("Linear Regression").config("spark.executor.memory", "256m").getOrCreate()

  from pyspark.ml.regression import LinearRegression
  from pyspark.ml.linalg import Vectors
  from pyspark.ml.feature import VectorAssembler
  from pyspark.ml.feature import IndexToString, StringIndexer
  from pyspark.ml import Pipeline, PipelineModel

  from pyspark import SQLContext, SparkConf, SparkContext
  from pyspark.sql import SparkSession
  #sc = SparkContext.getOrCreate()
  sc = spark.sparkContext
  if (sc is None):
      #sc = SparkContext(master="local[*]", appName="Linear Regression")

      spark = SparkSession.\
        builder.\
        appName("Linear Regression").\
        master("local[*]").\
        config("spark.executor.memory", "256m").\
        getOrCreate()

      sc = spark.sparkContext

      # ------------------
  spark = SparkSession(sparkContext=sc)
  # sqlcontext = SQLContext(sc)

  # Importing the dataset => ganti sesuai dengan case yg anda usulkan
  # a. Min. 30 Data dari case data simulasi dari yg Anda usulkan
  # b. Min. 30 Data dari real case, sesuai dgn yg Anda usulkan dari tugas minggu ke-3 (dari Kaggle/UCI Repository)
  # url = "./Salary_Data.csv"

  sqlcontext = SQLContext(sc)
  data = sqlcontext.read.csv(url, header = True, inferSchema = True)

  #from pyspark.ml.feature import VectorAssembler
  # mendifinisikan Salary sebagai variabel label/predictor
  dataset = data.select(data.YearsExperience, data.Salary.alias('label'))
  # split data menjadi 70% training and 30% testing
  training, test = dataset.randomSplit([0.7, 0.3], seed = 100)
  # mengubah fitur menjadi vektor
  assembler = VectorAssembler().setInputCols(['YearsExperience',]).setOutputCol('features')
  trainingSet = assembler.transform(training)
  # memilih kolom yang akan di vektorisasi
  trainingSet = trainingSet.select("features","label")

  #from pyspark.ml.regression import LinearRegression
  # fit data training ke model
  lr = LinearRegression()
  lr_Model = lr.fit(trainingSet)

  # Simpan hasil model fit
  #import tempfile
  #path = tempfile.mkdtemp()
  #path = os.path.join(BASE_DIR, "myModel_Spark")
  path_myModel_Spark = os.path.join(BASE_DIR, "myModel_Spark")
  #lr_Model.write.save(os.path.join(BASE_DIR, "myModelReg_Spark"))
  #lr_Model.save(spark, path_myModel_Spark)
  #lr_Model.save(path_myModel_Spark)
  lr_Model.write().overwrite().save(path_myModel_Spark)
  #write().overwrite().save(path_myModel_Spark)

  #save(sc, path)

  # Load hasil model fit
  #myModelReg_Spark_load = PipelineModel.load(os.path.join(BASE_DIR, "myModelReg_Spark"))
  #myModelReg_Spark_load = lr.load(spark, path_myModel_Spark)
  myModelReg_Spark_load = lr.load(path_myModel_Spark)


  # assembler : fitur menjadi vektor
  testSet = assembler.transform(test)
  # memilih kolom fitur dan label
  testSet = testSet.select("features", "label")

  # fit testing data ke model linear regression
  #testSet = lr_Model.transform(testSet)
  testSet = myModelReg_Spark_load.transform(testSet)

  # testSet.show(truncate=False)

  from pyspark.ml.evaluation import RegressionEvaluator
  evaluator = RegressionEvaluator()
  # print(evaluator.evaluate(testSet, {evaluator.metricName: "r2"}))

  y_pred2 = testSet.select("prediction")
  # y_pred2.show()


  return render_template('MybigdataAppsPySpark.html', y_aktual = y_pred2.rdd.flatMap(lambda x: x).collect(), y_prediksi = y_pred2.rdd.flatMap(lambda x: x).collect(), mape = evaluator.evaluate(testSet, {evaluator.metricName: "r2"}))

@app.route("/bigdataApps", methods=["GET", "POST"])
def bigdataApps():
  if request.method == 'POST':
    import pandas as pd
    import numpy as np
    import os.path

    #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #url = os.path.join(BASE_DIR, "dataset_dump.csv")

    dataset = request.files['inputDataset']
    # url = "./dataset_dump.csv"

    persentase_data_training = 90
    banyak_fitur = int(request.form['banyakFitur'])
    banyak_hidden_neuron = int(request.form['banyakHiddenNeuron'])
    dataset = pd.read_csv(dataset, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    # dataset = pd.read_csv(url, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    # dataset = dataset.fillna(method='ffill')
    minimum = int(dataset.min()-10000)
    maksimum = int(dataset.max()+10000)
    new_banyak_fitur = banyak_fitur + 1
    hasil_fitur = []
    for i in range((len(dataset)-new_banyak_fitur)+1):
      kolom = []
      j = i
      while j < (i+new_banyak_fitur):
        kolom.append(dataset.values[j][0])
        j += 1
      hasil_fitur.append(kolom)
    hasil_fitur = np.array(hasil_fitur)
    data_normalisasi = (hasil_fitur - minimum)/(maksimum - minimum)
    data_training = data_normalisasi[:int(persentase_data_training*len(data_normalisasi)/100)]
    data_testing = data_normalisasi[int(persentase_data_training*len(data_normalisasi)/100):]

    #Training
    bobot = np.random.rand(banyak_hidden_neuron, banyak_fitur)
    bias = np.random.rand(banyak_hidden_neuron)
    h = 1/(1 + np.exp(-(np.dot(data_training[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    h_plus = np.dot(np.linalg.inv(np.dot(np.transpose(h),h)),np.transpose(h))
    output_weight = np.dot(h_plus, data_training[:, banyak_fitur])

    #Testing
    h = 1/(1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    predict = np.dot(h, output_weight)
    predict = predict * (maksimum - minimum) + minimum

    #MAPE
    aktual = np.array(hasil_fitur[int(persentase_data_training*len(data_normalisasi)/100):, banyak_fitur])
    mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)

    print("predict = ", predict)
    print("aktual =", aktual)
    print("mape = ", mape)

    # return render_template('bigdataApps.html', data = {'y_aktual' : list(aktual),'y_prediksi' : list(predict),'mape' : mape})
    return render_template('bigdataApps.html', y_aktual = list(aktual), y_prediksi = list(predict), mape = mape)


    # return "Big Data Apps " + str(persentase_data_training) + " banyak_fitur = " + str(banyak_fitur) + " banyak_hidden_neuron = " + str(banyak_hidden_neuron) + " :D"
  else:
    return render_template('bigdataApps.html')

def connect_db():
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data.db")
    # with sqlite3.connect(db_path) as db:

    return sqlite3.connect(db_path)

#konversi Seq object menjadi array int [a-z], misal menjadi [1-26] => next untuk bahan optimasi penskalaan
def seq2val_space_plus_arr_a_z(seq_):
    #get unik kode atau simbol IUPAC utk nucleotides
    # print(set(seq_.lower()))
    # {'N', 'G', 't', 'M', 'C', 'A', 'g', 'T', 'c', 'R', 'a'}
    # ['n', 'g', 't', 'm', 'c', 'a', 'g', 't', 'c', 'r', 'a']
    # {'a', 'c', 'g', 'm', 'n', 'r', 't'}

    # konversi setiap char kodenya menjadi angka, misal a = 1, c = 2, g = 3, t = 4
    # Di mana konversi ini nantinya dapat juga dicari nilai yang optimal
    seq_ = str(seq_).lower()

    for idx_letter in range(26):
        seq_= seq_.replace(chr(idx_letter+97),str(idx_letter)+" ")

    val_seq_ = seq_.rstrip()
    # print(val_seq_)

    # upper() sequence
    # up_seq_ = seq_.upper()
    # print(up_seq_)

    arr_val_seq_ = np.fromstring(val_seq_,dtype=int,sep=' ')

    return arr_val_seq_

## untuk trendTwit
## mencoba streaming
class StreamListener(tweepy.StreamListener):
    def __init__(self, start_time):
        """
        Initalizes a StreamListener object.
        start_time: the time the stream was connected
        tweets: a dictionary to store processed tweets and their polarity
        """
        tweepy.StreamListener.__init__(self)
        self.start_time = start_time
        self.tweets = {}

    def on_status(self, status):
        """
        Function called when the stream gets connected. Filters the tweets by user and language.
        If 30 seconds have passed since the stream was connected, returns False so stream can disconnect.
        """
        if filter_users.add_user(status) and status.lang == "en":
            self.process_tweet(status)

        #we want to collect tweets every 30 seconds so we set an internal timer inside the class
        if datetime.datetime.now() <= self.start_time + datetime.timedelta(seconds=30):
            return True

        return False

    def process_tweet(self, status):
        """
        Links, mentions, "RT"s, emojis, and stopwords are removed from the tweet. Sentiment anlaysis is performed and
        the clean tweet (sans stopwords) and analysis result is stored in the tweets dict.

        status: a status object

        """
        #remove links, mentions, "RT"s, emojis, non-ascii chars from the tweet
        clean_tweet = re.sub(r"([^\w]?:\@|https?\://)\S+", "", status.text)
        clean_tweet = re.sub(r'[^\x00-\x7F]+'," ", clean_tweet)

        clean_tweet = clean_tweet.replace("RT ", "")

        #remove numbers and punctuation
        translator = str.maketrans("", "", string.punctuation + string.digits)
        clean_tweet = clean_tweet.translate(translator)


        clean_tweet = clean_tweet.lower()

        #https://stackoverflow.com/questions/2400504/easiest-way-to-replace-a-string-using-a-dictionary-of-replacements/2400577#2400577
        slang = re.compile(r'\b(' + '|'.join(settings.SLANG_DICT.keys()) + r')\b')
        clean_tweet = slang.sub(lambda x: settings.SLANG_DICT[x.group()], clean_tweet)
        ####

        polarity = StreamListener.get_polarity(clean_tweet)

        #remove stopwords(using the custom stopwords list in settings.py) to get most important words
        important_words = " ".join([word for word in clean_tweet.split() if word not in settings.STOPWORDS_SET])

        #add the processed tweet into the tweets list
        self.tweets[important_words] = polarity

    @staticmethod
    def get_polarity(tweet):
        """
        Determines the polarity of the tweet using TextBlob.

        tweet: a partially processed tweet (still has stopwords)
        return: int polarity -> 1 if positive, 0 if neutral, -1 if negative

        """

        text_blob = TextBlob(tweet)

        tweet_polarity_float = text_blob.sentiment.polarity

        #greater than 0.05 ->  positive, less than -0.05 -> negative, else neutral
        if tweet_polarity_float >= 0.05:
            polarity = 1
        elif tweet_polarity_float <= -0.05:
            polarity = -1
        else:
            polarity = 0

        return polarity


    def get_tweets(self):
        """
        Returns a copy of the tweets dictionary.
        """
        return self.tweets.copy()

    def on_error(self, status_code):
        """
        Handles errors coming from the Twitter API. If being rate limited,
        Twitter will send a 420 status code and we will disconnect.

        """
        if status_code == 420:
            return False


class SortData(object):
    data = {}

    def __init__(self, tweets):
        """
        Initializes a SortData object.
        tweets: a dictionary of processed tweets and their polarity
        """
        self.tweets = tweets

    def calculate_frequencies(self):
        """
        Calculates the frequencies of the words in processed tweets
        and creates the data dictionary. A key value pair for the dictionary
        will have the word as the key and a list as its value. The list will include
        the number of times the word has occurred in all the tweets seen so far and
        another list including the number of positive, neutral, and negative tweets
        containing that word.

        """
        #key value pair for the data dictionary -> word:[count, [numPositiveTweets, numNeutralTweets, numNegativeTweets]]

        for tweet, polarity in self.tweets.items():
            for word in tweet.split():
                if word not in self.data:

                    self.data[word] = [0, [0, 0, 0]]

                    self.data[word][0] = 1

                    self.update_polarity_frequency(word, polarity)

                else:
                    self.data[word][0] += 1

                    self.update_polarity_frequency(word, polarity)


    def update_polarity_frequency(self, word, polarity):
        """
        Determines what polarity (positive, neutral, negative) the tweet has
        according to the tweets dictionary and updates the value in the data dictionary.

        """
        if polarity == 1:
            self.data[word][1][0] += 1
        elif polarity == 0:
            self.data[word][1][1] += 1
        else:
            self.data[word][1][2] += 1


    def get_most_common_words(self):
        """
        Removes all the words in the data dictionary that have occurred
        less than two times in all the tweets seen so far. Sorts the data
        dictionary by frequency of the words in descending order.

        return: a JSON object version of the sorted dictionary

        """
        self.calculate_frequencies()

        data_copy = self.data.copy()

        for word in data_copy:
             if self.data[word][0] <= 2:
                 del self.data[word]

        sorted_words = OrderedDict(sorted(self.data.items(), key = itemgetter(1), reverse = True))

        #make sure the dictionary is less than or equal to 15 words so ajax request in javascript
        #doesn't slow down
        while len(sorted_words) >= 15:
            sorted_words.popitem()
        return json.dumps(sorted_words)

def event_stream():
    """
    Connects the stream, sorts and processes the data, and creates
    a dictionary of the most common words found.

    return: a JSON object containing the most common words found in the tweets sample
            and their frequencies and polarity data

    """
    try:
        stream_listener = StreamListener(datetime.datetime.now())
        # stream = tweepy.Stream(auth = api.auth, listener = stream_listener)
        stream = tweepy.Stream(auth, listener = stream_listener)

        # # receive tweets on assigned tracks,
        # # filter them by assigned conditions and send them to port
        # twitter_stream = Stream(auth, Listener(c_socket, api))
        # # twitter_stream.filter(lang=["en"],track=tracks)
        # twitter_stream.filter(track=tracks,languages=["id","en"])

        #we want a lot of tweets so we filter with most used words
        stream.filter(track = settings.COMMON_WORDS, locations = settings.LOCATIONS)
        stream.disconnect()
        sortData = SortData(stream_listener.get_tweets())
        return sortData.get_most_common_words()
    except ProtocolError:
        print("There was an error. Restarting stream...")
    except ConnectionError:
        print("There was an error. Restarting stream...")

@app.route('/twit')
def twit():
    #clear the data dictionary when page is refreshed
    SortData.data.clear()
    # return render_template("twit.html")
    return render_template("twity.html")

@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html")

# labels_trendTwit = []
# values_trendTwit = []
# @app.route("/trendTwit")
# def chart_trendTwit():
#     global labels_trendTwit,values_trendTwit
#     labels = []
#     values = []
#     return render_template('chart.html', values=values_trendTwit, labels=labels_trendTwit)


# @app.route('/refreshData_trendTwit')
# def refresh_graph_data_trendTwit():
#     global labels_trendTwit, values_trendTwit
#     print("labels now: " + str(labels_trendTwit))
#     print("data now: " + str(values_trendTwit))
#     return jsonify(sLabel=labels_trendTwit, sData=values_trendTwit)


# @app.route('/updateData_trendTwit', methods=['POST'])
# def update_data_post_trendTwit():
#     global labels_trendTwit, values_trendTwit
#     if not request.form or 'data' not in request.form:
#         return "error",400
#     labels_trendTwit = ast.literal_eval(request.form['label'])
#     values_trendTwit = ast.literal_eval(request.form['data'])
#     print("labels received: " + str(labels_trendTwit))
#     print("data received: " + str(values_trendTwit))
#     return "success",201


# cara akses, misal: http://imamcs.pythonanywhere.com/api/fp/3.0/?a=70&b=3&c=2
@app.route("/api/fp/3.0/", methods=["GET"])
def api():
    import os.path
    import sys

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    url = os.path.join(BASE_DIR, "static/data_contoh/dataset_dump_tiny.csv")

    # url = "../GGRM.JK.csv"
    # dataset=pd.read_csv(url)

    import pandas as pd
    import numpy as np
    import json
    # from django.http import HttpResponse
    from flask import Response


    a, b, c = request.args.get('a'), request.args.get('b'),request.args.get('c')
    # print(a,' ',b,' ',c)
    # bar = request.args.to_dict()
    # print(bar)

    # dataset = request.FILES['inputDataset']#'E:/Pak Imam/Digitalent/dataset_dump.csv'
    persentase_data_training = int(a)
    banyak_fitur = int(b)
    banyak_hidden_neuron = int(c)
    # print(persentase_data_training,banyak_fitur,banyak_hidden_neuron)

    dataset = pd.read_csv(url, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    #dataset = pd.read_csv(url, usecols=['Close'])
    dataset = dataset.fillna(method='ffill')

    # print("missing value", dataset.isna().sum())

    minimum = int(dataset.min())
    maksimum = int(dataset.max())
     # print(minimum,maksimum)
    new_banyak_fitur = banyak_fitur + 1
    hasil_fitur = []
    for i in range((len(dataset)-new_banyak_fitur)+1):
        kolom = []
        j = i
        while j < (i+new_banyak_fitur):
            kolom.append(dataset.values[j][0])
            j += 1
        hasil_fitur.append(kolom)
    hasil_fitur = np.array(hasil_fitur)
        # print(hasil_fitur)
    data_normalisasi = (hasil_fitur - minimum)/(maksimum - minimum)

    data_training = data_normalisasi[:int(
        persentase_data_training*len(data_normalisasi)/100)]
    data_testing = data_normalisasi[int(
        persentase_data_training*len(data_normalisasi)/100):]

    # print(data_training)
    # Training
    is_singular_matrix = True
    while(is_singular_matrix):
        bobot = np.random.rand(banyak_hidden_neuron, banyak_fitur)
        #print("bobot", bobot)
        bias = np.random.rand(banyak_hidden_neuron)
        h = 1 / \
            (1 + np.exp(-(np.dot(data_training[:, :banyak_fitur], np.transpose(bobot)) + bias)))

        #print("h", h)
        #print("h_transpose", np.transpose(h))
        #print("transpose dot h", np.dot(np.transpose(h), h))

        # cek matrik singular
        cek_matrik = np.dot(np.transpose(h), h)
        det_cek_matrik = np.linalg.det(cek_matrik)
        if det_cek_matrik != 0:
            #proceed

        #if np.linalg.cond(cek_matrik) < 1/sys.float_info.epsilon:
            # i = np.linalg.inv(cek_matrik)
            is_singular_matrix = False
        else:
            is_singular_matrix = True


    h_plus = np.dot(np.linalg.inv(cek_matrik), np.transpose(h))

    # print("h_plus", h_plus)
    output_weight = np.dot(h_plus, data_training[:, banyak_fitur])

        # print(output_weight)
        # [none,none,...]

    # Testing
    h = 1 / \
        (1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    predict = np.dot(h, output_weight)
    predict = (predict * (maksimum - minimum) + minimum)

    # MAPE
    aktual = np.array(hasil_fitur[int(
        persentase_data_training*len(data_normalisasi)/100):, banyak_fitur]).tolist()
    mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)
    prediksi = predict.tolist()
    # print(prediksi, 'vs', aktual)
    # response = json.dumps({'y_aktual': aktual, 'y_prediksi': prediksi, 'mape': mape})

    # return Response(response, content_type='text/json')
    # return Response(response, content_type='application/json')
    #return Response(response, content_type='text/xml')


    response = jsonify({'y_aktual': aktual, 'y_prediksi': prediksi, 'mape': mape})


    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("access-control-allow-credentials","false")
    # response.headers.add("access-control-allow-methods","GET, POST")


    # r = Response(response, status=200, mimetype="application/json")
    # r.headers["Content-Type"] = "application/json; charset=utf-8"
    return response



# get json data from a url using flask in python
@app.route('/baca_api', methods=["GET"])
def baca_api():
    import requests
    import json
    # uri = "https://api.stackexchange.com/2.0/users?order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
    uri = "http://enterumum.pythonanywhere.com/api/fp/3.0/?a=50&b=3&c=2"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
        return "Terdapat Error Pada Koneksi Anda"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    # json.loads(response.get_data().decode("utf-8"))
    # data = json.loads(requests.get(uri).decode("utf-8"))
    # data = json.loads(response.get(uri).get_data().decode("utf-8"))

    # import urllib.request
    # with urllib.request.urlopen("http://imamcs.pythonanywhere.com/api/fp/3.0/?a=90&b=3&c=2") as url:
    #     data = json.loads(url.read().decode())
    #     #print(data)

    # from urllib.request import urlopen

    # import json
    # import json
    # store the URL in url as
    # parameter for urlopen
    # url = "https://api.github.com"

    # store the response of URL
    # response = urlopen(url)

    # storing the JSON response
    # from url in data
    # data_json = json.loads(response.read())

    # print the json response
    # print(data_json)

    # data = \
    #     {
    #   "items": [
    #     {
    #       "badge_counts": {
    #         "bronze": 16,
    #         "silver": 4,
    #         "gold": 0
    #       },
    #       "account_id": 258084,
    #       "is_employee": false,
    #       "last_modified_date": 1573684556,
    #       "last_access_date": 1628710576,
    #       "reputation_change_year": 0,
    #       "reputation_change_quarter": 0,
    #       "reputation_change_month": 0,
    #       "reputation_change_week": 0,
    #       "reputation_change_day": 0,
    #       "reputation": 420,
    #       "creation_date": 1292207782,
    #       "user_type": "registered",
    #       "user_id": 540028,
    #       "accept_rate": 100,
    #       "location": "Minneapolis, MN, United States",
    #       "website_url": "http://fuchida.me",
    #       "link": "https://stackoverflow.com/users/540028/fuchida",
    #       "profile_image": "https://i.stack.imgur.com/kP5GW.png?s=128&g=1",
    #       "display_name": "Fuchida"
    #     }
    #   ],
    #   "has_more": false,
    #   "quota_max": 300,
    #   "quota_remaining": 299
    # }

    # displayName = data['items'][0]['display_name']# <-- The display name
    # reputation = data['items'][0]['reputation']# <-- The reputation

    # y_train = data['y_aktual']
    # y_pred = data['y_prediksi']
    # mape = data['mape']

    return data
    # return str(mape)
    # return render_template('MybigdataAppsNonPySpark.html', y_aktual = list(y_train), y_prediksi = list(y_pred), mape = mape)


@app.route('/upload', methods=["GET", "POST"])
def upload():

    form = UploadForm()
    if request.method == "POST":

        if form.validate_on_submit():
            file_name = form.file.data
            database(name=file_name.filename, data=file_name.read() )
            # return render_template("upload.html", form=form)
            return redirect(url_for("dashboard"))

    return render_template("upload.html", form=form)


@app.route('/hapus/file/', methods=["GET"])
def hapus():
    name = request.args.get('name')
    conn = connect_db()
    db = conn.cursor()

    db.execute("DELETE FROM  upload WHERE name =\'"+ name +"\'")
    # mydata
    # for x in c.fetchall():
    #     name_v=x[0]
    #     data_v=x[1]
    #     break

    conn.commit()
    db.close()
    conn.close()

    return redirect(url_for("dashboard"))

@app.route('/unduh/file/', methods=["GET"])
def unduh():
    name = request.args.get('name')
    conn = connect_db()
    db = conn.cursor()

    # c = db.execute(""" SELECT * FROM  upload WHERE name ="""+ name)
    c = db.execute("SELECT * FROM  upload WHERE name =\'"+ name +"\'")
    # mydata
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    conn.commit()
    db.close()
    conn.close()

    # return render_template('dashboard.html', header = mydata)


    return send_file(BytesIO(data_v), attachment_filename=name_v, as_attachment=True)


@app.route('/download', methods=["GET", "POST"])
def download():

    form = UploadForm()

    if request.method == "POST":
        conn = connect_db()
        db = conn.cursor()

        # conn= sqlite3.connect("fga_big_data_rev2.db")
        # cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = db.execute(""" SELECT * FROM  upload """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        db.close()
        conn.close()

        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)


    return render_template("upload.html", form=form)



# class LoginForm(FlaskForm):
class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField("submit")
    download = SubmitField("download")

def database(name, data):
    conn = connect_db()
    db = conn.cursor()

    # conn= sqlite3.connect("fga_big_data_rev2.db")
    # cursor = conn.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS upload (name TEXT,data BLOP) """)
    db.execute("""INSERT INTO upload (name, data) VALUES (?,?) """,(name,data))

    conn.commit()
    db.close()
    conn.close()

def query():
    # conn= sqlite3.connect("fga_big_data_rev2.db")
    # cursor = conn.cursor()

    conn = connect_db()
    db = conn.cursor()

    print("IN DATABASE FUNCTION ")
    c = db.execute(""" SELECT * FROM  upload """)

    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break



    conn.commit()
    db.close()
    conn.close()

    return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)

@app.route('/dashboard')
def dashboard():
    # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cur.execute('SELECT * FROM header')
    # data = cur.fetchall()
    # cur.close()

    conn = connect_db()
    db = conn.cursor()

    # conn= sqlite3.connect("fga_big_data_rev2.db")
    # cursor = conn.cursor()
    print("IN DATABASE FUNCTION ")
    c = db.execute(""" SELECT * FROM  upload """)

    mydata = c.fetchall()
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    hasil = []
    for v_login in c:
        hasil.append(v_login)

    conn.commit()
    db.close()
    conn.close()

    #return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=True)

    return render_template('dashboard.html', header = mydata)

@app.route('/iot', methods=["GET", "POST"])
def iot():

    if 'name' in session:
        name = session['name']
    else:
        name = 'Guest'

    # start kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv
    if request.method == "POST":

        from io import StringIO
        import csv

        # date_var = request.args.get('date_var')
        # kota_var = request.args.get('kota_var')
        conn = connect_db()
        db = conn.cursor()

        output = StringIO()
        writer = csv.writer(output)
        c = db.execute("SELECT * FROM data_suhu_dll")

        result = c.fetchall()
        writer.writerow([i[0] for i in c.description])

        for row in result:
            line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
            writer.writerow(line)

        output.seek(0)

        conn.commit()
        db.close()
        conn.close()

        return Response(output, mimetype="text/csv",
                        headers={"Content-Disposition": "attachment;filename=data_suhu_iot_all.csv"})
    # ending kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv


    # menampilkan data dari tabel data_suhu_dll
    conn = connect_db()
    db = conn.cursor()

    c = db.execute(""" SELECT * FROM  data_suhu_dll """)

    mydata = c.fetchall()
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    hasil = []
    for v_login in c:
        hasil.append(v_login)

    conn.commit()
    db.close()
    conn.close()


    return render_template("getsuhu_dll.html", header = mydata)

@app.route('/del_iot/', methods=["GET"])
def del_iot():
    date_var = request.args.get('date_var')
    kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    db.execute("DELETE FROM data_suhu_dll WHERE date =\'"+ date_var +"\' AND  kota =\'"+ kota_var +"\'")

    conn.commit()
    db.close()
    conn.close()

    return redirect(url_for("iot"))

@app.route('/dw_iot/', methods=["GET"])
def dw_iot():

    from io import StringIO
    import csv

    date_var = request.args.get('date_var')
    # kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    output = StringIO()
    writer = csv.writer(output)
    c = db.execute("SELECT * FROM data_suhu_dll WHERE date =\'"+ date_var +"\'")

    result = c.fetchall()
    writer.writerow([i[0] for i in c.description])

    for row in result:
        line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
        writer.writerow(line)

    output.seek(0)

    conn.commit()
    db.close()
    conn.close()

    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=data_suhu_iot.csv"})

@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))


# ================
# Egonomic Project

# @app.route('/qrcode')
# def qrcode():
#     return 'scan QRCode'

@app.route("/in")
def index_qrcode():
    return render_template("qrcode.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")


# @app.route('/qr_index')
# def qr_index():
#     attendance = Attendance.getAll()
#     return render_template("qr_scan.html", data=enumerate(attendance, 1))

@app.route('/qr_index')
def qr_index():
    attendance = Attendance.getAll()
    return render_template("qr_scan2.html", data=enumerate(attendance, 1))


@app.route("/qr_scan", methods=["GET"])
def qr_scan():
    return Response(scanner(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video',methods=['GET', 'POST'])
def video():
    vid = cv.VideoCapture(0)
    success, dfs = vid.read()
    if success:
        return Response(face_detector(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/qr_student", methods=["GET", "POST"])
def qr_student():
    if request.method == "POST":
        name = request.form['name']
        nim = request.form['nim']
        UUID = str(uuid.uuid4())
        qr_code_mark = "static/img/tmp_qr/{}.png".format(UUID)
        student = Student(nim=nim, name=name, qr_code=qr_code_mark)
        student.save()

        import qrcode

        # # /qrcode
        # qrcode_img = qrcode.make(student.id)
        # # buf = io.BytesIO()
        # buf_qrcode = BytesIO()
        # qrcode_img.save(buf_qrcode)
        # buf_qrcode.seek(0)
        # # return send_file(buf_qrcode, mimetype='image/jpeg')

        qrcode_img = qrcode.make(student.id)
        # qrcode_img = qrcode(student.id)
        # canvas = Image.new('RGB', (290,290), 'white')
        # draw = ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code_{self.name}.png'
        fname = f'static/img/tmp_qr/qr_code_{student.id}.png'.format(UUID)
        buffer = BytesIO()
        # canvas.save(buffer,'PNG')
        # qrcode_img.save(fname, File(buffer), save=False)
        # qrcode_img.save(fname, buffer, save=False)
        # qrcode_img.save(buffer)

        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        url_file_name_qrcode = os.path.join(BASE_DIR, fname)

        qrcode_img.save(url_file_name_qrcode, format="PNG")
        # canvas.close()
        # super().save(*args, **kwargs)

        # img = pyqrcode.create(student.id, error="L", mode="binary", version=5)
        # img.png(qr_code, scale=10)
    students = Student.getAll()
    return render_template("qr_student.html", data=enumerate(students, 1))


def scanner():
    camera = Scanner()
    while True:
        frame = camera.get_video_frame()

        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            break


# ================================================================================
# Untuk Penelitian 2022 | Modeling data real terkait seseorang yang pernah terpapar Covid-19 dan varian barunya
# dengan menggunakan Algoritma Quantum meta-Deep AI
#

# Algoritma meta-Deep AI
@app.route('/qumedea')
def riset2022():
    return 'Hello Algoritma Quantum meta-Deep AI'



# ================================================================================
# Untuk Pengmas 2022 | membuat tabel CloudAI_Air_Rev untuk Penentuan Durasi Pengairan / Penyiraman Tanaman
# dengan menggunakan ELM dalam Ekosistem Cloud-AI
#
def pengmas2022_create_database():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS CloudAI_Air_Rev (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
                """)

    conn.commit()
    conn.close()

def pengmas2022_generate_data():
    """Generate sintesis atau dummy data untuk percontohan."""
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM CloudAI_Air_Rev')
    entry = cur.fetchone()

    # rs = db.execute("SELECT * FROM user order by id")
    # datalist = rs.fetchall()

    # if entry is None:
    #     for i in range(1, 11):
    #     cur.execute("""INSERT INTO CloudAI_Air_Rev (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
    #                 (f"Suhu {i}", f"Kelembaban {i}", f"Hujan {i}", f"Angin {i}", f"Durasi {i}"))

    if entry is None:
        import numpy as np
        import pandas as pd
        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        # Misal skema dataset-nya seperti berikut: => Silahkan dimodifikasi sesuai case Anda
        kolomFitur_X_plus_Target_Y = ['Suhu (X1)','Kelembaban (X2)', 'Curah Hujan (X3)','Angin (X4)','Durasi Air Dlm Menit (Y)']

        # set bykData = 3*np.power(10,7)
        bykData = 10
        bykFitur = len(kolomFitur_X_plus_Target_Y)-1

        # Interval atau Variasi nilai fitur
        nilaiFitur_Suhu = [17,35]
        nilaiFitur_Kelembaban = [70,90]
        nilaiFitur_Curah_Hujan = [2,95]
        nilaiFitur_Angin = [0,15]
        labelTargetY = [0.0,90.0]

        # generate isi dataset
        content_dataGenerate = np.array([np.arange(bykData)]*(bykFitur+1)).T
        df_gen = pd.DataFrame(content_dataGenerate, columns=kolomFitur_X_plus_Target_Y)

        df_gen ['Suhu (X1)'] = np.random.randint(nilaiFitur_Suhu[0], nilaiFitur_Suhu[1], df_gen.shape[0])
        df_gen ['Kelembaban (X2)'] = np.random.randint(nilaiFitur_Kelembaban[0], nilaiFitur_Kelembaban[1], df_gen.shape[0])
        df_gen ['Curah Hujan (X3)'] = np.random.randint(nilaiFitur_Curah_Hujan[0], nilaiFitur_Curah_Hujan[1], df_gen.shape[0])
        df_gen ['Angin (X4)'] = np.random.randint(nilaiFitur_Angin[0], nilaiFitur_Angin[1], df_gen.shape[0])
        df_gen ['Durasi Air Dlm Menit (Y)'] = np.round(np.random.uniform(labelTargetY[0], labelTargetY[1], df_gen.shape[0]),2)



        # save dataframe generate ke *.csv
        import os
        # print(os.path.expanduser("~"))
        userhome = os.path.expanduser("~").split("/")[-1]
        # print(userhome)

        # file_name_data_generate = '/home/bigdatafga/mysite/static/data_contoh/Data_CloudAI_Air_Rev.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)

        path = "/home/"+userhome+"/mysite/static/data_contoh"
        if not os.path.exists(path):
            os.makedirs(path)
        # file_name_data_generate = 'static/data_contoh/Data_CloudAI_Air_Rev.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)
        url_file_name_data_generate = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air_Rev.csv")
        df_gen.to_csv(url_file_name_data_generate, encoding='utf-8', index=False)

        # read file *.csv dan tampilkan
        # data_generate = pd.read_csv(file_name_data_generate)

        url = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air_Rev.csv")

        # Importing the dataset => ganti sesuai dengan case yg anda usulkan
        dataset = pd.read_csv(url)
        # X = dataset.iloc[:, :-1].values
        # y = dataset.iloc[:, 1].values

        def pushCSVdatasetToDB(x1,x2,x3,x4,y):
            #inserting values inside the created table
            # db = sqlite3.connect("data.db")

            # conn = connect_db()
            # cur = conn.cursor()

            cmd = "INSERT INTO CloudAI_Air_Rev(suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES('{}','{}','{}','{}','{}')".format(x1,x2,x3,x4,y)
            cur.execute(cmd)
            conn.commit()

        # CSV_to_SQLite3 dari file dataset
        for i in range(0,len(dataset)):
            pushCSVdatasetToDB(dataset.iloc[i][0],dataset.iloc[i][1],dataset.iloc[i][2],dataset.iloc[i][3],dataset.iloc[i][4])

        # for i in range(1, 11):
        #     cur.execute("""INSERT INTO CloudAI_Air_Rev (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
        #             (f"Type {i}", f"Receipt {i}", f"Amount {i}", f"Description {i}"))
    else:
        ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'
        print(ket_hasil)

    # end - insert where tabel CloudAI_Air_Rev masih kosong

    conn.commit()
    cur.close()
    conn.close()

@app.route('/menu')
def pengmas2022_menu():
    return render_template("launchpad_menu3.html")
    #return render_template("launchpad_menu2.html")
    #return render_template("launchpad_menu.html")

# @app.route('/vidEdu1')
# def pengmas2022_vidEdu1():
#     template_view = '''
#     <div class="col-sm-3">
#         <h3 class="box-title m-b-0">Popup with Youtube Video</h3>
#         <small>You can use youtube video with popup just add class <code>popup-youtube</code></small>
#         <br>
#         <br> <a class="popup-youtube btn btn-danger" href="www.youtube.com/watch?v=Bp49uOYMNrk">Open YouTube video</a>
#         <br>
#     </div>
#     '''

#     return render_template_string(template_view)

# @app.route('/vidEdu2')
# def pengmas2022_vidEdu2():
#     return render_template("launchpad_menu3.html")

@app.route('/pengmas2022_vidEdu2')
def pengmas2022_vidEdu2():

    # template_view = '''
    # <iframe src="https://drive.google.com/file/d/1Rv_VwP8pgUAgeYvwuaQnTcuPtU7MEX8t/preview" width="880" height="489" allow="autoplay" sandbox="allow-same-origin allow-scripts"></iframe>
    # '''

    template_view = '''
    <iframe src="https://drive.google.com/file/d/1Rv_VwP8pgUAgeYvwuaQnTcuPtU7MEX8t/preview" width="871" height="484" allow="autoplay" sandbox="allow-same-origin allow-scripts"></iframe>
    '''

    # <iframe src="https://drive.google.com/file/d/1Rv_VwP8pgUAgeYvwuaQnTcuPtU7MEX8t/preview" width="640" height="480" allow="autoplay"></iframe>

    return render_template_string(template_view)

@app.route('/pengmas2022_ppt1')
def pengmas2022_ppt1():
    # template_view = '''
    # <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSXsEpKGUUZagp0WXjpTtQiuImsBiqAMsQXBq0pk4eBd_QPX5LnmRc_xpdO9jaZ2A/embed?start=true&loop=true&delayms=3000" frameborder="0" width="1280" height="749" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    # '''
    # template_view = '''
    # <div class="col-sm-3">
    # <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSXsEpKGUUZagp0WXjpTtQiuImsBiqAMsQXBq0pk4eBd_QPX5LnmRc_xpdO9jaZ2A/embed?start=true&loop=true&delayms=60000" frameborder="0" width="640" height="389" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    # </div>
    # '''
    # template_view = '''
    # <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSXsEpKGUUZagp0WXjpTtQiuImsBiqAMsQXBq0pk4eBd_QPX5LnmRc_xpdO9jaZ2A/embed?start=true&loop=true&delayms=60000" frameborder="0" width="880" height="489" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    # '''

    # <iframe src="https://onedrive.live.com/embed?cid=F4A0F481EA1DEE2D&resid=F4A0F481EA1DEE2D%21368&authkey=APiSSFU52i8G37Q&em=2" width="402" height="327" frameborder="0" scrolling="no"></iframe>

    template_view = '''
    <iframe src="https://onedrive.live.com/embed?cid=F4A0F481EA1DEE2D&resid=F4A0F481EA1DEE2D%21368&authkey=APiSSFU52i8G37Q&em=2" width="880" height="489" frameborder="0" scrolling="no"></iframe>
    '''



    return render_template_string(template_view)
    # <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSXsEpKGUUZagp0WXjpTtQiuImsBiqAMsQXBq0pk4eBd_QPX5LnmRc_xpdO9jaZ2A/embed?start=true&loop=true&delayms=3000" frameborder="0" width="1280" height="749" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

@app.route('/pengmas2022_timdosen', methods=['GET'])
def pengmas2022_timdosen():

    import time
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    template_view = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
              <form method="post">
                  <div class="row">
                    <!-- .col -->
                    <div class="col-sm-12">
                        <div class="white-box">
                            <h3 class="box-title m-b-0">Tim Dosen & Poster PengMas 2022</h3>
                            <div id="image-popups" class="row">
                                <div class="col-sm-2">
                                    <a href={{url_image2}} data-effect="mfp-zoom-in"><img src={{url_image2}} class="img-responsive">
                                        <br>Tim</a>
                                </div>
                                <div class="col-sm-2">
                                    <a href={{url_image3}} data-effect="mfp-newspaper"><img src={{url_image3}} class="img-responsive">
                                        <br>Poster</a>
                                </div>

                            </div>
                        </div>
                    </div>
                    <!-- .col -->
                  </div>
             </form>
            <!--- </body> --->
            <!--- </html> --->
        '''

    # Cara plot
    # ---------------
    # load file dalam path + nama file /static/img/..
    url_file_img1 = "static/img/TimDosen.png"
    url_file_img2 = "static/img/Desain_Banner-PengMas_2022_v2.0.png"

    # return hasil
    # return render_template_string(A_a+template_view+Z_z, url_image2 = url_file_img1, url_image3 = url_file_img2)
    return render_template_string(A_a_no_frame+template_view+Z_z_no_frame, url_image2 = url_file_img1, url_image3 = url_file_img2)

# @app.route('/pengmas2022_api')
# def pengmas2022_api():

@app.route('/pengmas2022')
def pengmas2022():
    # get data dari iot API
    import requests
    from datetime import datetime
    import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%A, %Y-%m-%d %H:%M'))
    Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%A, %d %m %Y, pukul %H:%M'))

    WeekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    NamaHari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum\'at', 'Sabtu', 'Ahad/Minggu']

    NamaBulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

    # get_indeks_hari
    get_indeks_hari = 0
    loop_init = 0
    get_hari_ini_dlm_eng = Date.split(",")[0]
    for i in WeekDays:
        if i == get_hari_ini_dlm_eng:
            get_indeks_hari = loop_init
            break
        loop_init +=1
    Date = Date.replace(WeekDays[get_indeks_hari],NamaHari[get_indeks_hari])

    # get_indeks_bulan
    get_indeks_bulan = 0
    get_tgl = Date.split(",")[1].split(" ")[1]
    get_bulan_ini_dlm_eng = Date.split(",")[1].split(" ")[2]
    for i, get_nama_bulan in enumerate(NamaBulan):
        if i == int(get_bulan_ini_dlm_eng):
            get_indeks_bulan = i
            break
    Date = Date.replace(get_tgl+' '+get_bulan_ini_dlm_eng+' ',get_tgl+' '+NamaBulan[get_indeks_bulan-1]+' ')

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)



        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            # resp['current']['condition'] = {"Cerah Berawan"}
            kondisi = resp['current']['condition']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error"), dgn menyiapkan sintesis resp
            # resp = '''
            # {
            #   "location": {
            #     "name": "Malang",
            #     "region": "East Java",
            #     "country": "Indonesia",
            #     "lat": -7.4,
            #     "lon": 112.7,
            #     "tz_id": "Asia/Jakarta",
            #     "localtime_epoch": 1660695399,
            #     "localtime": '''+Date+'''
            #   },
            #   "current": {
            #     "temp_c": '-',
            #     "condition": {},
            #     "wind_mph": '-',
            #     "precip_mm": '-',
            #     "humidity": '-',
            #     "uv": '-'
            #   }
            # }
            # '''

            resp ='{"location":{"name":"Malang","region":"East Java","country":"Indonesia","lat":-7.4,"lon":112.7,"tz_id":"Asia/Jakarta","localtime_epoch":1660696463,"localtime":"'+Date+'"},"current":{"temp_c":25.0,"condition":{},"wind_mph":2.2,"precip_mm":0.1,"humidity":77,"uv":5.0}}'

            # data = json.dumps(data) # dict to string
            # data = json.loads(data) # string to json

            # resp = jsonify(resp)
            resp = json.loads(resp)
            suhu = resp['current']['temp_c']
            # resp['current']['condition'] = {"Cerah Berawan"}
            kondisi = resp['current']['condition']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']

            # suhu = '-'
            # curah_hujan = '-'
            # lembab = '-'
            # angin = '-'

    # get durasi irigasi
    # resp2 = requests.get('https://bigdatafga.pythonanywhere.com/api/pengmas2022')
    # resp2 = requests.get('https://imamcs.pythonanywhere.com/api/fp/3.0/?a=70&b=3&c=2')

    # resp2 = api_pengmas2022_elm_test()
    # resp2 = resp2.json()


    import os
    import sys

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # url = os.path.join(BASE_DIR, "static/simpan_model_elm/dataset_dump_tiny.csv")

    import pandas as pd
    import numpy as np
    import json
    # from django.http import HttpResponse
    from flask import Response
    from datetime import datetime

    userhome = os.path.expanduser("~").split("/")[-1]
    # print(userhome)

    path = "/home/"+userhome+"/mysite/static/simpan_model_elm"
    if not os.path.exists(path):
        os.makedirs(path)


    folder_path = path
    # penjelasan makna [::-1] => mulai dari end sampai awal, down increment dengan 1
    # contoh:
    # >>> 'abcdefghijklm'[::3]  # beginning to end, counting by 3
    # 'adgjm'
    # >>> 'abcdefghijklm'[::-3] # end to beginning, counting down by 3
    # 'mjgda'

    list_file_last_modified=os.listdir(os.path.join(BASE_DIR,folder_path))[::-1][:]
    # print(list_file_last_modified)

    if(len(list_file_last_modified)>0):
        # 15-08-2022-22-42-49
        list_file_last_modified.sort(key=lambda x: datetime.strptime(x[:19], '%d-%m-%Y-%H-%M-%S'))
        # print(list_file_last_modified)

        # get 3 file by date terbaru
        hasil_get_3_file_by_date_terbaru = list_file_last_modified[-3:]
        # print(hasil_get_3_file_by_date_terbaru)

        hasil_str = ''
        for idx_get_filename in range(len(hasil_get_3_file_by_date_terbaru)):
            hasil_str += ''.join(str(hasil_get_3_file_by_date_terbaru[idx_get_filename]))
            hasil_str += '<br>'
        # return hasil_str

        # 16-08-2022-07-59-24-Ntrain-7-Ntest-3-af-sigmoid-hd-6-fi-4-ft-1_bobot_input.csv
        # 16-08-2022-07-59-24-Ntrain-7-Ntest-3-af-sigmoid-hd-6-fi-4-ft-1_bias.csv
        # 16-08-2022-07-59-24-Ntrain-7-Ntest-3-af-sigmoid-hd-6-fi-4-ft-1_bobot_output.csv
        nama_file_dasar_base_name_unik2save_using_date = str(hasil_get_3_file_by_date_terbaru[0])[:62]

        # Cara baca file csv diatas
        nama_file_csv_bobot_input = nama_file_dasar_base_name_unik2save_using_date + '_bobot_input.csv'
        baca_bobot_input = pd.read_csv(os.path.join(BASE_DIR, "static/simpan_model_elm/"+nama_file_csv_bobot_input), header=None).values
        # print('baca_bobot_input: \n', baca_bobot_input,'\n')

        nama_file_csv_bias = nama_file_dasar_base_name_unik2save_using_date + '_bias.csv'
        baca_bias = pd.read_csv(os.path.join(BASE_DIR, "static/simpan_model_elm/"+nama_file_csv_bias),  header=None).values.flat[:]
        # print('baca bias: \n', baca_bias,'\n')

        nama_file_csv_bobot_output = nama_file_dasar_base_name_unik2save_using_date + '_bobot_output.csv'
        baca_bobot_output = pd.read_csv(os.path.join(BASE_DIR, "static/simpan_model_elm/"+nama_file_csv_bobot_output), header=None).values
        # print('baca_bobot_output: \n', baca_bobot_output,'\n')

        # return ''.join(str(baca_bobot_input))



        # Testing
        # =============
        #
        # get data dari iot_api sebagai data test
        # suhu, curah_hujan, lembab, angin
        data_testing = np.array(pengmas2022_get_data_iot_api())

        # return ''.join(str(data_testing))

        banyak_fitur = 4 # dari Suhu (X1),Kelembaban (X2),Curah Hujan (X3),Angin (X4),Durasi Air Dlm Menit (Y)


        #  Normalisasi data testing
        # get_min = np.min(arr_df_idr_us)
        # get_max = np.max(arr_df_idr_us)
        get_min = 0
        get_max = 100
        lower_boundary,upper_boundary = 0.1,0.9
        data_testing_norm =(((data_testing-get_min)/(get_max-get_min))*(upper_boundary-lower_boundary))+lower_boundary



        # h = 1 / \
        #     (1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(baca_bobot_input)) + baca_bias)))

        # h = 1 /(1 + np.exp(-(np.dot(data_testing, np.transpose(baca_bobot_input)) + baca_bias)))
        h = 1 /(1 + np.exp(-(np.dot(data_testing_norm, np.transpose(baca_bobot_input)) + baca_bias)))
        predict = np.dot(h, baca_bobot_output)
        predict_denorm = (((predict - lower_boundary)/(upper_boundary-lower_boundary))*(get_max-get_min))+get_min

        hasil_rekomendasi_durasi = predict_denorm.item()
        hasil_rekomendasi_durasi_dlm_jam = hasil_rekomendasi_durasi/60
        # if predict_denorm.item() > 60:
        #     durasi_final = 60
        #     hasil_rekomendasi_durasi = durasi_final



        # response = jsonify({'durasi': hasil_rekomendasi_durasi, 'satuan': 'menit', 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})
        response = jsonify({'durasi': hasil_rekomendasi_durasi, 'satuan': 'menit', 'durasi dlm jam': hasil_rekomendasi_durasi_dlm_jam, 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})


        # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")
        # return response
    else:
        default_rekomendasi_standar = 33 # dalam menit untuk tiap harinya
        hasil_rekomendasi_durasi = default_rekomendasi_standar
        hasil_rekomendasi_durasi_dlm_jam = hasil_rekomendasi_durasi/60
        # response = jsonify({'durasi': default_rekomendasi_standar, 'satuan': 'menit', 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})
        response = jsonify({'durasi': default_rekomendasi_standar, 'satuan': 'menit', 'durasi dlm jam': hasil_rekomendasi_durasi_dlm_jam, 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})


        # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")
        # return response


    # if resp2.status_code==200:
    #     resp2=resp2.json()
    # else:
    #     # print("Error"), dgn menyiapkan sintesis resp2
    #     # {
    #     #   "durasi": 60,
    #     #   "keterangan": "PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang",
    #     #   "satuan": "menit"
    #     # }

    #     resp2 ='{"durasi":60,"keterangan":"PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang","satuan":"menit"}'
    #     # resp2 ='{"mape":7.678250359881673,"y_aktual":[65000,65000,65000],"y_prediksi":[70497.38469675701,69750.32426425672,69724.87924075553]}'


    return render_template("infografis_cloudAI.html", result = resp, celcius = suhu, date = Date, result2 = hasil_rekomendasi_durasi, result3 = hasil_rekomendasi_durasi_dlm_jam)

@app.route('/pengmas2022_crud')
def pengmas2022_index():
    return '<a href="/pengmas2022_list">Demo Menampilkan List dari Tabel + Support => Create, Read, Update, Delete (CRUD)</a>'

@app.route('/pengmas2022_list')
def pengmas2022_list():

    # buat tabel dan generate data dummy
    pengmas2022_create_database()
    pengmas2022_generate_data()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM CloudAI_Air_Rev")
    rows = cur.fetchall()

    conn.close()

    #return render_template("list.html", rows=rows)
    return render_template_string(template_list, rows=rows)


@app.route('/pengmas2022_edit/<int:number>', methods=['GET', 'POST'])
def pengmas2022_edit(number):
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        # suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit

        cur.execute("UPDATE CloudAI_Air_Rev SET suhu_dlm_celcius = ?, humidity_kelembaban_dlm_persen = ?, precipitation_curah_hujan_dlm_persen = ?, wind_angin_dlm_km_per_jam = ?, durasi_air_dlm_menit = ? WHERE id = ?",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi, item_id))
        conn.commit()

        return redirect('/pengmas2022_list')

    cur.execute("SELECT * FROM CloudAI_Air_Rev WHERE id = ?", (number,))
    item = cur.fetchone()

    conn.close()

    #return render_template("edit.html", item=item)
    return render_template_string(template_edit, item=item)

@app.route('/pengmas2022_delete/<int:number>')
def pengmas2022_delete(number):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM CloudAI_Air_Rev WHERE id = ?", (number,))

    conn.commit()
    conn.close()

    return redirect('/pengmas2022_list')

@app.route('/pengmas2022_add', methods=['GET', 'POST'])
def pengmas2022_add():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        # item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        cur.execute("""INSERT INTO CloudAI_Air_Rev (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi))
        conn.commit()

        return redirect('/pengmas2022_list')

    #return render_template("add.html", item=item)
    return render_template_string(template_add)

@app.route('/pengmas2022_add2')
def pengmas2022_add2():
    conn = connect_db()
    cur = conn.cursor()

    # get data dari iot API
    import requests
    # from datetime import datetime
    # import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)

        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error")
            suhu = '-'
            curah_hujan = '-'
            lembab = '-'
            angin = '-'

        # print(nama_kota, 'dengan suhu = ', round(float(suhu),2),'°C', end='\n')

        cur.execute("""INSERT INTO CloudAI_Air_Rev (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
                (suhu, lembab, curah_hujan, angin))

        conn.commit()
        cur.close()
        conn.close()

    return redirect('/pengmas2022_list')

def pengmas2022_get_data_iot_api():
    # get data dari iot API
    import requests
    # from datetime import datetime
    # import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)

        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error")
            suhu = '-'
            curah_hujan = '-'
            lembab = '-'
            angin = '-'


    return suhu, lembab, curah_hujan, angin

@app.route('/pengmas2022_elm_train')
def pengmas2022_elm_train():
    conn = connect_db()
    cur = conn.cursor()

    import os
    import sys

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    url = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air_Rev.csv")

    import pandas as pd
    import numpy as np
    import json

    from flask import Response

    from datetime import datetime
    # from time import strftime
    import pytz

    persentase_data_training = 75
    banyak_fitur = 4 # dari Suhu (X1),Kelembaban (X2),Curah Hujan (X3),Angin (X4),Durasi Air Dlm Menit (Y)
    banyak_fitur_target = 1
    banyak_hidden_neuron = 6
    # print(persentase_data_training,banyak_fitur,banyak_hidden_neuron)

    dataset = pd.read_csv(url)

    # convert df to array np
    arr_dataset = dataset.iloc[:,:].values
    arr_df_idr_us = arr_dataset

    # set nilai parameter ELM
    # inisialisasi jumlah fitur (n) yang digunakan sebanyak banyak_fitur,
    # sedangkan jumlah hidden neuron (m) sebanyak banyak_hidden_neuron,
    # dan untuk data training sebanyak persentase_data_training dan data testing sebanyak 100 - persentase_data_training
    n = banyak_fitur
    m = banyak_hidden_neuron

    byk_data = arr_df_idr_us.shape[0]
    Ntrain = int(persentase_data_training*byk_data/100)
    Ntest = byk_data - Ntrain

    # Interval atau Variasi nilai fitur, sbg nilai min max
    nilaiFitur_Suhu = [17,35]
    nilaiFitur_Kelembaban = [70,90]
    nilaiFitur_Curah_Hujan = [2,95]
    nilaiFitur_Angin = [0,15]
    labelTargetY = [0.0,90.0]

    # tetapi untuk menyederhanakan proses normalisasi, digunakan set nilai min = 0 max = 100

    #  Normalisasi data
    # get_min = np.min(arr_df_idr_us)
    # get_max = np.max(arr_df_idr_us)
    get_min = 0
    get_max = 100
    lower_boundary,upper_boundary = 0.1,0.9
    data_norm =(((arr_df_idr_us-get_min)/(get_max-get_min))*(upper_boundary-lower_boundary))+lower_boundary
    # print('data norm: \n',data_norm)

    data_normalisasi = data_norm

    data_training = data_normalisasi[:int(
        persentase_data_training*len(data_normalisasi)/100)]
    data_testing = data_normalisasi[int(
        persentase_data_training*len(data_normalisasi)/100):]

    # print(data_training)
    # Training
    is_singular_matrix = True
    while(is_singular_matrix):
        bobot = np.random.rand(banyak_hidden_neuron, banyak_fitur)
        #print("bobot", bobot)
        bias = np.random.rand(banyak_hidden_neuron)
        h = 1 / \
            (1 + np.exp(-(np.dot(data_training[:, :banyak_fitur], np.transpose(bobot)) + bias)))

        #print("h", h)
        #print("h_transpose", np.transpose(h))
        #print("transpose dot h", np.dot(np.transpose(h), h))

        # cek matrik singular
        cek_matrik = np.dot(np.transpose(h), h)
        det_cek_matrik = np.linalg.det(cek_matrik)
        if det_cek_matrik != 0:
            #proceed

        #if np.linalg.cond(cek_matrik) < 1/sys.float_info.epsilon:
            # i = np.linalg.inv(cek_matrik)
            is_singular_matrix = False
        else:
            is_singular_matrix = True


    h_plus = np.dot(np.linalg.inv(cek_matrik), np.transpose(h))

    # print("h_plus", h_plus)
    output_weight = np.dot(h_plus, data_training[:, banyak_fitur])

    # membuat name_unik2save utk simpan hasil training
    name_unik2save = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y-%H-%M-%S'))
    # hasil_txt_Ytrain_predict = arr_token_to_txt('filename_HasilTrain_'+name_unik2save+'.txt',arr_token_Ytrain_predict)

    # simpan bobot_input, bias dan bobot_output
    # set info_param
    # af mewakili parameter activation function
    # hd mewakili parameter jumlah_hidden
    # fi mewakili jumlah fitur input yg diset
    # ft mewakili jumlah fitur target
    # elm_train memakili label train ELM-nya

    af= 'sigmoid'
    # af= 'tanh'


    info_param = '-Ntrain-'+str(Ntrain)+'-Ntest-'+str(Ntest)+'-af-'+af+'-hd-'+str(m)+'-fi-'+str(n)+'-ft-'+str(banyak_fitur_target)

    # /home/bigdatafga/mysite/static/simpan_model_elm

    # save dataframe generate ke *.csv
    # print(os.path.expanduser("~"))
    userhome = os.path.expanduser("~").split("/")[-1]
    # print(userhome)

    path = "/home/"+userhome+"/mysite/static/simpan_model_elm"
    if not os.path.exists(path):
        os.makedirs(path)

    # url_file_name_data_generate = os.path.join(BASE_DIR, "static/simpan_model_elm/Data_CloudAI_Air_Rev.csv")
    # df_gen.to_csv(url_file_name_data_generate, encoding='utf-8', index=False)

    # nama_path_hasil = './HasilTrainNTest/'+name_unik2save+'/'
    # nama_path_hasil = './HasilTrainNTest/'+name_unik2save
    nama_path_hasil = "static/simpan_model_elm/"+name_unik2save
    nama_file_csv_bobot_input = nama_path_hasil+info_param+'_bobot_input.csv'
    nama_file_csv_bias = nama_path_hasil+info_param+'_bias.csv'
    nama_file_csv_bobot_output = nama_path_hasil+info_param+'_bobot_output.csv'

    bobot_input = bobot
    bobot_output = output_weight

    pd.DataFrame(bobot_input).to_csv(os.path.join(BASE_DIR, nama_file_csv_bobot_input), header=None, index=None)
    pd.DataFrame(bias).to_csv(os.path.join(BASE_DIR, nama_file_csv_bias), header=None, index=None)
    pd.DataFrame(bobot_output).to_csv(os.path.join(BASE_DIR, nama_file_csv_bobot_output), header=None, index=None)

    conn.commit()
    cur.close()
    conn.close()

    return redirect('/pengmas2022_list')

# cara akses, misal: http://imamcs.pythonanywhere.com/api/fp/3.0/?a=70&b=3&c=2
# @app.route("/api/pengmas2022", methods=["GET"])
@app.route("/api/pengmas2022")
def api_pengmas2022_elm_test():
    import os
    import sys

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # url = os.path.join(BASE_DIR, "static/simpan_model_elm/dataset_dump_tiny.csv")

    import pandas as pd
    import numpy as np
    import json
    # from django.http import HttpResponse
    from flask import Response
    from datetime import datetime

    userhome = os.path.expanduser("~").split("/")[-1]
    # print(userhome)

    path = "/home/"+userhome+"/mysite/static/simpan_model_elm"
    if not os.path.exists(path):
        os.makedirs(path)


    folder_path = path
    # penjelasan makna [::-1] => mulai dari end sampai awal, down increment dengan 1
    # contoh:
    # >>> 'abcdefghijklm'[::3]  # beginning to end, counting by 3
    # 'adgjm'
    # >>> 'abcdefghijklm'[::-3] # end to beginning, counting down by 3
    # 'mjgda'

    list_file_last_modified=os.listdir(os.path.join(BASE_DIR,folder_path))[::-1][:]
    # print(list_file_last_modified)

    if(len(list_file_last_modified)>0):
        # 15-08-2022-22-42-49
        list_file_last_modified.sort(key=lambda x: datetime.strptime(x[:19], '%d-%m-%Y-%H-%M-%S'))
        # print(list_file_last_modified)

        # get 3 file by date terbaru
        hasil_get_3_file_by_date_terbaru = list_file_last_modified[-3:]
        # print(hasil_get_3_file_by_date_terbaru)

        hasil_str = ''
        for idx_get_filename in range(len(hasil_get_3_file_by_date_terbaru)):
            hasil_str += ''.join(str(hasil_get_3_file_by_date_terbaru[idx_get_filename]))
            hasil_str += '<br>'
        # return hasil_str

        # 16-08-2022-07-59-24-Ntrain-7-Ntest-3-af-sigmoid-hd-6-fi-4-ft-1_bobot_input.csv
        # 16-08-2022-07-59-24-Ntrain-7-Ntest-3-af-sigmoid-hd-6-fi-4-ft-1_bias.csv
        # 16-08-2022-07-59-24-Ntrain-7-Ntest-3-af-sigmoid-hd-6-fi-4-ft-1_bobot_output.csv
        nama_file_dasar_base_name_unik2save_using_date = str(hasil_get_3_file_by_date_terbaru[0])[:62]

        # Cara baca file csv diatas
        nama_file_csv_bobot_input = nama_file_dasar_base_name_unik2save_using_date + '_bobot_input.csv'
        baca_bobot_input = pd.read_csv(os.path.join(BASE_DIR, "static/simpan_model_elm/"+nama_file_csv_bobot_input), header=None).values
        # print('baca_bobot_input: \n', baca_bobot_input,'\n')

        nama_file_csv_bias = nama_file_dasar_base_name_unik2save_using_date + '_bias.csv'
        baca_bias = pd.read_csv(os.path.join(BASE_DIR, "static/simpan_model_elm/"+nama_file_csv_bias),  header=None).values.flat[:]
        # print('baca bias: \n', baca_bias,'\n')

        nama_file_csv_bobot_output = nama_file_dasar_base_name_unik2save_using_date + '_bobot_output.csv'
        baca_bobot_output = pd.read_csv(os.path.join(BASE_DIR, "static/simpan_model_elm/"+nama_file_csv_bobot_output), header=None).values
        # print('baca_bobot_output: \n', baca_bobot_output,'\n')

        # return ''.join(str(baca_bobot_input))



        # Testing
        # =============
        #
        # get data dari iot_api sebagai data test
        # suhu, curah_hujan, lembab, angin
        data_testing = np.array(pengmas2022_get_data_iot_api())

        # return ''.join(str(data_testing))

        banyak_fitur = 4 # dari Suhu (X1),Kelembaban (X2),Curah Hujan (X3),Angin (X4),Durasi Air Dlm Menit (Y)


        #  Normalisasi data testing
        # get_min = np.min(arr_df_idr_us)
        # get_max = np.max(arr_df_idr_us)
        get_min = 0
        get_max = 100
        lower_boundary,upper_boundary = 0.1,0.9
        data_testing_norm =(((data_testing-get_min)/(get_max-get_min))*(upper_boundary-lower_boundary))+lower_boundary



        # h = 1 / \
        #     (1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(baca_bobot_input)) + baca_bias)))
        h = 1 /(1 + np.exp(-(np.dot(data_testing_norm, np.transpose(baca_bobot_input)) + baca_bias)))
        predict = np.dot(h, baca_bobot_output)
        predict_denorm = (((predict - lower_boundary)/(upper_boundary-lower_boundary))*(get_max-get_min))+get_min

        hasil_rekomendasi_durasi = predict_denorm.item()
        # if predict_denorm.item() > 60:
        #     durasi_final = 60
        #     hasil_rekomendasi_durasi = durasi_final

        # response = jsonify({'durasi': hasil_rekomendasi_durasi, 'satuan': 'menit', 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})

        hasil_rekomendasi_durasi_dlm_jam = hasil_rekomendasi_durasi/60
        # if predict_denorm.item() > 60:
        #     durasi_final = 60
        #     hasil_rekomendasi_durasi = durasi_final



        # response = jsonify({'durasi': hasil_rekomendasi_durasi, 'satuan': 'menit', 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})
        response = jsonify({'durasi dlm menit': hasil_rekomendasi_durasi, 'durasi dlm jam': hasil_rekomendasi_durasi_dlm_jam, 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})


        # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("access-control-allow-credentials","false")
        # response.headers.add("access-control-allow-methods","GET, POST")


        # r = Response(response, status=200, mimetype="application/json")
        # r.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    else:
        default_rekomendasi_standar = 33 # dalam menit untuk tiap harinya
        hasil_rekomendasi_durasi = default_rekomendasi_standar
        hasil_rekomendasi_durasi_dlm_jam = hasil_rekomendasi_durasi/60
        # response = jsonify({'durasi': default_rekomendasi_standar, 'satuan': 'menit', 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})
        response = jsonify({'durasi dlm menit': hasil_rekomendasi_durasi, 'durasi dlm jam': hasil_rekomendasi_durasi_dlm_jam, 'keterangan': 'PengMas Filkom UB 2022 | CloudAI penentuan lama waktu pengairan hidroponik dgn Algoritma ELM, untuk tiap harinya dari data iot API di kota Malang'})


        # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("access-control-allow-credentials","false")
        # response.headers.add("access-control-allow-methods","GET, POST")


        # r = Response(response, status=200, mimetype="application/json")
        # r.headers["Content-Type"] = "application/json; charset=utf-8"
        return response


template_list = """
<h2>Menampilkan Data CloudAI Air + Support Create, Read, Update, Delete (CRUD)</h2>
<a href="{{ url_for( "pengmas2022_add" ) }}">Tambah Data</a> |
<a href="{{ url_for( "pengmas2022_add2" ) }}">Tambah Data dari iot_api (tanpa nilai Durasi Waktu)</a> |
<a href="{{ url_for( "pengmas2022_elm_train" ) }}">Proses Training data dgn ELM</a>
{% if rows %}
<table border="1">
    <thead>
        <td>No</td>
        <td>Suhu (°C)</td>
        <td>Kelembaban (%)</td>
        <td>Curah Hujan (%)</td>
        <td>Kecepatan Angin (Km/Jam)</td>
        <td>Durasi Waktu Pengairan / Penyiraman (Menit)</td>
    </thead>

    {% for row in rows %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
        <td>
            <a href="{{ url_for( "pengmas2022_edit", number=row[0] ) }}">Edit</a> |
            <a href="{{ url_for( "pengmas2022_delete", number=row[0] ) }}">Hapus</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% else %}
Empty</br>
{% endif %}
"""

template_add = """
<h1>Tambah Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "pengmas2022_add" ) }}">
    Suhu: <input name="suhu" value=""/></br>
    Kelembaban: <input name="kelembaban" value=""/></br>
    Curah Hujan: <input name="hujan" value=""/></br>
    Kecepatan Angin: <input name="angin" value=""/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value=""/></br>
    <button>Simpan Data</button></br>
</form>
"""

template_edit = """
<h1>Edit Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "pengmas2022_edit", number=item[0] ) }}">
    Suhu: <input name="suhu" value="{{item[1]}}"/></br>
    Kelembaban: <input name="kelembaban" value="{{item[2]}}"/></br>
    Curah Hujan: <input name="hujan" value="{{item[3]}}"/></br>
    Kecepatan Angin: <input name="angin" value="{{item[4]}}"/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value="{{item[5]}}"/></br>
    <button>Simpan Update Data</button></br>
</form>
"""

# if __name__ == '__main__':
#     #import os
#     #os.environ["JAVA_HOME"] ="/usr/lib/jvm/java-8-openjdk-amd64"
#     #print(os.environ["JAVA_HOME"])
#     #print(os.environ["SPARK_HOME"])
#     #print(os.environ["PYTHONPATH"])
#     # db.create_all()

#     app.run()  # If address is in use, may need to terminate other sessions:
#              # Runtime > Manage Sessions > Terminate Other Sessions
#   # app.run(host='0.0.0.0', port=5004)  # If address is in use, may need to terminate other sessions:
#              # Runtime > Manage Sessions > Terminate Other Sessions
#     # socket.run(app, debug=True)
