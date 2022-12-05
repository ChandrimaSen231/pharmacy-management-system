import tkinter as tk
from tkinter import *
from tkinter import ttk
from theme import style
from ui_utils import *
from backend import *
from tkinter.messagebox import showinfo

class sales_login_page:
    def __init__(self, root,login_command):
        self.rootframe = ttk.Frame(root)
        self.note = ttk.Notebook(self.rootframe)
        

        self.rootframe.pack(fill="both", expand=1)
        grid_config(self.rootframe )

        l0 = ttk.Label(self.rootframe,text="Sales Login Page")
        l0.grid(row=0,column=3,padx=6, pady=2, sticky="sw")
        
        l1 = ttk.Label(self.rootframe,text="Enter username: ")
        l1.grid(row=3,column=2,padx=6, pady=2, sticky="sw")

        self.username_entry = ttk.Entry(self.rootframe)
        self.username_entry.grid(row=3,column=4,padx=6,pady=2,sticky="sew")

        l2 = ttk.Label(self.rootframe,text="Password: ")
        l2.grid(row=4,column=2,padx=6, pady=2, sticky="sw")

        self.password_entry = ttk.Entry(self.rootframe,show="*")
        self.password_entry.grid(row=4,column=4,padx=6,pady=2,sticky="sew")

        self.c_v1=IntVar(value=0)
        self.c1 = tk.Checkbutton(self.rootframe,text='Show Password',variable=self.c_v1,
	        onvalue=1,offvalue=0,command=self.my_show)
        self.c1.grid(row=5,column=4) 

        self.submit_btn = ttk.Button(self.rootframe, text='Login',command=lambda : self.verify_login(self.username_entry,self.password_entry,login_command), style="accent.TButton")
        self.submit_btn.grid(row=7, column=3, padx=10,pady=6,sticky='sew')

        self.invalid_warn_label = ttk.Label(
            self.rootframe,
            text="Invalid username or password!",
            style="accent.TLabel",
        )
        self.invalid_warn_label.grid(
            row=8,
            column=0,
            columnspan=8,
            ipadx=6,
            ipady=6,
            padx=10,
            pady=6,
            sticky="swe",
        )
        hide_grid_widget(self.invalid_warn_label)
    
    def my_show(self):
        if(self.c_v1.get()==1):
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def verify_login(self,e1,e2,cmd):
        if verify_data(e1.get(),e2.get(),"Sales"):
            hide_grid_widget(self.invalid_warn_label)
            cmd()
            
        else:
            show_grid_widget(self.invalid_warn_label)

    def as_tab(self):
        return self.rootframe
    
    def as_frame(self):
        return self.rootframe

    def close_win(self,top):
        top.destroy()

class admin_login_page:
    def __init__(self, root,login_command):
        self.rootframe = ttk.Frame(root)
        self.note = ttk.Notebook(self.rootframe)
        
        self.rootframe.pack(fill="both", expand=1)
        grid_config(self.rootframe)

        l0 = ttk.Label(self.rootframe,text="Inventory Login Page")
        l0.grid(row=0,column=3,padx=6, pady=2, sticky="sw")

        l1 = ttk.Label(self.rootframe,text="Enter username: ")
        l1.grid(row=3,column=2,padx=6, pady=2, sticky="sw")

        self.username_entry = ttk.Entry(self.rootframe)
        self.username_entry.grid(row=3,column=4,padx=6,pady=2,sticky="sew")

        l2 = ttk.Label(self.rootframe,text="Password: ")
        l2.grid(row=4,column=2,padx=6, pady=2, sticky="sw")

        self.password_entry = ttk.Entry(self.rootframe,show="*")
        self.password_entry.grid(row=4,column=4,padx=6,pady=2,sticky="sew")

        self.submit_btn = ttk.Button(self.rootframe, text='Login',command=lambda : self.verify_login(self.username_entry,self.password_entry), style="accent.TButton")
        self.submit_btn.grid(row=7, column=3, padx=10,pady=6,sticky='sew')

        self.c_v1=IntVar(value=0)
        self.c1 = tk.Checkbutton(self.rootframe,text='Show Password',variable=self.c_v1,
	        onvalue=1,offvalue=0,command=self.my_show)
        self.c1.grid(row=5,column=4) 

        self.submit_btn = ttk.Button(self.rootframe, text='Login',command=lambda : self.verify_login(self.username_entry,self.password_entry,login_command), style="accent.TButton")
        self.submit_btn.grid(row=7, column=3, padx=10,pady=6,sticky='sew')

        self.invalid_warn_label = ttk.Label(
            self.rootframe,
            text="Invalid username or password!",
            style="accent.TLabel",
        )
        self.invalid_warn_label.grid(
            row=8,
            column=0,
            columnspan=8,
            ipadx=6,
            ipady=6,
            padx=10,
            pady=6,
            sticky="swe",
        )
        hide_grid_widget(self.invalid_warn_label)
    
    def my_show(self):
        if(self.c_v1.get()==1):
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def verify_login(self,e1,e2,cmd):
        if verify_data(e1.get(),e2.get(),"Admin"):
            hide_grid_widget(self.invalid_warn_label)
            cmd()
            
        else:
            show_grid_widget(self.invalid_warn_label)

    def as_tab(self):
        return self.rootframe
    
    def as_frame(self):
        return self.rootframe

    def close_win(self,top):
        top.destroy()


