import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from backend import *
import os



def grid_config(root, rows=8, cols=8):
    i = 0
    while i < cols:
        root.grid_columnconfigure(i, weight=1, minsize=40)
        i += 1


def widget_packdata_fmt(widget):
    return {"widget": widget, "packinfo": widget.pack_info(), "hidden": False}


def hide_packed_widget(hidden_widget):
    hidden_widget["widget"].pack_forget()
    hidden_widget["hidden"] = True
    return hidden_widget


def show_packed_widget(hidden_widget):
    hidden_widget["widget"].pack(hidden_widget["packinfo"])
    hidden_widget["hidden"] = False
    return hidden_widget


def toggle_packed_widget(hidden_widget):
    if hidden_widget["hidden"]:
        show_packed_widget(hidden_widget)
    else:
        hide_packed_widget(hidden_widget)


def hide_grid_widget(widget):
    widget.grid_remove()


def show_grid_widget(widget):
    widget.grid()


def next_tab(notebk):
    all_tabs = notebk.tabs()
    sel_tab = notebk.select()

    if sel_tab != all_tabs[-1]:
        i = all_tabs.index(sel_tab)
        notebk.select(all_tabs[i + 1])


def prev_tab(notebk):
    all_tabs = notebk.tabs()
    sel_tab = notebk.select()

    if sel_tab != all_tabs[0]:
        i = all_tabs.index(sel_tab)
        notebk.select(all_tabs[i - 1])


def easy_treeview(master, columns):
    tv = ttk.Treeview(master=master, columns=columns, show="headings")

    for column in columns:
        tv.column(column, width=80, anchor="c", stretch=tk.YES)
        tv.heading(column, text=str(column))

    return tv


def ins_row_treeview(tv, row_data):
    num_rows = len(tv.get_children())
    tv.insert(parent="", index=num_rows, iid=num_rows, values=row_data)


def ins_rows_treeview(tv, rows):
    num_rows = len(tv.get_children())
    for i, row in enumerate(rows):
        tv.insert(parent="", index=num_rows + i, iid=num_rows + i, values=row)


def update_treeview(tv, updated_data):
    for item in tv.get_children():
        tv.delete(item)
    ins_rows_treeview(tv, updated_data)


class PageBuffer:
    def __init__(self, master):
        self.content_frame = ttk.Frame(master)
        self.current_page_index = -1
        self.page_buffer = []
        self.pack_info = {"fill": "both", "expand": 1}

    def show_page(self, page_index):
        if page_index != self.current_page_index:
            current_frame_data_widget = self.page_buffer[self.current_page_index][1]
            frame_data_widget = self.page_buffer[page_index][1]

            hide_packed_widget(current_frame_data_widget)
            show_packed_widget(frame_data_widget)
            self.current_page_index = page_index

    def show_page_by_name(self, name):
        index = self.current_page_index
        for i in self.page_buffer:
            if i[0] == name:
                index = self.page_buffer.index(i)
        self.show_page(index)

    def add(self, frame, name=None):
        if not isinstance(name, str):
            raise Exception("Entered text is not valid")

        frame.pack(**self.pack_info)
        frame_data_widget = {
            "widget": frame,
            "packinfo": self.pack_info,
            "hidden": False,
        }
        hide_packed_widget(frame_data_widget)
        self.page_buffer.append([name, frame_data_widget])
        self.current_page_index = len(self.page_buffer)-1

    def prev_page(self):
        if self.current_page_index != 0:
            self.show_page(self.current_page_index - 1)

    def next_page(self):
        if self.current_page_index != len(obj) - 1:
            self.show_page(self.current_page_index + 1)

    def pack(self, **pack_info):
        self.content_frame.pack(**self.pack_info)
        if self.page_buffer != []:
            self.show_page(0)


