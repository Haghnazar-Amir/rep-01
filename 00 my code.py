from    tkinter    import   *
from    tkinter    import   ttk, messagebox, filedialog
from    PIL        import   ImageTk, Image
import  sqlite3    as       sql
import  jdatetime  as       dt


class GroupsCodeValidation():

    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!کد گروه را وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!کد گروه را اصلاح کنید'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!کد گروه را اصلاح کنید'
                flg1 = False
            
        if flg1 and value != 0:
            if value > 999 or value < 101 :
                instance.__dict__[self.key] = 0
                instance.msg = '!کد گروه باید بین 100 تا 999 باشد'
                flg1 = False
                
        if flg1:
            instance.__dict__[self.key] = value


class GroupsNameValidation():

    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 'z'
            instance.msg = '!نام گروه را وارد کنید'
            flg1 = False
                
        if flg1:
            instance.__dict__[self.key] = value


class DocNumberValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!شمارۀ سند را وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!شمارۀ سند صحیح نیست'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!شمارۀ سند صحیح نیست'
                flg1 = False
            
        if flg1 and value != 0:
            if value > 299999 or value < 100001 :
                instance.__dict__[self.key] = 0
                instance.msg = '!شمارۀ سند باید بین 100000 و 200000 باشد'
                flg1 = False

        if flg1:
            instance.__dict__[self.key] = value


class GoodsCodeValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!کد کالا را وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!کد کالا صحیح نیست'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!کد کالا صحیح نیست'
                flg1 = False
            
        if flg1 and value != 0:
            if value > 99999 or value < 10101 :
                instance.__dict__[self.key] = 0
                instance.msg = '!کد کالا باید بین 10100 تا 20000 باشد'
                flg1 = False
                
        if flg1:
            instance.__dict__[self.key] = value


class GoodsnameValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 'z'
            instance.msg = '!نام کالا را وارد کنید'
            flg1 = False
                
        if flg1:
            instance.__dict__[self.key] = value


class GEBValidation():

    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        if value == '_':
            instance.__dict__[self.key] = value
        
        else:
            ref = '0123456789'
            flg1 = True

            if value == '':
                instance.__dict__[self.key] = 0
                instance.msg = '!تعداد/مقدار در هر بسته وارد کنید'
                flg1 = False
                
            else:
                value = str(value)
                for i in value:
                    if i not in ref:
                        flg1 = False
                        instance.__dict__[self.key] = 0
                        instance.msg = '!تعداد/مقدار در هر بسته صحیح نیست'
                        break

            if flg1:
                try:
                    value = int( value )
                except:
                    instance.__dict__[self.key] = 0
                    instance.msg = '!تعداد/مقدار در هر بسته صحیح نیست'
                    flg1 = False 
                    
            if flg1:
                instance.__dict__[self.key] = value
    

class ROPValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!نقطه سفارش وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!نقطه سفارش صحیح نیست'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!نقطه سفارش صحیح نیست'
                flg1 = False 
                
        if flg1:
            instance.__dict__[self.key] = value


class AmountsValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!تعداد/مقدار را وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!تعداد/مقدار صحیح نیست'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!تعداد/مقدار صحیح نیست'
                flg1 = False 
                
        if flg1:
            instance.__dict__[self.key] = value


class RequestNumberValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!شمارۀ درخواست را وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!شمارۀ درخواست صحیح نیست'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!شمارۀ درخواست صحیح نیست'
                flg1 = False
            
        if flg1 and value != 0:
            if value > 299999 or value < 200001 :
                instance.__dict__[self.key] = 0
                instance.msg = '!شمارۀ درخواست باید بین 200000 و 300000 باشد'
                flg1 = False
                     
        if flg1:
            instance.__dict__[self.key] = value


class NIDValidation():
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = 'insert {}! \n'.format(self.key)
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = 'invalid {}!\n'.format(self.key)
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = 'invalid {}! \n'.format(self.key)
                flg1 = False
            
        if flg1 and value != 0:
            if value > 9999999999 or value < 1000000000 :
                instance.__dict__[self.key] = 0
                instance.msg = 'invalid {}! \n'.format(self.key)
                flg1 = False
                      
        if flg1:
            instance.__dict__[self.key] = value


class PIDValidation(): 
    
    def __set_name__(self, instance, key):
        self.key = key
        
    def __set__(self, instance, value):
        ref = '0123456789'
        flg1 = True
        
        if value == '':
            instance.__dict__[self.key] = 0
            instance.msg = '!کد پرسنلی را وارد کنید'
            flg1 = False
            
        else:
            value = str(value)
            for i in value:
                if i not in ref:
                    flg1 = False
                    instance.__dict__[self.key] = 0
                    instance.msg = '!کد پرسنلی صحیح نیست'
                    break

        if flg1:
            try:
                value = int( value )
            except:
                instance.__dict__[self.key] = 0
                instance.msg = '!کد پرسنلی صحیح نیست'
                flg1 = False
            
        if flg1 and value != 0:
            if value > 299 or value < 201 :
                instance.__dict__[self.key] = 0
                instance.msg = '!کد پرسنلی بین 200 و 300 باشد'
                flg1 = False
                     
        if flg1:
            instance.__dict__[self.key] = value



class GUI(Tk):

    gr_code = GroupsCodeValidation()
    gr_name = GroupsNameValidation()
    g_code = GoodsCodeValidation()
    g_name = GoodsnameValidation()
    g_in_every_box = GEBValidation()
    g_reorder_point = ROPValidation()
    doc_number = DocNumberValidation()
    g_amount = AmountsValidation()
    s_supply = AmountsValidation()
    n_id = NIDValidation() 
    p_id = PIDValidation() 
    request_number = RequestNumberValidation()

    def __init__( self, gr_code = 0 , gr_name = 'z', g_code = 0, g_name = 'z', g_in_every_box = 0, g_reorder_point = 0, doc_number = 0,
                  g_amount = 0, g_supply = 0, n_id = 0, p_id = 0, g_unit = '', request_number = 0, msg = 'text' ) :
        
        Tk.__init__(self)
        self.gr_code = gr_code 
        self.gr_name = gr_name 
        self.g_code = g_code 
        self.g_name = g_name 
        self.g_in_every_box = g_in_every_box
        self.g_reorder_point = g_reorder_point
        self.doc_number = doc_number 
        self.doc_type = ''
        self.g_amount = g_amount
        self.g_supply = g_supply
        self.g_row = ''
        self.g_col = ''
        self.g_num = 0
        self.n_id = n_id 
        self.p_id = p_id
        self.g_unit = g_unit
        self.request_number = request_number
        self.current_doc_list1 = []
        self.current_doc_list2 = [] 
        self.msg = msg 
        self.user_n = 'z' 
        self.pass_w = 'z' 
        self.photo_path = ''
        self.photo_blob = ''
        self.current_user = []
        self.current_user_name = ''
        self.people_name_idd = []
        self.gr_codes_list = self.get_gr_codes() 
        self.gr_names_list = self.get_gr_names() 
        self.g_codes_list  = self.get_g_codes() 
        self.g_names_list  = self.get_g_names() 
        self.g_type = ''
        self.last_mes_type = ''
        self.last_weight_unit = ''
        self.g_amount = 0
        self.current_supply = 0
        self.gui()

#==========================================login page functions===========================================

    def login(self, event = None):
        '''
        log in to the program as admin or user
        '''
        if self.w2_ent1.get() != '' :
            self.user_n = self.w2_ent1.get()

            if self.w2_ent2.get != '' :
                self.pass_w = self.w2_ent2.get()

                if self.w2_cmb_var.get() != 'سمت':
                    self.pos = self.w2_cmb_var.get()

                    con = sql.connect('database.db')
                    cur = con.cursor()
                    cmd = '''SELECT * FROM people WHERE user_n = "{}"'''.format( self.user_n )
                    data = list( cur.execute( cmd ) )
                    con.close() 

                    if len(data) == 1 :
                        if self.user_n == data[0][1] and self.pass_w == data[0][2] and self.pos == data[0][5] : 

                            self.current_user_name = data[0][4] 

                            if self.pos == 'انباردار' :
                                self.current_user_lbl.config( text = '{} - {}'.format( data[0][4], data[0][5] ) )
                                self.set_admin_page()
                            elif self.pos == 'کارمند' :
                                self.current_user_lbl.config( text = '{} - {}'.format( data[0][4], data[0][5] ) ) 
                                self.set_user_page()

                            self.current_user = data
                            self.deiconify()
                            self.win2.withdraw()

                        else:
                            messagebox.showerror('!خطا', '!اطلاعات واردشده صحیح نیست')
                            self.w2_ent1.focus()
                    else:
                        messagebox.showerror('!خطا', '!اطلاعات واردشده صحیح نیست')
                        self.w2_ent1.focus()


                else:
                    messagebox.showerror('!خطا', '!سِمت را انتخاب کنید')
                    self.w2_cmb.focus()


            else:
                messagebox.showerror('Error!', 'رمز عبور را وارد کنید')
                self.w2_ent2.focus()

        else:
            messagebox.showerror('Error!', '!نام کاربری را وارد کنید')
            self.w2_ent1.focus()
        




#================================================= initializing functions =================================================
    def get_gr_codes(self):
        '''
        updates the list of groups codes once a groupe is defined
        '''
        temp = []
        con = sql.connect('database.db')
        cur = con.cursor()
        data = list( cur.execute( 'SELECT gr_code FROM groups' ) )
        con.close() 
        for i in data :
            temp.append(i[0])
        self.gr_codes_list = temp
        return self.gr_codes_list
    
    def get_gr_names(self):
        '''
        updates the list of groups names once a groupe is defined
        '''
        temp = []
        con = sql.connect('database.db')
        cur = con.cursor()
        data = list( cur.execute( 'SELECT gr_name FROM groups' ) )
        con.close()
        for i in data :
            temp.append(i[0])
        self.gr_names_list = temp
        return self.gr_names_list

    def get_g_codes(self):
        '''
        updates the list of goods codes once a groupe is defined
        '''
        temp = []
        con = sql.connect('database.db')
        cur = con.cursor()
        data = list( cur.execute( 'SELECT g_code FROM goods' ) )
        con.close()
        for i in data :
            temp.append(i[0])
        self.g_codes_list = temp
        return self.g_codes_list 
    
    def get_g_names(self): 
        '''
        updates the list of goods codes once a groupe is defined
        '''
        temp = []
        con = sql.connect('database.db')
        cur = con.cursor()
        data = list( cur.execute( 'SELECT g_name FROM goods' ) )
        con.close() 
        for i in data :
            temp.append(i[0])
        self.g_names_list = temp
        return self.g_names_list

  
#================================================ read and write binary functions ==========================================
    def read_binary(self, file_path):
        '''
        reads the file in binary mode and stores it in data parameter to save in database
        '''
        with open( file_path, 'rb' ) as f:
            data = f.read()
        return data

    def write_binary(self, data, file_path):
        '''
        recieves a data in binary code and writes it to a file and stores in the path
        the file can be read usin relatad programs
        '''
        with open( file_path, 'wb' ) as f:
            f.write( data )



#================================================ warehouse stock functions ===============================================
    def cmb012_show_type_func( self, event = None ):
        
        if self.cmb012_show_type_var.get() == 'به تفکیک ردیف': 
            self.btn012_show.config( state = 'disabled' )
            self.lbl012_row.pack( side = RIGHT )
            self.cmb012_row_var.set('...')
            self.cmb012_row.pack( side = RIGHT ) 
            self.cmb012_row.focus() 
        else:
            self.lbl012_row.pack_forget()
            self.cmb012_row.pack_forget()  
            self.btn012_show.config( state = 'normal' )
            self.btn012_show.focus() 
    
    def cmb012_row_func( self , event = None ):
        self.btn012_show.config( state = 'normal' )
        self.btn012_show.focus()
    

    def show_warehouse_stock( self, event = None ):
        
        for i in self.table012.get_children(): 
            self.table012.delete(i)

        if self.cmb012_show_type_var.get() == 'موجودی کل انبار' : 
            con = sql.connect('database.db')
            cur = con.cursor()
            data = list(cur.execute('SELECT * FROM stock'))
            con.close()

            temp = [] 
            for i in data:
                j = list(i)
                j.reverse()
                temp.append(j)
            data = temp

            for i in range(len(data)):
                if i%2 == 0 :
                    self.table012.insert( parent = '', index = END , value = data[i] , tags = ('evenrow',) )
                else:
                    self.table012.insert( parent = '', index = END , value = data[i] , tags = ('oddrow',) )
        
        elif self.cmb012_show_type_var.get() == 'نیازمند تجدید سفارش' : 
            con = sql.connect('database.db')
            cur = con.cursor()
            data = list(cur.execute('SELECT * FROM stock'))
            con.close()

            temp1 = [] 
            for i in data:
                j = list(i)
                j.reverse()
                temp1.append(j)
            data = temp1

            temp = [] 
            for i in data:
                if i[3] < i[1] :
                    temp.append(i)

            for i in range(len(temp)):
                if i%2 == 0 :
                    self.table012.insert( parent = '', index = END , value = temp[i] , tags = ('evenrow',) )
                else:
                    self.table012.insert( parent = '', index = END , value = temp[i] , tags = ('oddrow',) )
        
        else : 
            g_row = self.cmb012_row_var.get()

            con = sql.connect('database.db')
            cur = con.cursor()
            data = list( cur.execute( 'SELECT * FROM stock' ) ) 
            con.close() 

            temp1 = [] 
            for i in data:
                j = list(i)
                j.reverse()
                temp1.append(j)
            data = temp1

            temp = [] 
            for i in data:
                try:
                    if i[0][0] == g_row:
                        temp.append(i)
                except:
                    pass


            if temp: 
                for i in range(len(temp)):
                    if i%2 == 0 :
                        self.table012.insert( parent = '', index = END , value = temp[i] , tags = ('evenrow',) )
                    else:
                        self.table012.insert( parent = '', index = END , value = temp[i] , tags = ('oddrow',) )

            else:
                messagebox.showerror( 'Error!' , '!کالایی در این ردیف وجود ندارد' ) 


        self.cmb012_show_type.focus()


