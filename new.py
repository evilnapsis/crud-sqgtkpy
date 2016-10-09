import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3
con = sqlite3.connect("contacts")
cur = con.cursor()

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Nuevo Contacto")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        box = Gtk.Box()
        self.name_entry = Gtk.Entry()
        self.l1 = Gtk.Label("Nombre")
        box.add(self.l1)
        box.add(self.name_entry)
        self.box.add(box)

        box = Gtk.Box()
        self.lastname_entry = Gtk.Entry()
        self.l1 = Gtk.Label("Apellido")
        box.add(self.l1)
        box.add(self.lastname_entry)
        self.box.add(box)

        box = Gtk.Box()
        self.phone_entry = Gtk.Entry()
        self.l1 = Gtk.Label("Telefono")
        box.add(self.l1)
        box.add(self.phone_entry)
        self.box.add(box)

        box = Gtk.Box()
        self.address_entry = Gtk.Entry()
        self.l1 = Gtk.Label("Direccion")
        box.add(self.l1)
        box.add(self.address_entry)
        self.box.add(box)

        self.button1 = Gtk.Button(label="Guardar")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.add(self.button1)
#        self.box.pack_start(self.button1, True, True, 0)

 
    def on_button1_clicked(self, widget):
        if self.name_entry.get_text!="":
            contact = (self.name_entry.get_text(),self.lastname_entry.get_text(),self.phone_entry.get_text(),self.address_entry.get_text())
            cur.execute("insert into person (name,lastname,phone,address) values (?,?,?,?)",contact)
            con.commit()
            self.name_entry.set_text("")
            self.lastname_entry.set_text("")
            self.phone_entry.set_text("")
            self.address_entry.set_text("")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()