class VerticalNavMenu:
    def __init__(self, master, menu_button=False):
        self.root_frame = ttk.Frame(master)
        self.menu_button_flag = menu_button
        self.menu_frame = ttk.Frame(self.root_frame, style="NavMenu.TFrame")
        self.menu_frame.lift()
        self.menu_frame.pack(side="left", fill="both", expand=1, anchor="w")
        self.menu_data_widget = widget_packdata_fmt(self.menu_frame)

        self.content_frame = ttk.Frame(self.root_frame, style="verticalNavMenu.TFrame")
        self.content_frame.pack(
            side="right",
            fill="both",
            expand=7,
            ipady=4,
            ipadx=4,
        )

        self.current_frame_index = -1
        self.content_frame_buffer = []
        self.menu_btn_widgets = []
        self.pack_info = {"fill": "both", "expand": 1}

        if self.menu_button_flag:
            self.toggle_menu_button()

    def toggle_menu_button(self):

        self.menu_img = tk.PhotoImage(
            master=self.root_frame,
            file="".join(
                [os.getcwd(), os.path.sep, "assets", os.path.sep, "menu_dark_btn.png"]
            ),
            name="menu_btn_image",
        )

        self.menu_show_btn = ttk.Button(
            self.root_frame,
            image=self.menu_img,
            text="Menu",
            command=self.toggle_menu,
            style="menubtn.TButton",
        )
        self.menu_show_btn.lift()
        self.menu_show_btn.pack(in_=self.root_frame, anchor="nw")

    def toggle_menu(self):
        toggle_packed_widget(self.menu_data_widget)

    def show_frame(self, frame_index):
        if frame_index != self.current_frame_index:
            current_frame_data_widget = self.content_frame_buffer[
                self.current_frame_index
            ]
            frame_data_widget = self.content_frame_buffer[frame_index]

            hide_packed_widget(current_frame_data_widget)
            show_packed_widget(frame_data_widget)
            self.menu_btn_widgets[self.current_frame_index].state(["!pressed"])
            self.menu_btn_widgets[frame_index].state(["pressed"])
            self.current_frame_index = frame_index
            if self.menu_button_flag:
                self.toggle_menu()

    def add(self, frame, text=None, custom_cmd=None):
        if not isinstance(text, str):
            raise Exception("Entered text is not valid")

        frame_index = len(self.content_frame_buffer)
        frame.pack(**self.pack_info)
        frame_data_widget = {
            "widget": frame,
            "packinfo": self.pack_info,
            "hidden": False,
        }
        hide_packed_widget(frame_data_widget)
        self.content_frame_buffer.append(frame_data_widget)

        menu_btn = ttk.Button(
            self.menu_frame,
            text=text,
            style="NavMenu.TButton",
        )
        if custom_cmd is None:
            menu_btn.config(command=lambda: self.show_frame(frame_index))
        else:
            menu_btn.config(command=custom_cmd)
        menu_btn.pack(fill="x", padx=0, ipadx=4, pady=0, ipady=4)
        self.menu_btn_widgets.append(menu_btn)

    def prev_page(self):
        if self.current_frame_index > 0:
            self.show_frame(self.current_frame_index - 1)

    def next_page(self):
        if self.current_frame_index < len(self.content_frame_buffer) - 1:
            self.show_frame(self.current_frame_index + 1)

    def pack(self, **pack_info):
        self.root_frame.pack(**pack_info)
        if self.content_frame_buffer != []:
            self.show_frame(0)


class HorizontalNavMenu:
    def __init__(self, master):
        self.root_frame = ttk.Frame(master)
        self.menu_frame = ttk.Frame(self.root_frame, style="NavMenu.TFrame")
        self.menu_frame.lift()
        self.menu_frame.pack(
            side="top", fill="none", expand=0, anchor="center", padx=15, pady=15
        )
        self.menu_data_widget = widget_packdata_fmt(self.menu_frame)

        self.content_frame = ttk.Frame(self.root_frame, style="verticalNavMenu.TFrame")
        self.content_frame.pack(
            side="top",
            fill="both",
            expand=1,
            ipady=4,
            ipadx=4,
        )

        self.current_frame_index = -1
        self.content_frame_buffer = []
        self.menu_btn_widgets = []
        self.pack_info = {"fill": "both", "expand": 1}

    def show_frame(self, frame_index):
        if frame_index != self.current_frame_index:
            current_frame_data_widget = self.content_frame_buffer[
                self.current_frame_index
            ]
            frame_data_widget = self.content_frame_buffer[frame_index]

            hide_packed_widget(current_frame_data_widget)
            show_packed_widget(frame_data_widget)
            self.menu_btn_widgets[self.current_frame_index].state(["!pressed"])
            self.menu_btn_widgets[frame_index].state(["pressed"])
            self.current_frame_index = frame_index

    def add(self, frame, text=None, custom_cmd=None):
        if not isinstance(text, str):
            raise Exception("Entered text is not valid")

        frame_index = len(self.content_frame_buffer)
        frame.pack(**self.pack_info)
        frame_data_widget = {
            "widget": frame,
            "packinfo": self.pack_info,
            "hidden": False,
        }
        hide_packed_widget(frame_data_widget)
        self.content_frame_buffer.append(frame_data_widget)

        menu_btn = ttk.Button(
            self.menu_frame,
            text=text,
            style="NavMenu.TButton",
        )
        if custom_cmd is None:
            menu_btn.config(command=lambda: self.show_frame(frame_index))
        else:
            menu_btn.config(command=custom_cmd)
        menu_btn.pack(
            side="left", fill="y", padx=0, ipadx=20, pady=0, ipady=4, anchor="center"
        )
        self.menu_btn_widgets.append(menu_btn)

    def toggle_menu(self):
        toggle_packed_widget(self.menu_data_widget)

    def prev_page(self):
        if self.current_frame_index > 0:
            self.show_frame(self.current_frame_index - 1)

    def next_page(self):
        if self.current_frame_index < len(self.content_frame_buffer) - 1:
            self.show_frame(self.current_frame_index + 1)

    def pack(self, **pack_info):
        self.root_frame.pack(**pack_info)
        if self.content_frame_buffer != []:
            self.show_frame(0)



