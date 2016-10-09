import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3
con = sqlite3.connect("contacts")
cur = con.cursor()

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Actualizar Contacto")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        box = Gtk.Box()
        self.id_entry = Gtk.Entry()
        self.l1 = Gtk.Label("Id")
        self.bs = Gtk.Button("Buscar ...")
        box.add(self.l1)
        box.add(self.id_entry)
        box.add(self.bs)
        self.box.add(box)
        self.bs.connect("clicked", self.on_bs_clicked)

        box = Gtk.Box()
        self.lhelpr = Gtk.Label("Debes buscar un ID")
        box.add(self.lhelpr)
        self.box.add(box)

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

        self.button1 = Gtk.Button(label="Actualizar")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.add(self.button1)
#        self.box.pack_start(self.button1, True, True, 0)

 
    def on_button1_clicked(self, widget):
        if self.id_entry.get_text()!="" and self.name_entry.get_text!="":
            contact = (self.name_entry.get_text(),self.lastname_entry.get_text(),self.phone_entry.get_text(),self.address_entry.get_text(),self.id_entry.get_text())
            cur.execute("update person set name=?,lastname=?,phone=?,address=? where id=?",contact)
            con.commit()
            self.lhelpr.set_text("Id {0} Actualizado!!".format(self.id_entry.get_text()))

    def on_bs_clicked(self, widget):
        theid= self.id_entry.get_text()
        if theid!="":
            sql ="select * from person where id={0}".format(theid)
            data = cur.execute(sql ).fetchall()
            if len(data)>0:
                for row in data:
                    self.lhelpr.set_text("Id {0} Encontrado!!".format(theid))
                    self.name_entry.set_text(row[1])
                    self.lastname_entry.set_text(row[2])
                    self.phone_entry.set_text(row[3])
                    self.address_entry.set_text(row[4])
            else:
                self.lhelpr.set_text("Id {0} No encontrado!!".format(theid))
                self.name_entry.set_text("")
                self.lastname_entry.set_text("")
                self.phone_entry.set_text("")
                self.address_entry.set_text("")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()