class inventory_order_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master)
        self.note = HorizontalNavMenu(self.rootframe)

        self.filters = ttk.Frame(self.note.content_frame)
        self.view = ttk.Frame(self.note.content_frame)

        grid_config(self.filters)
        grid_config(self.view)

        self.invt_table = easy_treeview(
            self.view, columns=["Order ID", "Order Name","Order Date","Item ID","Quantity","Amount", "Status"]
        )
        self.invt_table.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            rowspan=6,
            columnspan=8,
            ipadx=6,
            ipady=4,
            sticky="nswe",
        )
        
        self.order_complete_btn = ttk.Button(self.view, text='Order completed', style="accent.TButton",command= self.orderRecievedBox ,state=tk.DISABLED)
        self.order_complete_btn.grid(row=7, column=0, padx=10,pady=6,sticky='sew')

        self.reset_btn = ttk.Button(self.view, text='Reset', style="accent.TButton",command= self.show_table)
        self.reset_btn.grid(row=7, column=7, padx=10,pady=6,sticky='sew')

        l1 = ttk.Label(self.filters, text="Item Id", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        setattr(self, "item_id", ttk.Entry(self.filters))
        getattr(self, "item_id").grid(row=1,column=0, padx=6,pady=2,sticky="sew",columnspan=8)

        l2 = ttk.Label(self.filters, text="Item Name", style="small.TLabel")
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sw")

        setattr(self, "item_name", ttk.Entry(self.filters))
        getattr(self, "item_name").grid(row=3,column=0, padx=6,pady=2,sticky="sew",columnspan=8)

        l3 = ttk.Label(self.filters, text="Status", style="small.TLabel")
        l3.grid(row=4, column=0, padx=6, pady=2, sticky="sw")

        setattr(self, "status", ttk.Entry(self.filters))
        getattr(self, "status").grid(row=5,column=0, padx=6,pady=2,sticky="sew",columnspan=8)
        

        self.show_table()
        #self.rootframe.after_idle(lambda : self.show_table(self.invt_table))

        self.invt_table.bind("<<TreeviewSelect>>",self.selected_item)

        self.apply_btn = ttk.Button(self.filters, text="Apply Filters", style="accent.TButton",command=self.select_from_filters)
        self.apply_btn.grid(row=6, column=0, padx=6, pady=10, columnspan=8, sticky="ew")


        self.note.add(self.view, text="Table View")
        self.note.add(self.filters, text="Filters")
        self.note.pack(fill="both", expand=1, padx=10)
        

        self.rootframe.pack(fill="both", expand=1)

    def toggle_filters(self):
        if not self.show_filters:
            self.filters.pack(**self.filter_packinfo)
            self.show_filters = True
        else:
            self.filters.pack_forget()
            self.show_filters = False

    def selected_item(self,a):
        selectedItem = self.invt_table.selection()[0]
        status = self.invt_table.item(selectedItem)['values'][6]
        if status == 'Pending':
            self.order_complete_btn.config(state=tk.NORMAL)
        else:
            self.order_complete_btn.config(state=tk.DISABLED)
    
    def show_table(self):
        self.order_complete_btn.config(state=tk.DISABLED)
        getattr(self,"item_id").delete(0,tk.END)
        getattr(self,"item_name").delete(0,tk.END)
        getattr(self,"status").delete(0,tk.END)
        for item in self.invt_table.get_children():
            self.invt_table.delete(item)
        for row in get_table("inventory_order"):
            self.invt_table.insert("",tk.END,values=row)


    def as_tab(self):
        return self.rootframe

    def close_win(self,top):
        top.destroy()
    
    def orderReceived(self,top):
        selectedItem = self.invt_table.selection()[0]
        order_id = self.invt_table.item(selectedItem)['values'][0]
        item_id = self.invt_table.item(selectedItem)['values'][3]
        change_order_status(int(order_id),int(item_id))
        top.destroy()
        self.select_from_filters()
        invt.show_table()
        items.show_table()


    def orderRecievedBox(self):
        top= tk.Toplevel(root)
        top.geometry("300x150")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill='both')
        grid_config(rootframe)

        selectedItem = self.invt_table.selection()[0]
        order_id = self.invt_table.item(selectedItem)['values'][0]
        item_name = self.invt_table.item(selectedItem)['values'][1]
        item_id = self.invt_table.item(selectedItem)['values'][3]

        l1 = ttk.Label(rootframe, text=f"Confirm Order {order_id}: {item_id}-{item_name} Received",style='small.TLabel')
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw",columnspan=6)

        confirm_row_btn = ttk.Button(rootframe, text='Yes', style="accent.TButton",command= lambda : self.orderReceived(top))
        confirm_row_btn.grid(row=7, column=0, padx=10,pady=6,sticky='sew',columnspan=2)

        cancel_button = ttk.Button(rootframe, text='No', style="accent.TButton",command= lambda : self.close_win(top))
        cancel_button.grid(row=7, column=2, padx=10,pady=6,sticky='sew',columnspan=2)

    def all_filter(self,row):
            d = {"item_id": 3, "item_name": 1,"status": 6}
            filter_list = ["item_id","item_name","status"]
            val = all(str(row[d[f]]) == getattr(self, f).get() or getattr(self, f).get() == '' for f in filter_list)
            return val

    def select_from_filters(self):
        self.invt_table.delete(*self.invt_table.get_children())
        for row in get_table("inventory_order"):
            if self.all_filter(row):
                self.invt_table.insert("", "end", values=list(row))
        self.note.prev_page()

