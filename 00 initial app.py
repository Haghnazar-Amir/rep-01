from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import sqlite3 as sql

con = sql.connect('database.db')
cur = con.cursor()
cmd = ''' CREATE TABLE IF NOT EXISTS groups (  gr_code INTEGER PRIMARY KEY UNIQUE 
                                             , gr_name TEXT  ) '''
cur.execute( cmd )
con.commit()
con.close()

con = sql.connect('database.db')
cur = con.cursor()
cmd = ''' CREATE TABLE IF NOT EXISTS goods (  g_code INTEGER PRIMARY KEY UNIQUE
                                            , g_name TEXT
                                            , gr_code INTEGER
                                            , gr_name TEXT
                                            , g_type TEXT
                                            , g_measuring TEXT
                                            , g_weight_unit TEXT
                                            , g_in_every_box INTEGER
                                            , g_reorder_point INTEGER
                                            , photo BLOB  ) '''
cur.execute( cmd )
con.commit()
con.close()

con = sql.connect('database.db')
cur = con.cursor()
cmd = ''' CREATE TABLE IF NOT EXISTS stock (  g_code INTEGER PRIMARY KEY UNIQUE
                                            , g_name TEXT
                                            , gr_code INTEGER
                                            , gr_name TEXT
                                            , g_type TEXT
                                            , g_supply INTEGER 
                                            , g_unit TEXT
                                            , g_reorder_point INTEGER
                                            , g_address TEXT) '''
cur.execute( cmd )
con.commit()
con.close()

con = sql.connect('database.db')
cur = con.cursor()
cmd = ''' CREATE TABLE IF NOT EXISTS docs  (  doc_number INTEGER 
                                            , doc_type TEXT 
                                            , g_code INTEGER
                                            , g_name TEXT
                                            , gr_code INTEGER
                                            , gr_name TEXT
                                            , g_type TEXT
                                            , g_amount REAL
                                            , g_unit TEXT
                                            , note TEXT
                                            , admin_name TEXT
                                            , delivery_name TEXT
                                            , delivery_idd INTEGER
                                            , time TEXT ) '''
cur.execute( cmd )
con.commit()
con.close()

con = sql.connect('database.db')
cur = con.cursor()
cmd = ''' CREATE TABLE IF NOT EXISTS requests  (  request_number INTEGER 
                                                , rq_name INTEGER
                                                , rq_pid INTEGER 
                                                , g_code INTEGER
                                                , g_name TEXT
                                                , g_amount REAL
                                                , g_unit TEXT
                                                , note TEXT
                                                , time TEXT
                                                , status TEXT
                                                , admin TEXT
                                                , note2 TEXT
                                                , time2 TEXT ) '''
cur.execute( cmd )
con.commit()
con.close()

con = sql.connect('database.db')
cur = con.cursor()
cmd = ''' CREATE TABLE IF NOT EXISTS people (  idd INTEGER PRIMARY KEY UNIQUE
                                             , user_n TEXT UNIQUE
                                             , pass_w TEXT
                                             , n_id INTEGER UNIQUE
                                             , full_name TEXT
                                             , position TEXT
                                             , photo BLOB  ) '''
cur.execute( cmd )
con.commit()
con.close()

class GUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.gui()

    def read_binary(self, file_name):
        with open( file_name, 'rb' ) as f:
            data = f.read()
        return data

    def write_binary(self, data, file_name):
        with open( file_name, 'wb' ) as f:
            f.write( data )

    def upload_photo(self, event = None):
        self.file = askopenfilename( initialdir = [('photos', '*.jpg;*.png' )] )
        if self.file:
            img = Image.open( self.file )
            img = img.resize( (110, 110) )
            img = ImageTk.PhotoImage( img )
            self.img_lbl.config( image = img )
            self.img_lbl.image = img
            data = self.read_binary( self.file )
            self.write_binary( data, 'z.png' )
            

    def submit(self):
        self.idd = self.ent1.get()
        self.user_n = self.ent2.get()
        self.pass_w = self.ent3.get()
        self.n_id = self.ent4.get()
        self.full_n = self.ent5.get()
        self.position = self.ent6.get()
        self.img_binary = self.read_binary('z.png')
        lst = [self.idd, self.user_n, self.pass_w, self.n_id, self.full_n, self.position, self.img_binary]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = '''INSERT INTO people ( idd, user_n, pass_w, n_id , full_name, position, photo  ) VALUES (?, ?, ?, ?, ?, ?, ?) '''
        cur.execute( cmd , lst )
        con.commit()
        con.close()

        self.ent1.delete( 0 , END )
        self.ent2.delete( 0 , END )
        self.ent3.delete( 0 , END )
        self.ent4.delete( 0 , END )
        self.ent5.delete( 0 , END )
        self.ent6.delete( 0 , END )
        self.img_lbl.config( image = self.img1 )
        self.ent1.focus() 



    def gui(self):
        self.geometry('700x500+300+150')
        self.title('مدیریت کارخانه - تعریف انباردار')

        self.management_bg = ImageTk.PhotoImage( file = 'management_bg.png' )
        self.img1 = ImageTk.PhotoImage( file = 'label_upload.png' )
        self.upload_btn_img = ImageTk.PhotoImage( file = 'button_photo_upload.png' )
        self.submit_btn_img = ImageTk.PhotoImage( file = 'button_submit.png' )

        self.bg_lbl = Label( self, image = self.management_bg )
        self.bg_lbl.place( x = -2 , y = -1)

        self.frm1 = LabelFrame( self, text = 'ثبت انباردار', labelanchor = 'n' , font = ('homa', 13) , bg = 'white', fg = '#345382', padx = 40 , pady = 20)
        self.frm1.pack( pady = 50 )

        self.lbl1 = Label( self.frm1, text = 'کد پرسنلی', anchor = 'e',
                           width = 6, bg = 'white', fg = '#345382', font = ('homa', 11), bd = 0 )
        self.lbl2 = Label( self.frm1, text = 'نام کاربری', anchor = 'e',
                           width = 6, bg = 'white', fg = '#345382', font = ('homa', 11), bd = 0 )
        self.lbl3 = Label( self.frm1, text = 'رمز عبور', anchor = 'e',
                           width = 6, bg = 'white', fg = '#345382', font = ('homa', 11), bd = 0 )
        self.lbl4 = Label( self.frm1, text = 'کد ملی', anchor = 'e',
                           width = 6, bg = 'white', fg = '#345382', font = ('homa', 11), bd = 0 )
        self.lbl5 = Label( self.frm1, text = 'نام کامل', anchor = 'e',
                           width = 6, bg = 'white', fg = '#345382', font = ('homa', 11), bd = 0 )
        self.lbl6 = Label( self.frm1, text = 'سِمت', anchor = 'e',
                           width = 6, bg = 'white', fg = '#345382', font = ('homa', 11), bd = 0 )

        self.ent1 = Entry( self.frm1, justify ='center', width = 15 )
        self.ent2 = Entry( self.frm1, justify ='center', width = 15 )
        self.ent3 = Entry( self.frm1, justify ='center', width = 15 )
        self.ent4 = Entry( self.frm1, justify ='center', width = 15 )
        self.ent5 = Entry( self.frm1, justify ='center', width = 15 )
        self.ent6 = Entry( self.frm1, justify ='center', width = 15 )

        self.img_lbl = Label( self.frm1, image = self.img1, width = 110, height = 110, bg = 'white', bd = 0 )
        self.btn0 = Button( self.frm1, image = self.upload_btn_img, bg = 'white', bd = 0,  command = self.upload_photo )

        self.btn1 = Button( self.frm1, image = self.submit_btn_img, bg = 'white', bd = 0, command = self.submit )

        self.lbl1.grid( row = 1 , column = 3 , padx = 10, pady = 5 )
        self.lbl2.grid( row = 2 , column = 3 , pady = 5 )
        self.lbl3.grid( row = 3 , column = 3 , pady = 5 )
        self.lbl4.grid( row = 4 , column = 3 , pady = 5 )
        self.lbl5.grid( row = 5 , column = 3 , pady = 5 )
        self.lbl6.grid( row = 6 , column = 3 , pady = 5 )

        self.ent1.grid( row = 1 , column = 2 , padx = 20 )
        self.ent2.grid( row = 2 , column = 2 )
        self.ent3.grid( row = 3 , column = 2 )
        self.ent4.grid( row = 4 , column = 2 )
        self.ent5.grid( row = 5 , column = 2 )
        self.ent6.grid( row = 6 , column = 2 )

        self.img_lbl.grid( row = 1 , rowspan = 4 , column = 1 , padx = 20)
        self.btn0.grid( row = 4 , rowspan = 5 , column = 1)

        self.btn1.grid( row = 7 , column = 1 , columnspan = 3, pady = 20)

        self.ent1.bind('<Return>', lambda event : self.ent2.focus() )
        self.ent2.bind('<Return>', lambda event : self.ent3.focus() )
        self.ent3.bind('<Return>', lambda event : self.ent4.focus() )
        self.ent4.bind('<Return>', lambda event : self.ent5.focus() )
        self.ent5.bind('<Return>', lambda event : self.ent6.focus() )
        self.ent6.bind('<Return>', lambda event : self.btn0.focus() )

o = GUI()
o.mainloop()