class EntrySuggestions:
    def __init__(self, root, onClick=False):
        self.root = root

        self.rootframe = ttk.Frame(root.master, style="suggestions.TFrame")
        self.rootframe.bind("<FocusOut>", lambda event: self.hide())
        self.rootframe.lift(root)
        self.rootframe.place(
            in_=root,
            relx=0,
            rely=1,
            relwidth=1,
        )
        self.info = self.rootframe.place_info()
        self.selected_val = None
        self.click_fn = onClick
        self.items = []
        self.data = []

    def hide(self):
        self.rootframe.place_forget()

    def show(self):
        self.rootframe.lift()
        self.rootframe.place(self.info)

    def delete_all(self):
        if self.items != []:
            for item in self.items:
                item.destroy()
        self.items.clear()

    def update(self):
        #print(len(self.items),len(self.data))
        if len(self.data) == 0:
            self.hide()
            self.delete_all()
        elif len(self.items) != len(self.data):
            self.hide()
            self.delete_all()
            #print(len(self.items),len(self.data))
            val = ""
            for i, val in enumerate(self.data):
                e = ttk.Button(
                    self.rootframe,
                    text=val,
                    command=lambda indx=i: self.on_sel(indx),
                    style="suggestions.TButton",
                )
                e.pack(fill="x", expand=1)
                self.items.append(e)
            self.show()
        
        

    def on_sel(self, i):
        self.root.delete(0, tk.END)
        self.root.insert(0, self.data[i])
        self.hide()

    # def _sel_data(self, widget):
    #     index = self.items.index(widget)
    #     self.selected_val = self.data[index]
    #     if self.click_fn:
    #         self.click_fn(self.selected_val)


class RecieptWidget:
    def __init__(self,root,name,gender,age,phone,date,med_list):
        self.main = Toplevel(root)
        self.rootframe = ttk.Frame(self.main)
        self.main.minsize(750,450)
        self.rootframe.pack(fill='both',expand=1)
        self.name =name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.date =date
        self.med_list = med_list
        grid_config(self.rootframe)

        self.name_label = ttk.Label(self.rootframe, text=f"Patient Name: {name}", style="small.TLabel")
        self.name_label.grid(row=0, column=0, padx=10, pady=4, sticky="sw")

        self.age_label = ttk.Label(self.rootframe, text=f"Age: {age}", style="small.TLabel")
        self.age_label.grid(row=0, column=4, padx=10, pady=4, sticky="sw")

        self.gender_label = ttk.Label(self.rootframe, text=f"Gender: {gender}", style="small.TLabel")
        self.gender_label.grid(row=0, column=6, padx=10, pady=4, sticky="sw")

        self.date_label = ttk.Label(self.rootframe, text=f"Date: {date}", style="small.TLabel")
        self.date_label.grid(row=1, column=4, padx=10, pady=4, sticky="sw")

        self.ph_label = ttk.Label(self.rootframe, text=f"Phone Number: {phone}", style="small.TLabel")
        self.ph_label.grid(row=1, column=0, padx=10, pady=4, sticky="sw")

        self.med_table = easy_treeview(
            self.rootframe, columns=["Medicine", "Quantity","Amount"]
        )
        self.med_table.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            columnspan=8,
            ipadx=6,
            ipady=4,
            sticky="nswe",
        )

        for row in med_list:
            self.med_table.insert("",tk.END,values=row)

        self.gen_recpt = ttk.Button(
            self.rootframe, text="Save Receipt", style="accent.TButton",command=self.generate_reciept
        )
        self.gen_recpt.grid(row=7, column=0, padx=10, pady=8, sticky="ew")

        self.gen_recpt = ttk.Button(
            self.rootframe, text="Close", style="accent.TButton",command=self.closeWin
        )
        self.gen_recpt.grid(row=7, column=2, padx=10, pady=8, sticky="ew")

    def generate_reciept(self):
        save_reciept(self.name,self.age,self.gender,self.date,self.phone,self.med_list)
        showinfo("Success","Reciept saved")
        self.closeWin()

    def closeWin(self):
        self.main.destroy()