#================================================ requests management page ================================================
    def table032_a_select(self, event = None ):
        
        for i in self.table032_b.get_children():
            self.table032_b.delete(i) 
        
        selected = self.table032_a.focus() 
        values = self.table032_a.item( selected, 'values' ) 
        self.request_number = values[2] 
        self.rq_name = values[1]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT * FROM requests WHERE request_number = {}'.format( self.request_number ) 
        data = list(cur.execute( cmd )) 
        con.close() 

        self.rq_pid = data[0][2] 
        time = values[0] 

        self.lbl032_request_number1.config( text = self.request_number )
        self.lbl032_rq_name1.config( text = self.rq_name )
        self.lbl032_p_id1.config( text = self.rq_pid )
        self.lbl032_time1.config( text = time ) 

        for i in range( len( data ) ) :

            self.g_code = data[i][3]
            self.g_name = data[i][4]
            self.g_amount = int( data[i][5] )
            self.g_unit = data[i][6]
            note = data[i][7] 

            con = sql.connect('database.db') 
            cur = con.cursor()
            cmd = 'SELECT g_supply, g_reorder_point FROM stock WHERE g_code = {}'.format( self.g_code ) 
            temp1 = list(cur.execute( cmd )) 
            con.close() 

            self.g_supply = temp1[0][0]
            self.g_reorder_point = temp1[0][1] 

            j = i+1

            temp = [self.g_reorder_point, self.g_supply, note, self.g_unit, self.g_amount, self.g_name, self.g_code, j ]
            if j%2 == 0 :
                self.table032_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            else: 
                self.table032_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 

        self.ent032_note2.config( state = 'normal' )        
        self.btn032_approve.config( state = 'normal' )
        self.btn032_reject.config( state = 'normal' )


    def reject_request(self, event = None ):
        
        now = dt.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        note2 = self.ent032_note2.get() 

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = '''UPDATE requests SET status = "رد شده", admin = "{}", note2 = "{}", time2 = "{}"
                 WHERE request_number = {}'''.format( self.current_user_name, note2, now, self.request_number ) 
        cur.execute( cmd )
        con.commit() 
        con.close() 
        
        self.scnd_btn032()
        self.scnd_btn032() 

    def approve_request(self, event = None ):

        now = dt.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        note2 = self.ent032_note2.get() 

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = '''UPDATE requests SET status = "تایید شده", admin = "{}", note2 = "{}", time2 = "{}"
                 WHERE request_number = {}'''.format( self.current_user_name, note2, now, self.request_number ) 
        cur.execute( cmd )
        con.commit() 
        con.close() 
        
        self.scnd_btn032()
        self.scnd_btn032() 



    def table033_a_select(self, event = None ):

        for i in self.table033_b.get_children():
            self.table033_b.delete(i) 
        
        selected = self.table033_a.focus() 
        values = self.table033_a.item( selected, 'values' ) 

        self.request_number = values[4] 
        self.rq_name = values[3]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT * FROM requests WHERE request_number = {}'.format( self.request_number ) 
        data = list(cur.execute( cmd )) 
        con.close() 

        self.rq_pid = data[0][2] 
        time = values[2] 
        note2 = data[0][-2] 
        self.lbl033_note21.config( text = note2 )

        self.lbl033_request_number1.config( text = self.request_number )
        self.lbl033_rq_name1.config( text = self.rq_name )
        self.lbl033_p_id1.config( text = self.rq_pid )
        self.lbl033_time1.config( text = time ) 

        for i in range( len( data ) ) :

            self.g_code = data[i][3]
            self.g_name = data[i][4]
            self.g_amount = int( data[i][5] )
            self.g_unit = data[i][6]
            note = data[i][7] 

            con = sql.connect('database.db') 
            cur = con.cursor()
            cmd = 'SELECT g_supply, g_reorder_point FROM stock WHERE g_code = {}'.format( self.g_code ) 
            temp1 = list(cur.execute( cmd )) 
            con.close() 

            self.g_supply = temp1[0][0]
            self.g_reorder_point = temp1[0][1] 

            j = i+1

            temp = [self.g_reorder_point, self.g_supply, note, self.g_unit, self.g_amount, self.g_name, self.g_code, j ]
            if j%2 == 0 :
                self.table033_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            else: 
                self.table033_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 
        
        self.btn033_submit.config( state = 'normal' )

    
    def btn033_submit_func(self, event = None ):
        
        data = [] 
        for i in self.table033_b.get_children():
            temp = self.table033_b.item( i, 'values' )
            data.append( temp ) 
        
        self.doc_number = self.lbl033_request_number1['text']
        self.doc_type   = 'Exit'
        self.admin_name = self.current_user_name 
        self.delivery_name = self.lbl033_rq_name1['text']
        self.delivery_idd  = self.lbl033_p_id1['text']
        now = dt.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')

        for i in data:
            self.g_code = i[6] 
            self.g_name = i[5] 
            self.g_amount = i[4] 
            self.g_unit   = i[3] 
            note = i[2]

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'SELECT gr_code, gr_name, g_type FROM goods WHERE g_code = {}'.format( self.g_code ) 
            g   = list(cur.execute( cmd )) 
            con.close() 

            self.gr_code = g[0][0] 
            self.gr_name = g[0][1] 
            self.g_type  = g[0][2] 

            doc_temp = [ self.doc_number, self.doc_type, self.g_code, self.g_name, self.gr_code, self.gr_name, self.g_type, self.g_amount,
                         self.g_unit, note, self.admin_name, self.delivery_name, self.delivery_idd, now ]
            
            stock_temp = [ self.g_code, self.g_amount ]

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ''' INSERT INTO docs (doc_number, doc_type, g_code, g_name, gr_code, gr_name, g_type, g_amount, g_unit, note,
                      admin_name, delivery_name, delivery_idd, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            cur.execute( cmd, doc_temp ) 
            con.commit()
            con.close()

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ' SELECT g_supply FROM stock WHERE g_code = {} '.format(self.g_code)
            current_supply = list(cur.execute(cmd))[0][0]
            con.commit() 
            con.close() 

            new_current_supply = float(current_supply) - float(self.g_amount)

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'UPDATE stock SET g_supply = {} WHERE g_code = {}'.format(new_current_supply, self.g_code)
            cur.execute(cmd) 
            con.commit() 
            con.close() 
    

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = '''UPDATE requests SET status = "تحویل شده", admin = "{}", time2 = "{}"
                     WHERE request_number = {}'''.format( self.current_user_name, now, self.request_number ) 
            cur.execute( cmd )
            con.commit() 
            con.close() 
        

        self.scnd_btn033()
        self.scnd_btn033() 
        



    def table034_a_select(self, event = None ):

        for i in self.table034_b.get_children():
            self.table034_b.delete(i) 
        
        selected = self.table034_a.focus() 
        values = self.table034_a.item( selected, 'values' ) 

        self.request_number = values[4] 
        self.rq_name = values[3]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT * FROM requests WHERE request_number = {}'.format( self.request_number ) 
        data = list(cur.execute( cmd )) 
        con.close() 

        self.rq_pid = data[0][2] 
        time = values[2] 
        note2 = data[0][-2] 
        self.lbl034_note21.config( text = note2 )

        self.lbl034_request_number1.config( text = self.request_number )
        self.lbl034_rq_name1.config( text = self.rq_name )
        self.lbl034_p_id1.config( text = self.rq_pid )
        self.lbl034_time1.config( text = time ) 

        for i in range( len( data ) ) :

            self.g_code = data[i][3]
            self.g_name = data[i][4]
            self.g_amount = int( data[i][5] )
            self.g_unit = data[i][6]
            note = data[i][7] 

            con = sql.connect('database.db') 
            cur = con.cursor()
            cmd = 'SELECT g_supply, g_reorder_point FROM stock WHERE g_code = {}'.format( self.g_code ) 
            temp1 = list(cur.execute( cmd )) 
            con.close() 

            self.g_supply = temp1[0][0]
            self.g_reorder_point = temp1[0][1] 

            j = i+1

            temp = [self.g_reorder_point, self.g_supply, note, self.g_unit, self.g_amount, self.g_name, self.g_code, j ]
            if j%2 == 0 :
                self.table034_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            else: 
                self.table034_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 
     


    def table035_a_select(self, event = None ): 
        
        for i in self.table035_b.get_children():
            self.table035_b.delete(i) 
        
        selected = self.table035_a.focus() 
        values = self.table035_a.item( selected, 'values' ) 

        self.request_number = values[4] 
        self.rq_name = values[3]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT * FROM requests WHERE request_number = {}'.format( self.request_number ) 
        data = list(cur.execute( cmd )) 
        con.close() 

        self.rq_pid = data[0][2] 
        time = values[2] 
        note2 = data[0][-2] 
        self.lbl035_note21.config( text = note2 )

        self.lbl035_request_number1.config( text = self.request_number )
        self.lbl035_rq_name1.config( text = self.rq_name )
        self.lbl035_p_id1.config( text = self.rq_pid )
        self.lbl035_time1.config( text = time ) 

        for i in range( len( data ) ) :

            self.g_code = data[i][3]
            self.g_name = data[i][4]
            self.g_amount = int( data[i][5] )
            self.g_unit = data[i][6]
            note = data[i][7] 

            j = i+1

            temp = [ note, self.g_unit, self.g_amount, self.g_name, self.g_code, j ]
            if j%2 == 0 :
                self.table035_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            else: 
                self.table035_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 



#================================================ goods in / out page =====================================================
    def ent042_delivery_doc_func(self, event = None ): 

        self.doc_number = self.ent042_delivery_doc.get() 
        if self.doc_number != 0 :
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'SELECT doc_number FROM docs'
            temp = list(cur.execute(cmd))
            con.close
            flg = True
            for i in temp :
                if self.doc_number == i[0] :
                    flg = False
                    self.msg = ('!شماره سند تکراری است') 
                    messagebox.showerror('Error!', self.msg ) 
                    break
            if flg :
                self.cmb042_delivery.config( state = 'readonly' )
                self.cmb042_delivery.focus()
        else:            
            messagebox.showerror('Error', self.msg)

    def ent042_delivery2_func(self, event = None ):
        self.n_id = self.ent042_delivery2.get()
        if self.n_id != 0:
            self.ent042_g_code.focus()
            self.ent042_g_code.config( state = 'normal' )
        else:           
            messagebox.showerror('Error', self.msg)


    def delivery_goods_search( self, event = None ): 
        self.g_code = self.ent042_g_code.get()
        if self.g_code != 0 : 
            con = sql.connect('database.db') 
            cur = con.cursor() 
            cmd = ' SELECT * FROM goods WHERE g_code = {} '.format( self.g_code ) 
            data = list( cur.execute( cmd ) ) 
            con.close() 
            if len(data) == 1 :
                self.write_binary(data[0][-1], 'z.png')
                img1 = Image.open('z.png')
                img1 = img1.resize((110,110))
                self.g_img = ImageTk.PhotoImage( img1 )
                self.imglbl042.config(image = self.g_img)
                self.imglbl042.image = self.g_img

                data = data[0][:-1]
                self.lbl042_g_name1.config( text = data[1] )
                self.lbl042_gr_code1.config( text = data[2] )
                self.lbl042_gr_name1.config( text = data[3] )
                self.lbl042_g_type1.config( text = data[4] )

                if data[5] == 'تعدادی':
                    self.lbl042_unit.config( text = 'عدد' )

                elif data[5] == 'وزنی':
                    self.lbl042_unit.config( text = data[6] )

                elif data[5] == 'بستۀ تعدادی':
                    self.lbl042_unit.config( text = 'بستۀ {} تایی'.format(data[7]) )

                elif data[5] == 'بستۀ وزنی' : 
                    if data[6] == 'گرم' : 
                        self.lbl042_unit.config( text = 'بستۀ {} گرمی'.format(data[7]) )
                    elif data[6] == 'کیلوگرم' : 
                        self.lbl042_unit.config( text = 'بستۀ {} کیلوگرمی'.format(data[7]) )
                    elif data[6] == 'تن' : 
                        self.lbl042_unit.config( text = 'بستۀ {} تنی'.format(data[7]) )

                self.lbl042_unit.grid( row = 1 , column = 1 , padx = 5 )
                self.ent042_amount.config( state = 'normal' )
                self.ent042_amount.focus() 
            else:
                self.msg = '!کالایی با این کد ثبت نشده است'
                messagebox.showerror('Error!', self.msg)
        else:
            messagebox.showerror('Error!', self.msg )

    def cmb042_delivery_setting_forget(self):
        self.lbl042_delivery1.grid_forget()
        self.cmb042_delivery1.grid_forget()
        self.lbl042_delivery2.config( text = '' )
        self.lbl042_delivery2.grid_forget()
        self.lbl042_delivery3.config( text = '' )
        self.lbl042_delivery3.grid_forget()
        self.ent042_delivery1.delete( 0 , END )
        self.ent042_delivery1.grid_forget()
        self.ent042_delivery2.delete( 0 , END )
        self.ent042_delivery2.grid_forget()
        self.ent042_g_code.delete( 0 , END )
        self.ent042_g_code.config( state = 'disabled' )


    def cmb042_delivery1_setting( self, event = None ):
        self.lbl042_delivery2.config( text = 'کد پرسنلی' ) 
        self.lbl042_delivery2.grid( row = 1 , column = 2 ) 
        name = self.cmb042_delivery1_var.get()
        idd = ''
        for i in self.people_name_idd :
            if i[1] == name:
                idd = i[0]
                break
        self.lbl042_delivery3.config( text = idd )
        self.lbl042_delivery3.grid( row = 1 , column = 1 )
        self.ent042_g_code.config( state = 'normal' )
        self.ent042_g_code.focus()


    def ent042_delivery1_func(self, event = None ):
        name = self.ent042_delivery1.get()
        if name:
            self.ent042_delivery2.config( state = 'normal' )
            self.ent042_delivery2.focus() 
        else:
            messagebox.showerror('Error', 'نام و نام خانوادگی را وارد کنید')


    def cmb042_delivery_setting( self, event = None ):
        self.cmb042_delivery_setting_forget() 
        if self.cmb042_delivery_var.get() == 'پرسنل مجموعه':
            self.lbl042_delivery1.grid( row = 1 , column = 4 ) 
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ''' SELECT idd , full_name FROM people WHERE position = 'کارمند' '''
            self.people_name_idd = list( cur.execute( cmd ) )
            con.close()
            options = []
            for i in self.people_name_idd:
                options.append(i[1]) 
            self.cmb042_delivery1.config( values = options ) 
            self.cmb042_delivery1.grid( row = 1 , column = 3 )
            self.cmb042_delivery1.focus() 
        else:
            self.lbl042_delivery1.grid( row = 1 , column = 4 ) 
            self.ent042_delivery1.grid( row = 1 , column = 3 )
            self.ent042_delivery1.focus()
            self.lbl042_delivery2.config( text = 'کد ملی' )
            self.lbl042_delivery2.grid( row = 1 , column = 2 )
            self.ent042_delivery2.grid( row = 1 , column = 1 )


    def ent042_amount_func( self, event = None ):
        self.g_amount = self.ent042_amount.get()
        if self.g_amount != 0 :
            self.cmb042_row.config( state = 'readonly' )
            self.cmb042_row.focus()
        else:
            messagebox.showerror('Error!', self.msg )


    def cmb042_row_func( self, event = None ):
        self.cmb042_col.config( state = 'readonly' )
        self.cmb042_col.focus()


    def cmb042_col_func( self, event = None ):
        self.cmb042_num.config( state = 'readonly' )
        self.cmb042_num.focus()


    def cmb042_num_func( self, event = None ):
        self.ent042_note.config( state = 'normal' )
        self.ent042_note.focus()
        self.btn042_add_to_list.config( state = 'normal' )


    def delivery_add_to_list(self, event = None ): 
        self.doc_type = 'Enter'
        self.g_code = self.ent042_g_code.get() 
        self.g_name = self.lbl042_g_name1['text'] 
        self.g_type = self.lbl042_g_type1['text']
        self.gr_code = self.lbl042_gr_code1['text']
        self.gr_name = self.lbl042_gr_name1['text'] 
        self.amount = self.ent042_amount.get()
        self.g_unit = self.lbl042_unit['text']
        self.g_row = self.cmb042_row_var.get()
        self.g_col = self.cmb042_col_var.get()
        self.g_num = self.cmb042_num_var.get()
        note = self.ent042_note.get()

        i = 0
        for j in self.table042_b.get_children() :
            i = i + 1

        temp = [ note, self.g_unit, self.amount, self.g_name, self.g_code ]
        if i%2 == 0 :
            self.table042_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
        else:
            self.table042_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )

        if self.cmb042_delivery1.winfo_ismapped():
            delivery_name = self.cmb042_delivery1_var.get()
            delivery_id = self.lbl042_delivery3['text']
        else:
            delivery_name = self.ent042_delivery1.get() 
            delivery_id = self.ent042_delivery2.get() 


        lst1 = [ self.doc_number, self.doc_type, self.g_code, self.g_name, self.gr_code, self.gr_name, self.g_type, self.amount,
                 self.g_unit, note, self.current_user_name, delivery_name, delivery_id ] 
        self.current_doc_list1.append(lst1) 

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT g_reorder_point FROM goods WHERE g_code = {}'.format(self.g_code)
        data = list(cur.execute(cmd))
        con.commit()
        con.close() 

        self.g_reorder_point = data[0][0] 
        address = '{},{},{}'.format(self.g_row, self.g_col, self.g_num)

        lst2 = [self.g_code, self.amount, address]
        self.current_doc_list2.append(lst2)

        self.ent042_g_code.delete( 0 , END )
        self.lbl042_g_name1['text'] = '' 
        self.lbl042_g_type1['text'] = '' 
        self.lbl042_gr_code1['text'] = '' 
        self.lbl042_gr_name1['text'] = '' 
        self.ent042_amount.delete( 0 , END )
        self.cmb042_row_var.set('')
        self.cmb042_col_var.set('')
        self.cmb042_num_var.set('')
        self.ent042_note.delete( 0 , END )
        self.ent042_amount.config( state = 'disabled' )
        self.cmb042_row.config( state = 'disabled' )
        self.cmb042_col.config( state = 'disabled' )
        self.cmb042_num.config( state = 'disabled' )
        self.lbl042_unit.config( text = '' )
        self.ent042_note.config( state = 'disabled' )
        self.imglbl042.config( image = self.upload_img )
        self.btn042_add_to_list.config( state = 'disabled' )
        self.ent042_g_code.focus()
        self.btn042_delete_list.config( state = 'normal' )
        self.btn042_submit.config( state = 'normal' )


    def btn042_delete_list_func(self, event = None ):
        for i in self.table042_b.get_children():
            self.table042_b.delete(i)
        self.current_doc_list1 = []
        self.current_doc_list2 = []
        self.btn042_delete_list.config( state = 'disabled' )
        self.btn042_submit.config( state = 'disabled' ) 


    def submit_doc( self, event = None ):
        for i in self.table042_b.get_children():
            self.table042_b.delete(i)

        temp1 = self.current_doc_list1

        now = dt.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        for i in temp1:
            i.append(now) 

        for i in range(len(temp1)) :
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ''' INSERT INTO docs (doc_number, doc_type, g_code, g_name, gr_code, gr_name, g_type, g_amount, g_unit, note,
                    admin_name, delivery_name, delivery_idd, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            cur.execute(cmd, temp1[i]) 
            con.commit()
            con.close()

        temp2 = self.current_doc_list2  

        for i in range(len(temp2)) :
            g_code = temp2[i][0]
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ' SELECT g_supply FROM stock WHERE g_code = {} '.format(g_code)
            last_amount = list(cur.execute(cmd))[0][0]
            con.commit() 
            con.close() 
            new_amount = temp2[i][1]
            amount = float(last_amount) + float(new_amount) 
            address = temp2[i][2]
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'UPDATE stock SET g_supply = {} , g_address = "{}" WHERE g_code = {}'.format(amount, address, g_code)
            cur.execute(cmd) 
            con.commit() 
            con.close() 

        self.frm042_clear()

        self.current_doc_list1 = [] 
        self.current_doc_list2 = [] 

        self.btn042_submit.config( state = 'disabled' )
        self.btn042_delete_list.config( state = 'disabled' )



#********************** صفحه خروج کالا **************************

    def ent043_take_doc_func(self, event = None ): 

        self.doc_number = self.ent043_take_doc.get() 
        if self.doc_number != 0 :
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'SELECT doc_number FROM docs'
            temp = list(cur.execute(cmd))
            con.close
            flg = True
            for i in temp :
                if self.doc_number == i[0] :
                    flg = False
                    self.msg = ('!شماره سند تکراری است') 
                    messagebox.showerror('Error!', self.msg ) 
                    break
            if flg :
                self.cmb043_take.config( state = 'readonly' )
                self.cmb043_take.focus()
        else:            
            messagebox.showerror('Error', self.msg)


    def cmb043_take_setting_forget(self):
        self.lbl043_take1.grid_forget()
        self.cmb043_take1.grid_forget()
        self.lbl043_take2.config( text = '' )
        self.lbl043_take2.grid_forget()
        self.lbl043_take3.config( text = '' )
        self.lbl043_take3.grid_forget()
        self.ent043_take1.delete( 0 , END )
        self.ent043_take1.grid_forget()
        self.ent043_take2.delete( 0 , END )
        self.ent043_take2.grid_forget()
        self.ent043_g_code.delete( 0 , END )
        self.ent043_g_code.config( state = 'disabled' )


    def cmb043_take_setting( self, event = None ):
        self.cmb043_take_setting_forget() 
        if self.cmb043_take_var.get() == 'پرسنل مجموعه':
            self.lbl043_take1.grid( row = 1 , column = 4 ) 
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ''' SELECT idd , full_name FROM people WHERE position = 'کارمند' '''
            self.people_name_idd = list( cur.execute( cmd ) )
            con.close()
            options = []
            for i in self.people_name_idd:
                options.append(i[1]) 
            self.cmb043_take1.config( values = options ) 
            self.cmb043_take1.grid( row = 1 , column = 3 )
            self.cmb043_take1.focus() 
        else:
            self.lbl043_take1.grid( row = 1 , column = 4 ) 
            self.ent043_take1.grid( row = 1 , column = 3 )
            self.ent043_take1.focus()
            self.lbl043_take2.config( text = 'کد ملی' )
            self.lbl043_take2.grid( row = 1 , column = 2 )
            self.ent043_take2.grid( row = 1 , column = 1 )


    def cmb043_take1_setting( self, event = None ):
        self.lbl043_take2.config( text = 'کد پرسنلی' ) 
        self.lbl043_take2.grid( row = 1 , column = 2 ) 
        name = self.cmb043_take1_var.get()
        idd = ''
        for i in self.people_name_idd :
            if i[1] == name:
                idd = i[0]
                break
        self.lbl043_take3.config( text = idd )
        self.lbl043_take3.grid( row = 1 , column = 1 )
        self.ent043_g_code.config( state = 'normal' )
        self.ent043_g_code.focus()

    def ent043_take1_func(self, event = None ):
        name = self.ent043_take1.get()
        if name:
            self.ent043_take2.config( state = 'normal' )
            self.ent043_take2.focus() 
        else:
            messagebox.showerror('Error', 'نام و نام خانوادگی را وارد کنید')


    def ent043_take2_func(self, event = None ):
        self.n_id = self.ent043_take2.get()
        if self.n_id != 0:
            self.ent043_g_code.focus()
            self.ent043_g_code.config( state = 'normal' )
        else:           
            messagebox.showerror('Error', self.msg)


    def take_goods_search( self, event = None ): 
        self.g_code = self.ent043_g_code.get()
        if self.g_code != 0 : 
            
            con = sql.connect('database.db') 
            cur = con.cursor() 
            cmd = ' SELECT g_supply, g_address, g_reorder_point FROM stock WHERE g_code = {} '.format( self.g_code ) 
            data = list( cur.execute( cmd ) ) 
            con.close() 

            self.current_supply = data[0][0]
            self.g_address = data[0][1] 
            self.g_reorder_point = data[0][2]

            if self.current_supply > 0 :
                con = sql.connect('database.db') 
                cur = con.cursor() 
                cmd = ' SELECT * FROM goods WHERE g_code = {} '.format( self.g_code ) 
                data = list( cur.execute( cmd ) ) 
                con.close() 
                if len(data) == 1 :
                    self.write_binary(data[0][-1], 'z.png')
                    img1 = Image.open('z.png')
                    img1 = img1.resize((110,110))
                    self.g_img = ImageTk.PhotoImage( img1 )
                    self.imglbl043.config(image = self.g_img)
                    self.imglbl043.image = self.g_img

                    data = data[0][:-1]
                    self.lbl043_g_name1.config( text = data[1] )
                    self.lbl043_gr_code1.config( text = data[2] )
                    self.lbl043_gr_name1.config( text = data[3] )
                    self.lbl043_g_type1.config( text = data[4] )

                    if data[5] == 'تعدادی':
                        self.lbl043_unit.config( text = 'عدد' )

                    elif data[5] == 'وزنی':
                        self.lbl043_unit.config( text = data[6] )

                    elif data[5] == 'بستۀ تعدادی':
                        self.lbl043_unit.config( text = 'بستۀ {} تایی'.format(data[7]) )

                    elif data[5] == 'بستۀ وزنی' : 
                        if data[6] == 'گرم' : 
                            self.lbl043_unit.config( text = 'بستۀ {} گرمی'.format(data[7]) )
                        elif data[6] == 'کیلوگرم' : 
                            self.lbl043_unit.config( text = 'بستۀ {} کیلوگرمی'.format(data[7]) )
                        elif data[6] == 'تن' : 
                            self.lbl043_unit.config( text = 'بستۀ {} تنی'.format(data[7]) )
                    

                    self.lbl043_current_supply.config( text = self.current_supply )
                    self.lbl043_address1.config( text = self.g_address )              
                    self.lbl043_g_reorder_point.config( text = self.g_reorder_point )
                    self.lbl043_unit_rp.config( text = self.lbl043_unit['text'] ) 
                    self.lbl043_unit_am.config( text = self.lbl043_unit['text'] ) 
                    self.ent043_g_amount.config( state = 'normal' )
                    self.ent043_g_amount.focus() 
                else:
                    msg = '!کالایی با این کد ثبت نشده است'
                    messagebox.showerror('Error!', msg)
            else:
                msg = '!موجودی فعلی این کالا صفر است'
                messagebox.showerror('Error!', msg)
        else:
            messagebox.showerror('Error!', self.msg )


    def ent043_g_amount_func( self, event = None ):
        self.g_amount = self.ent043_g_amount.get()
        if self.g_amount != 0 :
            if self.g_amount <= self.current_supply:
                self.ent043_note.config( state = 'normal' )
                self.ent043_note.focus()
                self.btn043_add_to_list.config( state = 'normal' )
            else:
                msg = '!تعداد/مقدار بیشتر از موجودی فعلی است' 
                messagebox.showerror( 'Error!', msg )
        else:
            messagebox.showerror('Error!', 'self.msg' )


    def take_add_to_list(self, event = None ): 

        self.g_amount = self.ent043_g_amount.get()
        self.doc_type = 'Exit'
        self.g_code = self.ent043_g_code.get() 
        self.g_name = self.lbl043_g_name1['text'] 
        self.g_type = self.lbl043_g_type1['text']
        self.gr_code = self.lbl043_gr_code1['text']
        self.gr_name = self.lbl043_gr_name1['text'] 
        self.g_unit = self.lbl043_unit['text']
        note = self.ent043_note.get() 

        i = 0
        for j in self.table043_b.get_children() :
            i = i + 1

        temp = [ note, self.g_unit, self.g_amount, self.g_name, self.g_code ]
        if i%2 == 0 :
            self.table043_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
        else:
            self.table043_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )

        if self.cmb043_take1.winfo_ismapped():
            take_name = self.cmb043_take1_var.get()
            take_id = self.lbl043_take3['text']
        else:
            take_name = self.ent043_take1.get() 
            take_id = self.ent043_take2.get() 

        # list for docs table
        lst1 = [ self.doc_number, self.doc_type,  self.g_code, self.g_name, self.gr_code, self.gr_name, self.g_type, self.g_amount,
                 self.g_unit, note, self.current_user_name, take_name, take_id ] 
        self.current_doc_list1.append(lst1) 

        # list for stock table 
        lst2 = [ self.g_code, self.g_amount ]
        self.current_doc_list2.append(lst2)

        self.ent043_g_code.delete( 0 , END )
        self.lbl043_g_name1.config( text = '' )
        self.lbl043_g_type1.config( text = '' )
        self.lbl043_gr_code1.config( text = '' )
        self.lbl043_gr_name1.config( text = '' )
        self.ent043_g_amount.delete( 0 , END )
        self.ent043_note.delete( 0 , END )
        self.ent043_g_amount.config( state = 'disabled' )
        self.lbl043_current_supply.config( text = '' )
        self.lbl043_g_reorder_point.config( text = '' )
        self.lbl043_unit.config( text = '' )
        self.lbl043_unit_rp.config( text = '' )
        self.lbl043_unit_am.config( text = '' )
        self.lbl043_address1.config( text = '' )
        self.ent043_note.config( state = 'disabled' )
        self.imglbl043.config( image = self.upload_img )
        self.btn043_add_to_list.config( state = 'disabled' )
        self.ent043_g_code.focus()
        self.btn043_delete_list.config( state = 'normal' )
        self.btn043_take_submit.config( state = 'normal' )
    

    def btn043_delete_list_func(self, event = None ):
        for i in self.table043_b.get_children():
            self.table043_b.delete(i)
        self.current_doc_list1 = []
        self.current_doc_list2 = []
        self.btn043_delete_list.config( state = 'disabled' )
        self.btn043_take_submit.config( state = 'disabled' ) 


    def btn043_take_submit_doc_func( self, event = None ):
        for i in self.table043_b.get_children():
            self.table043_b.delete(i)

        temp1 = self.current_doc_list1

        now = dt.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        for i in temp1:
            i.append(now) 

        for i in range(len(temp1)) :
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ''' INSERT INTO docs (doc_number, doc_type, g_code, g_name, gr_code, gr_name, g_type, g_amount, g_unit, note,
                    admin_name, delivery_name, delivery_idd, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            cur.execute(cmd, temp1[i]) 
            con.commit()
            con.close()


        temp2 = self.current_doc_list2  

        for i in range(len(temp2)) :
            g_code = temp2[i][0]
            amount = temp2[i][1] 
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = ' SELECT g_supply FROM stock WHERE g_code = {} '.format(g_code)
            current_supply = list(cur.execute(cmd))[0][0]
            con.commit() 
            con.close() 

            new_current_supply = float(current_supply) - float(amount)

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'UPDATE stock SET g_supply = {} WHERE g_code = {}'.format(new_current_supply, g_code)
            cur.execute(cmd) 
            con.commit() 
            con.close() 

        self.frm043_clear()

        self.current_doc_list1 = [] 
        self.current_doc_list2 = [] 

        self.btn043_take_submit.config( state = 'disabled' )
        self.btn043_delete_list.config( state = 'disabled' )     



#*********************** صفحه تاریخچه ورود و خروج *************************
    
    def table044_a_select(self, event = None ) :
        for i in self.table044_b.get_children():
            self.table044_b.delete(i)

        self.lbl044_doc_number1.config( text = '' )
        self.lbl044_doc_type1  .config( text = '' )
        self.lbl044_admin1     .config( text = '' )
        self.lbl044_time1      .config( text = '' )

        selected = self.table044_a.focus() 
        values   = self.table044_a.item( selected, 'values' ) 
        self.doc_number = values[4]

        self.lbl044_doc_number1.config( text = values[4] ) 


        if values[3] == 'Enter':
            self.lbl044_doc_type1  .config( text = 'ورود کالا' )
        else:
            self.lbl044_doc_type1  .config( text = 'خروج کالا' )

        self.lbl044_admin1     .config( text = values[1] )
        self.lbl044_time1      .config( text = values[2] )


        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT note, g_unit, g_amount, g_name, g_code FROM docs WHERE doc_number = {}'.format( self.doc_number )
        data = list( cur.execute( cmd ) )
        con.close() 

        temp = []         
        for i in data:
            i = list(i)
            temp.append(i)

        for i in range( len( temp) ) :
            j = i + 1
            temp[i] = temp[i] + [j]

            if j % 2 :
                self.table044_b.insert( parent = '', index = END , value = temp[i] , tags = ('evenrow',) )
            else: 
                self.table044_b.insert( parent = '', index = END , value = temp[i] , tags = ('oddrow',) )




#================================================ groups and goods page functions ==========================================
    def ent062_gr_code_func( self, event = None ):
        self.gr_code = self.ent062_gr_code.get() 
        if self.gr_code != 0 :
            temp = self.get_gr_codes()
            flg_gr = True
            for i in temp :
                if self.gr_code == i:
                    flg_gr = False
                    self.msg = '!کد گروه تکراری است'
                    break
            if flg_gr:
                self.ent062_gr_name.config( state = 'normal' )
                self.ent062_gr_name.focus()
            else:
                messagebox.showerror('Error!', self.msg )
        else:
            messagebox.showerror('Error!', self.msg )

    def ent062_gr_name_func( self, event = None):
        self.gr_name = self.ent062_gr_name.get()
        if self.gr_name != 'z' :
            temp = self.get_gr_names()
            flg_gr = True
            for i in temp :
                if self.gr_code == i:
                    flg_gr = False
                    self.msg = '!نام گروه تکراری است'
                    break
            if flg_gr:
                self.btn062_submit_group.config( state = 'normal' )
                self.btn062_submit_group.focus() 
            else:
                messagebox.showerror('Error!', self.msg )
        else:
            messagebox.showerror('Error!', self.msg )


    def submit_group(self, event = None):
        self.gr_code = self.ent062_gr_code.get()
        self.gr_name = self.ent062_gr_name.get()
        temp = [self.gr_code, self.gr_name] 
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = ''' INSERT INTO groups ( gr_code , gr_name ) VALUES (?, ?) '''
        cur.execute( cmd , temp )
        con.commit()
        con.close()
        self.ent062_gr_code.delete( 0 , END )
        self.ent062_gr_name.delete( 0 , END )
        self.ent062_gr_name.config( state = 'disabled' )
        self.btn062_submit_group.config( state = 'disabled' ) 
        self.gr_codes_list = self.get_gr_codes() 
        self.cmb062_g_gr.config( values = self.gr_codes_list )
        self.ent062_gr_code.focus()


    def cmb062_g_gr_func( self, event = None ):
        self.gr_code = self.cmb062_g_gr_var.get()
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = ' SELECT gr_name FROM groups WHERE gr_code = {} '.format( self.gr_code )
        data = list(cur.execute(cmd))
        con.commit() 
        con.close() 
        self.gr_name = data[0][0]
        self.lbl062_gr_name1.config( text = self.gr_name )
        self.ent062_g_code.config( state = 'normal' )
        self.ent062_g_code.delete( 0 , END )
        self.ent062_g_code.focus()
        self.ent062_g_name.delete( 0 , END )
        self.ent062_g_name.config( state = 'disabled' )
        self.cmb062_g_type_var.set('انتخاب کنید')
        self.cmb062_g_type.config( state = 'disabled' )
        self.cmb062_g_measuring.config( state = 'disabled' )
        self.units_map_forget()
        self.imglbl062_02.config( image = self.upload_img )
        self.btn062_g_add_photo.config( state = 'normal' )
        self.ent062_g_code.focus() 


    def ent062_g_code_func( self, event = None ):
        self.g_code = self.ent062_g_code.get()
        if self.g_code != 0 :
            temp = self.get_g_codes()
            flg_g = True 
            for i in temp:
                if self.g_code == i: 
                    flg_g = False
                    self.msg = '!کد کالا تکراری است'
                    break
            if flg_g:
                self.ent062_g_name.config( state = 'normal' )
                self.ent062_g_name.focus()
                self.btn062_g_add_photo.config( state = 'normal' )
            else:
                messagebox.showerror('Error!', self.msg )
        else:
            messagebox.showerror('Error!', self.msg )
        

    def ent062_g_name_func( self, event = None ):
        self.g_name = self.ent062_g_name.get()
        if self.g_name != 'z' :
            temp = self.get_g_names() 
            flg_g = True 
            for i in temp:
                if self.g_name == i: 
                    flg_g = False
                    self.msg = '!نام کالا تکراری است'
                    break
            if flg_g:
                self.cmb062_g_type.config( state = 'readonly' )
                self.cmb062_g_type.focus()
            else:
                messagebox.showerror('Error!', self.msg )
        else:
            messagebox.showerror('Error!', self.msg ) 


    def cmb062_g_type_func( self, event = None ):
        self.cmb062_g_measuring.config( state = 'readonly' )
        self.cmb062_g_measuring.focus()


    def cmb062_g_measuring_func(self, event = None):
        if self.cmb062_g_measuring_var.get() == 'تعدادی':
            self.units_map_forget()
            self.lbl062_g_reorder_point.grid( row = 2 , column = 3 )
            self.ent062_g_reorder_point.grid( row = 2 , column = 2 )
            self.ent062_g_reorder_point.config( state = 'normal' )
            self.ent062_g_reorder_point.focus()

        elif self.cmb062_g_measuring_var.get() == 'وزنی':
            self.units_map_forget()
            self.lbl062_g_weight_unit.grid( row = 2 , column = 3 )
            self.cmb062_g_weight_unit.grid( row = 2 , column = 2 )
            self.cmb062_g_weight_unit.focus()
            self.lbl062_g_reorder_point.grid( row = 3 , column = 3 )
            self.ent062_g_reorder_point.grid( row = 3 , column = 2 )

        elif self.cmb062_g_measuring_var.get() == 'بستۀ تعدادی':
            self.units_map_forget()
            self.lbl062_g_in_every_box.grid( row = 2 , column = 3 )
            self.ent062_g_in_every_box.grid( row = 2 , column = 2 )
            self.ent062_g_in_every_box.config( state = 'normal' )
            self.ent062_g_in_every_box.focus()
            self.lbl062_g_reorder_point.grid( row = 3 , column = 3 )
            self.ent062_g_reorder_point.grid( row = 3 , column = 2 )

        elif self.cmb062_g_measuring_var.get() == 'بستۀ وزنی':
            self.units_map_forget()
            self.lbl062_g_weight_unit.grid( row = 2 , column = 3 )
            self.cmb062_g_weight_unit.grid( row = 2 , column = 2 )
            self.cmb062_g_weight_unit.focus()
            self.lbl062_g_in_every_box.grid( row = 3 , column = 3 )
            self.ent062_g_in_every_box.grid( row = 3 , column = 2 )
            self.lbl062_g_reorder_point.grid( row = 4 , column = 3 )
            self.ent062_g_reorder_point.grid( row = 4 , column = 2 )


    def cmb062_g_weight_unit_func( self, event = None ) :
        if self.ent062_g_in_every_box.winfo_ismapped():
            self.ent062_g_in_every_box.config( state = 'normal' )
            self.ent062_g_in_every_box.focus()
        else:
            self.ent062_g_reorder_point.config( state = 'normal' )
            self.ent062_g_reorder_point.focus()


    def ent062_g_in_every_box_func( self, event = None ):
        self.g_in_every_box = self.ent062_g_in_every_box.get() 
        if self.g_in_every_box != 0 :
            self.ent062_g_reorder_point.config( state = 'normal' ) 
            self.ent062_g_reorder_point.focus() 
        else: 
            messagebox.showerror('Error!', self.msg ) 


    def ent062_g_reorder_point_func( self, event = None ):
        self.g_reorder_point = self.ent062_g_reorder_point.get()
        if self.g_reorder_point != 0 :
            self.btn062_g_submit.config( state = 'normal' ) 
            self.btn062_g_submit.focus() 
        else:
            messagebox.showerror('Error!', self.msg ) 
            

    def open_g_photo(self, event = None):
        self.photo_path = filedialog.askopenfilename( initialdir = [('photos','*.png')] )
        if self.photo_path:
            img = Image.open( self.photo_path )
            img = img.resize( (110, 110) )
            img = ImageTk.PhotoImage( img )
            self.imglbl062_02.config( image = img )
            self.imglbl062_02.image = img
            data = self.read_binary( self.photo_path )
            self.write_binary( data, 'z.png' )
            self.btn062_g_add_photo.focus()


    def units_map_forget(self):
        self.lbl062_g_reorder_point.grid_forget()
        self.lbl062_g_in_every_box.grid_forget()
        self.lbl062_g_weight_unit.grid_forget()
        self.ent062_g_reorder_point.grid_forget() 
        self.ent062_g_reorder_point.delete( 0 , END ) 
        self.ent062_g_reorder_point.config( state = 'disabled' )
        self.ent062_g_in_every_box.grid_forget()
        self.ent062_g_in_every_box.delete( 0 , END ) 
        self.ent062_g_in_every_box.config( state = 'disabled' ) 
        self.cmb062_g_weight_unit.grid_forget()
        self.cmb062_g_weight_unit_var.set('انتخاب کنید')


    def submit_goods(self, event = None): 
        self.g_code  = self.ent062_g_code.get() 
        self.g_name  = self.ent062_g_name.get() 
        self.gr_code = self.cmb062_g_gr_var.get() 
        con = sql.connect( 'database.db' ) 
        cur = con.cursor() 
        cmd = ' SELECT gr_name FROM groups WHERE gr_code = {} '.format( self.gr_code ) 
        temp = list( cur.execute( cmd ) ) 
        con.close() 
        self.gr_name = temp[0][0] 
        self.g_type      = self.cmb062_g_type_var.get()
        self.g_measuring = self.cmb062_g_measuring_var.get()
        if self.g_measuring == 'تعدادی':
            self.g_weight_unit = '_'
            self.g_in_every_box = '_'
            self.g_reorder_point = self.ent062_g_reorder_point.get()
            self.g_unit = 'عدد'

        elif self.g_measuring == 'وزنی':
            self.g_weight_unit = self.cmb062_g_weight_unit_var.get()
            self.g_in_every_box = '_'
            self.g_reorder_point = self.ent062_g_reorder_point.get()
            self.g_unit = self.g_weight_unit

        elif self.g_measuring == 'بستۀ تعدادی':
            self.g_weight_unit = '_'
            self.g_in_every_box = self.ent062_g_in_every_box.get() 
            self.g_reorder_point = self.ent062_g_reorder_point.get() 
            self.g_unit = 'بستۀ {} عددی'.format(self.g_in_every_box)

        elif self.g_measuring == 'بستۀ وزنی':
            self.g_weight_unit = self.cmb062_g_weight_unit.get()
            self.g_in_every_box = self.ent062_g_in_every_box.get()
            self.g_reorder_point = self.ent062_g_reorder_point.get() 
            if self.g_weight_unit == 'گرم' : 
                self.g_unit = 'بستۀ {} گرمی'.format(self.g_in_every_box) 
            elif self.g_weight_unit == 'کیلوگرم' : 
                self.g_unit = 'بستۀ {} کیلوگرمی'.format(self.g_in_every_box) 
            elif self.g_weight_unit == 'تن' : 
                self.g_unit = 'بستۀ {} تنی'.format(self.g_in_every_box) 

        
        self.photo_blob  = self.read_binary( 'z.png' )
        temp = [self.g_code, self.g_name, self.gr_code, self.gr_name, self.g_type, self.g_measuring,
                self.g_weight_unit, self.g_in_every_box, self.g_reorder_point, self.photo_blob] 

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = ''' INSERT INTO goods ( g_code, g_name, gr_code ,gr_name, g_type, g_measuring, g_weight_unit, g_in_every_box, g_reorder_point, photo )
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
        cur.execute( cmd , temp )
        con.commit()
        con.close()

        temp1 = temp[:5]+[0, self.g_unit, self.g_reorder_point ]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = ''' INSERT INTO stock ( g_code, g_name, gr_code ,gr_name, g_type, g_supply, g_unit, g_reorder_point)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''
        cur.execute( cmd , temp1 )
        con.commit()
        con.close()

        self.cmb062_g_gr_var.set('انتخاب کنید')
        self.lbl062_gr_name1.config( text = '' )
        self.ent062_g_code.delete(0, END)
        self.ent062_g_code.config( state = 'disabled' ) 
        self.ent062_g_name.delete(0, END)
        self.ent062_g_name.config( state = 'disabled' ) 
        self.cmb062_g_type_var.set('انتخاب کنید')
        self.cmb062_g_type.config( state = 'disabled' ) 
        self.cmb062_g_measuring_var.set('انتخاب کنید')
        self.cmb062_g_measuring.config( state = 'disabled' )  
        self.imglbl062_02.config( image = self.upload_img ) 
        self.units_map_forget() 
        self.g_codes_list = self.get_g_codes() 
        self.btn062_g_submit.config( state = 'disabled' ) 
        self.btn062_g_add_photo.config( state = 'disabled' ) 
        self.cmb062_g_gr.focus()
        

    def show_all_groups(self):
        for i in self.my_table_063_01_1.get_children():
            self.my_table_063_01_1.delete(i)
        con = sql.connect('database.db')
        cur = con.cursor()
        data = list(cur.execute('SELECT * FROM groups'))
        con.close()
        temp = []
        for i in data:
            j = list(i)
            j.reverse()
            temp.append(j)
        data = temp
        for i in range(len(data)):
            if i%2 == 0 :
                self.my_table_063_01_1.insert( parent = '', index = END, value = data[i], tags =('evenrow',) )
            else: 
                self.my_table_063_01_1.insert( parent = '', index = END, value = data[i], tags =('oddrow',) )


    def show_all_goods(self):
        for i in self.my_table_063_02.get_children():
            self.my_table_063_02.delete(i)
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = '''SELECT g_code, g_name, gr_code, gr_name, g_type, g_measuring,
                        g_weight_unit, g_in_every_box, g_reorder_point FROM goods'''
        data = list(cur.execute(cmd))
        con.close()
        temp = []
        for i in data:
            j = list(i)
            j.reverse()
            temp.append(j)
        data = temp
        for i in range(len(data)):
            if i%2 == 0 :
                self.my_table_063_02.insert( parent = '', index = END, value = data[i], tags =('evenrow',) )
            else: 
                self.my_table_063_02.insert( parent = '', index = END, value = data[i], tags =('oddrow',) )


    def frm064_gr_clear( self, event = None ):
        self.ent064_gr_name.delete(0, END)
        self.ent064_gr_name.config( state = 'disabled')
        self.btn064_gr_edit.config( state = 'disabled')
        self.btn064_gr_delete.config( state = 'disabled')


    def btn064_gr_search_func( self, event = None ):
        self.gr_code = self.ent064_gr_code.get()
        if self.gr_code != 0 :
            try:
                con = sql.connect('database.db')
                cur = con.cursor()
                cmd = 'SELECT gr_name FROM groups WHERE gr_code = {}'.format(self.gr_code)
                data = list(cur.execute( cmd ))
                con.close()
            except sql.Error as e:
                messagebox.showerror('Error!', e ) 
            else:
                if len(data) == 1 :
                    self.gr_name = data[0][0]
                    self.ent064_gr_name.config( state = 'normal' )
                    self.ent064_gr_name.delete(0, END)
                    self.ent064_gr_name.insert( 0 , self.gr_name )
                    self.ent064_gr_name.focus() 
                    self.btn064_gr_delete.config( state = 'normal' )
                else:
                    self.msg = '!گروهی با این کد ثبت نشده است'
                    messagebox.showerror('Error!', self.msg )
                    self.ent064_gr_code.focus() 
        else:
            messagebox.showerror('Error!', self.msg ) 


    def gr_update(self):
        self.gr_code = self.ent064_gr_code.get()
        self.gr_name = self.ent064_gr_name.get()
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'UPDATE groups SET gr_name = "{}" WHERE gr_code = {}'.format(self.gr_name, self.gr_code)
        cur.execute( cmd )
        con.commit()
        con.close()
        self.ent064_gr_code.delete( 0 , END )
        self.frm064_gr_clear()
        self.ent064_gr_code.focus()


    def gr_delete(self):
        self.gr_code = self.ent064_gr_code.get()
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'DELETE FROM groups WHERE gr_code = {}'.format( self.gr_code)
        cur.execute( cmd )
        con.commit()
        con.close()
        self.ent064_gr_code.delete( 0 , END )
        self.ent064_gr_name.delete( 0 , END )
        self.ent064_gr_code.focus()


    def measuring_map_forget(self):
        self.lbl064_g_weight_unit.grid_forget()
        self.lbl064_g_in_every_box.grid_forget()
        self.lbl064_g_reorder_point.grid_forget()
        self.ent064_g_in_every_box.grid_forget()
        self.ent064_g_reorder_point.grid_forget()
        self.ent064_g_in_every_box.delete( 0 , END )
        self.ent064_g_reorder_point.delete( 0 , END )
        self.ent064_g_in_every_box.config( state = 'disabled' )
        self.ent064_g_reorder_point.config( state = 'disabled' )
        self.cmb064_g_weight_unit.grid_forget()
        self.cmb064_g_weight_unit_var.set('')


    def measuring_cmb_func_2(self, event = None ):
        if self.cmb064_g_measuring_var.get() != self.last_mes_type:
            self.last_mes_type = self.cmb064_g_measuring_var.get()
            self.measuring_map_forget()
            self.btn064_g_edit.config( state = 'disabled' )
            if self.cmb064_g_measuring.get() == 'تعدادی' :
                self.lbl064_g_reorder_point.grid( row = 2 , column = 3 )
                self.ent064_g_reorder_point.grid( row = 2 , column = 2 )
                self.ent064_g_reorder_point.config( state = 'normal' )
            elif self.cmb064_g_measuring.get() == 'وزنی':
                self.lbl064_g_weight_unit.grid( row = 2 , column = 3 )
                self.cmb064_g_weight_unit.grid( row = 2 , column = 2 )
                self.lbl064_g_reorder_point.grid( row = 3 , column = 3 )
                self.ent064_g_reorder_point.grid( row = 3 , column = 2 )
            elif self.cmb064_g_measuring.get() == 'بستۀ تعدادی':
                self.lbl064_g_in_every_box.grid( row = 2 , column = 3 ) 
                self.ent064_g_in_every_box.grid( row = 2 , column = 2 ) 
                self.lbl064_g_reorder_point.grid( row = 3 , column = 3 ) 
                self.ent064_g_reorder_point.grid( row = 3 , column = 2 )
                self.ent064_g_in_every_box.config( state = 'normal' )
            elif self.cmb064_g_measuring.get() == 'بستۀ وزنی':
                self.lbl064_g_weight_unit.grid( row = 2 , column = 3 )
                self.cmb064_g_weight_unit.grid( row = 2 , column = 2 ) 
                self.lbl064_g_in_every_box.grid( row = 3 , column = 3 )
                self.ent064_g_in_every_box.grid( row = 3 , column = 2 )
                self.lbl064_g_reorder_point.grid( row = 4 , column = 3 )
                self.ent064_g_reorder_point.grid( row = 4 , column = 2 )


    def cmb064_g_weight_unit_func( self, event = None ):
        self.last_weight_unit = self.cmb064_g_weight_unit_var.get()
        self.ent064_g_in_every_box.config( state = 'normal' )
        self.ent064_g_reorder_point.config( state = 'normal' )
        self.ent064_g_in_every_box.delete( 0 , END )
        self.ent064_g_reorder_point.delete( 0 , END ) 
        if self.ent064_g_in_every_box.winfo_ismapped():
            self.ent064_g_in_every_box.focus() 
        else:
            self.ent064_g_reorder_point.focus()


    def ent064_g_in_every_box_func( self, event = None ):
        self.g_in_every_box = self.ent064_g_in_every_box.get()
        if self.g_in_every_box != 0 :
            self.ent064_g_reorder_point.config( state = 'normal' ) 
            self.ent064_g_reorder_point.focus()
        else:
            messagebox.showerror( 'Error!', self.msg )


    def ent064_g_reorder_point_func( self, event = None ):
        self.g_reorder_point = self.ent064_g_reorder_point.get()
        if self.g_reorder_point != 0 :
            self.btn064_g_edit.config( state = 'normal' )
            self.btn064_g_edit.focus()
        else:
            messagebox.showerror('Error!', self.msg )


    def g_search(self , event = None ):
        self.g_code = self.ent064_g_code.get()
        if self.g_code == 0 :
            messagebox.showerror('Error!', self.msg )
        else:
            try:
                con = sql.connect('database.db') 
                cur = con.cursor() 
                cmd = '''SELECT g_name, gr_code, gr_name, g_type, g_measuring, g_weight_unit, g_in_every_box,
                         g_reorder_point, photo FROM goods WHERE g_code = {}'''.format( self.g_code )
                data = list(cur.execute( cmd )) 
                con.close() 
            except sql.Error as e :
                messagebox.showerror('Error!', e ) 
            else:
                self.ent064_g_name.config( state = 'normal' ) 
                self.ent064_g_name.delete(0, END)
                self.ent064_a_gr_code.config( state = 'normal' ) 
                self.ent064_a_gr_code.delete(0, END)
                self.lbl064_a_gr_name1.config( text = '' )
                self.cmb064_g_type.config( state = 'readonly' ) 
                self.cmb064_g_measuring.config( state = 'readonly' ) 
                self.measuring_map_forget()
                self.btn064_g_delete.config( state = 'normal' )
                self.btn064_g_edit.config( state = 'normal' )

                self.write_binary(data[0][-1], 'z.png')
                img1 = Image.open('z.png')
                img1 = img1.resize((110,110))
                self.g_img = ImageTk.PhotoImage( img1 )
                self.imglbl064.config(image = self.g_img)
                self.imglbl064.image = self.g_img
                self.imgbtn064.config( state = 'normal' )
                
                data = data[0][:-1]
                self.ent064_g_name.insert( 0 , data[0] )
                self.ent064_a_gr_code.insert( 0 , data[1] )
                self.lbl064_a_gr_name1.config( text = data[2] )
                self.cmb064_g_type_var.set( data[3] )
                self.cmb064_g_measuring_var.set( data[4] )
                self.last_mes_type = data[4]
                self.last_weight_unit = data[5]
                if data[4] == 'تعدادی' :
                    self.ent064_g_reorder_point.config( state = 'normal')
                    self.ent064_g_reorder_point.insert( 0 , data[7] )
                    self.lbl064_g_reorder_point.grid( row = 2 , column = 3 )
                    self.ent064_g_reorder_point.grid( row = 2 , column = 2 )
                elif data[4] == 'وزنی':
                    self.cmb064_g_weight_unit_var.set( data[5] )
                    self.ent064_g_reorder_point.config( state = 'normal')
                    self.ent064_g_reorder_point.insert( 0 , data[7] )
                    self.lbl064_g_weight_unit.grid( row = 2 , column = 3 )
                    self.cmb064_g_weight_unit.grid( row = 2 , column = 2 )
                    self.lbl064_g_reorder_point.grid( row = 3 , column = 3 )
                    self.ent064_g_reorder_point.grid( row = 3 , column = 2 )
                elif data[4] == 'بستۀ تعدادی':
                    self.ent064_g_in_every_box.config( state = 'normal')
                    self.ent064_g_in_every_box.insert( 0 , data[6] )
                    self.ent064_g_reorder_point.config( state = 'normal') 
                    self.ent064_g_reorder_point.insert( 0 , data[7] )
                    self.lbl064_g_in_every_box.grid( row = 2 , column = 3 )
                    self.ent064_g_in_every_box.grid( row = 2 , column = 2 )
                    self.lbl064_g_reorder_point.grid( row = 3 , column = 3 )
                    self.ent064_g_reorder_point.grid( row = 3 , column = 2 )
                elif data[4] == 'بستۀ وزنی':
                    self.cmb064_g_weight_unit_var.set( data[5] )
                    self.ent064_g_in_every_box.config( state = 'normal')
                    self.ent064_g_in_every_box.insert( 0 , data[6] )
                    self.ent064_g_reorder_point.config( state = 'normal') 
                    self.ent064_g_reorder_point.insert( 0 , data[7] )
                    self.lbl064_g_weight_unit.grid( row = 2 , column = 3 )
                    self.cmb064_g_weight_unit.grid( row = 2 , column = 2 )
                    self.lbl064_g_in_every_box.grid( row = 3 , column = 3 )
                    self.ent064_g_in_every_box.grid( row = 3 , column = 2 )
                    self.lbl064_g_reorder_point.grid( row = 4 , column = 3 )
                    self.ent064_g_reorder_point.grid( row = 4 , column = 2 )


    def change_g_photo(self, event = None):
        if self.cmb064_g_measuring.get():
            self.photo_path = filedialog.askopenfilename( initialdir = [('photos','*.png')] )
            if self.photo_path:
                img = Image.open( self.photo_path )
                img = img.resize( (110, 110) )
                img = ImageTk.PhotoImage( img )
                self.imglbl064.config( image = img )
                self.imglbl064.image = img
                data = self.read_binary( self.photo_path )
                self.write_binary( data, 'z.png' )
                self.imgbtn064.focus()


    def g_update(self, event = None ):
        self.g_code = self.ent064_g_code.get()
        self.g_name = self.ent064_g_name.get()
        self.gr_code = self.ent064_a_gr_code.get()
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT gr_name FROM groups WHERE gr_code = {}'.format(self.gr_code)
        data = list(cur.execute( cmd ))
        con.close()        
        self.gr_name = data[0][0]
        self.g_type = self.cmb064_g_type_var.get()
        self.g_measuring = self.cmb064_g_measuring_var.get()
        if self.g_measuring == 'تعدادی':
            self.g_weight_unit = '_'
            self.g_in_every_box = '_'
            self.g_reorder_point = self.ent064_g_reorder_point.get()

        elif self.g_measuring == 'وزنی':
            self.g_weight_unit = self.cmb064_g_weight_unit_var.get()
            self.g_in_every_box = '_'
            self.g_reorder_point = self.ent064_g_reorder_point.get()

        elif self.g_measuring == 'بستۀ تعدادی':
            self.g_weight_unit = '_'
            self.g_in_every_box = self.ent064_g_in_every_box.get()
            self.g_reorder_point = self.ent064_g_reorder_point.get()

        elif self.g_measuring == 'بستۀ وزنی':
            self.g_weight_unit = self.cmb064_g_weight_unit_var.get()
            self.g_in_every_box = self.ent064_g_in_every_box.get()
            self.g_reorder_point = self.ent064_g_reorder_point.get()


        self.photo_blob = self.read_binary('z.png')
        temp = [self.g_code, self.g_name, self.gr_code, self.gr_name, self.g_type, self.g_measuring,
                self.g_weight_unit, self.g_in_every_box, self.g_reorder_point, self.photo_blob] 
        
        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'DELETE FROM goods WHERE g_code = {}'.format(self.g_code)
        cur.execute( cmd )
        con.commit()
        con.close()

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = ''' INSERT INTO goods ( g_code, g_name, gr_code ,gr_name, g_type, g_measuring, g_weight_unit,
                  g_in_every_box, g_reorder_point, photo ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
        cur.execute( cmd , temp )
        con.commit()
        con.close() 

        data = temp 
        if data[5] == 'تعدادی':
            self.g_unit = 'عدد'

        elif data[5] == 'وزنی':
            self.g_unit = data[6] 

        elif data[5] == 'بستۀ تعدادی':
            self.g_unit = 'بستۀ {} تایی'.format(data[7]) 

        elif data[5] == 'بستۀ وزنی' : 
            if data[6] == 'گرم' : 
                self.g_unit = 'بستۀ {} گرمی'.format(data[7]) 
            elif data[6] == 'کیلوگرم' : 
                self.g_unit = 'بستۀ {} کیلوگرمی'.format(data[7]) 
            elif data[6] == 'تن' : 
                self.g_unit = 'بستۀ {} تنی'.format(data[7]) 


        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = '''UPDATE stock SET g_name ="{}", gr_code ={}, gr_name="{}", g_type="{}", g_unit="{}", g_reorder_point={}
                 WHERE g_code = {}'''.format( self.g_name, self.gr_code, self.gr_name, self.g_type, self.g_unit, self.g_reorder_point, self.g_code )
        cur.execute( cmd )
        con.commit()
        con.close()
        
        self.ent064_g_code.delete( 0 , END ) 
        self.ent064_g_name.delete( 0 , END ) 
        self.ent064_g_name.config( state = 'disabled' ) 
        self.ent064_a_gr_code.delete( 0 , END ) 
        self.ent064_a_gr_code.config( state = 'disabled' ) 
        self.lbl064_a_gr_name1.config( text = '' ) 
        self.cmb064_g_type_var.set('') 
        self.cmb064_g_type.config( state = 'disabled' ) 
        self.cmb064_g_measuring_var.set('') 
        self.cmb064_g_measuring.config( state = 'disabled' ) 
        self.measuring_map_forget() 
        self.imglbl064.config( image = self.upload_img ) 
        self.imgbtn064.config( state = 'disabled' ) 
        self.btn064_g_edit.config( state = 'disabled' )
        self.btn064_g_delete.config( state = 'disabled' )


    def g_delete(self, event = None ): 
        if self.cmb064_g_measuring.get():
            self.g_code = self.ent064_g_code.get()
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'DELETE FROM goods WHERE g_code = {}'.format(self.g_code)
            cur.execute( cmd )
            con.commit()
            con.close()
        self.ent064_g_code.delete( 0 , END ) 
        self.ent064_g_name.delete( 0 , END ) 
        self.ent064_g_name.config( state = 'disabled' ) 
        self.ent064_a_gr_code.delete( 0 , END ) 
        self.ent064_a_gr_code.config( state = 'disabled' ) 
        self.lbl064_a_gr_name1.config( text = '' ) 
        self.cmb064_g_type_var.set('') 
        self.cmb064_g_type.config( state = 'disabled' ) 
        self.cmb064_g_measuring_var.set('') 
        self.cmb064_g_measuring.config( state = 'disabled' ) 
        self.measuring_map_forget() 
        self.imglbl064.config( image = self.upload_img ) 
        self.imgbtn064.config( state = 'disabled' ) 
        self.btn064_g_edit.config( state = 'disabled' )
        self.btn064_g_delete.config( state = 'disabled' )



#=================================================== User sign up Page Functions ===========================================    
    def upload_user_photo( self, event = None ):
        self.photo_path = filedialog.askopenfilename( initialdir = [('photos','*.png')] )
        if self.photo_path:
            img = Image.open( self.photo_path )
            img = img.resize( (110, 110) )
            img = ImageTk.PhotoImage( img )
            self.imglbl072.config( image = img )
            self.imglbl072.image = img
            data = self.read_binary( self.photo_path )
            self.write_binary( data, 'z.png' )

            self.btn072_submit.focus()
    

    def ent072_user_p_id_func( self, event = None ):
        self.p_id = self.ent072_user_p_id.get()
        flg = True 
        if self.p_id != 0 :
            con = sql.connect('database.db')
            cur = con.cursor()
            data = list(cur.execute( 'SELECT idd FROM people' ))
            con.close()

            for i in data:
                if self.p_id == i[0] :
                    messagebox.showerror('Error!', '!کد پرسنلی تکراری است')
                    self.ent072_user_p_id.focus()
                    flg = False
            if flg:
                self.ent072_user_name.focus()

        else:
            messagebox.showerror('Error!', self.msg )



    def submit_user( self, event = None ):
        self.p_id = self.ent072_user_p_id.get()

        flg = True
        con = sql.connect('database.db')
        cur = con.cursor()
        data = list(cur.execute( 'SELECT idd FROM people' ))
        con.close()

        for i in data:
            if self.p_id == i[0] :
                flg = False
                messagebox.showerror('Error!', '!کد پرسنلی تکراری است')
                self.ent072_user_p_id.focus()

        if flg:
            if self.p_id != 0 :
                name = self.ent072_user_name.get()

                if name != '' :
                    self.n_id = self.ent072_user_n_id.get()

                    if self.n_id != 0 :
                        username = self.ent072_user_username.get()

                        if username != '' :
                            password = self.ent072_user_password.get()

                            if password != '' :
                                photo = self.read_binary('z.png')
                                temp = [ self.p_id, username, password, self.n_id, name, 'کارمند', photo ]

                                con = sql.connect('database.db')
                                cur = con.cursor()
                                cmd = '''INSERT INTO people (idd, user_n, pass_w, n_id, full_name, position, photo )
                                        VALUES (?, ?, ?, ?, ?, ?, ?)'''
                                cur.execute( cmd , temp )
                                con.commit()
                                con.close()

                                self.scnd_btn072() 
                                self.scnd_btn072() 
                            
                            else:
                                messagebox.showerror('Error!', '!رمز عبور را وارد کنید' ) 

                        else:
                            messagebox.showerror('Error!', '!نام کاربری را وارد کنید' ) 

                    else:
                        messagebox.showerror('Error!', self.msg )

                else:
                    messagebox.showerror('Error!', '!نام را وارد کنید' ) 

            else:
                messagebox.showerror('Error!', self.msg )


    def show_all_users( self, event = None ) :

        for i in self.users_table_073.get_children():
            self.users_table_073.delete(i)

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT position, user_n, n_id, full_name, idd FROM people'
        data = list( cur.execute( cmd ) )
        con.commit()
        con.close()

        temp = []
        for i in data:
            i = list(i)          
            temp.append(i)
        
        for i in range( len( temp ) ):
            j = i + 1 
            temp[i] = temp[i] + [j]

            if j%2 :
                self.users_table_073.insert( parent = '', index = END, value = temp[i], tags =('evenrow',) )
            else: 
                self.users_table_073.insert( parent = '', index = END, value = temp[i], tags =('oddrow',) )


    def btn074_user_search_func( self, event = None ) : 
        self.p_id = self.ent074_user_p_id.get()
        if self.p_id != 0 :
            try :
                con = sql.connect('database.db')
                cur = con.cursor()
                cmd = 'SELECT * FROM people WHERE idd = {}'.format(self.p_id)
                data = list( cur.execute( cmd ) )
                con.commit() 
                con.close()
            except sql.Error as e :
                messagebox.showerror( 'Error!', e )
            else:
                if len(data) == 1 :
                    self.ent074_user_name.delete( 0 , END )
                    self.ent074_user_n_id.delete( 0 , END )
                    self.ent074_user_username.delete( 0 , END )
                    self.ent074_user_password.delete( 0 , END ) 

                    self.write_binary(data[0][-1], 'z.png')
                    img1 = Image.open('z.png')
                    img1 = img1.resize((110,110))
                    self.g_img = ImageTk.PhotoImage( img1 )
                    self.imglbl074.config(image = self.g_img)
                    self.imglbl074.image = self.g_img 

                    self.ent074_user_name.config( state = 'normal' ) 
                    self.ent074_user_name.insert( 0 , data[0][4] ) 

                    self.ent074_user_n_id.config( state = 'normal' ) 
                    self.ent074_user_n_id.insert( 0 , data[0][3] ) 

                    self.ent074_user_username.config( state = 'normal' ) 
                    self.ent074_user_username.insert( 0 , data[0][1] ) 

                    self.ent074_user_password.config( state = 'normal' ) 
                    self.ent074_user_password.insert( 0 , data[0][2] ) 

                    self.imgbtn074.config( state = 'normal' ) 
                    self.btn074_user_edit.config( state = 'normal' ) 
                    self.btn074_user_delete.config( state = 'normal' ) 
                    self.ent074_user_name.focus()
                    
                else:
                    messagebox.showerror('Error!', '!کارمندی با این کد در سیستم ثبت نشده است')
                    self.ent074_user_p_id.focus()

        else:
            messagebox.showerror('Error!', self.msg )
            self.ent074_user_p_id.focus()



#=================================================== User Request Page Functions ===========================================
    def ent082_request_num_func0( self , event = None ) :
        self.ent082_g_code.delete( 0 , END )
        self.ent082_amount.delete( 0 , END )
        self.ent082_note.delete( 0 , END )
        self.lbl082_g_name1.config( text = '' )
        self.lbl082_unit.config( text = '' )
        self.ent082_amount.config( state = 'disabled' )
        self.ent082_g_code.config( state = 'disabled' )
        self.ent082_note.config( state = 'disabled' )
        self.btn082_add_to_list.config( state = 'disabled' )
        self.imglbl082.config( image = self.upload_img )
        # self.btn082_3_delete_from_list.config( state = 'disabled' )
        # self.btn082_3_delete_list.config( state = 'disabled' )
        # self.btn082_3_submit_list.config( state = 'disabled' )


    def ent082_request_num_func( self , event = None ) :
        self.request_number = self.ent082_request_num.get()
        if self.request_number != 0 :
            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'SELECT request_number FROM requests'
            data = list( cur.execute( cmd ) )
            con.commit()
            con.close()

            flg = True
            for i in data:
                if int(i[0]) == self.request_number:
                    flg = False 
                    self.ent082_request_num.focus() 
                    messagebox.showerror('Error!', '!از این شماره قبلا استفاده شده است')
                    break
            
            if flg:
                for i in self.table082_2.get_children():
                    self.table082_2.delete(i) 
                self.ent082_g_code.config( state = 'normal' )
                con = sql.connect('database.db')
                cur = con.cursor()
                cmd = 'SELECT g_code, g_name, g_measuring, g_weight_unit, g_in_every_box FROM goods'
                data = list( cur.execute( cmd ) )
                con.commit()
                con.close()

                temp1 = [] 
                for i in data:
                    j = list(i)
                    j.reverse()
                    temp1.append(j)
                data = temp1

                temp = []
                for i in data:
                    if i[2] == 'تعدادی':
                        self.g_unit = 'عدد'

                    elif i[2] == 'وزنی':
                        self.g_unit = i[1] 

                    elif i[2] == 'بستۀ تعدادی':
                        self.g_unit = 'بستۀ {} تایی'.format(i[0]) 

                    elif i[2] == 'بستۀ وزنی' : 
                        if i[1] == 'گرم' : 
                            self.g_unit = 'بستۀ {} گرمی'.format(i[0]) 
                        elif i[1] == 'کیلوگرم' : 
                            self.g_unit = 'بستۀ {} کیلوگرمی'.format(i[0]) 
                        elif i[1] == 'تن' : 
                            self.g_unit = 'بستۀ {} تنی'.format(i[0]) 
                    temp.append([self.g_unit, i[3], i[4]])
                
                self.ent082_g_code.focus() 

                for i in range(len(temp)):
                    if i%2 == 0 :
                        self.table082_2.insert( parent = '', index = END , value = temp[i] , tags = ('evenrow',) )
                    else:
                        self.table082_2.insert( parent = '', index = END , value = temp[i] , tags = ('oddrow',) )
        else:
            messagebox.showerror('Error!', self.msg ) 
    


    def ent082_g_code_func0( self, event = None ):
        self.lbl082_g_name1.config( text = '' )
        self.lbl082_unit.config( text = '' )
        self.ent082_note.delete( 0 , END )
        self.ent082_amount.config( state = 'disabled' )
        self.ent082_note.config(state = 'disabled' )
        self.btn082_add_to_list.config( state = 'disabled' ) 
        self.imglbl082.config( image = self.upload_img )
        for i in self.table082_2.get_children():
            self.table082_2.selection_remove(i)


    def ent082_g_code_func( self, event = None ):
        self.g_code = self.ent082_g_code.get()
        if self.g_code != 0 :
            data = [] 
            for i in self.table082_2.get_children():
                temp = self.table082_2.item(i, 'values') 
                data.append(temp)
            
            for i in data:
                if int(i[2]) == self.g_code:
                    self.g_name = i[1]
                    self.lbl082_g_name1.config( text = self.g_name )
                    self.g_unit = i[0]
                    self.lbl082_unit.config( text = self.g_unit )
                    break

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = 'SELECT photo FROM goods WHERE g_code = {}'.format( self.g_code )
            data = list( cur.execute( cmd ) )
            con.commit()
            con.close()
            self.write_binary( data[0][0] , 'z.png' )
            img1 = Image.open('z.png')
            img1 = img1.resize((110,110))
            self.g_img = ImageTk.PhotoImage( img1 )
            self.imglbl082.config(image = self.g_img)
            self.imglbl082.image = self.g_img 

            self.ent082_amount.config( state = 'normal' )
            self.ent082_amount.focus()
        else:
            messagebox.showerror( 'Error!' , self.msg )


    def table082_2_select(self, event = None):
        self.ent082_g_code.delete( 0 , END )
        self.lbl082_g_name1.config( text = '' )
        self.ent082_amount.config( state = 'normal' )
        self.ent082_amount.delete( 0 , END ) 
        self.lbl082_unit.config( text = '' ) 
        self.btn082_add_to_list.config( state = 'disabled' ) 

        selected = self.table082_2.focus() 
        values = self.table082_2.item( selected, 'values' ) 
        data = values

        self.ent082_g_code.insert( 0 , data[2] ) 
        self.lbl082_g_name1.config( text = data[1] )
        self.lbl082_unit.config( text = data[0] )
        self.ent082_amount.focus()

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT photo FROM goods WHERE g_code = {}'.format( data[2] )
        data = list( cur.execute( cmd ) ) 
        con.commit()
        con.close()

        self.write_binary( data[0][0] , 'z.png' )
        img1 = Image.open('z.png')
        img1 = img1.resize((110,110))
        self.g_img = ImageTk.PhotoImage( img1 )
        self.imglbl082.config(image = self.g_img )
        self.imglbl082.image = self.g_img 
        

    def ent082_amount_func( self, event = None ):
        self.g_amount = self.ent082_amount.get() 
        if self.g_amount != 0 :
            self.btn082_add_to_list.config( state = 'normal' )
            self.ent082_note.config( state = 'normal' )
            self.ent082_note.focus()
        else:
            messagebox.showerror('Error!', self.msg )


    def btn082_add_to_list_func( self, event = None ):
        self.btn082_add_to_list.config( state = 'disabled' )
        self.g_code = self.ent082_g_code.get()
        self.g_name = self.lbl082_g_name1['text']
        self.g_amount = self.ent082_amount.get()
        self.g_unit = self.lbl082_unit['text'] 
        note = self.ent082_note.get() 

        self.lbl082_g_name1.config( text = '' ) 
        self.ent082_amount.delete( 0 , END )
        self.ent082_amount.config( state = 'disabled' )
        self.ent082_note.delete( 0 , END )
        self.ent082_note.config( state = 'disabled' ) 
        self.imglbl082.config( image = self.upload_img )

        data = []
        for i in self.table082_3.get_children():
            temp = self.table082_3.item(i, 'values' )
            data.append(temp) 
        
        flg1 = True
        for i in data:
            if int(i[4]) == self.g_code:
                flg1 = False
                self.msg = '.این کالا قبلا وارد شده است' 
                self.ent082_g_code.focus() 
                self.lbl082_unit.config( text = '' )
                messagebox.showerror('Error!', self.msg ) 
                break
        
        if flg1:
            temp = [note, self.g_unit, self.g_amount, self.g_name, self.g_code ]

            i = 0
            for i in range(len(self.table082_3.get_children())):
                i = i + 1
            i = i + 1
            temp = temp + [i] 

            if i%2 != 0 :
                self.table082_3.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
            else:
                self.table082_3.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )

            self.ent082_g_code.delete( 0, END )
            self.lbl082_g_name1.config( text = '' )
            self.ent082_amount.delete( 0, END )
            self.lbl082_unit.config( text = '' )
            
            self.btn082_3_delete_list.config( state = 'normal' )
            self.btn082_3_submit_list.config( state = 'normal' )
            self.ent082_g_code.focus() 
            for i in self.table082_2.get_children():
                self.table082_2.selection_remove(i) 


    def btn082_delete_list_func( self, event = None ):
        for i in self.table082_3.get_children() :
            self.table082_3.delete(i) 
        self.btn082_3_delete_list.config( state = 'disabled' )
        self.btn082_3_delete_from_list.config( state = 'disabled' )
        self.btn082_3_submit_list.config( state = 'disabled' ) 


    def table082_3_select_func( self, event = None ) :
        self.btn082_3_delete_from_list.config(state = 'normal') 

        for i in self.table082_2.get_children():
            self.table082_2.selection_remove(i) 
        self.ent082_g_code.delete( 0 , END ) 
        self.lbl082_g_name1.config( text = '' ) 
        self.ent082_amount.delete( 0 , END )
        self.ent082_amount.config( state = 'disabled' )
        self.lbl082_unit.config( text = '' ) 
        self.ent082_note.delete( 0 , END )
        self.ent082_note.config( state = 'disabled' ) 
        self.btn082_add_to_list.config( state = 'disabled' )
        
    

    def btn082_delete_from_list_func(self, event = None):  # ***** delete_from_list *****      
        selected = self.table082_3.focus()
        self.table082_3.delete( selected ) 
        j = 0
        for i in self.table082_3.get_children():
            j = j + 1
            if j%2:
                self.table082_3.item(i, tags = 'evenrow' )
            else:
                self.table082_3.item(i, tags = 'oddrow' )        
        j = 1
        for i in self.table082_3.get_children():
            temp = self.table082_3.item(i, 'values' ) 
            temp = list( temp )
            temp = temp[:-1] + [j]
            self.table082_3.item(i, values = temp ) 
            j = j + 1
        self.btn082_3_delete_from_list.config( state = 'disabled' ) 

        if j == 1 :
            self.btn082_3_delete_list.config( state = 'disabled' ) 
            self.btn082_3_submit_list.config( state = 'disabled' ) 
        
        self.ent082_g_code.focus() 
    

    def btn082_submit_list_func( self, event = None ):
        self.request_number = self.ent082_request_num.get() 
        self.current_user_name = self.current_user[0][4]
        self.p_id = self.current_user[0][0] 

        now = dt.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')  

        for i in self.table082_3.get_children():
            record = self.table082_3.item( i , 'values' ) 
            self.g_code   = record[4]
            self.g_name   = record[3]
            self.g_amount = record[2]
            self.g_unit   = record[1]
            note          = record[0]

            temp = [ self.request_number, self.current_user_name, self.p_id, self.g_code, self.g_name,
                     self.g_amount, self.g_unit, note, 'در انتظار تایید', now ] 

            con = sql.connect('database.db')
            cur = con.cursor()
            cmd = '''INSERT INTO requests (request_number, rq_name, rq_pid, g_code, g_name, g_amount, g_unit, note, status, time)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cur.execute( cmd , temp ) 
            con.commit()
            con.close() 
        
        for i in self.table082_3.get_children():
            self.table082_3.delete(i) 
        
        self.ent082_request_num.delete( 0 , END ) 
        self.ent082_request_num.focus()
        self.ent082_g_code.config( state = 'disabled' )   
        for i in self.table082_2.get_children():
            self.table082_2.delete(i)  
        self.btn082_3_delete_list.config( state = 'disabled' )
        self.btn082_3_submit_list.config( state = 'disabled' )


    # my_requests page functions 
    
    def cmb082_show_type_func( self, event = None ):
        for i in self.table083_a.get_children():
            self.table083_a.delete(i)
            
        for i in self.table083_b.get_children():
            self.table083_b.delete(i)

        self.lbl083_note21.config( text = '' )
        self.btn083_show.config( state = 'normal' ) 
        self.btn083_show.focus() 
        

    def show_my_requests( self, event = None ):

        for i in self.table083_a.get_children():
            self.table083_a.delete(i)

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = '''SELECT time2,  admin, status, time, request_number FROM requests 
                 WHERE rq_name = "{}" '''.format( self.current_user_name )
        data = list( cur.execute( cmd ) ) 
        con.close()

        if len(data) > 0 : 
            temp1 = []
            for i in data:
                i = list(i)
                temp1.append(i)
            temp1.reverse() 

            temp = [temp1[0]]
            doc_number = temp1[0][-1] 
            for i in range( len( temp1 ) ):
                if temp1[i][-1] != doc_number:
                    temp.append(temp1[i])
                    doc_number = temp1[i][-1] 

            show_type = self.cmb083_show_type_var.get()

            if show_type == 'همۀ درخواست‌ها':
                for i in range(len(temp)):
                    j = i + 1
                    temp[i] = temp[i] + [j] 

                    if j%2 : 
                        self.table083_a.insert( parent = '' , index = END , value = temp[i] , tags = ('evenrow',) )
                    else:
                        self.table083_a.insert( parent = '' , index = END , value = temp[i] , tags = ('oddrow',) )

            elif show_type == 'درخواست‌های در انتظار':
                temp2 = []
                for i in temp:
                    if i[2] == 'در انتظار تایید' :
                        temp2.append(i)

                if len(temp2) > 0 :
                    for i in range(len(temp2)):
                        j = i + 1
                        temp2[i] = temp2[i] + [j] 

                        if j%2 : 
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('evenrow',) )
                        else:
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('oddrow',) )

            elif show_type == 'درخواست‌های تحویل شده':
                temp2 = []
                for i in temp:
                    if i[2] == 'تحویل شده' :
                        temp2.append(i)

                if len(temp2) > 0 :
                    for i in range(len(temp2)):
                        j = i + 1
                        temp2[i] = temp2[i] + [j] 

                        if j%2 : 
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('evenrow',) )
                        else:
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('oddrow',) )

            elif show_type == 'درخواست‌های جاری':
                temp2 = []
                for i in temp:
                    if i[2] == 'تایید شده' :
                        temp2.append(i)

                if len(temp2) > 0 :
                    for i in range(len(temp2)):
                        j = i + 1
                        temp2[i] = temp2[i] + [j] 

                        if j%2 : 
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('evenrow',) )
                        else:
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('oddrow',) )

            elif show_type == 'درخواست‌های رد شده':
                temp2 = []
                for i in temp:
                    if i[2] == 'رد شده' :
                        temp2.append(i)

                if len(temp2) > 0 :
                    for i in range(len(temp2)):
                        j = i + 1
                        temp2[i] = temp2[i] + [j] 

                        if j%2 : 
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('evenrow',) )
                        else:
                            self.table083_a.insert( parent = '' , index = END , value = temp2[i] , tags = ('oddrow',) )
        
        else: 
            msg = '!شما تاکنون درخواستی ثبت نکرده‌اید'
            messagebox.showerror( 'Error!', msg ) 
        
        self.cmb083_show_type.focus()

    

    def table083_a_select( self, event = None ):
        for i in self.table083_b.get_children():
            self.table083_b.delete(i) 
        
        selected = self.table083_a.focus() 
        values = self.table083_a.item( selected, 'values' ) 

        self.request_number = values[4] 
        self.rq_name = values[3]

        con = sql.connect('database.db')
        cur = con.cursor()
        cmd = 'SELECT * FROM requests WHERE request_number = {}'.format( self.request_number ) 
        data = list(cur.execute( cmd )) 
        con.close() 

        note2 = data[0][-2]
        self.lbl083_note21.config( text = note2 )

        for i in range( len( data ) ) :

            self.g_code = data[i][3]
            self.g_name = data[i][4]
            self.g_amount = int( data[i][5] )
            self.g_unit = data[i][6]
            note = data[i][7] 
            j = i+1

            temp = [ note, self.g_unit, self.g_amount, self.g_name, self.g_code, j ]

            if j%2 == 0 :
                self.table083_b.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            else: 
                self.table083_b.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 



#=================================================== gui settings functions ================================================

    def set_admin_page(self, event = None):
        self.mainbtn01.grid( row = 1  , column = 1 )
        # self.mainbtn02.grid( row = 3  , column = 1 )
        self.mainbtn03.grid( row = 5  , column = 1 )
        self.mainbtn04.grid( row = 7  , column = 1 )
        # self.mainbtn05.grid( row = 9  , column = 1 )
        self.mainbtn06.grid( row = 11 , column = 1 )
        self.mainbtn07.grid( row = 13 , column = 1 )
        self.mainbtn10.grid( row = 19 , column = 1 ) 


    def set_user_page(self, event = None):
        self.mainbtn08.grid( row = 15 , column = 1 )
        self.mainbtn10.grid( row = 19 , column = 1 )


    def f_map_forget(self, event = None):
        self.frm01.grid_forget()
        # self.frm02.grid_forget()
        self.frm03.grid_forget()
        self.frm04.grid_forget()
        # self.frm05.grid_forget()
        self.frm06.grid_forget()
        self.frm07.grid_forget()
        self.frm08.grid_forget()
        self.frm10.grid_forget()


    def b_map_forget(self, event = None):
        self.mainbtn01.grid_forget()
        # self.mainbtn02.grid_forget()
        self.mainbtn03.grid_forget()
        self.mainbtn04.grid_forget()
        # self.mainbtn05.grid_forget()
        self.mainbtn06.grid_forget()
        self.mainbtn07.grid_forget()
        self.mainbtn08.grid_forget()
        self.mainbtn10.grid_forget()


    def set_color(self, event = None):
        self.mainbtn01.configure( bg = '#345382' )
        # self.mainbtn02.configure( bg = '#345382' )
        self.mainbtn03.configure( bg = '#345382' )
        self.mainbtn04.configure( bg = '#345382' )
        # self.mainbtn05.configure( bg = '#345382' )
        self.mainbtn06.configure( bg = '#345382' )
        self.mainbtn07.configure( bg = '#345382' )
        self.mainbtn08.configure( bg = '#345382' )
        self.mainbtn10.configure( bg = '#345382' )


    def inner_frames_map_forget(self):
        self.frm012.place_forget()
        self.frm032_1.place_forget()
        self.frm032_2.place_forget()
        self.frm033_1.place_forget()
        self.frm033_2.place_forget()
        self.frm034_1.place_forget()
        self.frm034_2.place_forget()
        self.frm035_1.place_forget()
        self.frm035_2.place_forget()
        self.frm042.place_forget()
        self.frm043.place_forget()
        self.frm044_1.place_forget()
        self.frm044_2.place_forget()
        self.frm062_gr.place_forget()
        self.frm062_g.place_forget()
        self.frm063_01.place_forget()
        self.frm063_02.place_forget()
        self.frm064_gr.place_forget()
        self.frm064_g.place_forget()
        self.frm072.place_forget()
        self.frm073.place_forget()
        self.frm074.place_forget()
        self.frm082_1.place_forget()
        self.frm082_2.place_forget() 
        self.frm082_3.place_forget() 
        self.frm083_1.place_forget()
        self.frm083_2.place_forget()


#======================================================= main buttons functions =================================================
    def main_btn01(self, event = None):
        self.set_color()
        if event :
            self.mainbtn01.configure( bg = '#436291' )
        else :
            self.set_admin_page()
            self.mainbtn01.grid_forget()
            self.f_map_forget()
            self.frm01.grid( row = 2 , column = 1 )

    # def main_btn02(self, event = None):
    #     self.set_color()
    #     if event:
    #         self.mainbtn02.configure( bg = '#436291' )
    #     else:
    #         self.set_admin_page()
    #         self.mainbtn02.grid_forget()
    #         self.f_map_forget()
    #         self.frm02.grid( row = 4 , column = 1 )


    def main_btn03(self, event = None):
        self.set_color()
        if event:
            self.mainbtn03.configure( bg = '#436291' )
        else:
            self.set_admin_page()
            self.mainbtn03.grid_forget()
            self.f_map_forget()
            self.frm03.grid( row = 6 , column = 1 )


    def main_btn04(self, event = None):
        self.set_color()
        if event:
            self.mainbtn04.configure( bg = '#436291' )
        else:
            self.set_admin_page()
            self.mainbtn04.grid_forget() 
            self.f_map_forget()
            self.frm04.grid( row = 8 , column = 1 )


    # def main_btn05(self, event = None):
    #     self.set_color()
    #     if event:
    #         self.mainbtn05.configure( bg = '#436291' )
    #     else:
    #         self.set_admin_page()
    #         self.mainbtn05.grid_forget()
    #         self.f_map_forget()
    #         self.frm05.grid( row = 10 , column = 1 )


    def main_btn06(self, event = None):
        self.set_color()
        if event:
            self.mainbtn06.configure( bg = '#436291' )
        else:
            self.set_admin_page()
            self.mainbtn06.grid_forget()
            self.f_map_forget()
            self.frm06.grid( row = 12 , column = 1 )


    def main_btn07(self, event = None):
        self.set_color()
        if event:
            self.mainbtn07.configure( bg = '#436291' )
        else:
            self.set_admin_page()
            self.mainbtn07.grid_forget()
            self.f_map_forget()
            self.frm07.grid( row = 14 , column = 1 )


    def main_btn08(self, event = None):
        self.set_color()
        if event:
            self.mainbtn08.configure( bg = '#436291' )
        else:
            self.set_user_page()
            self.mainbtn08.grid_forget()
            self.f_map_forget()
            self.frm08.grid( row = 16 , column = 1 )


    def main_btn10(self, event = None):
        self.set_color()
        if event:
            self.mainbtn10.configure( bg = '#436291' )
        else:
            if self.mainbtn01.winfo_ismapped():
                self.set_admin_page()
            else:
                self.set_user_page()
            self.mainbtn10.grid_forget()
            self.f_map_forget()
            self.frm10.grid( row = 20 , column = 1 )


#============================================== secondary buttons functions =================================
    def scnd_btn011(self):
        self.mainbtn01.grid( row = 1 , column = 1 )
        self.f_map_forget()
    
    def scnd_btn012(self):  # صفحه موجودی انبار 
        if self.frm012.winfo_ismapped():
            self.frm012.place_forget()
        else:
            self.inner_frames_map_forget()
            for i in self.table012.get_children():
                self.table012.delete(i)
            self.cmb012_show_type_var.set('انتخاب کنید')
            self.cmb012_show_type.focus() 
            self.lbl012_row.pack_forget() 
            self.cmb012_row_var.set('...')
            self.cmb012_row.pack_forget() 
            self.frm012.place( x = 40 , y = 170 )

    def scnd_btn013(self):
        pass

    def scnd_btn014(self):
        pass



    # def scnd_btn021(self):
    #     self.mainbtn02.grid( row = 3 , column = 1 )
    #     self.f_map_forget()

    # def scnd_btn022(self):
    #     pass

    # def scnd_btn023(self):
    #     pass

    # def scnd_btn024(self):
    #     pass

    # def scnd_btn025(self):
    #     pass


    def scnd_btn031(self):
        self.mainbtn03.grid( row = 5 , column = 1 ) 
        self.f_map_forget() 

    def scnd_btn032(self): 
        if self.frm032_1.winfo_ismapped(): 
            self.frm032_1.place_forget() 
            self.frm032_2.place_forget() 
        else:
            self.inner_frames_map_forget()  
            for i in self.table032_a.get_children(): 
                self.table032_a.delete(i) 
            for i in self.table032_b.get_children(): 
                self.table032_b.delete(i) 
            
            self.lbl032_request_number1.config( text = '' )
            self.lbl032_rq_name1.config( text = '' )
            self.lbl032_p_id1.config( text = '' )
            self.lbl032_time1.config( text = '' )

            con = sql.connect( 'database.db' ) 
            cur = con.cursor() 
            data = list( cur.execute( 'SELECT * FROM requests WHERE status == "{}" '.format( 'در انتظار تایید' ) ) )  
            con.close() 

            if len(data) > 0 :
                self.request_number = data[0][0]
                self.rq_name = data[0][1]
                time = data[0][8]
                j = 1 
                temp = [ time, self.rq_name, self.request_number, j ]
                self.table032_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 
                
                for i in range( len( data ) ): 
                    if data[i][0] != self.request_number:
                        self.request_number = data[i][0]
                        self.rq_name = data[i][1]
                        time = data[i][8] 
                        j = j + 1
                        temp = [ time, self.rq_name, self.request_number, j ]
                        if j % 2 :
                            self.table032_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
                        else: 
                            self.table032_a.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            
            self.ent032_note2.delete( 0 , END )
            self.ent032_note2.config( state = 'disabled' )

            self.btn032_approve.config( state = 'disabled' )
            self.btn032_reject.config( state = 'disabled' )

            self.frm032_1.place( x = 190 , y = 100 ) 
            self.frm032_2.place( x = 50  , y = 350 ) 

    def scnd_btn033(self):
        if self.frm033_1.winfo_ismapped(): 
            self.frm033_1.place_forget() 
            self.frm033_2.place_forget() 
        else:
            self.inner_frames_map_forget()  
            for i in self.table033_a.get_children(): 
                self.table033_a.delete(i) 
            for i in self.table033_b.get_children(): 
                self.table033_b.delete(i) 
            
            self.lbl033_request_number1.config( text = '' )
            self.lbl033_rq_name1.config( text = '' )
            self.lbl033_p_id1.config( text = '' )
            self.lbl033_time1.config( text = '' )

            con = sql.connect( 'database.db' ) 
            cur = con.cursor() 
            data = list( cur.execute( 'SELECT * FROM requests WHERE status == "{}" '.format( 'تایید شده' ) ) ) 
            con.close() 

            if len(data) > 0 :
                self.request_number = data[0][0]
                self.rq_name = data[0][1]
                time = data[0][8]
                admin = data[0][10] 
                time2 = data[0][12] 
                j = 1 
                temp = [ time2, admin, time, self.rq_name, self.request_number, j ] 
                self.table033_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 
                
                for i in range( len( data ) ): 
                    if data[i][0] != self.request_number:
                        self.request_number = data[i][0] 
                        self.rq_name = data[i][1]
                        time = data[i][8] 
                        admin = data[i][10] 
                        time2 = data[i][12] 
                        j = j + 1
                        temp = [ time2, admin, time, self.rq_name, self.request_number, j ]
                        if j % 2 :
                            self.table033_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
                        else: 
                            self.table033_a.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            
            self.lbl033_note21.config( text = '' )
           
            self.btn033_submit.config( state = 'disabled' )

            self.frm033_1.place( x = 50 , y = 100 ) 
            self.frm033_2.place( x = 50  , y = 350 ) 

    def scnd_btn034(self):
        if self.frm034_1.winfo_ismapped(): 
            self.frm034_1.place_forget() 
            self.frm034_2.place_forget() 
        else:
            self.inner_frames_map_forget()  
            for i in self.table034_a.get_children(): 
                self.table034_a.delete(i) 
            for i in self.table034_b.get_children(): 
                self.table034_b.delete(i) 
            
            self.lbl034_request_number1.config( text = '' )
            self.lbl034_rq_name1.config( text = '' )
            self.lbl034_p_id1.config( text = '' )
            self.lbl034_time1.config( text = '' )

            con = sql.connect( 'database.db' ) 
            cur = con.cursor() 
            data = list( cur.execute( 'SELECT * FROM requests WHERE status == "{}" '.format( 'رد شده' ) ) ) 
            con.close() 

            if len(data) > 0 :
                self.request_number = data[0][0]
                self.rq_name = data[0][1]
                time = data[0][8]
                admin = data[0][10] 
                time2 = data[0][12] 
                j = 1 
                temp = [ time2, admin, time, self.rq_name, self.request_number, j ] 
                self.table034_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 
                
                for i in range( len( data ) ): 
                    if data[i][0] != self.request_number:
                        self.request_number = data[i][0] 
                        self.rq_name = data[i][1]
                        time = data[i][8] 
                        admin = data[i][10] 
                        time2 = data[i][12] 
                        j = j + 1
                        temp = [ time2, admin, time, self.rq_name, self.request_number, j ]
                        if j % 2 :
                            self.table034_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
                        else: 
                            self.table034_a.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            
            self.lbl034_note21.config( text = '' ) 

            self.frm034_1.place( x = 50 , y = 100 ) 
            self.frm034_2.place( x = 50  , y = 350 ) 

    def scnd_btn035(self):
        if self.frm035_1.winfo_ismapped(): 
            self.frm035_1.place_forget() 
            self.frm035_2.place_forget() 
        else:
            self.inner_frames_map_forget()  
            for i in self.table035_a.get_children(): 
                self.table035_a.delete(i) 
            for i in self.table035_b.get_children(): 
                self.table035_b.delete(i) 
            
            self.lbl035_request_number1.config( text = '' )
            self.lbl035_rq_name1.config( text = '' )
            self.lbl035_p_id1.config( text = '' )
            self.lbl035_time1.config( text = '' )

            con = sql.connect( 'database.db' ) 
            cur = con.cursor() 
            data = list( cur.execute( 'SELECT * FROM requests WHERE status == "{}" '.format( 'تحویل شده' ) ) ) 
            con.close() 

            if len(data) > 0 :
                self.request_number = data[0][0]
                self.rq_name = data[0][1]
                time = data[0][8]
                admin = data[0][10] 
                time2 = data[0][12] 
                j = 1 
                temp = [ time2, admin, time, self.rq_name, self.request_number, j ] 
                self.table035_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) ) 
                
                for i in range( len( data ) ): 
                    if data[i][0] != self.request_number:
                        self.request_number = data[i][0] 
                        self.rq_name = data[i][1]
                        time = data[i][8] 
                        admin = data[i][10] 
                        time2 = data[i][12] 
                        j = j + 1
                        temp = [ time2, admin, time, self.rq_name, self.request_number, j ]
                        if j % 2 :
                            self.table035_a.insert( parent = '', index = END , value = temp , tags = ('evenrow',) )
                        else: 
                            self.table035_a.insert( parent = '', index = END , value = temp , tags = ('oddrow',) )
            
            self.lbl035_note21.config( text = '' ) 

            self.frm035_1.place( x = 50 , y = 100 ) 
            self.frm035_2.place( x = 50  , y = 350 ) 


    def scnd_btn041(self):
        self.mainbtn04.grid( row = 7 , column = 1 )
        self.f_map_forget()
    
    def frm042_clear(self):
        self.ent042_g_code.delete( 0 , END )
        self.lbl042_g_name1['text'] = '' 
        self.lbl042_g_type1['text'] = '' 
        self.lbl042_gr_code1['text'] = '' 
        self.lbl042_gr_name1['text'] = '' 
        self.ent042_amount.delete( 0 , END )
        self.lbl042_unit.config( text = '' )
        self.cmb042_row_var.set('')
        self.cmb042_col_var.set('')
        self.cmb042_num_var.set('')
        self.ent042_note.delete( 0 , END )
        self.ent042_amount.config( state = 'disabled' )
        self.cmb042_row.config( state = 'disabled' )
        self.cmb042_col.config( state = 'disabled' )
        self.cmb042_num.config( state = 'disabled' )
        self.ent042_note.config( state = 'disabled' )
        self.imglbl042.config( image = self.upload_img )
        self.btn042_add_to_list.config( state = 'disabled' )

        self.ent042_delivery_doc.delete( 0 , END )
        self.ent042_delivery_doc.focus() 
        self.cmb042_delivery_var.set('انتخاب کنید')
        self.cmb042_delivery.config( state = 'disabled' )
        self.cmb042_delivery1_var.set('انتخاب کنید')
        self.cmb042_delivery1.grid_forget()
        self.lbl042_delivery1.grid_forget()
        self.lbl042_delivery2.grid_forget()
        self.lbl042_delivery3.grid_forget()
        self.ent042_delivery1.delete( 0 , END )
        self.ent042_delivery1.delete( 0 , END )
        self.ent042_delivery1.grid_forget()
        self.ent042_delivery2.grid_forget()

    def scnd_btn042(self):
        if self.frm042.winfo_ismapped():
            self.frm042.place_forget()
        else: 
            self.inner_frames_map_forget() 
            self.frm042_clear()
            self.frm042.place( x = 50 , y = 100 ) 
            self.ent042_delivery_doc.focus()
    
    def frm043_clear(self):
        self.ent043_g_code.delete( 0 , END )
        self.lbl043_g_name1['text'] = '' 
        self.lbl043_g_type1['text'] = '' 
        self.lbl043_gr_code1['text'] = '' 
        self.lbl043_gr_name1['text'] = '' 
        self.ent043_g_amount.delete( 0 , END )
        self.lbl043_unit.config( text = '' )
        self.ent043_note.delete( 0 , END )
        self.ent043_g_amount.config( state = 'disabled' )
        self.ent043_note.config( state = 'disabled' )
        self.btn043_add_to_list.config( state = 'disabled' )

        self.ent043_take_doc.delete( 0 , END )
        self.ent043_take_doc.focus() 
        self.cmb043_take_var.set('انتخاب کنید')
        self.cmb043_take.config( state = 'disabled' )
        self.cmb043_take1_var.set('انتخاب کنید')
        self.cmb043_take1.grid_forget()
        self.lbl043_take1.grid_forget()
        self.lbl043_take2.grid_forget()
        self.lbl043_take3.grid_forget()
        self.ent043_take1.delete( 0 , END )
        self.ent043_take1.delete( 0 , END )
        self.ent043_take1.grid_forget()
        self.ent043_take2.grid_forget()


    def scnd_btn043(self):
        if self.frm043.winfo_ismapped():
            self.frm043.place_forget()
        else: 
            self.inner_frames_map_forget() 
            self.frm043_clear() 
            self.frm043.place( x = 50 , y = 100 ) 
            self.ent043_take_doc.focus()

    def scnd_btn044(self): 
        
        if self.frm044_1.winfo_ismapped(): 
            self.frm044_1.place_forget() 
            self.frm044_2.place_forget() 
        else:
            self.inner_frames_map_forget()  
            for i in self.table044_a.get_children(): 
                self.table044_a.delete(i) 
            for i in self.table044_b.get_children(): 
                self.table044_b.delete(i)           
            
            self.lbl044_doc_number1.config( text = '' )
            self.lbl044_doc_type1.config( text = '' )
            self.lbl044_admin1.config( text = '' )
            self.lbl044_time1.config( text = '' )

            con = sql.connect( 'database.db' ) 
            cur = con.cursor() 
            data = list( cur.execute( 'SELECT * FROM docs' ) ) 
            con.close() 

            if len(data) > 0 :
                temp1 = []
                for i in data:
                    i = list(i)
                    temp1.append(i)

                temp = [temp1[0]]
                doc_number = temp1[0][0]
                for i in range( len( temp1 ) ) :
                    if temp1[i][0] != doc_number : 
                        temp.append(temp1[i])
                        doc_number = temp1[i][0] 
                
                for i in range( len( temp) ) :
                    j = i + 1
                    if temp[i][1] == 'Enter' :
                        lst = [temp[i][11], temp[i][10], temp[i][-1], 'ورود کالا', temp[i][0], j ]
                    else :
                        lst = [temp[i][11], temp[i][10], temp[i][-1], 'خروج کالا', temp[i][0], j ]

                    if j % 2 :
                        self.table044_a.insert( parent = '', index = END , value = lst , tags = ('evenrow',) )
                    else: 
                        self.table044_a.insert( parent = '', index = END , value = lst , tags = ('oddrow',) )

            self.frm044_1.place( x = 60 , y = 110 ) 
            self.frm044_2.place( x = 60 , y = 370 ) 


    # def scnd_btn051(self):
    #     self.mainbtn05.grid( row = 9 , column = 1 )
    #     self.f_map_forget()

    # def scnd_btn052(self):
    #     pass

    # def scnd_btn053(self):
    #     pass

    # def scnd_btn054(self):
    #     pass


    def scnd_btn061(self):                             # مربوط به صفحه تعريف گروه و کالا
        self.mainbtn06.grid( row = 11 , column = 1 )
        self.f_map_forget()

    def scnd_btn062(self):
        if self.frm062_gr.winfo_ismapped():
            self.frm062_gr.place_forget()
            self.frm062_g.place_forget()
        else:
            self.inner_frames_map_forget()
            self.ent062_gr_code.delete( 0 , END )
            self.ent062_gr_name.delete( 0 , END )
            self.ent062_gr_name.config( state = 'disabled' ) 
            self.btn062_submit_group.config( state = 'disabled' ) 
            self.gr_codes_list = self.get_gr_codes() 
            self.cmb062_g_gr.config( values = self.gr_codes_list )
            self.frm062_gr.place( x = 250 , y = 115 )

            self.cmb062_g_gr_var.set('انتخاب کنید')
            self.lbl062_gr_name1.config( text = '' )
            self.ent062_g_code.delete(0, END)
            self.ent062_g_name.delete(0, END)
            self.cmb062_g_type_var.set('انتخاب کنید')
            self.cmb062_g_measuring_var.set('انتخاب کنید')
            self.imglbl062_02.config( image = self.upload_img )
            self.units_map_forget()
            self.frm062_g.place( x = 140 , y = 330 ) 
            self.cmb062_g_gr.focus()
 
    def scnd_btn063(self):
        if self.frm063_01.winfo_ismapped():
            self.frm063_01.place_forget()
            self.frm063_02.place_forget()
        else:
            self.inner_frames_map_forget()
            for i in self.my_table_063_01_1.get_children():
                self.my_table_063_01_1.delete(i)
            for i in self.my_table_063_02.get_children():
                self.my_table_063_02.delete(i)
            self.frm063_01.place( x = 250 , y = 110 )
            self.frm063_02.place( x = 40  , y = 340 )

    def scnd_btn064(self): 
        if self.frm064_gr.winfo_ismapped():
            self.frm064_gr.place_forget() 
            self.frm064_g.place_forget() 
        else: 
            self.inner_frames_map_forget() 
            self.ent064_gr_code.delete( 0 , END ) 
            self.ent064_gr_name.delete( 0 , END )
            self.ent064_g_code .delete( 0 , END )
            self.ent064_g_name.delete( 0 , END )
            self.cmb064_g_type_var.set( '' )
            self.ent064_a_gr_code.delete( 0 , END )
            self.lbl064_a_gr_name1.config( text = '' )
            self.cmb064_g_measuring_var.set( '' )
            self.measuring_map_forget()
            self.imglbl064.config( image = self.upload_img )
            self.frm064_gr.place( x = 255 , y = 100 ) 
            self.frm064_g.place( x = 110 , y = 330 ) 
            self.ent064_gr_code.focus()


    def scnd_btn071(self):
        self.mainbtn07.grid( row = 13 , column = 1 )
        self.f_map_forget()

    def scnd_btn072(self):
        if self.frm072.winfo_ismapped():
            self.frm072.place_forget()
        else: 
            self.inner_frames_map_forget() 
            self.ent072_user_p_id.delete( 0 , END ) 
            self.ent072_user_name.delete( 0 , END )
            self.ent072_user_n_id.delete( 0 , END )
            self.ent072_user_username.delete( 0 , END )
            self.ent072_user_password.delete( 0 , END )
            self.imglbl072.config( image = self.upload_img )
            self.frm072.place( x = 150 , y = 160 ) 
            self.ent072_user_p_id.focus()

    def scnd_btn073(self):
        if self.frm073.winfo_ismapped():
            self.frm073.place_forget()
        else:
            self.inner_frames_map_forget()
            for i in self.users_table_073.get_children():
                self.users_table_073.delete(i)
            self.frm073.place( x = 150 , y = 150 ) 

    def scnd_btn074(self):
        if self.frm074.winfo_ismapped():
            self.frm074.place_forget()
        else:
            self.inner_frames_map_forget()
            self.ent074_user_p_id.delete( 0 , END )
            self.ent074_user_name.delete( 0 , END )
            self.ent074_user_n_id.delete( 0 , END )
            self.ent074_user_username.delete( 0 , END )
            self.ent074_user_password.delete( 0 , END ) 
            self.imglbl074.config( image = self.upload_img )
            self.ent074_user_p_id.focus()
            self.ent074_user_name.config( state = 'disabled' )
            self.ent074_user_n_id.config( state = 'disabled' )
            self.ent074_user_username.config( state = 'disabled' )
            self.ent074_user_password.config( state = 'disabled' )
            self.imgbtn074.config( state = 'disabled' )
            self.btn074_user_edit.config( state = 'disabled' )
            self.btn074_user_delete.config( state = 'disabled' )
            self.frm074.place( x = 120 , y = 160 )


    def scnd_btn081(self):
        self.mainbtn08.grid( row = 15 , column = 1 )
        self.f_map_forget()

    def scnd_btn082(self):
        if self.frm082_1.winfo_ismapped():
            self.frm082_1.place_forget()
            self.frm082_2.place_forget()
            self.frm082_3.place_forget()
        else:
            self.inner_frames_map_forget()
            self.ent082_request_num.delete( 0 , END ) 
            self.lbl082_requester1.config( text = self.current_user_lbl['text'] ) 
            self.frm082_1.place( x = 120 , y = 95 )
            for i in self.table082_2.get_children():
                self.table082_2.delete(i)
            self.frm082_2.place( x = 35 , y = 195 )
            self.frm082_3.place( x = 40 , y = 440 )
            self.ent082_request_num.focus()
            self.ent082_request_num.delete( 0 , END ) 
            self.ent082_g_code.delete( 0 , END )
            self.ent082_amount.delete( 0 , END )
            self.ent082_amount.config( state = 'disabled' )
            self.lbl082_g_name1.config( text = '' )
            self.lbl082_unit.config( text = '' )
            self.imglbl082.config( image = self.upload_img )
            self.ent082_note.config( state = 'disabled' )
            self.btn082_add_to_list.config( state = 'disabled' )
            for i in self.table082_2.get_children():
                self.table082_2.delete(i)
            for i in self.table082_3.get_children():
                self.table082_3.delete(i)

            self.btn082_3_delete_list.config( state = 'disabled' )
            self.btn082_3_submit_list.config( state = 'disabled' )


    def scnd_btn083(self):
        if self.frm083_1.winfo_ismapped():
            self.frm083_1.place_forget()
            self.frm083_2.place_forget()
        else:
            self.inner_frames_map_forget()
            for i in self.table083_a.get_children():
                self.table083_a.delete(i)
            for i in self.table083_b.get_children():
                self.table083_b.delete(i)
            self.cmb083_show_type_var.set('انتخاب کنید')
            self.cmb083_show_type.focus() 
            self.btn083_show.config( state = 'disabled' )
            self.lbl083_note21.config( text = '' )
            self.frm083_1.place( x = 65 , y = 105 ) 
            self.frm083_2.place( x = 65 , y = 390 )


    def scnd_btn101(self):
        self.mainbtn10.grid( row = 19 , column = 1 )
        self.f_map_forget()

    def scnd_btn102(self):                  # مربوط به خروج
        self.withdraw()
        self.w2_ent1.delete( 0 , END )
        self.w2_ent2.delete( 0 , END )
        self.w2_cmb_var.set( 'سمت' )
        self.w2_ent1.focus()
        self.win2.deiconify()
        self.f_map_forget()
        self.b_map_forget()
        self.w2_ent1.focus()
        self.inner_frames_map_forget()

    def scnd_btn103(self):
        self.destroy()


#================================================= main gui function =============================================
    def gui(self):
        self.geometry('1100x700+200+50')
        self.iconbitmap( '96.ico' )
        self.title( 'انبارداری صنعتی' )
        self.state('withdrawn')
        self.resizable( 0 , 0 ) 

        self.upload_img = ImageTk.PhotoImage( file = 'label_upload.png' )
        self.white_img = ImageTk.PhotoImage( file = 'label_blank.png' )
        self.note_img = ImageTk.PhotoImage( file = 'kate.png' )

        self.login_btn_bg = ImageTk.PhotoImage( file = 'button_enter.png' )
        self.submit_btn_bg = ImageTk.PhotoImage( file = 'button_submit.png' )
        self.upload_btn_bg = ImageTk.PhotoImage( file = 'button_photo_upload.png' )
        self.show_gr_btn_bg = ImageTk.PhotoImage( file = 'button_show_gr.png' )
        self.show_g_btn_bg = ImageTk.PhotoImage( file = 'button_show_g.png' )
        self.show_btn_bg = ImageTk.PhotoImage( file = 'button_show.png' )
        self.users_list_btn_bg = ImageTk.PhotoImage( file = 'button_show_users.png' )
        self.search_btn_bg = ImageTk.PhotoImage( file = 'button_search.png' )
        self.edit_btn_bg = ImageTk.PhotoImage( file = 'button_edit.png' )
        self.delete_btn_bg = ImageTk.PhotoImage( file = 'button_delete.png' )
        self.change_btn_bg = ImageTk.PhotoImage( file = 'button_photo_change.png' )
        self.add_to_list_btn_bg = ImageTk.PhotoImage( file = 'button_add_to_list.png' )
        self.delete_from_list_btn_bg = ImageTk.PhotoImage( file = 'button_delete_from_list.png' )
        self.delete_list_btn_bg = ImageTk.PhotoImage( file = 'button_delete_list.png' )
        self.delivery_submit_btn_bg = ImageTk.PhotoImage( file = 'button_delivery_submit.png' )
        self.take_submit_btn_bg = ImageTk.PhotoImage( file = 'button_take_submit.png' )
        self.take_submit_btn2_bg = ImageTk.PhotoImage( file = 'button_take_submit2.png' )
        self.approve_request_btn_bg = ImageTk.PhotoImage( file = 'button_approve_request.png' )
        self.approve_reject_btn_bg = ImageTk.PhotoImage( file = 'button_reject_request.png' )

        self.loginbg = ImageTk.PhotoImage( file = 'login_bg.png' )

        self.main_bg = ImageTk.PhotoImage( file = 'main_bg1.png' )
        self.bg_lbl = Label( self, image = self.main_bg )
        self.bg_lbl.place( x = -2 , y = -2 )


               
        self.frm0 = Frame( self , bg = '#345382' )
        self.frm0.place( x = 872 , y = 100 )


        self.current_user_lbl = Label( self, width = 13, height = 1, bd = 0, text = '',
                                       font = ('homa', 12), fg = 'gray35', bg = 'white', anchor = 'e' )
        

        self.mainbtn01 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'وضعيت انبار',
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn01 )
        # self.mainbtn02 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'ثبت سفارش انباردار',
        #                         font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn02 )
        self.mainbtn03 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'مديريت درخواست‌ها', 
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn03 )
        self.mainbtn04 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'ورود و خروج کالا',
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn04 )
        # self.mainbtn05 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'مدیریت دوره', 
        #                         font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn05 )
        self.mainbtn06 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'تعریف گروه و کالا',
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn06 )
        self.mainbtn07 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'تعریف افراد', 
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn07 )
        self.mainbtn08 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'درخواست کالا',  
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn08 )
        self.mainbtn10 = Button( self.frm0, width = 18, height = 1, bd = 0, text = 'خروج', 
                                font = ('homa', 12), fg = 'white', bg = '#345382', command = self.main_btn10 )

        self.frm01 = Frame( self.frm0 )
        # self.frm02 = Frame( self.frm0 )
        self.frm03 = Frame( self.frm0 )
        self.frm04 = Frame( self.frm0 )
        # self.frm05 = Frame( self.frm0 )
        self.frm06 = Frame( self.frm0 )
        self.frm07 = Frame( self.frm0 )
        self.frm08 = Frame( self.frm0 )
        self.frm10 = Frame( self.frm0 )
        
        self.scndbtn011 = Button( self.frm01, width = 18, bd = 0, text = 'وضعيت انبار', 
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn011 )
        self.scndbtn012 = Button( self.frm01, width = 18, bd = 0, text = 'موجودی انبار', 
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn012 )
        self.scndbtn013 = Button( self.frm01, width = 18, bd = 0, text = 'جستجوی کالا در انبار', 
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn013 )
        self.scndbtn014 = Button( self.frm01, width = 18, bd = 0, text = 'انبارگردانی', 
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn014 )
        

        # self.scndbtn021 = Button( self.frm02, width = 18, bd = 0, text = 'ثبت سفارش انباردار',
        #                          font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn021 )
        # self.scndbtn022 = Button( self.frm02, width = 18, bd = 0, text = 'ثبت سفارش تامین کالا',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn022 )
        # self.scndbtn023 = Button( self.frm02, width = 18, bd = 0, text = 'صدور حواله مرجوعی',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn023 )
        # self.scndbtn024 = Button( self.frm02, width = 18, bd = 0, text = 'صدور حواله تخلیه',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn024 )
        # self.scndbtn025 = Button( self.frm02, width = 18, bd = 0, text = 'تاریخچه',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn025 )
        

        self.scndbtn031 = Button( self.frm03, width = 18, bd = 0, text = 'مديريت درخواست‌ها', 
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn031 )
        self.scndbtn032 = Button( self.frm03, width = 18, bd = 0, text = 'درخواست‌های در صف انتظار',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn032 )
        self.scndbtn033 = Button( self.frm03, width = 18, bd = 0, text = 'درخواست‌های جاری',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn033 )
        self.scndbtn034 = Button( self.frm03, width = 18, bd = 0, text = 'درخواست‌های رد شده',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn034 )
        self.scndbtn035 = Button( self.frm03, width = 18, bd = 0, text = 'درخواست‌های تحویل شده',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn035 )
        

        self.scndbtn041 = Button( self.frm04, width = 18, bd = 0, text = 'ورود و خروج کالا',
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn041 )
        self.scndbtn042 = Button( self.frm04, width = 18, bd = 0, text = 'ثبت ورود کالا',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn042 )
        self.scndbtn043 = Button( self.frm04, width = 18, bd = 0, text = 'ثبت خروج کالا',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn043 )
        self.scndbtn044 = Button( self.frm04, width = 18, bd = 0, text = 'تاریخچه ورود و خروج',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn044 )
        

        # self.scndbtn051 = Button( self.frm05, width = 18, bd = 0, text = 'مدیریت دوره',
        #                          font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn051 )
        # self.scndbtn052 = Button( self.frm05, width = 18, bd = 0, text = 'تعریف دوره جدید',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn052 )
        # self.scndbtn053 = Button( self.frm05, width = 18, bd = 0, text = 'گزارشات دوره کنونی',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn053 )
        # self.scndbtn054 = Button( self.frm05, width = 18, bd = 0, text = 'دوره‌های قبلی',
        #                          font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn054 )
        

        self.scndbtn061 = Button( self.frm06, width = 18, bd = 0, text = 'تعريف گروه و کالا',
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn061 )
        self.scndbtn062 = Button( self.frm06, width = 18, bd = 0, text = 'تعریف گروه/کالای جدید',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn062 )
        self.scndbtn063 = Button( self.frm06, width = 18, bd = 0, text = 'لیست گروه‌ها/کالاها',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn063 )
        self.scndbtn064 = Button( self.frm06, width = 18, bd = 0, text = 'جستجو و ویرایش',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn064 )
        

        self.scndbtn071 = Button( self.frm07, width = 18, bd = 0, text = 'تعريف افراد',
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn071 )
        self.scndbtn072 = Button( self.frm07, width = 18, bd = 0, text = 'تعریف کاربر جدید',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn072 )
        self.scndbtn073 = Button( self.frm07, width = 18, bd = 0, text = 'لیست کاربران',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn073 )
        self.scndbtn074 = Button( self.frm07, width = 18, bd = 0, text = 'ویرایش/حذف کاربر',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn074 )
        

        self.scndbtn081 = Button( self.frm08, width = 18, bd = 0, text = 'درخواست کالا',
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn081 )
        self.scndbtn082 = Button( self.frm08, width = 18, bd = 0, text = 'ثبت درخواست کالا',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn082 )
        self.scndbtn083 = Button( self.frm08, width = 18, bd = 0, text = 'درخواست‌های من',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn083 )
        

        self.scndbtn101 = Button( self.frm10, width = 18, bd = 0, text = 'خروج',
                                 font = ('homa', 12), fg = 'white', bg = '#436291', command = self.scnd_btn101 )
        self.scndbtn102 = Button( self.frm10, width = 18, bd = 0, text = 'خروج از حساب کاربری',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn102 )
        self.scndbtn103 = Button( self.frm10, width = 18, bd = 0, text = 'خروج از برنامه',
                                 font = ('homa', 12), fg = 'white', bg = '#4c6c9c', command = self.scnd_btn103 )

        

         # صفحه موجودی انبار
        self.frm012 = LabelFrame( self , text = '  موجودی انبار  ' , font = ('homa', 13) , bg = 'white' ,
                                  fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 10 )

        self.frm012_a = Frame( self.frm012 ) 
        self.frm012_a.pack( side = TOP , fill = X , pady = 5)

        self.scrl012 = Scrollbar( self.frm012_a ) 
        self.scrl012.pack( side = RIGHT , fill = Y)

        self.table012 = ttk.Treeview( self.frm012_a, columns = ['آدرس', 'نقطه سفارش', 'واحد', 'تعداد/مقدار', 'نوع کالا', 
                                                                'نام گروه', 'کد گروه', 'نام کالا', 'کد کالا'],
                                             yscrollcommand = self.scrl012.set, selectmode = 'browse', height = 10 )
        self.scrl012.config( command = self.table012.yview )

        self.table012.column( '#0'           , width = 0  , minwidth = 0 )
        self.table012.column( 'آدرس'         , width = 60 , minwidth = 50 , anchor = 'center' )
        self.table012.column( 'نقطه سفارش'   , width = 80 , minwidth = 50 , anchor = 'center' )
        self.table012.column( 'واحد'          , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table012.column( 'تعداد/مقدار'  , width = 70 , minwidth = 50 , anchor = 'center' )
        self.table012.column( 'نوع کالا'      , width = 70 , minwidth = 50  , anchor = 'center' )
        self.table012.column( 'نام گروه'     , width = 110 , minwidth = 50 , anchor = 'center' )
        self.table012.column( 'کد گروه'      , width = 50 , minwidth = 50  , anchor = 'center' )
        self.table012.column( 'نام کالا'      , width = 120 , minwidth = 50 , anchor = 'center' )
        self.table012.column( 'کد کالا'       , width = 50 , minwidth = 50  , anchor = 'center' )

        self.table012.heading( '#0'           , text = ''              , anchor = 'center' )
        self.table012.heading( 'آدرس'         , text = 'آدرس'          , anchor = 'center' )
        self.table012.heading( 'نقطه سفارش'   , text = 'نقطه سفارش'   , anchor = 'center' )
        self.table012.heading( 'واحد'          , text = 'واحد'         , anchor = 'center' )
        self.table012.heading( 'تعداد/مقدار'  , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table012.heading( 'نوع کالا'      , text = 'نوع کالا'       , anchor = 'center' )
        self.table012.heading( 'نام گروه'     , text = 'نام گروه'      , anchor = 'center' )
        self.table012.heading( 'کد گروه'      , text = 'کد گروه'       , anchor = 'center' )
        self.table012.heading( 'نام کالا'      , text = 'نام کالا'       , anchor = 'center' )
        self.table012.heading( 'کد کالا'       , text = 'کد کالا'        , anchor = 'center' )

        self.table012.tag_configure('oddrow',  background = 'white') 
        self.table012.tag_configure('evenrow', background = 'lightblue') 

        self.lbl012_show_type = Label( self.frm012, text = '  :نوع نمایش  ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 


        self.cmb012_show_type_var = StringVar( self ) 
        self.cmb012_show_type_var.set( 'انتخاب کنید' ) 
        self.cmb012_show_type_options = ['موجودی کل انبار', 'نیازمند تجدید سفارش', 'به تفکیک ردیف'] 
        self.cmb012_show_type = ttk.Combobox( self.frm012 , width = 18 , textvariable = self.cmb012_show_type_var,
                                             values = self.cmb012_show_type_options, state = 'readonly', justify = 'center') 
        
        self.cmb012_show_type.bind('<<ComboboxSelected>>', self.cmb012_show_type_func ) 
        
        self.lbl012_row = Label( self.frm012, text = '  :ردیف  ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 

        
        self.cmb012_row_var = StringVar( self ) 
        self.cmb012_row_var.set( '...' ) 
        self.cmb012_row_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] 
        self.cmb012_row = ttk.Combobox( self.frm012, width = 3 , textvariable = self.cmb012_row_var,
                                       values = self.cmb012_row_options, state = 'readonly', justify = 'center') 
        

        self.btn012_show = Button( self.frm012, image = self.show_btn_bg, bd = 0, bg = 'white', state = 'disabled', command = self.show_warehouse_stock )

        self.table012.pack()
        self.lbl012_show_type.pack( side = RIGHT , pady = 5 )
        self.cmb012_show_type.pack( side = RIGHT, pady = 5 )
        self.btn012_show.pack( side = LEFT, pady = 5 )

        self.cmb012_row.bind('<<ComboboxSelected>>', self.cmb012_row_func )  
        self.btn012_show.bind('<Return>', self.show_warehouse_stock )

         # صفحه جستجوی کالا در انبار
        self.frm013 = Frame( self )

         # صفحه انبارگردانی
        self.frm014 = Frame( self )


 

        #  # صفحه سفارش تامین کالا
        # self.frm022 = Frame( self )

        #  # صفحه صدور حواله مرجوعی
        # self.frm023 = Frame( self )

        #  # صفحه صدور حواله تخلیه ضایعات
        # self.frm024 = Frame( self )

        #  # صفحه تاریخچه
        # self.frm025 = Frame( self )



         # صفحه درخواست های در صف انتظار
        self.frm032_1 = LabelFrame( self , text = '  لیست درخواست‌ها  ' , font = ('homa', 13) , 
                                  bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 15 )

        self.frm032_a = Frame( self.frm032_1 ) 
        self.frm032_a.grid( row = 1 , rowspan = 5 , column = 1 )

        self.scrl032_a = Scrollbar( self.frm032_a ) 

        self.table032_a = ttk.Treeview( self.frm032_a, columns = ['تاریخ', 'ثبت کننده', 'شماره درخواست', 'ردیف'],
                                        yscrollcommand = self.scrl032_a.set, selectmode = 'extended', height = 8 )
        
        self.scrl032_a.config( command = self.table032_a.yview )

        self.table032_a.column( '#0'             , width = 0  , minwidth = 0 ) 
        self.table032_a.column( 'تاریخ'          , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table032_a.column( 'ثبت کننده'      , width = 130 , minwidth = 80 , anchor = 'center' ) 
        self.table032_a.column( 'شماره درخواست'  , width = 120  , minwidth = 60 , anchor = 'center' )  
        self.table032_a.column( 'ردیف'            , width = 50  , minwidth = 50 , anchor = 'center' ) 

        self.table032_a.heading( '#0'             , text = ''                  , anchor = 'center' ) 
        self.table032_a.heading( 'تاریخ'          , text = 'تاریخ'            , anchor = 'center' ) 
        self.table032_a.heading( 'ثبت کننده'      , text = 'ثبت کننده'        , anchor = 'center' ) 
        self.table032_a.heading( 'شماره درخواست' , text = 'شماره درخواست'    , anchor = 'center' )  
        self.table032_a.heading( 'ردیف'           , text = 'ردیف'             , anchor = 'center' ) 

        self.table032_a.tag_configure('oddrow',  background = 'white') 
        self.table032_a.tag_configure('evenrow', background = 'lightblue') 


        self.scrl032_a.pack( side = RIGHT , fill = Y ) 
        self.table032_a.pack() 

        
        self.table032_a.bind( '<ButtonRelease-1>', self.table032_a_select ) 



        self.frm032_2 = LabelFrame( self , text = '  جزئیات درخواست  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl032_request_number  = Label( self.frm032_2, text = ':شماره درخواست', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl032_request_number1 = Label( self.frm032_2, bg = 'white', width = 6 ) 
        self.lbl032_rq_name  = Label( self.frm032_2, text = ':ثبت کننده' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl032_rq_name1 = Label( self.frm032_2, bg = 'white', width = 10 ) 
        self.lbl032_p_id     = Label( self.frm032_2, text = ':کد پرسنلی' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl032_p_id1    = Label( self.frm032_2, bg = 'white', width = 4 ) 
        self.lbl032_time     = Label( self.frm032_2, text = ':تاریخ'     , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl032_time1    = Label( self.frm032_2, bg = 'white', width = 14 ) 

        self.frm032_b = Frame( self.frm032_2 )

        self.scrl032_b = Scrollbar( self.frm032_b ) 
        self.scrl032_b.pack( side = RIGHT , fill = Y )

        self.table032_b = ttk.Treeview( self.frm032_b, columns = ['نقطۀ سفارش', 'موجودی فعلی', 'توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl032_b.set, selectmode = 'extended', height = 8 )
        
        self.scrl032_b.config( command = self.table032_b.yview )

        self.table032_b.column( '#0'              , width = 0  , minwidth = 0   )  
        self.table032_b.column( 'نقطۀ سفارش'     , width = 80 , minwidth = 80 , anchor = 'center' ) 
        self.table032_b.column( 'موجودی فعلی'    , width = 80 , minwidth = 80  , anchor = 'center' ) 
        self.table032_b.column( 'توضیح'          , width = 150 , minwidth = 60  , anchor = 'center' )  
        self.table032_b.column( 'واحد'           , width = 100 , minwidth = 50  , anchor = 'center' ) 
        self.table032_b.column( 'تعداد/مقدار'    , width = 70 , minwidth = 50 , anchor = 'center' ) 
        self.table032_b.column( 'نام کالا'        , width = 130  , minwidth = 50 , anchor = 'center' ) 
        self.table032_b.column( 'کد کالا'         , width = 50  , minwidth = 50 , anchor = 'center' ) 
        self.table032_b.column( 'ردیف'           , width = 35  , minwidth = 35 , anchor = 'center' )  

        self.table032_b.heading( '#0'           , text = ''             , anchor = 'center' ) 
        self.table032_b.heading( 'نقطۀ سفارش'  , text = 'نقطۀ سفارش'  , anchor = 'center' ) 
        self.table032_b.heading( 'موجودی فعلی' , text = 'موجودی فعلی' , anchor = 'center' ) 
        self.table032_b.heading( 'توضیح'       , text = 'توضیح'        , anchor = 'center' )  
        self.table032_b.heading( 'واحد'        , text = 'واحد'         , anchor = 'center' ) 
        self.table032_b.heading( 'تعداد/مقدار' , text = 'تعداد/مقدار' , anchor = 'center' ) 
        self.table032_b.heading( 'نام کالا'     , text = 'نام کالا'      , anchor = 'center' ) 
        self.table032_b.heading( 'کد کالا'      , text = 'کد کالا'       , anchor = 'center' ) 
        self.table032_b.heading( 'ردیف'        , text = 'ردیف'         , anchor = 'center' ) 

        self.table032_b.tag_configure('oddrow',  background = 'white') 
        self.table032_b.tag_configure('evenrow', background = 'lightblue') 

        self.table032_b.pack() 

        self.lbl032_note2 = Label( self.frm032_2, text = ':توضیح انباردار', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent032_note2 = Entry( self.frm032_2, bg = 'white', justify = 'right', state = 'disabled', width = 55 ) 

        self.btn032_approve = Button( self.frm032_2, image = self.approve_request_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.approve_request ) 
        self.btn032_reject  = Button( self.frm032_2, image = self.approve_reject_btn_bg  , bd = 0, bg = 'white', state = 'disabled', command = self.reject_request  ) 

        self.lbl032_request_number .grid( row = 1 , column = 8 , padx = 5 , pady = 5 )    
        self.lbl032_request_number1.grid( row = 1 , column = 7 , padx = 5 )
        self.lbl032_rq_name        .grid( row = 1 , column = 6 , padx = 5 ) 
        self.lbl032_rq_name1       .grid( row = 1 , column = 5 , padx = 5 ) 
        self.lbl032_p_id           .grid( row = 1 , column = 4 , padx = 5 )
        self.lbl032_p_id1          .grid( row = 1 , column = 3 , padx = 5 )
        self.lbl032_time           .grid( row = 1 , column = 2 , padx = 5 )
        self.lbl032_time1          .grid( row = 1 , column = 1 , padx = 5 )
        self.frm032_b              .grid( row = 2 , column = 1 , columnspan = 8 )
        self.table032_b            .pack( ) 
        self.lbl032_note2          .grid( row = 3 , column = 8 , pady = 5  )
        self.ent032_note2          .grid( row = 3 , column = 4 , columnspan = 4 , sticky = 'e' ) 
        self.btn032_approve        .grid( row = 3 , column = 1 , pady = 5 )
        self.btn032_reject         .grid( row = 3 , column = 2 , columnspan = 1 , sticky = 'w' ) 


         # درخواست های جاری
        self.frm033_1 = LabelFrame( self , text = '  لیست درخواست‌های جاری  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 15 )

        self.frm033_a = Frame( self.frm033_1 ) 
        self.frm033_a.grid( row = 1 , rowspan = 5 , column = 1 )

        self.scrl033_a = Scrollbar( self.frm033_a ) 

        self.table033_a = ttk.Treeview( self.frm033_a, columns = ['تاریخ تایید', 'تایید کننده', 'تاریخ درخواست', 'ثبت کننده', 'شماره درخواست', 'ردیف'],
                                        yscrollcommand = self.scrl033_a.set, selectmode = 'extended', height = 8 )
        
        self.scrl033_a.config( command = self.table033_a.yview )

        self.table033_a.column( '#0'               , width = 0    , minwidth = 0  )  
        self.table033_a.column( 'تاریخ تایید'     , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table033_a.column( 'تایید کننده'     , width = 130  , minwidth = 80  , anchor = 'center' ) 
        self.table033_a.column( 'تاریخ درخواست'   , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table033_a.column( 'ثبت کننده'       , width = 130  , minwidth = 80  , anchor = 'center' ) 
        self.table033_a.column( 'شماره درخواست'   , width = 125  , minwidth = 60  , anchor = 'center' )  
        self.table033_a.column( 'ردیف'             , width = 50   , minwidth = 50  , anchor = 'center' ) 

        self.table033_a.heading( '#0'               , text = ''                  , anchor = 'center' ) 
        self.table033_a.heading( 'تاریخ تایید'     , text = 'تاریخ تایید'      , anchor = 'center' ) 
        self.table033_a.heading( 'تایید کننده'     , text = 'تایید کننده'      , anchor = 'center' ) 
        self.table033_a.heading( 'تاریخ درخواست'   , text = 'تاریخ درخواست'    , anchor = 'center' ) 
        self.table033_a.heading( 'ثبت کننده'       , text = 'ثبت کننده'         , anchor = 'center' ) 
        self.table033_a.heading( 'شماره درخواست'   , text = 'شماره درخواست'    , anchor = 'center' )  
        self.table033_a.heading( 'ردیف'             , text = 'ردیف'              , anchor = 'center' ) 

        self.table033_a.tag_configure('oddrow',  background = 'white') 
        self.table033_a.tag_configure('evenrow', background = 'lightblue') 

        self.scrl033_a.pack( side = RIGHT , fill = Y ) 
        self.table033_a.pack() 
     
        self.table033_a.bind( '<ButtonRelease-1>', self.table033_a_select ) 



        self.frm033_2 = LabelFrame( self , text = '  جزئیات درخواست  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl033_request_number  = Label( self.frm033_2, text = ':شماره درخواست', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl033_request_number1 = Label( self.frm033_2, bg = 'white', width = 6 ) 
        self.lbl033_rq_name  = Label( self.frm033_2, text = ':ثبت کننده' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl033_rq_name1 = Label( self.frm033_2, bg = 'white', width = 10 ) 
        self.lbl033_p_id     = Label( self.frm033_2, text = ':کد پرسنلی' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl033_p_id1    = Label( self.frm033_2, bg = 'white', width = 4 ) 
        self.lbl033_time     = Label( self.frm033_2, text = ':تاریخ'     , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl033_time1    = Label( self.frm033_2, bg = 'white', width = 14 ) 

        self.frm033_b = Frame( self.frm033_2 )

        self.scrl033_b = Scrollbar( self.frm033_b ) 
        self.scrl033_b.pack( side = RIGHT , fill = Y )

        self.table033_b = ttk.Treeview( self.frm033_b, columns = ['نقطۀ سفارش', 'موجودی فعلی', 'توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl033_b.set, selectmode = 'extended', height = 8 )
        
        self.scrl033_b.config( command = self.table033_b.yview )

        self.table033_b.column( '#0'               , width = 0   , minwidth = 0   )  
        self.table033_b.column( 'نقطۀ سفارش'      , width = 80  , minwidth = 80 , anchor = 'center' ) 
        self.table033_b.column( 'موجودی فعلی'     , width = 80  , minwidth = 80 , anchor = 'center' ) 
        self.table033_b.column( 'توضیح'           , width = 150 , minwidth = 60 , anchor = 'center' )  
        self.table033_b.column( 'واحد'            , width = 100 , minwidth = 50 , anchor = 'center' ) 
        self.table033_b.column( 'تعداد/مقدار'    , width = 70  , minwidth = 50 , anchor = 'center' ) 
        self.table033_b.column( 'نام کالا'        , width = 130 , minwidth = 50 , anchor = 'center' ) 
        self.table033_b.column( 'کد کالا'         , width = 50  , minwidth = 50 , anchor = 'center' ) 
        self.table033_b.column( 'ردیف'           , width = 35  , minwidth = 35 , anchor = 'center' )  

        self.table033_b.heading( '#0'            , text = ''             , anchor = 'center' ) 
        self.table033_b.heading( 'نقطۀ سفارش'   , text = 'نقطۀ سفارش'  , anchor = 'center' ) 
        self.table033_b.heading( 'موجودی فعلی'  , text = 'موجودی فعلی' , anchor = 'center' ) 
        self.table033_b.heading( 'توضیح'        , text = 'توضیح'        , anchor = 'center' )  
        self.table033_b.heading( 'واحد'         , text = 'واحد'         , anchor = 'center' ) 
        self.table033_b.heading( 'تعداد/مقدار' , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table033_b.heading( 'نام کالا'     , text = 'نام کالا'       , anchor = 'center' ) 
        self.table033_b.heading( 'کد کالا'      , text = 'کد کالا'        , anchor = 'center' ) 
        self.table033_b.heading( 'ردیف'        , text = 'ردیف'          , anchor = 'center' ) 

        self.table033_b.tag_configure('oddrow',  background = 'white') 
        self.table033_b.tag_configure('evenrow', background = 'lightblue') 

        self.table033_b.pack() 

        self.lbl033_note2  = Label( self.frm033_2, text = ':توضیح انباردار', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl033_note21 = Label( self.frm033_2, text = '', bg = 'white')

        self.btn033_submit  = Button( self.frm033_2, image = self.take_submit_btn2_bg  , bd = 0, bg = 'white', state = 'disabled', command = self.btn033_submit_func ) 

        self.lbl033_request_number .grid( row = 1 , column = 8 , padx = 5 , pady = 5 )    
        self.lbl033_request_number1.grid( row = 1 , column = 7 , padx = 5 )
        self.lbl033_rq_name        .grid( row = 1 , column = 6 , padx = 5 ) 
        self.lbl033_rq_name1       .grid( row = 1 , column = 5 , padx = 5 ) 
        self.lbl033_p_id           .grid( row = 1 , column = 4 , padx = 5 )
        self.lbl033_p_id1          .grid( row = 1 , column = 3 , padx = 5 )
        self.lbl033_time           .grid( row = 1 , column = 2 , padx = 5 )
        self.lbl033_time1          .grid( row = 1 , column = 1 , padx = 5 )
        self.frm033_b              .grid( row = 2 , column = 1 , columnspan = 8 )
        self.table033_b            .pack( ) 
        self.lbl033_note2          .grid( row = 3 , column = 8 , pady = 5 )
        self.lbl033_note21         .grid( row = 3 , column = 4 , columnspan = 4 , sticky = 'e' )
        self.btn033_submit         .grid( row = 3 , column = 1 , pady = 5 )


         # درخواست های رد شده
        self.frm034_1 = LabelFrame( self , text = '  لیست درخواست‌های رد شده  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 15 )

        self.frm034_a = Frame( self.frm034_1 ) 
        self.frm034_a.grid( row = 1 , rowspan = 5 , column = 1 )

        self.scrl034_a = Scrollbar( self.frm034_a ) 

        self.table034_a = ttk.Treeview( self.frm034_a, columns = ['تاریخ رد درخواست', 'رد کننده درخواست', 'تاریخ درخواست', 'ثبت کننده', 'شماره درخواست', 'ردیف'],
                                        yscrollcommand = self.scrl034_a.set, selectmode = 'extended', height = 8 )
        
        self.scrl034_a.config( command = self.table034_a.yview )

        self.table034_a.column( '#0'                , width = 0  , minwidth = 0 ) 
        self.table034_a.column( 'تاریخ رد درخواست' , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table034_a.column( 'رد کننده درخواست' , width = 130  , minwidth = 80 , anchor = 'center' ) 
        self.table034_a.column( 'تاریخ درخواست'    , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table034_a.column( 'ثبت کننده'        , width = 130  , minwidth = 80 , anchor = 'center' ) 
        self.table034_a.column( 'شماره درخواست'    , width = 125  , minwidth = 60 , anchor = 'center' )  
        self.table034_a.column( 'ردیف'              , width = 50  , minwidth = 50 , anchor = 'center' ) 

        self.table034_a.heading( '#0'                 , text = ''                   , anchor = 'center' ) 
        self.table034_a.heading( 'تاریخ رد درخواست'  , text = 'تاریخ رد درخواست'  , anchor = 'center' ) 
        self.table034_a.heading( 'رد کننده درخواست'  , text = 'رد کننده درخواست'  , anchor = 'center' ) 
        self.table034_a.heading( 'تاریخ درخواست'     , text = 'تاریخ درخواست'     , anchor = 'center' ) 
        self.table034_a.heading( 'ثبت کننده'         , text = 'ثبت کننده'          , anchor = 'center' ) 
        self.table034_a.heading( 'شماره درخواست'     , text = 'شماره درخواست'     , anchor = 'center' )  
        self.table034_a.heading( 'ردیف'               , text = 'ردیف'               , anchor = 'center' ) 

        self.table034_a.tag_configure('oddrow',  background = 'white') 
        self.table034_a.tag_configure('evenrow', background = 'lightblue') 

        self.scrl034_a.pack( side = RIGHT , fill = Y ) 
        self.table034_a.pack() 
        
        self.table034_a.bind( '<ButtonRelease-1>', self.table034_a_select ) 



        self.frm034_2 = LabelFrame( self , text = '  جزئیات درخواست  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl034_request_number  = Label( self.frm034_2, text = ':شماره درخواست', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl034_request_number1 = Label( self.frm034_2, bg = 'white', width = 6 ) 
        self.lbl034_rq_name  = Label( self.frm034_2, text = ':ثبت کننده' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl034_rq_name1 = Label( self.frm034_2, bg = 'white', width = 10 ) 
        self.lbl034_p_id     = Label( self.frm034_2, text = ':کد پرسنلی' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl034_p_id1    = Label( self.frm034_2, bg = 'white', width = 4 ) 
        self.lbl034_time     = Label( self.frm034_2, text = ':تاریخ'     , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl034_time1    = Label( self.frm034_2, bg = 'white', width = 14 ) 

        self.frm034_b = Frame( self.frm034_2 )

        self.scrl034_b = Scrollbar( self.frm034_b ) 
        self.scrl034_b.pack( side = RIGHT , fill = Y )

        self.table034_b = ttk.Treeview( self.frm034_b, columns = ['نقطۀ سفارش', 'موجودی فعلی', 'توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl034_b.set, selectmode = 'extended', height = 8 )
        
        self.scrl034_b.config( command = self.table034_b.yview )

        self.table034_b.column( '#0'               , width = 0   , minwidth = 0   )  
        self.table034_b.column( 'نقطۀ سفارش'      , width = 80  , minwidth = 80 , anchor = 'center' ) 
        self.table034_b.column( 'موجودی فعلی'     , width = 80  , minwidth = 80 , anchor = 'center' ) 
        self.table034_b.column( 'توضیح'           , width = 150 , minwidth = 60 , anchor = 'center' )  
        self.table034_b.column( 'واحد'            , width = 100 , minwidth = 50 , anchor = 'center' ) 
        self.table034_b.column( 'تعداد/مقدار'    , width = 70  , minwidth = 50 , anchor = 'center' ) 
        self.table034_b.column( 'نام کالا'        , width = 130 , minwidth = 50 , anchor = 'center' ) 
        self.table034_b.column( 'کد کالا'         , width = 50  , minwidth = 50 , anchor = 'center' ) 
        self.table034_b.column( 'ردیف'           , width = 35  , minwidth = 35 , anchor = 'center' )  

        self.table034_b.heading( '#0'            , text = ''              , anchor = 'center' ) 
        self.table034_b.heading( 'نقطۀ سفارش'   , text = 'نقطۀ سفارش'   , anchor = 'center' ) 
        self.table034_b.heading( 'موجودی فعلی'  , text = 'موجودی فعلی'  , anchor = 'center' ) 
        self.table034_b.heading( 'توضیح'        , text = 'توضیح'         , anchor = 'center' )  
        self.table034_b.heading( 'واحد'         , text = 'واحد'          , anchor = 'center' ) 
        self.table034_b.heading( 'تعداد/مقدار'  , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table034_b.heading( 'نام کالا'      , text = 'نام کالا'       , anchor = 'center' ) 
        self.table034_b.heading( 'کد کالا'       , text = 'کد کالا'        , anchor = 'center' ) 
        self.table034_b.heading( 'ردیف'         , text = 'ردیف'          , anchor = 'center' ) 

        self.table034_b.tag_configure('oddrow',  background = 'white') 
        self.table034_b.tag_configure('evenrow', background = 'lightblue') 

        self.table034_b.pack() 

        self.lbl034_note2  = Label( self.frm034_2, text = ':توضیح انباردار', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl034_note21 = Label( self.frm034_2, text = '               ' , bg = 'white' ) 

        self.lbl034_request_number .grid( row = 1 , column = 8 , padx = 5 , pady = 5 )    
        self.lbl034_request_number1.grid( row = 1 , column = 7 , padx = 5 )
        self.lbl034_rq_name        .grid( row = 1 , column = 6 , padx = 5 ) 
        self.lbl034_rq_name1       .grid( row = 1 , column = 5 , padx = 5 ) 
        self.lbl034_p_id           .grid( row = 1 , column = 4 , padx = 5 )
        self.lbl034_p_id1          .grid( row = 1 , column = 3 , padx = 5 )
        self.lbl034_time           .grid( row = 1 , column = 2 , padx = 5 )
        self.lbl034_time1          .grid( row = 1 , column = 1 , padx = 5 )
        self.frm034_b              .grid( row = 2 , column = 1 , columnspan = 8 )
        self.table034_b            .pack( ) 
        self.lbl034_note2          .grid( row = 3 , column = 8 , pady = 5 )
        self.lbl034_note21         .grid( row = 3 , column = 1 , columnspan = 7 , sticky = 'e' ) 

         # صفحه درخواست های تحویل شده
        self.frm035_1 = LabelFrame( self , text = '  لیست درخواست‌های تحویل شده  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 15 )

        self.frm035_a = Frame( self.frm035_1 ) 
        self.frm035_a.grid( row = 1 , rowspan = 5 , column = 1 )

        self.scrl035_a = Scrollbar( self.frm035_a ) 

        self.table035_a = ttk.Treeview( self.frm035_a, columns = ['تاریخ تحویل', 'تحویل دهنده', 'تاریخ درخواست', 'ثبت کننده', 'شماره درخواست', 'ردیف'],
                                        yscrollcommand = self.scrl035_a.set, selectmode = 'extended', height = 8 )
        
        self.scrl035_a.config( command = self.table035_a.yview )

        self.table035_a.column( '#0'               , width = 0    , minwidth = 0  )  
        self.table035_a.column( 'تاریخ تحویل'     , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table035_a.column( 'تحویل دهنده'     , width = 130  , minwidth = 80  , anchor = 'center' ) 
        self.table035_a.column( 'تاریخ درخواست'   , width = 130  , minwidth = 100 , anchor = 'center' ) 
        self.table035_a.column( 'ثبت کننده'       , width = 130  , minwidth = 80  , anchor = 'center' ) 
        self.table035_a.column( 'شماره درخواست'   , width = 125  , minwidth = 60  , anchor = 'center' )  
        self.table035_a.column( 'ردیف'             , width = 50   , minwidth = 50  , anchor = 'center' ) 

        self.table035_a.heading( '#0'               , text = ''                  , anchor = 'center' ) 
        self.table035_a.heading( 'تاریخ تحویل'     , text = 'تاریخ تحویل'      , anchor = 'center' ) 
        self.table035_a.heading( 'تحویل دهنده'     , text = 'تحویل دهنده'      , anchor = 'center' ) 
        self.table035_a.heading( 'تاریخ درخواست'   , text = 'تاریخ درخواست'    , anchor = 'center' ) 
        self.table035_a.heading( 'ثبت کننده'       , text = 'ثبت کننده'         , anchor = 'center' ) 
        self.table035_a.heading( 'شماره درخواست'   , text = 'شماره درخواست'    , anchor = 'center' )  
        self.table035_a.heading( 'ردیف'             , text = 'ردیف'              , anchor = 'center' ) 

        self.table035_a.tag_configure('oddrow',  background = 'white') 
        self.table035_a.tag_configure('evenrow', background = 'lightblue') 


        self.scrl035_a.pack( side = RIGHT , fill = Y ) 
        self.table035_a.pack() 


        self.frm035_2 = LabelFrame( self , text = '  جزئیات درخواست  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl035_request_number  = Label( self.frm035_2, text = ':شماره درخواست', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl035_request_number1 = Label( self.frm035_2, bg = 'white', width = 6 ) 
        self.lbl035_rq_name  = Label( self.frm035_2, text = ':ثبت کننده' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl035_rq_name1 = Label( self.frm035_2, bg = 'white', width = 10 ) 
        self.lbl035_p_id     = Label( self.frm035_2, text = ':کد پرسنلی' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl035_p_id1    = Label( self.frm035_2, bg = 'white', width = 4 ) 
        self.lbl035_time     = Label( self.frm035_2, text = ':تاریخ'     , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl035_time1    = Label( self.frm035_2, bg = 'white', width = 14 ) 

        self.frm035_b = Frame( self.frm035_2 )

        self.scrl035_b = Scrollbar( self.frm035_b ) 
        self.scrl035_b.pack( side = RIGHT , fill = Y )

        self.table035_b = ttk.Treeview( self.frm035_b, columns = ['توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl035_b.set, selectmode = 'extended', height = 8 )
        
        self.scrl035_b.config( command = self.table035_b.yview )

        self.table035_b.column( '#0'               , width = 0   , minwidth = 0   )  
        self.table035_b.column( 'توضیح'           , width = 190 , minwidth = 60 , anchor = 'center' )  
        self.table035_b.column( 'واحد'            , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table035_b.column( 'تعداد/مقدار'    , width = 120  , minwidth = 50 , anchor = 'center' ) 
        self.table035_b.column( 'نام کالا'        , width = 150 , minwidth = 50 , anchor = 'center' ) 
        self.table035_b.column( 'کد کالا'         , width = 65  , minwidth = 50 , anchor = 'center' ) 
        self.table035_b.column( 'ردیف'           , width = 50  , minwidth = 35 , anchor = 'center' )  

        self.table035_b.heading( '#0'            , text = ''             , anchor = 'center' ) 
        self.table035_b.heading( 'توضیح'        , text = 'توضیح'        , anchor = 'center' )  
        self.table035_b.heading( 'واحد'         , text = 'واحد'         , anchor = 'center' ) 
        self.table035_b.heading( 'تعداد/مقدار' , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table035_b.heading( 'نام کالا'     , text = 'نام کالا'       , anchor = 'center' ) 
        self.table035_b.heading( 'کد کالا'      , text = 'کد کالا'        , anchor = 'center' ) 
        self.table035_b.heading( 'ردیف'        , text = 'ردیف'          , anchor = 'center' ) 

        self.table035_b.tag_configure('oddrow',  background = 'white') 
        self.table035_b.tag_configure('evenrow', background = 'lightblue') 

        self.table035_b.pack() 

        self.lbl035_note2  = Label( self.frm035_2, text = ':توضیح انباردار', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl035_note21 = Label( self.frm035_2, text = '', bg = 'white')

        self.lbl035_request_number .grid( row = 1 , column = 8 , padx = 5 , pady = 5 )    
        self.lbl035_request_number1.grid( row = 1 , column = 7 , padx = 5 )
        self.lbl035_rq_name        .grid( row = 1 , column = 6 , padx = 5 ) 
        self.lbl035_rq_name1       .grid( row = 1 , column = 5 , padx = 5 ) 
        self.lbl035_p_id           .grid( row = 1 , column = 4 , padx = 5 )
        self.lbl035_p_id1          .grid( row = 1 , column = 3 , padx = 5 )
        self.lbl035_time           .grid( row = 1 , column = 2 , padx = 5 )
        self.lbl035_time1          .grid( row = 1 , column = 1 , padx = 5 )
        self.frm035_b              .grid( row = 2 , column = 1 , columnspan = 8 )
        self.table035_b            .pack( ) 
        self.lbl035_note2          .grid( row = 3 , column = 8 , pady = 5 )
        self.lbl035_note21         .grid( row = 3 , column = 4 , columnspan = 4 , sticky = 'e' )

        self.table035_a.bind( '<ButtonRelease-1>', self.table035_a_select ) 



         # صفحه ثبت ورور کالا
        self.frm042 = LabelFrame( self , text = '  ثبت ورود کالا  ' , font = ('homa', 13) , 
                                  bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl042_delivery_doc = Label( self.frm042, text = '   :شماره سند   ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent042_delivery_doc = Entry( self.frm042, justify = 'center', width = 14 ) 

        self.lbl042_delivery = Label( self.frm042, text = ':تحویل دهنده', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 

        self.cmb042_delivery_var = StringVar( self ) 
        self.cmb042_delivery_var.set( 'انتخاب کنید' ) 
        self.cmb042_delivery_options = ['پرسنل مجموعه', 'متفرقه'] 
        self.cmb042_delivery = ttk.Combobox( self.frm042 , width = 14 , textvariable = self.cmb042_delivery_var,
                                             values = self.cmb042_delivery_options, state = 'disabled', justify = 'center') 
        
        self.lbl042_delivery1 = Label( self.frm042, text = ':نام و نام خانوادگی', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 

        self.cmb042_delivery1_var = StringVar( self )  # نام (اگر پرسنل مجموعه باشد)
        self.cmb042_delivery1_var.set( 'انتخاب کنید' ) 
        self.cmb042_delivery1 = ttk.Combobox( self.frm042 , width = 14 , textvariable = self.cmb042_delivery1_var,
                                              state = 'readonly', justify = 'center')
        
        self.ent042_delivery1 = Entry( self.frm042, justify = 'center', width = 14 ) # نام (اگر متفرقه باشد)

        self.lbl042_delivery2 = Label( self.frm042, text = '', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) # کد پرسنلی / کد ملی

        self.lbl042_delivery3 = Label( self.frm042, text = '', bg = 'white') # اگر کد پرسنلی باشه
        self.ent042_delivery2 = Entry( self.frm042, justify = 'center', width = 14, state = 'disabled' ) # اگر کد ملی باشه

        self.lbl042_g_code = Label( self.frm042, text = '   :کد کالا   ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent042_g_code = Entry( self.frm042, justify = 'center', width = 14, state = 'disabled' ) 

        self.lbl042_g_name  = Label( self.frm042, text = '  :نام کالا  ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl042_g_name1 = Label( self.frm042, text = ' ', width = 14, bg = 'white' ) 

        self.lbl042_gr_code  = Label( self.frm042, text = '   :کد گروه   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl042_gr_code1 = Label( self.frm042, text = ' ', width = 14, bg = 'white' ) 

        self.lbl042_gr_name  = Label( self.frm042, text = '  :نام گروه   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl042_gr_name1 = Label( self.frm042, text = ' ', width = 14, bg = 'white' ) 

        self.lbl042_g_type  = Label( self.frm042, text = '   :نوع کالا   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl042_g_type1 = Label( self.frm042, text = ' ', width = 14, bg = 'white' ) 
 

        self.frm042_amount = LabelFrame( self.frm042 , text = ' :تعداد/مقدار    ' , font = ('homa', 13) ,
                                         bg = 'white' , fg = '#345382' , bd = 0 , labelanchor = 'e' , padx = 60 , pady = 5 )
        self.ent042_amount = Entry( self.frm042_amount, justify = 'center', width = 5 , state = 'disabled' ) 
        self.lbl042_unit = Label( self.frm042_amount, text = ' ', bg = 'white' ) 

        self.frm042_a = LabelFrame( self.frm042 , text = ':آدرس کالا در انبار ' , font = ('homa', 13) ,
                                     bg = 'white' , fg = '#345382' , bd = 0 , labelanchor = 'e' , padx = 20, pady = 7 )

        self.lbl042_address_row = Label( self.frm042_a, text = 'ردیف', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.cmb042_row_var = StringVar( self ) 
        self.cmb042_row_var.set( '...' ) 
        self.cmb042_row_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] 
        self.cmb042_row = ttk.Combobox( self.frm042_a , width = 3 , textvariable = self.cmb042_row_var,
                                        values = self.cmb042_row_options, state = 'disabled', justify = 'center') 
        
        self.lbl042_address_col = Label( self.frm042_a, text = 'ستون', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.cmb042_col_var = StringVar( self ) 
        self.cmb042_col_var.set( '...' ) 
        self.cmb042_col_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] 
        self.cmb042_col = ttk.Combobox( self.frm042_a , width = 3 , textvariable = self.cmb042_col_var,
                                        values = self.cmb042_col_options, state = 'disabled', justify = 'center')
        
        self.lbl042_address_num = Label( self.frm042_a, text = 'شماره', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.cmb042_num_var = StringVar( self ) 
        self.cmb042_num_var.set( '...' ) 
        self.cmb042_num_options = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'] 
        self.cmb042_num = ttk.Combobox( self.frm042_a , width = 3 , textvariable = self.cmb042_num_var,
                                        values = self.cmb042_num_options, state = 'disabled', justify = 'center')  
        
        self.lbl042_address_000 = Label( self.frm042_a, text = '         ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 

        self.lbl042_note = Label( self.frm042, text = '   :توضیح   ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent042_note = Entry( self.frm042, justify = 'right', width = 85, state = 'disabled' ) 

        self.imglbl042 = Label ( self.frm042 , image = self.upload_img , bg = 'white' , bd = 0 , width = 110 , height = 110 )

        self.btn042_add_to_list = Button( self.frm042, image = self.add_to_list_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.delivery_add_to_list ) 


        #================= table =================== 
        self.frm042_b = Frame( self.frm042 ) 

        self.scrl042_b_y = ttk.Scrollbar( self.frm042_b , orient = 'vertical' )
        self.scrl042_b_y.pack( side = RIGHT , fill = Y )
        self.table042_b = ttk.Treeview( self.frm042_b, columns = ['توضیحات', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا'], 
                                        yscrollcommand = self.scrl042_b_y.set , selectmode = 'extended', height = 7 )
        self.scrl042_b_y.config( command = self.table042_b.yview )

        self.table042_b.column( '#0'             , width = 0    , minwidth = 0 ) 
        self.table042_b.column( 'توضیحات'       , width = 150  , minwidth = 50 , anchor = 'center' )
        self.table042_b.column( 'واحد'          , width = 120  , minwidth = 50 , anchor = 'center' )
        self.table042_b.column( 'تعداد/مقدار'   , width = 120  , minwidth = 50 , anchor = 'center' )
        self.table042_b.column( 'نام کالا'       , width = 130  , minwidth = 50 , anchor = 'center' )
        self.table042_b.column( 'کد کالا'        , width = 130  , minwidth = 50 , anchor = 'center' )

        self.table042_b.heading( '#0'            , text = ''             , anchor = 'center' ) 
        self.table042_b.heading( 'توضیحات'      , text = 'توضیحات'      , anchor = 'center' ) 
        self.table042_b.heading( 'واحد'         , text = 'واحد'         , anchor = 'center' ) 
        self.table042_b.heading( 'تعداد/مقدار'  , text = 'تعداد/مقدار' , anchor = 'center' ) 
        self.table042_b.heading( 'نام کالا'      , text = 'نام کالا'      , anchor = 'center' ) 
        self.table042_b.heading( 'کد کالا'       , text = 'کد کالا'       , anchor = 'center' ) 

        self.table042_b.tag_configure( 'oddrow', background = 'white' ) 
        self.table042_b.tag_configure( 'evenrow', background = 'lightblue' ) 

        self.table042_b.pack() 

        self.btn042_delete_list = Button( self.frm042, image = self.delete_list_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.btn042_delete_list_func ) 

        self.btn042_submit = Button( self.frm042, image = self.delivery_submit_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.submit_doc ) 


        self.lbl042_delivery_doc.grid( row = 0 , column = 6 , pady = 5)
        self.ent042_delivery_doc.grid( row = 0 , column = 5 )

        self.lbl042_delivery.grid( row = 1 , column = 6 )
        self.cmb042_delivery.grid( row = 1 , column = 5 )

        self.lbl042_g_code.grid( row = 2 , column = 6 , padx = 15 , pady = 5 )
        self.ent042_g_code.grid( row = 2 , column = 5 , padx = 15 , pady = 5 )

        self.lbl042_g_name.grid ( row = 2 , column = 4 , padx = 15 , pady = 5 )
        self.lbl042_g_name1.grid( row = 2 , column = 3 , padx = 15 , pady = 5 )

        self.lbl042_g_type.grid ( row = 2 , column = 2 , padx = 15 , pady = 5 )
        self.lbl042_g_type1.grid( row = 2 , column = 1 , padx = 15 , pady = 5 )

        self.lbl042_gr_code.grid ( row = 3 , column = 6 , padx = 15 , pady = 5 )
        self.lbl042_gr_code1.grid( row = 3 , column = 5 , padx = 15 , pady = 5 )

        self.lbl042_gr_name.grid ( row = 3 , column = 4 , padx = 15 , pady = 5 )
        self.lbl042_gr_name1.grid( row = 3 , column = 3 , padx = 15 , pady = 5 )

        self.frm042_amount.grid  ( row = 4 , column = 4 , columnspan = 6 , sticky= 'e' )
        self.ent042_amount.grid ( row = 1 , column = 2  )

        self.imglbl042.grid( row = 3 , rowspan = 3 , column = 1 , columnspan = 2 , padx = 20 , pady = 5 )

        self.frm042_a.grid          ( row = 5 , column = 3 , columnspan = 4 )
        self.lbl042_address_row.grid( row = 1 , column = 6 , padx = 5 )
        self.cmb042_row.grid( row = 1 , column = 5 , padx = 5 )
        self.lbl042_address_col.grid( row = 1 , column = 4 , padx = 5 )
        self.cmb042_col.grid( row = 1 , column = 3 , padx = 5 )
        self.lbl042_address_num.grid( row = 1 , column = 2 , padx = 5 )
        self.cmb042_num.grid( row = 1 , column = 1 , padx = 5 )
        self.lbl042_address_000.grid( row = 1 , column = 0 , padx = 5 )

        self.lbl042_note.grid( row = 6 , column = 6 , pady = 5 )
        self.ent042_note.grid( row = 6 , column = 1 , columnspan = 5 , sticky = 'e' )

        self.btn042_add_to_list.grid( row = 7 , column = 1 , columnspan = 6 , padx = 20 , pady = 5 ) 

        self.frm042_b.grid( row = 8 , column = 1 , columnspan = 6 ) 

        self.btn042_delete_list.grid( row = 9 , column = 2 )
        self.btn042_submit.grid( row = 9 , column = 1 , pady = 5 )   

        
        self.ent042_delivery_doc.bind('<Return>', self.ent042_delivery_doc_func )    
        self.cmb042_delivery.bind('<<ComboboxSelected>>', self.cmb042_delivery_setting ) 
        self.cmb042_delivery1.bind('<<ComboboxSelected>>', self.cmb042_delivery1_setting ) 
        self.ent042_delivery1.bind( '<Return>', self.ent042_delivery1_func )
        self.ent042_delivery2.bind( '<Return>' , self.ent042_delivery2_func )
        self.ent042_amount.bind('<Return>', self.ent042_amount_func )
        self.cmb042_row.bind('<<ComboboxSelected>>', self.cmb042_row_func )
        self.cmb042_col.bind('<<ComboboxSelected>>', self.cmb042_col_func )
        self.cmb042_num.bind('<<ComboboxSelected>>', self.cmb042_num_func )
        self.ent042_note.bind('<Return>', lambda event : self.btn042_add_to_list.focus() )
        self.btn042_add_to_list.bind('<Return>', self.delivery_add_to_list ) 
        self.ent042_g_code.bind( '<Return>' , self.delivery_goods_search ) 


         # صفحه ثبت خروج کالا
        self.frm043 = LabelFrame( self , text = '  ثبت خروج کالا  ' , font = ('homa', 13) , 
                                  bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl043_take_doc = Label( self.frm043, text = '   :شماره سند   ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent043_take_doc = Entry( self.frm043, justify = 'center', width = 14 ) 

        self.lbl043_take = Label( self.frm043, text = ':تحویل گیرنده', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 

        self.cmb043_take_var = StringVar( self ) 
        self.cmb043_take_var.set( 'انتخاب کنید' ) 
        self.cmb043_take_options = ['پرسنل مجموعه', 'متفرقه'] 
        self.cmb043_take = ttk.Combobox( self.frm043 , width = 14 , textvariable = self.cmb043_take_var,
                                             values = self.cmb043_take_options, state = 'disabled', justify = 'center') 
        
        self.lbl043_take1 = Label( self.frm043, text = ':نام و نام خانوادگی', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 

        self.cmb043_take1_var = StringVar( self )  # نام (اگر پرسنل مجموعه باشد)
        self.cmb043_take1_var.set( 'انتخاب کنید' ) 
        self.cmb043_take1 = ttk.Combobox( self.frm043 , width = 14 , textvariable = self.cmb043_take1_var, state = 'readonly', justify = 'center')

        self.ent043_take1 = Entry( self.frm043, justify = 'center', width = 14 ) # نام (اگر متفرقه باشد)

        self.lbl043_take2 = Label( self.frm043, text = '', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) # کد پرسنلی / کد ملی

        self.lbl043_take3 = Label( self.frm043, text = '', bg = 'white') # اگر کد پرسنلی باشه
        self.ent043_take2 = Entry( self.frm043, justify = 'center', width = 14, state = 'disabled' ) # اگر کد ملی باشه

        self.lbl043_g_code = Label( self.frm043, text = '   :کد کالا   ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent043_g_code = Entry( self.frm043, justify = 'center', width = 14, state = 'disabled' ) 

        self.lbl043_g_name  = Label( self.frm043, text = '  :نام کالا  ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl043_g_name1 = Label( self.frm043, text = ' ', width = 14, bg = 'white' ) 

        self.lbl043_gr_code  = Label( self.frm043, text = '   :کد گروه   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl043_gr_code1 = Label( self.frm043, text = ' ', width = 14, bg = 'white' ) 

        self.lbl043_gr_name  = Label( self.frm043, text = '  :نام گروه   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl043_gr_name1 = Label( self.frm043, text = ' ', width = 14, bg = 'white' ) 

        self.lbl043_g_type  = Label( self.frm043, text = '   :نوع کالا   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl043_g_type1 = Label( self.frm043, text = ' ', width = 14, bg = 'white' ) 

        self.frm043_current_supply = LabelFrame( self.frm043 , text = ' :موجودی فعلی    ' , font = ('homa', 13) ,
                                         bg = 'white' , bd = 0 , fg = '#345382' , labelanchor = 'e' , padx = 5 , pady = 10 )
        self.lbl043_current_supply = Label( self.frm043_current_supply, text = ' ', bg = 'white' ) 
        self.lbl043_unit    = Label( self.frm043_current_supply, text = ' ', bg = 'white' ) 

        self.frm043_g_reorder_point = LabelFrame( self.frm043 , text = ' :نقطۀ سفارش    ' , font = ('homa', 13) ,
                                         bg = 'white' , bd = 0 , fg = '#345382' , labelanchor = 'e' , padx = 5 , pady = 10 )
        self.lbl043_g_reorder_point =  Label( self.frm043_g_reorder_point, text = ' ', bg = 'white' ) 
        self.lbl043_unit_rp = Label( self.frm043_g_reorder_point, text = ' ', bg = 'white' ) 

        self.frm043_g_amount = LabelFrame( self.frm043 , text = ' :تعداد/مقدار    ' , font = ('homa', 13) ,
                                         bg = 'white' , bd = 0 , fg = '#345382' , labelanchor = 'e' , padx = 5 , pady = 10 )
        self.ent043_g_amount = Entry( self.frm043_g_amount, justify = 'center', width = 5 , state = 'disabled' ) 
        self.lbl043_unit_am  = Label( self.frm043_g_amount, text = ' ', bg = 'white' ) 

        self.lbl043_address = Label( self.frm043 , text = ':آدرس در انبار ',  bg = 'white' , fg = '#345382' , font = ('homa', 13) )
        self.lbl043_address1 = Label( self.frm043, text = ' ', width = 14, bg = 'white' ) 

        self.lbl043_note = Label( self.frm043, text = '   :توضیح   ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.ent043_note = Entry( self.frm043, justify = 'right', width = 65 , state = 'disabled' ) 

        self.imglbl043 = Label( self.frm043 , image = self.upload_img , bg = 'white' , bd = 0 , width = 110 , height = 110 )

        self.btn043_add_to_list = Button( self.frm043, image = self.add_to_list_btn_bg , bd = 0 , bg = 'white', state = 'disabled', command = self.take_add_to_list ) 


        #================= table =================== 
        self.frm043_b = Frame( self.frm043 ) 

        self.scrl043_b_y = ttk.Scrollbar( self.frm043_b , orient = 'vertical' )
        self.scrl043_b_y.pack( side = RIGHT , fill = Y )
        self.table043_b = ttk.Treeview( self.frm043_b, columns = ['توضیحات', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا'], 
                                        yscrollcommand = self.scrl043_b_y.set , selectmode = 'extended', height = 7 )
        self.scrl043_b_y.config( command = self.table043_b.yview )

        self.table043_b.column( '#0'             , width = 0    , minwidth = 0 ) 
        self.table043_b.column( 'توضیحات'       , width = 150  , minwidth = 50 , anchor = 'center' )
        self.table043_b.column( 'واحد'          , width = 120  , minwidth = 50 , anchor = 'center' )
        self.table043_b.column( 'تعداد/مقدار'   , width = 120  , minwidth = 50 , anchor = 'center' )
        self.table043_b.column( 'نام کالا'       , width = 130  , minwidth = 50 , anchor = 'center' )
        self.table043_b.column( 'کد کالا'        , width = 130  , minwidth = 50 , anchor = 'center' )

        self.table043_b.heading( '#0'            , text = ''             , anchor = 'center' ) 
        self.table043_b.heading( 'توضیحات'      , text = 'توضیحات'      , anchor = 'center' ) 
        self.table043_b.heading( 'واحد'         , text = 'واحد'         , anchor = 'center' ) 
        self.table043_b.heading( 'تعداد/مقدار'  , text = 'تعداد/مقدار' , anchor = 'center' ) 
        self.table043_b.heading( 'نام کالا'      , text = 'نام کالا'      , anchor = 'center' ) 
        self.table043_b.heading( 'کد کالا'       , text = 'کد کالا'       , anchor = 'center' ) 

        self.table043_b.tag_configure( 'oddrow', background = 'white' ) 
        self.table043_b.tag_configure( 'evenrow', background = 'lightblue' ) 

        self.table043_b.pack() 

        self.btn043_delete_list = Button( self.frm043, image = self.delete_list_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.btn043_delete_list_func ) 

        self.btn043_take_submit = Button( self.frm043, image = self.take_submit_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.btn043_take_submit_doc_func ) 


        self.lbl043_take_doc.grid( row = 0 , column = 6 , pady = 5)
        self.ent043_take_doc.grid( row = 0 , column = 5 )

        self.lbl043_take.grid( row = 1 , column = 6 )
        self.cmb043_take.grid( row = 1 , column = 5 )

        self.lbl043_g_code.grid( row = 2 , column = 6 , padx = 15 , pady = 10 )
        self.ent043_g_code.grid( row = 2 , column = 5 , padx = 15 , pady = 5 )

        self.lbl043_g_name.grid ( row = 2 , column = 4 , padx = 15 , pady = 5 )
        self.lbl043_g_name1.grid( row = 2 , column = 3 , padx = 15 , pady = 5 )

        self.lbl043_g_type.grid ( row = 2 , column = 2 , padx = 15 , pady = 5 )
        self.lbl043_g_type1.grid( row = 2 , column = 1 , padx = 15 , pady = 5 )

        self.lbl043_gr_code.grid ( row = 3 , column = 6 , padx = 15 , pady = 5 )
        self.lbl043_gr_code1.grid( row = 3 , column = 5 , padx = 15 , pady = 5 )

        self.lbl043_gr_name.grid ( row = 3 , column = 4 , padx = 15 , pady = 5 )
        self.lbl043_gr_name1.grid( row = 3 , column = 3 , padx = 15 , pady = 5 )

        self.frm043_current_supply.grid( row = 4 , column = 5 , columnspan = 2 , sticky = 'e' )
        self.lbl043_current_supply.grid( row = 1 , column = 2 )
        self.lbl043_unit          .grid( row = 1 , column = 1 )

        self.frm043_g_reorder_point.grid( row = 4 , column = 3 , columnspan = 2 , sticky = 'e' )
        self.lbl043_g_reorder_point.grid( row = 1 , column = 2 )
        self.lbl043_unit_rp        .grid( row = 1 , column = 1 )

        self.frm043_g_amount.grid( row = 5 , column = 5 , columnspan = 2 , sticky = 'e' )
        self.ent043_g_amount.grid( row = 1 , column = 2 )
        self.lbl043_unit_am.grid( row = 1 , column = 1 )

        self.imglbl043.grid( row = 3 , rowspan = 4 , column = 1 , columnspan = 2 , padx = 20 , pady = 5 )

        self.lbl043_address.grid ( row = 5 , column = 4 , pady = 5 )
        self.lbl043_address1.grid( row = 5 , column = 3 , padx = 5 )

        self.lbl043_note.grid( row = 6 , column = 6 )
        self.ent043_note.grid( row = 6 , column = 1 , columnspan = 5 , sticky = 'e' )

        self.btn043_add_to_list.grid( row = 7 , column = 1 , columnspan = 6 , padx = 20 , pady = 5 ) 

        self.frm043_b.grid( row = 8 , column = 1 , columnspan = 6 ) 

        self.btn043_delete_list.grid( row = 9 , column = 2 )
        self.btn043_take_submit.grid( row = 9 , column = 1 , pady = 5 )    

        self.ent043_take_doc.bind('<Return>' , self.ent043_take_doc_func ) 
        self.cmb043_take.bind('<<ComboboxSelected>>' , self.cmb043_take_setting ) 
        self.cmb043_take1.bind('<<ComboboxSelected>>' , self.cmb043_take1_setting ) 
        self.ent043_take1.bind( '<Return>' , self.ent043_take1_func ) 
        self.ent043_take2.bind( '<Return>' , self.ent043_take2_func ) 
        self.ent043_g_code.bind( '<Return>' , self.take_goods_search ) 
        self.ent043_g_amount.bind('<Return>' , self.ent043_g_amount_func ) 
        self.ent043_note.bind('<Return>' , lambda event : self.btn043_add_to_list.focus() ) 
        self.btn043_add_to_list.bind('<Return>' , self.take_add_to_list ) 



        # تاریخچه ورود و خروج
        self.frm044_1 = LabelFrame( self , text = '  لیست اسناد ورود و خروج کالا  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 15 )

        self.frm044_a = Frame( self.frm044_1 ) 
        self.frm044_a.grid( row = 1 , rowspan = 5 , column = 1 )

        self.scrl044_a = Scrollbar( self.frm044_a ) 

        self.table044_a = ttk.Treeview( self.frm044_a, columns = ['تحویل دهنده/گیرنده', 'انباردار', 'تاریخ', 'نوع سند', 'شماره سند', 'ردیف'],
                                        yscrollcommand = self.scrl044_a.set, selectmode = 'extended', height = 8 )
        
        self.scrl044_a.config( command = self.table044_a.yview )

        self.table044_a.column( '#0'                     , width = 0    , minwidth = 0  )  
        self.table044_a.column( 'تحویل دهنده/گیرنده'    , width = 150  , minwidth = 100 , anchor = 'center' ) 
        self.table044_a.column( 'انباردار'               , width = 150  , minwidth = 80  , anchor = 'center' ) 
        self.table044_a.column( 'تاریخ'                  , width = 150  , minwidth = 100 , anchor = 'center' ) 
        self.table044_a.column( 'نوع سند'                , width = 95  , minwidth = 80  , anchor = 'center' ) 
        self.table044_a.column( 'شماره سند'              , width = 100  , minwidth = 60  , anchor = 'center' )  
        self.table044_a.column( 'ردیف'                    , width = 50   , minwidth = 50  , anchor = 'center' ) 

        self.table044_a.heading( '#0'                   , text = ''                     , anchor = 'center' ) 
        self.table044_a.heading( 'تحویل دهنده/گیرنده'  , text = 'تحویل دهنده/گیرنده' , anchor = 'center' ) 
        self.table044_a.heading( 'انباردار'             , text = 'انباردار'           , anchor = 'center' ) 
        self.table044_a.heading( 'تاریخ'                , text = 'تاریخ'               , anchor = 'center' ) 
        self.table044_a.heading( 'نوع سند'              , text = 'نوع سند'             , anchor = 'center' ) 
        self.table044_a.heading( 'شماره سند'            , text = 'شماره سند'          , anchor = 'center' )  
        self.table044_a.heading( 'ردیف'                 , text = 'ردیف'                , anchor = 'center' ) 

        self.table044_a.tag_configure('oddrow',  background = 'white') 
        self.table044_a.tag_configure('evenrow', background = 'lightblue') 


        self.scrl044_a.pack( side = RIGHT , fill = Y ) 
        self.table044_a.pack() 


        self.frm044_2 = LabelFrame( self , text = '  جزئیات سند  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 5 )

        self.lbl044_doc_number  = Label( self.frm044_2, text = ':شماره سند', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl044_doc_number1 = Label( self.frm044_2, bg = 'white', width = 12 ) 
        self.lbl044_doc_type    = Label( self.frm044_2, text = ':نوع سند' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl044_doc_type1   = Label( self.frm044_2, bg = 'white', width = 12 ) 
        self.lbl044_admin       = Label( self.frm044_2, text = ':انباردار' , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl044_admin1      = Label( self.frm044_2, bg = 'white', width = 12 ) 
        self.lbl044_time        = Label( self.frm044_2, text = ':تاریخ'     , bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl044_time1       = Label( self.frm044_2, bg = 'white', width = 14 ) 

        self.frm044_b = Frame( self.frm044_2 )

        self.scrl044_b = Scrollbar( self.frm044_b ) 
        self.scrl044_b.pack( side = RIGHT , fill = Y )

        self.table044_b = ttk.Treeview( self.frm044_b, columns = ['توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl044_b.set, selectmode = 'extended', height = 8 )
        
        self.scrl044_b.config( command = self.table044_b.yview )

        self.table044_b.column( '#0'             , width = 0   , minwidth = 0  )  
        self.table044_b.column( 'توضیح'          , width = 190 , minwidth = 60 , anchor = 'center' )  
        self.table044_b.column( 'واحد'           , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table044_b.column( 'تعداد/مقدار'    , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table044_b.column( 'نام کالا'        , width = 150 , minwidth = 50 , anchor = 'center' ) 
        self.table044_b.column( 'کد کالا'         , width = 65  , minwidth = 50 , anchor = 'center' ) 
        self.table044_b.column( 'ردیف'           , width = 50  , minwidth = 35 , anchor = 'center' )  

        self.table044_b.heading( '#0'            , text = ''              , anchor = 'center' ) 
        self.table044_b.heading( 'توضیح'        , text = 'توضیح'         , anchor = 'center' )  
        self.table044_b.heading( 'واحد'         , text = 'واحد'          , anchor = 'center' ) 
        self.table044_b.heading( 'تعداد/مقدار'  , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table044_b.heading( 'نام کالا'      , text = 'نام کالا'       , anchor = 'center' ) 
        self.table044_b.heading( 'کد کالا'       , text = 'کد کالا'        , anchor = 'center' ) 
        self.table044_b.heading( 'ردیف'         , text = 'ردیف'          , anchor = 'center' ) 

        self.table044_b.tag_configure('oddrow',  background = 'white') 
        self.table044_b.tag_configure('evenrow', background = 'lightblue') 

        self.lbl044_doc_number .grid( row = 1 , column = 8 , padx = 5 )    
        self.lbl044_doc_number1.grid( row = 1 , column = 7 , padx = 5 )
        self.lbl044_doc_type   .grid( row = 1 , column = 6 , padx = 5 ) 
        self.lbl044_doc_type1  .grid( row = 1 , column = 5 , padx = 5 ) 
        self.lbl044_admin      .grid( row = 1 , column = 4 , padx = 5 )
        self.lbl044_admin1     .grid( row = 1 , column = 3 , padx = 5 )
        self.lbl044_time       .grid( row = 1 , column = 2 , padx = 5 )
        self.lbl044_time1      .grid( row = 1 , column = 1 , padx = 5 )
        self.frm044_b          .grid( row = 2 , column = 1 , columnspan = 8 , pady = 10 )
        self.table044_b        .pack( ) 

        self.table044_a.bind( '<ButtonRelease-1>', self.table044_a_select ) 




        #  # صفحه تعریف دوره جدید
        # self.frm052 = Frame( self )

        #  # صفحه گزارشات دوره کنونی
        # self.frm053 = Frame( self )

        #  # صفحه دوره های قبلی
        # self.frm054 = Frame( self )



        # صفحه تعریف گروه / کالای جدید
        
        self.frm062_gr = LabelFrame( self , text = '  تعریف گروه جدید  ' , font = ('homa', 13) ,
                                     bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.lbl062_gr_code = Label( self.frm062_gr , text = 'کد گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_gr_name = Label( self.frm062_gr , text = 'نام گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )

        self.ent062_gr_code = Entry( self.frm062_gr , justify = 'center' , width = 16 )
        self.ent062_gr_name = Entry( self.frm062_gr , justify = 'center' , width = 16, state = 'disabled' ) 

        self.imglbl062_01 = Label( self.frm062_gr , image = self.note_img , bg = 'white' , bd = 0 , width = 110 , height = 110 )
        
        self.btn062_submit_group = Button( self.frm062_gr , image = self.submit_btn_bg , bg = 'white' , bd = 0 ,
                                           state = 'disabled', command = self.submit_group )

        self.lbl062_gr_code.grid( row = 2 , column = 3 , padx = 7 )
        self.lbl062_gr_name.grid( row = 3 , column = 3 )
        self.ent062_gr_code.grid( row = 2 , column = 2 )
        self.ent062_gr_name.grid( row = 3 , column = 2 , padx = 22 )
        self.imglbl062_01.grid( row = 1 , rowspan = 3 , column = 1 , padx = 15 )
        self.btn062_submit_group.grid( row = 4 , column = 1 , columnspan = 3 , padx = 21 , pady = 20 )
        
        self.ent062_gr_code.bind('<Return>', self.ent062_gr_code_func )
        self.ent062_gr_code.bind('<Escape>', lambda event : self.ent062_gr_code.delete(0,END) )
        self.ent062_gr_name.bind('<Return>', self.ent062_gr_name_func )
        self.ent062_gr_name.bind('<Escape>', lambda event : self.ent062_gr_name.delete(0,END) )
        self.btn062_submit_group.bind('<Return>', self.submit_group ) 



        self.frm062_g = LabelFrame( self , text = '  تعریف کالای جدید  ' , font = ('homa', 13) , bg = 'white',
                                    fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 10 )

        self.lbl062_g_gr     = Label( self.frm062_g , text = 'کد گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_gr_name  = Label( self.frm062_g, text = 'نام گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl062_gr_name1 = Label( self.frm062_g, bg = 'white' ) #, fg = '#345382' , font = ( 'homa' , 11 ) ) 

        self.lbl062_g_code = Label( self.frm062_g , text = 'کد کالا'  , bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_g_name = Label( self.frm062_g , text = 'نام کالا' , bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_g_type = Label( self.frm062_g , text = 'نوع کالا' , bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_g_measuring = Label( self.frm062_g , text = '   انداز‌ه‌گیری   ', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )

        self.cmb062_g_gr_var = StringVar( self ) 
        self.cmb062_g_gr_var.set( 'انتخاب کنید' ) 
        self.cmb062_g_gr = ttk.Combobox( self.frm062_g , width = 14 , textvariable = self.cmb062_g_gr_var,
                                         values = self.gr_codes_list, state = 'readonly', justify = 'center' )
        
        self.ent062_g_code = Entry( self.frm062_g , justify = 'center' , width = 16, state = 'disabled' ) 
        self.ent062_g_name = Entry( self.frm062_g , justify = 'center' , width = 16, state = 'disabled' ) 

        self.cmb062_g_type_var = StringVar( self )
        self.cmb062_g_type_var.set( 'انتخاب کنید' ) 
        self.cmb062_g_type_options = ['خریداری', 'تولیدی']
        self.cmb062_g_type = ttk.Combobox( self.frm062_g , width = 14 , textvariable = self.cmb062_g_type_var,
                                           values = self.cmb062_g_type_options, justify = 'center', state = 'disabled' )

        self.cmb062_g_measuring_var = StringVar( self )
        self.cmb062_g_measuring_var.set( 'انتخاب کنید' ) 
        self.cmb062_g_measuring_options = ['تعدادی', 'وزنی', 'بستۀ تعدادی', 'بستۀ وزنی']
        self.cmb062_g_measuring = ttk.Combobox( self.frm062_g , width = 14 , textvariable = self.cmb062_g_measuring_var,
                                                values = self.cmb062_g_measuring_options, justify = 'center', state = 'disabled' )
        
        self.lbl062_g_weight_unit   = Label( self.frm062_g , text = 'واحد وزن'   , bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_g_in_every_box  = Label( self.frm062_g , text = 'در هر بسته' , bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )
        self.lbl062_g_reorder_point = Label( self.frm062_g , text = 'نقطۀ سفارش' , bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )

        self.cmb062_g_weight_unit_var = StringVar( self ) 
        self.cmb062_g_weight_unit_var.set( 'انتخاب کنید' ) 
        self.cmb062_g_weight_unit_options = [ 'گرم', 'کیلوگرم', 'تن' ] 
        self.cmb062_g_weight_unit = ttk.Combobox( self.frm062_g , width = 14 , textvariable = self.cmb062_g_weight_unit_var,
                                         values = self.cmb062_g_weight_unit_options, state = 'readonly', justify = 'center' )
        
        self.ent062_g_in_every_box  = Entry( self.frm062_g , justify = 'center' , width = 14 , state = 'disabled' ) 
        self.ent062_g_reorder_point = Entry( self.frm062_g , justify = 'center' , width = 14 , state = 'disabled' ) 

        self.imglbl062_02 = Label       ( self.frm062_g , image = self.upload_img , width = 110 , height = 110 , bg = 'white' )
        self.btn062_g_add_photo = Button( self.frm062_g , image = self.upload_btn_bg , bg = 'white' , bd = 0 , state = 'disabled', command = self.open_g_photo )

        self.btn062_g_submit = Button   ( self.frm062_g , image = self.submit_btn_bg , bg = 'white' , bd = 0 , state = 'disabled' , command = self.submit_goods )

        self.lbl062_g_gr.grid       ( row = 1 , column = 5 ) 
        self.lbl062_gr_name.grid    ( row = 2 , column = 5 , pady = 10 ) 
        self.lbl062_g_code.grid     ( row = 3 , column = 5 ) 
        self.lbl062_g_name.grid     ( row = 4 , column = 5 , pady = 10) 
        self.lbl062_g_type.grid     ( row = 5 , column = 5 ) 
        self.lbl062_g_measuring.grid( row = 1 , column = 3 , padx = 10 ) 
        self.cmb062_g_gr.grid       ( row = 1 , column = 4 ) 
        self.lbl062_gr_name1.grid   ( row = 2 , column = 4 ) 
        self.ent062_g_code.grid     ( row = 3 , column = 4 , padx = 20 ) 
        self.ent062_g_name.grid     ( row = 4 , column = 4 ) 
        self.cmb062_g_type.grid     ( row = 5 , column = 4 )
        self.cmb062_g_measuring.grid( row = 1 , column = 2 , padx = 15 )
        self.imglbl062_02.grid      ( row = 1 , rowspan = 4 , column = 1 , padx = 20 )
        self.btn062_g_add_photo.grid( row = 5 , column = 1 )
        self.btn062_g_submit.grid   ( row = 6 , column = 1 , columnspan = 5 , pady = 10 )

        self.cmb062_g_gr.bind('<<ComboboxSelected>>', self.cmb062_g_gr_func ) 
        self.ent062_g_code.bind('<Return>', self.ent062_g_code_func )
        self.ent062_g_name.bind('<Return>', self.ent062_g_name_func )
        self.cmb062_g_type.bind('<<ComboboxSelected>>', self.cmb062_g_type_func )
        self.cmb062_g_measuring.bind('<<ComboboxSelected>>', self.cmb062_g_measuring_func )
        self.cmb062_g_weight_unit.bind('<<ComboboxSelected>>', self.cmb062_g_weight_unit_func )
        self.ent062_g_in_every_box.bind('<Return>', self.ent062_g_in_every_box_func )
        self.ent062_g_reorder_point.bind('<Return>', self.ent062_g_reorder_point_func ) 
        self.btn062_g_submit.bind('<Return>', self.submit_goods ) 


         # صفحه گروه ها / کالا ها
        self.frm063_01 = LabelFrame( self , text = '  گروه‌های تعریف‌‌ شده  ' , font = ('homa', 13) , bg = 'white' ,
                                     fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 45 , pady = 10 )

        self.frm063_01_1 = Frame( self.frm063_01 ) 
        self.frm063_01_1.pack( side = TOP , fill = X , pady = 5 ) 

        self.my_scroll063_01_1 = Scrollbar( self.frm063_01_1 )
        self.my_scroll063_01_1.pack( side = RIGHT , fill = Y )
        self.my_table_063_01_1 = ttk.Treeview( self.frm063_01_1, columns = ['نام گروه' , 'کد گروه'],
                                               yscrollcommand = self.my_scroll063_01_1.set, selectmode = 'extended', height = 5 )
        self.my_scroll063_01_1.config( command = self.my_table_063_01_1.yview )

        self.my_table_063_01_1.column( '#0'        , width = 0    , minwidth = 0 )
        self.my_table_063_01_1.column( 'کد گروه'   , width = 120  , minwidth = 50 , anchor = 'center' )
        self.my_table_063_01_1.column( 'نام گروه'  , width = 160 , minwidth = 50 , anchor = 'center' )

        self.my_table_063_01_1.heading( '#0'        , text = ''          , anchor = 'center' )
        self.my_table_063_01_1.heading( 'کد گروه'   , text = 'کد گروه'  , anchor = 'center' )
        self.my_table_063_01_1.heading( 'نام گروه'  , text = 'نام گروه' , anchor = 'center' )

        self.my_table_063_01_1.tag_configure('oddrow', background = 'white')
        self.my_table_063_01_1.tag_configure('evenrow', background = 'lightblue')

        self.my_table_063_01_1.pack()

        self.btn063_1 = Button( self.frm063_01, image = self.show_gr_btn_bg, bd = 0, bg = 'white' , command = self.show_all_groups )

        self.btn063_1.pack( pady = 5 ) 



        self.frm063_02 = LabelFrame( self , text = '  کالاهای تعریف شده  ' , font = ('homa', 13) , bg = 'white' ,
                                     fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 10 )

        self.frm063_02_1 = Frame( self.frm063_02 ) 
        self.frm063_02_1.pack( side = TOP , fill = X , pady = 5)

        self.my_scroll063_02 = Scrollbar( self.frm063_02_1 ) 
        self.my_scroll063_02.pack( side = RIGHT , fill = Y)

        self.my_table_063_02 = ttk.Treeview( self.frm063_02_1, columns = ['نقطه سفارش' , 'در هر بسته', 'واحد وزن', 'اندازه گیری', 'نوع کالا', 
                                                                          'نام گروه', 'کد گروه', 'نام کالا', 'کد کالا'],
                                             yscrollcommand = self.my_scroll063_02.set, selectmode = 'extended', height = 10 )
        self.my_scroll063_02.config( command = self.my_table_063_02.yview )

        self.my_table_063_02.column( '#0'            , width = 0  , minwidth = 0 )
        self.my_table_063_02.column( 'نقطه سفارش'   , width = 80 , minwidth = 50 , anchor = 'center' )
        self.my_table_063_02.column( 'در هر بسته'   , width = 70 , minwidth = 50 , anchor = 'center' )
        self.my_table_063_02.column( 'واحد وزن'     , width = 70 , minwidth = 50 , anchor = 'center' )
        self.my_table_063_02.column( 'اندازه گیری'  , width = 80 , minwidth = 50 , anchor = 'center' )
        self.my_table_063_02.column( 'نوع کالا'      , width = 80 , minwidth = 50  , anchor = 'center' )
        self.my_table_063_02.column( 'نام گروه'     , width = 110 , minwidth = 50 , anchor = 'center' )
        self.my_table_063_02.column( 'کد گروه'      , width = 50 , minwidth = 50  , anchor = 'center' )
        self.my_table_063_02.column( 'نام کالا'      , width = 120 , minwidth = 50 , anchor = 'center' )
        self.my_table_063_02.column( 'کد کالا'       , width = 80 , minwidth = 50  , anchor = 'center' )

        self.my_table_063_02.heading( '#0'            , text = ''              , anchor = 'center' )
        self.my_table_063_02.heading( 'نقطه سفارش'   , text = 'نقطه سفارش'   , anchor = 'center' )
        self.my_table_063_02.heading( 'در هر بسته'   , text = 'در هر بسته'   , anchor = 'center' )
        self.my_table_063_02.heading( 'واحد وزن'     , text = 'واحد وزن'     , anchor = 'center' )
        self.my_table_063_02.heading( 'اندازه گیری'  , text = 'اندازه گیری'  , anchor = 'center' )
        self.my_table_063_02.heading( 'نوع کالا'      , text = 'نوع کالا'       , anchor = 'center' )
        self.my_table_063_02.heading( 'نام گروه'     , text = 'نام گروه'      , anchor = 'center' )
        self.my_table_063_02.heading( 'کد گروه'      , text = 'کد گروه'       , anchor = 'center' )
        self.my_table_063_02.heading( 'نام کالا'      , text = 'نام کالا'       , anchor = 'center' )
        self.my_table_063_02.heading( 'کد کالا'       , text = 'کد کالا'        , anchor = 'center' )

        self.my_table_063_02.tag_configure('oddrow',  background = 'white') 
        self.my_table_063_02.tag_configure('evenrow', background = 'lightblue') 

        # self.my_table_063_02.bind('<ButtonRelease-1>', self.grab )
        self.my_table_063_02.pack()

        self.btn063_021 = Button( self.frm063_02, image = self.show_g_btn_bg, bd = 0, bg = 'white', command = self.show_all_goods )
        self.btn063_021.pack( pady = 5 ) 



         # صفحه جستجو و ویرایش کالا
        self.frm064_gr = LabelFrame( self , text = '  جستجو و ویرایش گروه  ' , font = ('homa', 13) , bg = 'white' ,
                                     fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 30 , pady = 5 ) 
        
        self.lbl064_gr_code = Label( self.frm064_gr, text = 'کد گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent064_gr_code = Entry( self.frm064_gr, justify = 'center' , width = 14 )
        self.btn064_gr_search = Button( self.frm064_gr, image = self.search_btn_bg, bd = 0, bg = 'white', command = self.btn064_gr_search_func ) 
        self.frm064_gr_a = LabelFrame( self.frm064_gr , text = '' , bg = 'white' , fg = '#345382' , bd = 2 , padx = 30 , pady = 10 ) 
        self.lbl064_gr_name = Label( self.frm064_gr_a, text = 'نام گروه', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ), state = 'disabled' ) 
        self.ent064_gr_name = Entry( self.frm064_gr_a, justify = 'center' , width = 14, state = 'disabled' ) 
        self.btn064_gr_edit   = Button( self.frm064_gr, image = self.edit_btn_bg, bd = 0, bg = 'white', state = 'disabled', command = self.gr_update ) 
        self.btn064_gr_delete = Button( self.frm064_gr, image = self.delete_btn_bg, bd = 0, bg = 'white', state = 'disabled', command = self.gr_delete ) 

        self.lbl064_gr_code.grid( row = 1 , column = 3 , padx = 10 , pady = 10 )
        self.ent064_gr_code.grid( row = 1 , column = 2 , padx = 10 )
        self.btn064_gr_search .grid( row = 1 , column = 1 , padx = 10 ) 
        self.frm064_gr_a.grid( row = 2 , column = 1 , columnspan = 3 )
        self.lbl064_gr_name.grid( row = 1 , column = 2 , padx = 10 , pady = 10 )
        self.ent064_gr_name.grid( row = 1 , column = 1 , padx = 10 , pady = 10 )
        self.btn064_gr_edit   .grid( row = 3 , column = 2 , padx = 10 )
        self.btn064_gr_delete .grid( row = 3 , column = 1 , padx = 10 , pady = 10 )

        self.ent064_gr_code.bind( '<Return>', lambda event : self.btn064_gr_search.focus() )
        self.ent064_gr_code.bind( '<Key>', self.frm064_gr_clear ) 
        self.btn064_gr_search.bind( '<Return>', self.btn064_gr_search_func )
        self.ent064_gr_name.bind('<Key>', lambda event : self.btn064_gr_edit.config( state = 'normal' ) )
       
        
        
        self.frm064_g = LabelFrame( self , text = '  جستجو و ویرایش کالا  ' , font = ('homa', 13) , bg = 'white' ,
                                    fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 5 ) 

        self.lbl064_g_code = Label( self.frm064_g, text = 'کد کالا', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent064_g_code = Entry( self.frm064_g, justify = 'center' , width = 14 )
        self.btn064_g_search = Button( self.frm064_g, image = self.search_btn_bg, bd = 0, bg = 'white', command = self.g_search ) 

        self.frm064_g_a = LabelFrame( self.frm064_g , text = '' , bg = 'white' , fg = '#345382' ,
                                      bd = 2 , padx = 30 , pady = 5 ) 
        
        self.lbl064_g_name = Label( self.frm064_g_a, text = 'نام کالا', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent064_g_name = Entry( self.frm064_g_a, justify = 'center' , width = 14 , state = 'disabled' ) 

        self.lbl064_a_gr_code = Label( self.frm064_g_a, text = 'کد گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent064_a_gr_code = Entry( self.frm064_g_a, justify = 'center' , width = 14 , state = 'disabled' ) 

        self.lbl064_a_gr_name  = Label( self.frm064_g_a, text = 'نام گروه', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl064_a_gr_name1 = Label( self.frm064_g_a, text = '', bg = 'white' ) 

        self.lbl064_g_type = Label( self.frm064_g_a, text = 'نوع کالا', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 

        self.cmb064_g_type_var = StringVar( self )
        self.cmb064_g_type_options = ['خریداری', 'تولیدی']
        self.cmb064_g_type = ttk.Combobox( self.frm064_g_a , width = 14 , textvariable = self.cmb064_g_type_var,
                                       values = self.cmb064_g_type_options, state = 'disabled', justify = 'center' ) 

        self.lbl064_g_measuring = Label( self.frm064_g_a, text = 'اندازه‌گیری', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) )

        self.cmb064_g_measuring_var = StringVar( self ) 
        self.cmb064_g_measuring_options = ['تعدادی', 'وزنی', 'بستۀ تعدادی', 'بستۀ وزنی']
        self.cmb064_g_measuring = ttk.Combobox( self.frm064_g_a , width = 14 , textvariable = self.cmb064_g_measuring_var,
                                       values = self.cmb064_g_measuring_options, state = 'disabled', justify = 'center' ) 

        self.lbl064_g_weight_unit = Label( self.frm064_g_a, text = 'واحد وزن', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl064_g_in_every_box = Label( self.frm064_g_a, text = 'در هر بسته', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl064_g_reorder_point = Label( self.frm064_g_a, text = 'نقطه سفارش', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 

        self.ent064_g_in_every_box = Entry( self.frm064_g_a, justify = 'center' , width = 14 , state = 'disabled' ) 
        self.ent064_g_reorder_point = Entry( self.frm064_g_a, justify = 'center' , width = 14 , state = 'disabled' ) 

        self.cmb064_g_weight_unit_var = StringVar( self ) 
        self.cmb064_g_weight_unit_options = ['گرم', 'کیلوگرم', 'تن']
        self.cmb064_g_weight_unit = ttk.Combobox( self.frm064_g_a , width = 14 , textvariable = self.cmb064_g_weight_unit_var,
                                       values = self.cmb064_g_weight_unit_options, state = 'readonly', justify = 'center' ) 
        

        self.imglbl064 = Label ( self.frm064_g_a , image = self.upload_img , bg = 'white' , bd = 0 , width = 110 , height = 110 )
        self.imgbtn064 = Button( self.frm064_g_a , image = self.change_btn_bg , bg = 'white' , bd = 0, state = 'disabled', command = self.change_g_photo )

        self.btn064_g_edit   = Button( self.frm064_g, image = self.edit_btn_bg, bd = 0, bg = 'white', state = 'disabled', command = self.g_update ) 
        self.btn064_g_delete = Button( self.frm064_g, image = self.delete_btn_bg, bd = 0, bg = 'white', state = 'disabled', command = self.g_delete )

        self.lbl064_g_code.grid( row = 1 , column = 5 , padx = 10 , pady = 10 )
        self.ent064_g_code.grid( row = 1 , column = 4 , padx = 10 )
        self.btn064_g_search.grid( row = 1 , column = 3 , padx = 10 )
        self.frm064_g_a.grid( row = 2 , column = 1 , columnspan = 5 )
        self.lbl064_g_name.grid( row = 1 , column = 5 , padx = 10 , pady = 5 )
        self.ent064_g_name.grid( row = 1 , column = 4 , padx = 10 )
        self.lbl064_a_gr_code.grid( row = 2 , column = 5 , padx = 10 , pady = 5 )
        self.ent064_a_gr_code.grid( row = 2 , column = 4 , padx = 10 )
        self.lbl064_a_gr_name .grid( row = 3 , column = 5 , padx = 10 , pady = 5 )
        self.lbl064_a_gr_name1.grid( row = 3 , column = 4 , padx = 10 )
        self.lbl064_g_type.grid( row = 4 , column = 5 , padx = 10 , pady = 5 )
        self.cmb064_g_type.grid( row = 4 , column = 4 , padx = 10 )
        self.lbl064_g_measuring.grid( row = 1 , column = 3 , padx = 10 )
        self.cmb064_g_measuring.grid( row = 1 , column = 2 , padx = 10 )
        self.imglbl064.grid( row = 1 , rowspan = 3, column = 1 , padx = 20 )
        self.imgbtn064.grid( row = 4 ,              column = 1 , padx = 20 )
        self.btn064_g_edit   .grid( row = 3 , column = 2 , padx = 10 )
        self.btn064_g_delete .grid( row = 3 , column = 1 , padx = 10 , pady = 10 )

        self.ent064_g_code.bind('<Return>', lambda event : self.btn064_g_search.focus() ) 
        self.btn064_g_search.bind('<Return>', self.g_search )
        self.cmb064_g_measuring.bind('<<ComboboxSelected>>', self.measuring_cmb_func_2 ) 
        self.ent064_g_in_every_box.bind('<Return>', self.ent064_g_in_every_box_func )
        self.ent064_g_reorder_point.bind('<Return>', self.ent064_g_reorder_point_func )
        self.cmb064_g_weight_unit.bind( '<<ComboboxSelected>>', self.cmb064_g_weight_unit_func )
        self.btn064_g_edit.bind('<Return>', self.g_update )
        self.btn064_g_delete.bind('<Return>', self.g_delete ) 


         # صفحه تعریف کاربر جدید
        self.frm072 = LabelFrame( self , text = '  تعریف کاربر جدید  ' , font = ('homa', 13) , bg = 'white' ,
                                     fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 30 , pady = 15 )

        self.lbl072_user_p_id = Label( self.frm072, text = 'کد پرسنلی', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent072_user_p_id = Entry( self.frm072, justify = 'center' , width = 14 ) 

        self.lbl072_user_name = Label( self.frm072, text = 'نام کامل', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent072_user_name = Entry( self.frm072, justify = 'center' , width = 14 ) 

        self.lbl072_user_n_id = Label( self.frm072, text = 'کد ملی', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent072_user_n_id = Entry( self.frm072, justify = 'center' , width = 14 ) 

        self.lbl072_user_username = Label( self.frm072, text = 'نام کاربری', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent072_user_username = Entry( self.frm072, justify = 'center' , width = 14 ) 

        self.lbl072_user_password = Label( self.frm072, text = 'کلمه عبور', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent072_user_password = Entry( self.frm072, justify = 'center' , width = 14 ) 

        self.imglbl072 = Label ( self.frm072 , image = self.upload_img    , bg = 'white' , bd = 0 , width = 110 , height = 110 )
        self.imgbtn072 = Button( self.frm072 , image = self.upload_btn_bg , bg = 'white' , bd = 0, command = self.upload_user_photo )

        self.btn072_submit = Button( self.frm072, image = self.submit_btn_bg , bd = 0, bg = 'white' , command = self.submit_user ) 

        self.lbl072_user_p_id.grid( row = 1 , column = 5 , padx = 10 , pady = 5 )
        self.ent072_user_p_id.grid( row = 1 , column = 4 , padx = 10 , pady = 5 )

        self.lbl072_user_name.grid( row = 2 , column = 5 , padx = 10 , pady = 5 )
        self.ent072_user_name.grid( row = 2 , column = 4 , padx = 10 , pady = 5 )

        self.lbl072_user_n_id.grid( row = 3 , column = 5 , padx = 10 , pady = 5 )
        self.ent072_user_n_id.grid( row = 3 , column = 4 , padx = 10 , pady = 5 )

        self.lbl072_user_username.grid( row = 1 , column = 3 , padx = 10 , pady = 5 )
        self.ent072_user_username.grid( row = 1 , column = 2 , padx = 10 , pady = 5 )

        self.lbl072_user_password.grid( row = 2 , column = 3 , padx = 10 , pady = 5 )
        self.ent072_user_password.grid( row = 2 , column = 2 , padx = 10 , pady = 5 )

        self.imglbl072.grid( row = 1 , rowspan = 3 , column = 1 , padx = 20 , pady = 5 )
        self.imgbtn072.grid( row = 4 ,               column = 1 , padx = 20 , pady = 5 )

        self.btn072_submit.grid( row = 5 , column = 1 , columnspan = 5 )

        self.ent072_user_p_id.bind('<Return>', self.ent072_user_p_id_func )
        self.ent072_user_name.bind('<Return>', lambda event: self.ent072_user_n_id.focus() )
        self.ent072_user_n_id.bind('<Return>', lambda event: self.ent072_user_username.focus() )
        self.ent072_user_username.bind('<Return>', lambda event: self.ent072_user_password.focus() )
        self.ent072_user_password.bind('<Return>', lambda event: self.imgbtn072.focus() )


         # صفحه لیست کاربران
        self.frm073 = LabelFrame( self , text = '  کاربران تعریف‌‌ شده  ' , font = ('homa', 13) , bg = 'white' ,
                                  fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 30 , pady = 10 )
        
        self.frm073_a = Frame( self.frm073 ) 
        self.frm073_a.pack( side = TOP , fill = X , pady = 5)

        self.my_scroll073 = Scrollbar( self.frm073_a ) 
        self.my_scroll073.pack( side = RIGHT , fill = Y) 

        self.users_table_073 = ttk.Treeview( self.frm073_a, columns = [ 'سمت', 'نام کاربری', 'کد ملی', 'نام کامل', 'کد پرسنلی' ], 
                                             yscrollcommand = self.my_scroll073.set, selectmode = 'extended', height = 10 )
        self.my_scroll073.config( command = self.users_table_073.yview )

        self.users_table_073.column( '#0'           , width = 0  , minwidth = 0 )
        self.users_table_073.column( 'سمت'         , width = 100 , minwidth = 80 , anchor = 'center' ) 
        self.users_table_073.column( 'نام کاربری'  , width = 100 , minwidth = 80 , anchor = 'center' ) 
        self.users_table_073.column( 'کد ملی'      , width = 100 , minwidth = 80 , anchor = 'center' )
        self.users_table_073.column( 'نام کامل'    , width = 100 , minwidth = 80 , anchor = 'center' )
        self.users_table_073.column( 'کد پرسنلی'   , width = 100 , minwidth = 80 , anchor = 'center' )

        self.users_table_073.heading( '#0'           , text = ''            , anchor = 'center' )
        self.users_table_073.heading( 'سمت'         , text = 'سمت'          , anchor = 'center' ) 
        self.users_table_073.heading( 'نام کاربری'  , text = 'نام کاربری'  , anchor = 'center' )
        self.users_table_073.heading( 'کد ملی'      , text = 'کد ملی'       , anchor = 'center' )
        self.users_table_073.heading( 'نام کامل'    , text = 'نام کامل'    , anchor = 'center' )
        self.users_table_073.heading( 'کد پرسنلی'   , text = 'کد پرسنلی'   , anchor = 'center' )

        self.users_table_073.tag_configure('oddrow',  background = 'white') 
        self.users_table_073.tag_configure('evenrow', background = 'lightblue') 

        self.users_table_073.pack()

        self.btn073 = Button( self.frm073, image = self.users_list_btn_bg, bd = 0, bg = 'white', command = self.show_all_users ) 
        self.btn073.pack( pady = 5 )



         # صفحه جستجو و ویرایش افراد
        
        self.frm074 = LabelFrame( self , text = '  ویرایش / حذف کاربر  ' , font = ('homa', 13) , bg = 'white' ,
                                     fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 5 ) 
        
        self.lbl074_user_p_id   = Label( self.frm074, text = 'کد پرسنلی', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent074_user_p_id   = Entry( self.frm074, justify = 'center' , width = 14 ) 
        self.ent074_user_p_id.bind('<Return>', lambda event : self.btn074_user_search.focus())
        self.btn074_user_search = Button( self.frm074, image = self.search_btn_bg, bd = 0, bg = 'white', command = self.btn074_user_search_func ) 
        self.btn074_user_search.bind('<Return>', self.btn074_user_search_func )

        self.frm074_a = LabelFrame( self.frm074 , text = '' , bg = 'white' , fg = '#345382' , bd = 2 , padx = 30 , pady = 5 ) 
        
        self.lbl074_user_name = Label( self.frm074_a, text = 'نام کامل', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent074_user_name = Entry( self.frm074_a, justify = 'center' , width = 14 ) 

        self.lbl074_user_n_id = Label( self.frm074_a, text = 'کد ملی', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent074_user_n_id = Entry( self.frm074_a, justify = 'center' , width = 14 ) 

        self.lbl074_user_username = Label( self.frm074_a, text = 'نام کاربری', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent074_user_username = Entry( self.frm074_a, justify = 'center' , width = 14 ) 

        self.lbl074_user_password = Label( self.frm074_a, text = 'کلمه عبور', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent074_user_password = Entry( self.frm074_a, justify = 'center' , width = 14 ) 

        self.imglbl074 = Label ( self.frm074_a , image = self.upload_img , bg = 'white' , bd = 0 , width = 110 , height = 110 )
        self.imgbtn074 = Button( self.frm074_a , image = self.change_btn_bg , bg = 'white' , bd = 0) #, command = self.change_user_photo )

        self.btn074_user_edit   = Button( self.frm074, image = self.edit_btn_bg, bd = 0, bg = 'white') #, command = self.user_update ) 
        self.btn074_user_delete = Button( self.frm074, image = self.delete_btn_bg, bd = 0, bg = 'white') #, command = self.user_delete )

        self.lbl074_user_p_id  .grid( row = 1 , column = 5 , padx = 10 , pady = 10 )
        self.ent074_user_p_id  .grid( row = 1 , column = 4 , padx = 10 )
        self.btn074_user_search.grid( row = 1 , column = 3 , padx = 10 )

        self.frm074_a.grid( row = 2 , column = 1 , columnspan = 5 )

        self.lbl074_user_name.grid( row = 1 , column = 5 , padx = 10 , pady = 5 )
        self.ent074_user_name.grid( row = 1 , column = 4 , padx = 10 )

        self.lbl074_user_n_id.grid( row = 2 , column = 5 , padx = 10 , pady = 5 )
        self.ent074_user_n_id.grid( row = 2 , column = 4 , padx = 10 )

        self.lbl074_user_username .grid( row = 3 , column = 5 , padx = 10 , pady = 5 )
        self.ent074_user_username.grid( row = 3 , column = 4 , padx = 10 )

        self.lbl074_user_password.grid( row = 3 , column = 3 , padx = 10 , pady = 5 )
        self.ent074_user_password.grid( row = 3 , column = 2 , padx = 10 )

        self.imglbl074.grid( row = 1 , rowspan = 3, column = 1 , padx = 20 )
        self.imgbtn074.grid( row = 4 ,              column = 1 , padx = 20 )

        self.btn074_user_edit  .grid( row = 3 , column = 2 , padx = 15 )
        self.btn074_user_delete.grid( row = 3 , column = 1 , padx = 10 , pady = 15 )





#================================== صفحه ثبت درخواست کالا توسط کاربر ============================

        self.frm082_1 = LabelFrame( self , text = '  مشخصات  ' , font = ('homa', 13) , bg = 'white' ,
                                     fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 5 )

        self.lbl082_request_num = Label( self.frm082_1, text = ':شمارۀ درخواست', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent082_request_num = Entry( self.frm082_1, justify = 'center' , width = 14 ) 

        self.lbl082_blank = Label( self.frm082_1, text = '', bg = 'white', font = ( 'homa' , 11 ), width = 5 ) 

        self.lbl082_requester  = Label( self.frm082_1, text = ':ثبت کنندۀ درخواست', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl082_requester1 = Label( self.frm082_1, text = '', bg = 'white' , font = ( 'nazanin' , 11 , 'bold' ) ) 

        self.lbl082_request_num.pack( side = RIGHT, padx = 10 , pady = 10 )
        self.ent082_request_num.pack( side = RIGHT, padx = 10 , pady = 10 )
        self.lbl082_blank.pack( side = RIGHT, padx = 10 , pady = 10 )
        self.lbl082_requester.pack( side = RIGHT, padx = 10 , pady = 10 )
        self.lbl082_requester1.pack( side = RIGHT, padx = 10 , pady = 10 )

        self.ent082_request_num.bind('<Return>', self.ent082_request_num_func )
        self.ent082_request_num.bind('<Key>', self.ent082_request_num_func0 )




        self.frm082_2 = LabelFrame( self , text = '  جستجوی کالای مورد نظر  ' , font = ('homa', 13) , bg = 'white' ,
                                    fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 )

        self.frm082_21 = Frame( self.frm082_2 ) 
        self.frm082_21.grid( row = 1 , rowspan = 5 , column = 1 )

        self.scrl082_2 = Scrollbar( self.frm082_21 ) 
        self.scrl082_2.pack( side = RIGHT , fill = Y )

        self.table082_2 = ttk.Treeview( self.frm082_21, columns = ['واحد', 'نام کالا', 'کد کالا'],
                                        yscrollcommand = self.scrl082_2.set, selectmode = 'extended', height = 8 )
        
        self.scrl082_2.config( command = self.table082_2.yview )

        self.table082_2.column( '#0'        , width = 0  , minwidth = 0 ) 
        self.table082_2.column( 'واحد'     , width = 120  , minwidth = 50 , anchor = 'center' ) 
        self.table082_2.column( 'نام کالا'  , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table082_2.column( 'کد کالا'   , width = 60  , minwidth = 50 , anchor = 'center' ) 

        self.table082_2.heading( '#0'        , text = ''          , anchor = 'center' ) 
        self.table082_2.heading( 'واحد'     , text = 'واحد'      , anchor = 'center' ) 
        self.table082_2.heading( 'نام کالا'  , text = 'نام کالا'   , anchor = 'center' ) 
        self.table082_2.heading( 'کد کالا'   , text = 'کد کالا'    , anchor = 'center' ) 

        self.table082_2.tag_configure('oddrow',  background = 'white') 
        self.table082_2.tag_configure('evenrow', background = 'lightblue') 

        self.lbl082_g_code = Label( self.frm082_2, text = ':کد کالا', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent082_g_code = Entry( self.frm082_2, justify = 'center' , width = 14, state = 'disabled' ) 

        self.lbl082_g_name  = Label( self.frm082_2, text = ':نام کالا', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.lbl082_g_name1 = Label( self.frm082_2, text = '', bg = 'white' , font = ( 'homa' , 10 ) ) 

        self.lbl082_amount = Label( self.frm082_2, text = ':تعداد/مقدار', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent082_amount = Entry( self.frm082_2, justify = 'center' , width = 6 ) 
        self.lbl082_unit   = Label( self.frm082_2, text = '                      ', bg = 'white' , font = ( 'homa' , 10 ) ) 

        self.lbl082_note = Label( self.frm082_2, text = ':توضیح', bg = 'white' , fg = '#345382' , font = ( 'homa' , 11 ) ) 
        self.ent082_note = Entry( self.frm082_2, justify = 'right', width = 58, state = 'disabled' )  

        self.imglbl082 = Label ( self.frm082_2, image = self.upload_img , bg = 'white' , bd = 0 , width = 110 , height = 110 )

        self.btn082_add_to_list = Button( self.frm082_2, image = self.add_to_list_btn_bg , bd = 0, bg = 'white', state = 'disabled', command = self.btn082_add_to_list_func ) 

        self.table082_2.pack()
        self.imglbl082.grid( row = 1 , rowspan = 3 , column = 2 , padx = 20 , pady = 10 ) 
        self.ent082_g_code.grid( row = 1 , column = 4 , padx = 5 , pady = 3 )
        self.lbl082_g_code.grid( row = 1 , column = 5 , padx = 5 )
        self.lbl082_g_name1.grid( row = 2 , column = 4 , pady = 3 ) 
        self.lbl082_g_name.grid( row = 2 , column = 5 )
        self.lbl082_unit.grid( row = 3 , column = 3 , pady = 3 , sticky = 'e' )
        self.ent082_amount.grid( row = 3 , column = 4 )
        self.lbl082_amount.grid( row = 3 , column = 5 )
        self.ent082_note.grid( row = 4 , column = 2 , columnspan = 4 , padx = 5 , sticky = 'w' )
        self.lbl082_note.grid( row = 4 , column = 5 , pady = 3 ) 
        self.btn082_add_to_list.grid( row = 5 , column = 3 , pady = 3 ) 

        self.ent082_g_code.bind('<BackSpace>', self.ent082_g_code_func0 ) 
        self.ent082_g_code.bind('<Return>', self.ent082_g_code_func )
        self.table082_2.bind('<ButtonRelease-1>', self.table082_2_select )
        self.ent082_amount.bind('<Return>', self.ent082_amount_func )
        self.ent082_note.bind('<Return>', lambda event : self.btn082_add_to_list.focus())
        self.btn082_add_to_list.bind('<Return>', self.btn082_add_to_list_func )



        self.frm082_3 = LabelFrame( self , text = '  لیست کالاهای درخواستی  ' , font = ('homa', 13) , bg = 'white' ,
                                    fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 35 , pady = 5 ) 

        self.frm082_31 = Frame( self.frm082_3 ) 
        self.frm082_31.pack( side = TOP , fill = X , pady = 5 )

        self.scrl082_3 = Scrollbar( self.frm082_31 ) 
        self.scrl082_3.pack( side = RIGHT , fill = Y )

        self.table082_3 = ttk.Treeview( self.frm082_31, columns = ['توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl082_3.set, selectmode = 'extended', height = 6 ) 
        
        self.scrl082_3.config( command = self.table082_3.yview )

        self.table082_3.column( '#0'            , width = 0  , minwidth = 0 ) 
        self.table082_3.column( 'توضیح'         , width = 250  , minwidth = 50 , anchor = 'center' ) 
        self.table082_3.column( 'واحد'          , width = 100  , minwidth = 50 , anchor = 'center' ) 
        self.table082_3.column( 'تعداد/مقدار'  , width = 100 , minwidth = 50 , anchor = 'center' ) 
        self.table082_3.column( 'نام کالا'      , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table082_3.column( 'کد کالا'       , width = 80  , minwidth = 50 , anchor = 'center' ) 
        self.table082_3.column( 'ردیف'         , width = 50  , minwidth = 50 , anchor = 'center' ) 

        self.table082_3.heading( '#0'             , text = ''              , anchor = 'center' ) 
        self.table082_3.heading( 'توضیح'          , text = 'توضیح'        , anchor = 'center' ) 
        self.table082_3.heading( 'واحد'           , text = 'واحد'         , anchor = 'center' ) 
        self.table082_3.heading( 'تعداد/مقدار'   , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table082_3.heading( 'نام کالا'       , text = 'نام کالا'       , anchor = 'center' ) 
        self.table082_3.heading( 'کد کالا'        , text = 'کد کالا'        , anchor = 'center' ) 
        self.table082_3.heading( 'ردیف'          , text = 'ردیف'          , anchor = 'center' ) 

        self.table082_3.tag_configure('oddrow',  background = 'white') 
        self.table082_3.tag_configure('evenrow', background = 'lightblue') 

        self.btn082_3_delete_list = Button( self.frm082_3, image = self.delete_list_btn_bg , bd = 0, 
                                            bg = 'white', state = 'disabled', command = self.btn082_delete_list_func ) 
        self.btn082_3_delete_from_list = Button( self.frm082_3, image = self.delete_from_list_btn_bg , bd = 0, 
                                            bg = 'white', state = 'disabled', command = self.btn082_delete_from_list_func ) 
        self.btn082_3_submit_list = Button( self.frm082_3, image = self.submit_btn_bg , bd = 0, 
                                            bg = 'white', state = 'disabled', command = self.btn082_submit_list_func ) 
        
        self.table082_3.pack()
        self.btn082_3_delete_list.pack( side = RIGHT , pady = 5 , padx = 5 )
        self.btn082_3_delete_from_list.pack( side = RIGHT , pady = 5 , padx = 5 )
        self.btn082_3_submit_list.pack( side = LEFT , pady = 5 , padx = 5 )

        self.table082_3.bind('<ButtonRelease-1>', self.table082_3_select_func )

        # درخواست‌های من
        self.frm083_1 = LabelFrame( self , text = '  لیست درخواست‌های من  ' , font = ('homa', 13) , bg = 'white' ,
                                    fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20 , pady = 10 ) 

        self.frm083_a = Frame( self.frm083_1 ) 
        self.frm083_a.pack( side = TOP , fill = X , pady = 5)

        self.scrl083_a = Scrollbar( self.frm083_a ) 
        self.scrl083_a.pack( side = RIGHT , fill = Y)

        self.table083_a = ttk.Treeview( self.frm083_a, columns = [ 'تاریخ رسیدگی', 'انباردار', 'آخرین وضعیت', 'تاریخ صدور', 'شماره درخواست', 'ردیف'],
                                             yscrollcommand = self.scrl083_a.set, selectmode = 'browse', height = 7 )
        self.scrl083_a.config( command = self.table083_a.yview )

        self.table083_a.column( '#0'               , width = 0  , minwidth = 0 )
        self.table083_a.column( 'تاریخ رسیدگی'    , width = 130 , minwidth = 50 , anchor = 'center' )
        self.table083_a.column( 'انباردار'        , width = 130 , minwidth = 50  , anchor = 'center' )
        self.table083_a.column( 'آخرین وضعیت'     , width = 130 , minwidth = 50 , anchor = 'center' )
        self.table083_a.column( 'تاریخ صدور'      , width = 130 , minwidth = 50  , anchor = 'center' )
        self.table083_a.column( 'شماره درخواست'   , width = 120 , minwidth = 50 , anchor = 'center' )
        self.table083_a.column( 'ردیف'             , width = 50 , minwidth = 50  , anchor = 'center' )

        self.table083_a.heading( '#0'              , text = ''                , anchor = 'center' )
        self.table083_a.heading( 'تاریخ رسیدگی'   , text = 'تاریخ رسیدگی'   , anchor = 'center' )
        self.table083_a.heading( 'انباردار'       , text = 'انباردار'       , anchor = 'center' )
        self.table083_a.heading( 'آخرین وضعیت'    , text = 'آخرین وضعیت'    , anchor = 'center' )
        self.table083_a.heading( 'تاریخ صدور'     , text = 'تاریخ صدور'     , anchor = 'center' ) 
        self.table083_a.heading( 'شماره درخواست'  , text = 'شماره درخواست'  , anchor = 'center' )
        self.table083_a.heading( 'ردیف'            , text = 'ردیف'            , anchor = 'center' )


        self.table083_a.tag_configure('oddrow',  background = 'white') 
        self.table083_a.tag_configure('evenrow', background = 'lightblue') 

        self.lbl083_show_type = Label( self.frm083_1, text = '  :نوع نمایش  ', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 


        self.cmb083_show_type_var = StringVar( self ) 
        self.cmb083_show_type_var.set( 'انتخاب کنید' ) 
        self.cmb083_show_type_options = [ 'همۀ درخواست‌ها', 'درخواست‌های در انتظار', 'درخواست‌های تحویل شده', 'درخواست‌های جاری', 'درخواست‌های رد شده'] 
        self.cmb083_show_type = ttk.Combobox( self.frm083_1 , width = 23 , textvariable = self.cmb083_show_type_var,
                                               values = self.cmb083_show_type_options, state = 'readonly', justify = 'center') 
        
        
        self.btn083_show = Button( self.frm083_1, image = self.show_btn_bg, bd = 0, bg = 'white', state = 'disabled', command = self.show_my_requests )


        self.table083_a.pack()
        self.lbl083_show_type.pack( side = RIGHT , pady = 5 )
        self.cmb083_show_type.pack( side = RIGHT, pady = 5 )
        self.btn083_show.pack( side = LEFT, pady = 5 )

        self.cmb083_show_type.bind('<<ComboboxSelected>>', self.cmb082_show_type_func )  
        self.btn083_show.bind('<Return>', self.show_my_requests ) 
        self.table083_a.bind( '<ButtonRelease-1>', self.table083_a_select )


        self.frm083_2 = LabelFrame( self , text = '  جزئیات درخواست  ' , font = ('homa', 13) , 
                                    bg = 'white' , fg = '#345382' , bd = 2 , labelanchor = 'ne' , padx = 20, pady = 10 )

        self.frm083_b = Frame( self.frm083_2 )

        self.scrl083_b = Scrollbar( self.frm083_b ) 
        self.scrl083_b.pack( side = RIGHT , fill = Y )

        self.table083_b = ttk.Treeview( self.frm083_b, columns = ['توضیح', 'واحد', 'تعداد/مقدار', 'نام کالا', 'کد کالا', 'ردیف'],
                                        yscrollcommand = self.scrl083_b.set, selectmode = 'extended', height = 8 )
        
        self.scrl083_b.config( command = self.table083_b.yview )

        self.table083_b.column( '#0'               , width = 0   , minwidth = 0   )  
        self.table083_b.column( 'توضیح'           , width = 185 , minwidth = 60 , anchor = 'center' )  
        self.table083_b.column( 'واحد'            , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table083_b.column( 'تعداد/مقدار'    , width = 120 , minwidth = 50 , anchor = 'center' ) 
        self.table083_b.column( 'نام کالا'        , width = 150 , minwidth = 50 , anchor = 'center' ) 
        self.table083_b.column( 'کد کالا'         , width = 65  , minwidth = 50 , anchor = 'center' ) 
        self.table083_b.column( 'ردیف'           , width = 50  , minwidth = 35 , anchor = 'center' )  

        self.table083_b.heading( '#0'            , text = ''             , anchor = 'center' ) 
        self.table083_b.heading( 'توضیح'        , text = 'توضیح'        , anchor = 'center' )  
        self.table083_b.heading( 'واحد'         , text = 'واحد'         , anchor = 'center' ) 
        self.table083_b.heading( 'تعداد/مقدار' , text = 'تعداد/مقدار'  , anchor = 'center' ) 
        self.table083_b.heading( 'نام کالا'     , text = 'نام کالا'       , anchor = 'center' ) 
        self.table083_b.heading( 'کد کالا'      , text = 'کد کالا'        , anchor = 'center' ) 
        self.table083_b.heading( 'ردیف'        , text = 'ردیف'          , anchor = 'center' ) 

        self.table083_b.tag_configure('oddrow',  background = 'white') 
        self.table083_b.tag_configure('evenrow', background = 'lightblue') 

        self.table083_b.pack() 

        self.lbl083_note2  = Label( self.frm083_2, text = ':توضیح انباردار', bg = 'white', fg = '#345382', font = ( 'homa' , 11 ) ) 
        self.lbl083_note21 = Label( self.frm083_2, text = '', bg = 'white')

        self.frm083_b     .pack( side = TOP , fill = X , pady = 5)
        self.table083_b   .pack( ) 
        self.lbl083_note2 .pack( side = RIGHT , padx = 5 )
        self.lbl083_note21.pack( side = RIGHT )


        self.frm102 = Frame( self )
        self.frm103 = Frame( self )        

        self.current_user_lbl.place( x = 885 , y = 34 )
        
        self.scndbtn011.pack()
        self.scndbtn012.pack()
        self.scndbtn013.pack()
        self.scndbtn014.pack()
        
        # self.scndbtn021.pack()
        # self.scndbtn022.pack()
        # self.scndbtn023.pack()
        # self.scndbtn024.pack()
        # self.scndbtn025.pack()
        
        self.scndbtn031.pack()
        self.scndbtn032.pack()
        self.scndbtn033.pack()
        self.scndbtn034.pack()
        self.scndbtn035.pack()
        
        self.scndbtn041.pack()
        self.scndbtn042.pack()
        self.scndbtn043.pack()
        self.scndbtn044.pack()
        
        # self.scndbtn051.pack()
        # self.scndbtn052.pack()
        # self.scndbtn053.pack()
        # self.scndbtn054.pack()

        self.scndbtn061.pack()
        self.scndbtn062.pack()
        self.scndbtn063.pack()
        self.scndbtn064.pack()

        self.scndbtn071.pack()
        self.scndbtn072.pack()
        self.scndbtn073.pack()
        self.scndbtn074.pack()

        self.scndbtn081.pack()
        self.scndbtn082.pack()
        self.scndbtn083.pack()

        self.scndbtn101.pack()
        self.scndbtn102.pack()
        self.scndbtn103.pack()


        self.mainbtn01.bind('<Enter>', self.main_btn01 )
        self.mainbtn01.bind('<Leave>', self.set_color  )
        # self.mainbtn02.bind('<Enter>', self.main_btn02 )
        # self.mainbtn02.bind('<Leave>', self.set_color  )
        self.mainbtn03.bind('<Enter>', self.main_btn03 )
        self.mainbtn03.bind('<Leave>', self.set_color  )
        self.mainbtn04.bind('<Enter>', self.main_btn04 )
        self.mainbtn04.bind('<Leave>', self.set_color  )
        # self.mainbtn05.bind('<Enter>', self.main_btn05 )
        # self.mainbtn05.bind('<Leave>', self.set_color  )
        self.mainbtn06.bind('<Enter>', self.main_btn06 )
        self.mainbtn06.bind('<Leave>', self.set_color  )
        self.mainbtn07.bind('<Enter>', self.main_btn07 )
        self.mainbtn07.bind('<Leave>', self.set_color  )
        self.mainbtn08.bind('<Enter>', self.main_btn08 )
        self.mainbtn08.bind('<Leave>', self.set_color  )
        self.mainbtn10.bind('<Enter>', self.main_btn10 )
        self.mainbtn10.bind('<Leave>', self.set_color  )


        self.scndbtn012.bind('<Enter>', lambda event : self.scndbtn012.configure( bg = '#708dba' ) )
        self.scndbtn012.bind('<Leave>', lambda event : self.scndbtn012.configure( bg = '#4c6c9c' ) )
        self.scndbtn013.bind('<Enter>', lambda event : self.scndbtn013.configure( bg = '#708dba' ) )
        self.scndbtn013.bind('<Leave>', lambda event : self.scndbtn013.configure( bg = '#4c6c9c' ) )
        self.scndbtn014.bind('<Enter>', lambda event : self.scndbtn014.configure( bg = '#708dba' ) )
        self.scndbtn014.bind('<Leave>', lambda event : self.scndbtn014.configure( bg = '#4c6c9c' ) )

        # self.scndbtn022.bind('<Enter>', lambda event : self.scndbtn022.configure( bg = '#708dba' ) )
        # self.scndbtn022.bind('<Leave>', lambda event : self.scndbtn022.configure( bg = '#4c6c9c' ) )
        # self.scndbtn023.bind('<Enter>', lambda event : self.scndbtn023.configure( bg = '#708dba' ) )
        # self.scndbtn023.bind('<Leave>', lambda event : self.scndbtn023.configure( bg = '#4c6c9c' ) )
        # self.scndbtn024.bind('<Enter>', lambda event : self.scndbtn024.configure( bg = '#708dba' ) )
        # self.scndbtn024.bind('<Leave>', lambda event : self.scndbtn024.configure( bg = '#4c6c9c' ) )
        # self.scndbtn025.bind('<Enter>', lambda event : self.scndbtn025.configure( bg = '#708dba' ) )
        # self.scndbtn025.bind('<Leave>', lambda event : self.scndbtn025.configure( bg = '#4c6c9c' ) )

        self.scndbtn032.bind('<Enter>', lambda event : self.scndbtn032.configure( bg = '#708dba' ) )
        self.scndbtn032.bind('<Leave>', lambda event : self.scndbtn032.configure( bg = '#4c6c9c' ) )
        self.scndbtn033.bind('<Enter>', lambda event : self.scndbtn033.configure( bg = '#708dba' ) )
        self.scndbtn033.bind('<Leave>', lambda event : self.scndbtn033.configure( bg = '#4c6c9c' ) )
        self.scndbtn034.bind('<Enter>', lambda event : self.scndbtn034.configure( bg = '#708dba' ) )
        self.scndbtn034.bind('<Leave>', lambda event : self.scndbtn034.configure( bg = '#4c6c9c' ) )
        self.scndbtn035.bind('<Enter>', lambda event : self.scndbtn035.configure( bg = '#708dba' ) )
        self.scndbtn035.bind('<Leave>', lambda event : self.scndbtn035.configure( bg = '#4c6c9c' ) )

        self.scndbtn042.bind('<Enter>', lambda event : self.scndbtn042.configure( bg = '#708dba' ) )
        self.scndbtn042.bind('<Leave>', lambda event : self.scndbtn042.configure( bg = '#4c6c9c' ) )
        self.scndbtn043.bind('<Enter>', lambda event : self.scndbtn043.configure( bg = '#708dba' ) )
        self.scndbtn043.bind('<Leave>', lambda event : self.scndbtn043.configure( bg = '#4c6c9c' ) )
        self.scndbtn044.bind('<Enter>', lambda event : self.scndbtn044.configure( bg = '#708dba' ) )
        self.scndbtn044.bind('<Leave>', lambda event : self.scndbtn044.configure( bg = '#4c6c9c' ) )

        # self.scndbtn052.bind('<Enter>', lambda event : self.scndbtn052.configure( bg = '#708dba' ) )
        # self.scndbtn052.bind('<Leave>', lambda event : self.scndbtn052.configure( bg = '#4c6c9c' ) )
        # self.scndbtn053.bind('<Enter>', lambda event : self.scndbtn053.configure( bg = '#708dba' ) )
        # self.scndbtn053.bind('<Leave>', lambda event : self.scndbtn053.configure( bg = '#4c6c9c' ) )
        # self.scndbtn054.bind('<Enter>', lambda event : self.scndbtn054.configure( bg = '#708dba' ) )
        # self.scndbtn054.bind('<Leave>', lambda event : self.scndbtn054.configure( bg = '#4c6c9c' ) )

        self.scndbtn062.bind('<Enter>', lambda event : self.scndbtn062.configure( bg = '#708dba' ) )
        self.scndbtn062.bind('<Leave>', lambda event : self.scndbtn062.configure( bg = '#4c6c9c' ) )
        self.scndbtn063.bind('<Enter>', lambda event : self.scndbtn063.configure( bg = '#708dba' ) )
        self.scndbtn063.bind('<Leave>', lambda event : self.scndbtn063.configure( bg = '#4c6c9c' ) )
        self.scndbtn064.bind('<Enter>', lambda event : self.scndbtn064.configure( bg = '#708dba' ) )
        self.scndbtn064.bind('<Leave>', lambda event : self.scndbtn064.configure( bg = '#4c6c9c' ) )

        self.scndbtn072.bind('<Enter>', lambda event : self.scndbtn072.configure( bg = '#708dba' ) )
        self.scndbtn072.bind('<Leave>', lambda event : self.scndbtn072.configure( bg = '#4c6c9c' ) )
        self.scndbtn073.bind('<Enter>', lambda event : self.scndbtn073.configure( bg = '#708dba' ) )
        self.scndbtn073.bind('<Leave>', lambda event : self.scndbtn073.configure( bg = '#4c6c9c' ) )
        self.scndbtn074.bind('<Enter>', lambda event : self.scndbtn074.configure( bg = '#708dba' ) )
        self.scndbtn074.bind('<Leave>', lambda event : self.scndbtn074.configure( bg = '#4c6c9c' ) )

        self.scndbtn082.bind('<Enter>', lambda event : self.scndbtn082.configure( bg = '#708dba' ) )
        self.scndbtn082.bind('<Leave>', lambda event : self.scndbtn082.configure( bg = '#4c6c9c' ) )
        self.scndbtn083.bind('<Enter>', lambda event : self.scndbtn083.configure( bg = '#708dba' ) )
        self.scndbtn083.bind('<Leave>', lambda event : self.scndbtn083.configure( bg = '#4c6c9c' ) )

        self.scndbtn102.bind('<Enter>', lambda event : self.scndbtn102.configure( bg = '#708dba' ) )
        self.scndbtn102.bind('<Leave>', lambda event : self.scndbtn102.configure( bg = '#4c6c9c' ) )
        self.scndbtn103.bind('<Enter>', lambda event : self.scndbtn103.configure( bg = '#708dba' ) )
        self.scndbtn103.bind('<Leave>', lambda event : self.scndbtn103.configure( bg = '#4c6c9c' ) )



#========================================= Login Page GUI ============================================

        self.win2 = Toplevel(self)
        self.win2.geometry('596x352+470+250')
        self.win2.iconbitmap( '146.ico' )
        self.win2.title('ورود به سامانه انبارداری') 
        self.win2.deiconify()
        self.win2.resizable( 0 , 0 )

        
        self.loginbg_lbl = Label( self.win2, image = self.loginbg )
        self.loginbg_lbl.place( x = -2 , y = -2 )

        self.w2_frm1 = Frame( self.win2 , bg = 'white')
        self.w2_frm1.place( x = 380 , y = 52 )

        # combobox
        self.w2_cmb_options = ('انباردار', 'کارمند')

        self.w2_cmb_var = StringVar( self.win2 )
        self.w2_cmb_var.set( 'سمت' )
        
        self.w2_cmb = ttk.Combobox(self.w2_frm1, width = 10, textvariable = self.w2_cmb_var,
                                   values = self.w2_cmb_options, state = 'readonly', foreground = '#345382', 
                                   justify = 'center', font = ('homa' , 9))
        
        # labels, entries and login button
        self.w2_lbl0 = Label(self.w2_frm1, width = 8, text = 'لطفاً وارد شوید', 
                             font = ('homa', 13 ), fg = '#345382' , bg = 'white' )        
        self.w2_lbl1 = Label(self.w2_frm1, width = 5, text = 'نام کاربری', 
                             font = ('homa', 11 ), fg = '#345382' ,  bg = 'white', anchor = 'e' )
        self.w2_lbl2 = Label(self.w2_frm1, width = 5, text = 'رمز عبور', 
                             font = ('homa', 11 ), fg = '#345382' ,  bg = 'white', anchor = 'e' )

        self.w2_ent1 = Entry(self.w2_frm1, width = 15 )
        self.w2_ent2 = Entry(self.w2_frm1, width = 15, show = '*' )

        self.w2_btn  = Button(self.w2_frm1, image = self.login_btn_bg , bd = 0, bg = 'white', command = self.login )

        self.w2_lbl0.grid( row = 0 , column = 1 , columnspan = 2 , pady = 15 )
        self.w2_lbl1.grid( row = 1 , column = 2 )
        self.w2_ent1.grid( row = 1 , column = 1 )
        self.w2_lbl2.grid( row = 2 , column = 2 , pady = 10 )
        self.w2_ent2.grid( row = 2 , column = 1 )
        self.w2_cmb .grid( row = 3 , column = 1 , columnspan = 2 , pady = 0  )
        self.w2_btn .grid( row = 4 , column = 1 , columnspan = 2 , pady = 20 )

        self.w2_ent1.focus()
        self.w2_ent1.bind('<Return>', lambda event : self.w2_ent2.focus() )
        self.w2_ent2.bind('<Return>', lambda event : self.w2_cmb.focus() ) 
        self.w2_btn .bind('<Return>', self.login )
        self.w2_cmb .bind('<<ComboboxSelected>>', lambda event : self.w2_btn.focus() )
        
        self.win2.protocol('WM_DELETE_WINDOW', self.destroy ) 

     
o = GUI()
o.mainloop()