class item_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master)
        self.note = HorizontalNavMenu(self.rootframe)

        self.filters = ttk.Frame(self.note.content_frame)
        self.view = ttk.Frame(self.note.content_frame)

        grid_config(self.filters)
        grid_config(self.view)


        self.search_entry = ttk.Entry(self.view)
        self.search_entry.grid(
            row=0, column=1, padx=10, pady=2, columnspan=7, sticky="we"
        )

        self.search_btn = ttk.Button(self.view, text="Search by Item Name")
        self.search_btn.grid(row=0, column=0, padx=10, pady=2, sticky="swe")

        self.search_entry.bind('<KeyRelease>', self.searchItem)

        self.item_table = easy_treeview(
            self.view, columns=["Item Id", "Item Name", "Manufacturer","Stock Quantity","Amount", "GST"]
        )
        self.item_table.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            rowspan=6,
            columnspan=8,
            ipadx=6,
            ipady=4,
            sticky="nswe",
        )


        self.place_order = ttk.Button(self.view, text='Place Order', command=self.placeOrderBox, state=tk.DISABLED)
        self.place_order.grid(row=8, column=5, padx=10,pady=6,sticky='w')

        self.add_item = ttk.Button(self.view, text='+ Add item',command=self.addItemBox)
        self.add_item.grid(row=8, column=6, padx=10,pady=6,sticky='w')

        self.delete_row_btn = ttk.Button(self.view, text='- Delete item',command= self.deleteItemBox, state=tk.DISABLED)
        self.delete_row_btn.grid(row=8, column=7, padx=10,pady=6,sticky='w')

        self.reset_btn = ttk.Button(self.view, text='Reset', style="accent.TButton",command= self.show_table)
        self.reset_btn.grid(row=8, column=0, padx=10,pady=6,sticky='sew')

        l1 = ttk.Label(self.filters, text="Item Id", style="small.TLabel")
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        setattr(self, "item_id", ttk.Entry(self.filters))
        getattr(self, "item_id").grid(row=1,column=0, padx=6,pady=2,sticky="sew",columnspan=8)

        l2 = ttk.Label(self.filters, text="Item Name", style="small.TLabel")
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sew")

        setattr(self, "item_name", ttk.Entry(self.filters))
        getattr(self, "item_name").grid(row=3,column=0, padx=6,pady=2,sticky="sw",columnspan=8)

        l3 = ttk.Label(self.filters, text="Manufacturer", style="small.TLabel")
        l3.grid(row=4, column=0, padx=6, pady=2, sticky="sew")

        setattr(self, "manufacturer", ttk.Entry(self.filters))
        getattr(self, "manufacturer").grid(row=5,column=0, padx=6,pady=2,sticky="sew",columnspan=8)


        self.show_table()

        self.apply_btn = ttk.Button(
            self.filters, text="Apply Filters", style="accent.TButton", command=self.select_from_filters
        )
        self.apply_btn.grid(row=6, column=0, padx=6, pady=10, columnspan=8, sticky="ew")

        self.item_table.bind("<<TreeviewSelect>>",self.selected_item)
        

        self.note.add(self.view, text="Table View")
        self.note.add(self.filters, text="Filters")
        self.note.pack(fill="both", expand=1, padx=10)
        

        self.rootframe.pack(fill="both", expand=1)
    
        
    def selected_item(self,a):
        self.place_order.config(state=tk.NORMAL)
        self.delete_row_btn.config(state=tk.NORMAL)

    def show_table(self):
        self.place_order.config(state=tk.DISABLED)
        self.delete_row_btn.config(state=tk.DISABLED)
        for item in self.item_table.get_children():
            self.item_table.delete(item)
        for row in get_table("meds"):
            self.item_table.insert("",tk.END,values=row)
    
    def searchItem(self,a):
        search_val = self.search_entry.get()
        for item in self.item_table.get_children():
            self.item_table.delete(item)
        for row in search_item(search_val):
            self.item_table.insert("",tk.END,values=row)


    def as_tab(self):
        return self.rootframe

    def close_win(self,top):
        top.destroy()

    def get_order_data(self,e1,e2,e3,top):
        item_num = int(e1.get())
        item_name = e2.get()
        qty = int(e3.get())
        place_order(item_num, item_name, qty)
        self.close_win(top)
        invt.show_table()

    def add_item_data(self,e1,e2,e3,e4,e5,e6,top):
        item_num = int(e1.get())
        item_name = e2.get()
        manufacturer = e3.get()
        qty = int(e4.get())
        amt = int(e5.get())
        gst = int(e6.get())
        addItemtoDB(item_num,item_name,manufacturer, qty,amt,gst)
        self.close_win(top)
        items.show_table()
        
    
    def addItemBox(self):
        top= tk.Toplevel(root)
        top.geometry("750x350")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill='both', expand=1)
        grid_config(rootframe)

        l1 = ttk.Label(rootframe, text="Item Id",style='small.TLabel')
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        e1 = ttk.Entry(rootframe)
        e1.grid(row=1, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l2 = ttk.Label(rootframe, text=f"Item Name",style='small.TLabel')
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sw")

        e2 = ttk.Entry(rootframe)
        e2.grid(row=3, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l3 = ttk.Label(rootframe, text='Manufacturer',style='small.TLabel')
        l3.grid(row=4, column=0, padx=6, pady=2, sticky="sw")

        e3 = ttk.Entry(rootframe)
        e3.grid(row=5, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l4 = ttk.Label(rootframe, text='Quantity',style='small.TLabel')
        l4.grid(row=6, column=0, padx=6, pady=2, sticky="sw")

        e4 = ttk.Entry(rootframe)
        e4.grid(row=7, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l5 = ttk.Label(rootframe, text='Amount',style='small.TLabel')
        l5.grid(row=8, column=0, padx=6, pady=2, sticky="sw")

        e5 = ttk.Entry(rootframe)
        e5.grid(row=9, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l6 = ttk.Label(rootframe, text='GST',style='small.TLabel')
        l6.grid(row=10, column=0, padx=6, pady=2, sticky="sw")

        e6 = ttk.Entry(rootframe)
        e6.grid(row=11, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        confirm_row_btn = ttk.Button(rootframe, text='Confirm', style="accent.TButton",command= lambda : self.add_item_data(e1,e2,e3,e4,e5,e6,top))
        confirm_row_btn.grid(row=12, column=0, padx=10,pady=6,sticky='sew')

        cancel_button = ttk.Button(rootframe, text='Cancel', style="accent.TButton",command= lambda : self.close_win(top))
        cancel_button.grid(row=12, column=5, padx=10,pady=6,sticky='sew')

    def delete_item_data(self,item_id,top):
        deleteItemfromDB(item_id)
        self.close_win(top)
        items.show_table()
        invt.show_table()

    def deleteItemBox(self):
        top= tk.Toplevel(root)
        top.geometry("750x250")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill='both', expand=1)
        grid_config(rootframe)

        selectedItem = self.item_table.selection()[0]
        item_id = self.item_table.item(selectedItem)['values'][0]

        l1 = ttk.Label(rootframe, text="Do you want to delete item?",style='small.TLabel')
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw",columnspan=6)

        confirm_row_btn = ttk.Button(rootframe, text='Yes', style="accent.TButton",command= lambda : self.delete_item_data(item_id,top))
        confirm_row_btn.grid(row=7, column=0, padx=10,pady=6,sticky='sew',columnspan=2)

        cancel_button = ttk.Button(rootframe, text='No', style="accent.TButton",command= lambda : self.close_win(top))
        cancel_button.grid(row=7, column=2, padx=10,pady=6,sticky='sew',columnspan=2)


    def placeOrderBox(self):
        top= tk.Toplevel(root)
        top.geometry("750x250")
        rootframe = ttk.Frame(top)
        rootframe.pack(fill='both', expand=1)
        grid_config(rootframe)

        selectedItem = self.item_table.selection()[0]
        item_id = self.item_table.item(selectedItem)['values'][0]
        item_name = self.item_table.item(selectedItem)['values'][1]

        l1 = ttk.Label(rootframe, text="Item Id",style='small.TLabel')
        l1.grid(row=0, column=0, padx=6, pady=2, sticky="sw")

        e1 = ttk.Entry(rootframe)
        e1.insert(0,item_id)
        e1.grid(row=1, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l2 = ttk.Label(rootframe, text=f"Item Name",style='small.TLabel')
        l2.grid(row=2, column=0, padx=6, pady=2, sticky="sw")

        e2 = ttk.Entry(rootframe)
        e2.insert(0,item_name)
        e2.grid(row=3, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        l3 = ttk.Label(rootframe, text='Quantity',style='small.TLabel')
        l3.grid(row=4, column=0, padx=6, pady=2, sticky="sw")

        e3 = ttk.Entry(rootframe)
        e3.grid(row=5, column=0, padx=6, pady=2, sticky="sew",columnspan=8)

        confirm_row_btn = ttk.Button(rootframe, text='Confirm', style="accent.TButton",command= lambda : self.get_order_data(e1,e2,e3,top))
        confirm_row_btn.grid(row=7, column=0, padx=10,pady=6,sticky='sew')

        cancel_button = ttk.Button(rootframe, text='Cancel', style="accent.TButton",command= lambda : self.close_win(top))
        cancel_button.grid(row=7, column=5, padx=10,pady=6,sticky='sew')

    def all_filter(self,row):
        d = {"item_id": 0, "item_name": 1,"manufacturer": 2}
        filter_list = ["item_id","item_name","manufacturer"]
        
        val = all(str(row[d[f]]) == getattr(self, f).get() or getattr(self, f).get() == '' for f in filter_list)
        return val

    def select_from_filters(self):
        self.item_table.delete(*self.item_table.get_children())
        for row in get_table("meds"):
            if self.all_filter(row):
                self.item_table.insert("", "end", values=list(row))
        self.note.prev_page()

# This class is used to create a page object for the POS system.
class pos_page:
    def __init__(self, master, root_window):
        self.rootframe = ttk.Frame(master)
        self.rootframe.pack(fill="both", expand=1)

        self.menu = HorizontalNavMenu(self.rootframe)

        # customer details
        self.customer_details_page = ttk.Frame(self.menu.content_frame)
        grid_config(self.customer_details_page)

        self.cust_reg_lbl = ttk.Label(
            self.customer_details_page, text="Customer Details", style="big.TLabel"
        )
        self.cust_reg_lbl.grid(
            row=0, column=0, columnspan=8, padx=10, pady=6, sticky="nswe"
        )

        l2 = ttk.Label(
            self.customer_details_page, text="Phone Number", style="small.TLabel"
        )
        l2.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.cust_phone_number_entry = ttk.Entry(self.customer_details_page, style='Table.TEntry')
        self.cust_phone_number_entry.grid(
            row=2, column=0, padx=10, pady=4, columnspan=6, sticky="nswe"
        )
        self.cust_search_btn = ttk.Button(
            self.customer_details_page,
            text="Search",
            command=self.search_by_ph_no
        )
        self.cust_search_btn.grid(
            row=2, column=6, columnspan=2, padx=10, pady=4, sticky="swe"
        )
        l1 = ttk.Label(
            self.customer_details_page, text="Customer Name", style="small.TLabel"
        )
        l1.grid(row=3, column=0, padx=10, pady=4, sticky="sw")

        self.cust_name_entry = ttk.Entry(self.customer_details_page)
        self.cust_name_entry.grid(
            row=4, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        l3 = ttk.Label(self.customer_details_page, text="Age", style="small.TLabel")
        l3.grid(row=5, column=0, padx=10, pady=4, sticky="sw")

        self.cust_age_entry = ttk.Entry(self.customer_details_page)
        self.cust_age_entry.grid(
            row=6, column=0, padx=10, pady=4, columnspan=3, sticky="nswe"
        )

        l4 = ttk.Label(self.customer_details_page, text="Sex", style="small.TLabel")
        l4.grid(row=5, column=4, padx=10, pady=4, sticky="sw")

        self.cust_sex_entry = ttk.Entry(self.customer_details_page)
        self.cust_sex_entry.grid(
            row=6, column=4, padx=10, pady=4, columnspan=4, sticky="nswe"
        )

        l5 = ttk.Label(self.customer_details_page, text="Address", style="small.TLabel")
        l5.grid(row=7, column=0, padx=10, pady=4, sticky="sw")

        self.cust_addr_entry = ttk.Entry(self.customer_details_page)
        self.cust_addr_entry.grid(
            row=8, column=0, padx=10, pady=4, columnspan=8, sticky="nswe"
        )

        self.new_cust_reg_btn = ttk.Button(
            self.customer_details_page,
            text="Register New Customer",
            style="accent.TButton",
            command=self.reg_new_cust,
            state=tk.DISABLED,
        )
        self.new_cust_reg_btn.grid(
            row=9, column=0, columnspan=4, padx=10, pady=6, sticky="swe"
        )

        self.new_cust_warn_label = ttk.Label(
            self.customer_details_page,
            text="Customer not found! Register new customer",
            style="accent.TLabel",
        )
        self.new_cust_reg_btn.grid(
            row=9,
            column=0,
            columnspan=4,
            ipadx=6,
            ipady=6,
            padx=10,
            pady=6,
            sticky="swe",
        )
        hide_grid_widget(self.new_cust_warn_label)

        #########################
        # Medicine Details Page #
        #########################
        self.medicine_details_page = ttk.Frame(self.menu.content_frame)
        grid_config(self.medicine_details_page)

        grid_config(self.medicine_details_page)

        l1 = ttk.Label(
            self.medicine_details_page, text="Medicine Name", style="small.TLabel"
        )
        l1.grid(row=0, column=0, padx=10, pady=4, sticky="sw")

        self.med_name_entry = ttk.Entry(self.medicine_details_page)
        self.med_name_entry.grid(
            row=1, column=0, padx=10, pady=4, columnspan=7, sticky="we"
        )

        self.med_dropdown = EntrySuggestions(self.med_name_entry)
        self.med_name_entry.bind("<KeyRelease>", self.med_suggestions)

        
        l2 = ttk.Label(
            self.medicine_details_page, text="Quantity", style="small.TLabel"
        )
        l2.grid(row=2, column=0, padx=10, pady=4, sticky="sw")

        self.qty_entry = ttk.Entry(self.medicine_details_page)
        self.qty_entry.grid(
            row=3, column=0, padx=10, pady=4, columnspan=6, sticky="sew"
        )
        self.med_search_btn = ttk.Button(
            self.medicine_details_page,
            text="Check availability",
            command = lambda : self.check_availability(self.med_name_entry,self.qty_entry)
        )

        self.med_search_btn.grid(row=3, column=6, padx=10, pady=4, sticky="ne")


        self.add_sel_btn = ttk.Button(
            self.medicine_details_page, text="Add Selected", style="accent.TButton",state=tk.DISABLED,
            command = lambda : self.add_item(self.med_name_entry,self.qty_entry)
        )
        self.add_sel_btn.grid(
            row=4, column=0, padx=10, pady=8, columnspan=8, sticky="ew"
        )

        self.qty_entry.bind('<FocusIn>',self.disable)

        self.med_table = easy_treeview(
            self.medicine_details_page, columns=["Medicine", "Quantity","Amount"]
        )
        self.med_table.grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
            columnspan=8,
            ipadx=6,
            ipady=4,
            sticky="nswe",
        )
        self.med_table.bind("<<TreeviewSelect>>",self.selected_item)

        self.delete_row_btn = ttk.Button(self.medicine_details_page, text='- Delete item',command= self.delete_item, state=tk.DISABLED)
        self.delete_row_btn.grid(row=7, column=0, padx=10,pady=6,sticky='w')

        #########################
        # Payment Details Page #
        #########################
        self.payment_details_page = ttk.Frame(self.menu.content_frame)
        grid_config(self.payment_details_page)

        l1 = ttk.Label(
            self.payment_details_page, text="Payment Date", style="small.TLabel"
        )
        l1.grid(row=0, column=0, padx=10, pady=4, sticky="sw")

        self.datetime_entry = ttk.Entry(self.payment_details_page)
        self.datetime_entry.grid(
            row=1, column=0, padx=10, pady=4, columnspan=5, sticky="ew"
        )

        self.ct_btn = ttk.Button(
            self.payment_details_page,
            text="Insert Current Date",
            command=lambda: self.datetime_entry.insert(
                "0", str(datetime.datetime.now().date())
            ),
        )
        self.ct_btn.grid(row=1, column=6, columnspan=3, padx=10, pady=4, sticky="new")

        self.gen_recpt = ttk.Button(
            self.payment_details_page, text="Generate Receipt", style="accent.TButton",command=self.generate_reciept
        )
        self.gen_recpt.grid(row=3, column=0, padx=10, pady=8, columnspan=8, sticky="ew")

        var = tk.StringVar()
        self.payment_method_menu = ttk.OptionMenu(
            self.payment_details_page, var, *["Cash", "Credit/Debit Card", "UPI"]
        )
        # self.payment_method_menu.config()
        self.payment_method_menu.grid(
            row=2, column=0, padx=10, pady=8, columnspan=8, sticky="ew"
        )

        self.menu.add(self.customer_details_page, text="Customer Details")
        self.menu.add(self.medicine_details_page, text="Medicines")
        self.menu.add(self.payment_details_page, text="Payment")
        self.menu.pack(fill="both", expand=1, padx=10)

        # Pagination
        self.n_btn = ttk.Button(
            master=self.rootframe,
            text="Next >",
            command=self.menu.next_page,
            style="borderless.TButton",
        )
        self.n_btn.pack(side="right", anchor="se", padx=24, pady=10)

        self.b_btn = ttk.Button(
            master=self.rootframe,
            text="< Back",
            command=self.menu.prev_page,
            style="borderless.TButton",
        )
        self.b_btn.pack(side="left", anchor="sw", padx=24, pady=10)

    def disable(self,a):
        self.add_sel_btn.config(state=tk.DISABLED)

    def selected_item(self,a):
        self.delete_row_btn.config(state=tk.NORMAL)


    def check_availability(self,e1,e2):
        med_name = e1.get()
        qty = int(e2.get())
        if check_med_availability(med_name,qty):
            self.add_sel_btn.config(state=tk.NORMAL)
        else:
            self.add_sel_btn.config(state=tk.DISABLED)

    def add_item(self,e1,e2):
        row = [e1.get(),e2.get()]
        amt = get_amount([row])
        gst = get_gst([row])
        row.append(round(amt[0]*(1+0.01*gst[0])*int(e2.get()),2))
        self.med_table.insert("",tk.END,values=row)
        self.add_sel_btn.config(state=tk.DISABLED)
        self.med_name_entry.delete(0,tk.END)
        self.qty_entry.delete(0,tk.END)
        self.show_amt()

    def delete_item(self):
        selected_items = self.med_table.selection()        
        for selected_item in selected_items:          
            self.med_table.delete(selected_item)
        self.show_amt()

    def display_cust_data(self, data):
        self.cust_name_entry.insert(tk.END, data[1])
        self.cust_age_entry.insert(tk.END, data[2])
        self.cust_sex_entry.insert(tk.END, data[3])
        self.cust_addr_entry.insert(tk.END, data[4])

    def show_error_dialog(self):
        tk.messagebox.showinfo("Error","Fields cannot be blank")

    def reg_new_cust(self):
        data = {}
        if self.cust_name_entry.get() == "" or self.cust_age_entry.get() == "" or self.cust_sex_entry.get() == ""or self.cust_addr_entry.get() == "":
            self.show_error_dialog()
        else:
            data["name"] = self.cust_name_entry.get()
            data["age"] = self.cust_age_entry.get()
            data["sex"] = self.cust_sex_entry.get()
            data["address"] = self.cust_addr_entry.get()
            data["phone_no"] = self.cust_phone_number_entry.get()
            insert_from_dict("customers", data)
            showinfo("Success","Customer Registered")
            self.new_cust_reg_btn.config(state=tk.DISABLED)

    def customer_notfound(self):
        showinfo("Error","Customer Not Found")

    def search_by_ph_no(self):
        self.cust_name_entry.delete(0,tk.END)
        self.cust_age_entry.delete(0,tk.END)
        self.cust_sex_entry.delete(0,tk.END)
        self.cust_addr_entry.delete(0,tk.END)
        ph_no = int(self.cust_phone_number_entry.get())
        data = search_cust_by_phone_no(ph_no)
        if data == None:
            self.customer_notfound()
            self.new_cust_reg_btn.config(state=tk.NORMAL)
            
        else:
            self.display_cust_data(data)
            self.new_cust_reg_btn.config(state=tk.DISABLED)

    def med_suggestions(self, event):
        #print(self.med_name_entry.get())
        
       
        self.med_dropdown.data.clear()
        self.med_dropdown.data.extend(search_med_by_name(self.med_name_entry.get()))
        self.med_dropdown.update()

    def show_amt(self):
        med_list = []
        
        for row in self.med_table.get_children():
            med_list.append((self.med_table.item(row)['values'][0],self.med_table.item(row)['values'][1]))

        amt = get_amount(med_list)
        gst = get_gst(med_list)
        total_amt = 0
        for a,g,m in  zip(amt,gst,med_list):
            total_amt += a*(1+0.01*g)*m[1]

        amt_lbl = ttk.Label(self.medicine_details_page, text=f"Total amount: {round(total_amt,2)}", style="small.TLabel"
        )
        amt_lbl.grid(row=7, column=6, padx=10, pady=4, sticky="sw")
    
    def generate_reciept(self):
        med_list = []
        
        for row in self.med_table.get_children():
            med_list.append((self.med_table.item(row)['values'][0],self.med_table.item(row)['values'][1],self.med_table.item(row)['values'][2]))
        purchase_med(med_list)
        #get_reciept(self.cust_name_entry.get(),self.cust_age_entry.get(),self.cust_sex_entry.get(),self.datetime_entry.get(),med_list)
        RecieptWidget(self.payment_details_page,self.cust_name_entry.get(),self.cust_sex_entry.get(),self.cust_age_entry.get(),self.cust_phone_number_entry.get(),self.datetime_entry.get(),med_list)
        self.cust_name_entry.delete(0,tk.END)
        self.cust_age_entry.delete(0,tk.END)
        self.cust_sex_entry.delete(0,tk.END)
        self.cust_addr_entry.delete(0,tk.END)
        self.cust_phone_number_entry.delete(0,tk.END)
        #showinfo("reciept","Reciept Generated.")
        self.customer_details_page.pack(fill='both',expand=1)
        self.payment_details_page.pack_forget()

    def as_tab(self):
        return self.rootframe


class about_page:
    def __init__(self, master, root_window):
        self.root_window = root_window
        self.rootframe = ttk.Frame(master)
        l0 = ttk.Label(self.rootframe, text="About", style="big.TLabel")
        l0.pack(padx=20, pady=15, anchor="n", expand=1)
        l1 = ttk.Label(
            self.rootframe,
            text="Made by Subhrojyoti Sen and Shashank Daga.",
        )
        l1.pack(padx=20, pady=5, anchor="n", expand=1)
        l2 = ttk.Label(
            self.rootframe, text=" ", style="small.TLabel"
        )
        l2.pack(padx=20, pady=5, anchor="n", expand=1)
        quit_btn = ttk.Button(self.rootframe, text="Quit", command=self.quit_app)
        quit_btn.pack(padx=20, pady=10, anchor="center")

    def quit_app(self):
        close()
        self.root_window.destroy()
        exit()

    def as_tab(self):
        return self.rootframe

    
    
def main():
    global items,invt,root
    root = tk.Tk()

    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry(f"{int(height/1.4)}x{int(width/1.4)}")
    root.minsize(620, 384)
    s = style(root)

    page_buf = PageBuffer(root)

    login_menu = HorizontalNavMenu(page_buf.content_frame)
    ret_login = sales_login_page(
        login_menu.content_frame, lambda: page_buf.show_page_by_name("retail")
    )
    inv_login = admin_login_page(
        login_menu.content_frame, lambda: page_buf.show_page_by_name("inv")
    )
    login_menu.add(ret_login.as_frame(), text="Retail Login")
    login_menu.add(inv_login.as_frame(), text="Inventory Login")

    ret_menu = VerticalNavMenu(page_buf.content_frame,menu_button=True)
    inv_menu = VerticalNavMenu(page_buf.content_frame,menu_button=True)

    pos = pos_page(master=ret_menu.content_frame, root_window=root)

    items = item_page(master=inv_menu.content_frame, root_window=root)
    invt = inventory_order_page(master=inv_menu.content_frame, root_window=root)

    ret_abt = about_page(master=ret_menu.content_frame, root_window=root)
    inv_abt = about_page(master=inv_menu.content_frame, root_window=root)

    ret_menu.add(pos.as_tab(), text="New Order")
    ret_menu.add(ret_abt.as_tab(), text="About")
    ret_menu.add(ttk.Frame(), text="Quit", custom_cmd=ret_abt.quit_app)

    inv_menu.add(items.as_tab(), text="Items")
    inv_menu.add(invt.as_tab(), text="Inventory Orders")
    inv_menu.add(inv_abt.as_tab(), text="About")
    inv_menu.add(ttk.Frame(), text="Quit", custom_cmd=inv_abt.quit_app)

    page_buf.add(login_menu.root_frame, name="login")
    page_buf.add(ret_menu.root_frame, name="retail")
    page_buf.add(inv_menu.root_frame, name="inv")

    login_menu.pack()
    page_buf.pack(fill="both", expand=1)

    root.mainloop()
    return root
    
if __name__ == "__main__":
    main()