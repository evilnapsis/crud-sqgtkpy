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
        self.bs = Gtk.Button("Buscar y eliminar ...")
        box.add(self.l1)
        box.add(self.id_entry)
        box.add(self.bs)
        self.box.add(box)
        self.bs.connect("clicked", self.on_bs_clicked)

        box = Gtk.Box()
        self.lhelpr = Gtk.Label("Debes buscar un ID")
        box.add(self.lhelpr)
        self.box.add(box)

    def on_bs_clicked(self, widget):
        theid= self.id_entry.get_text()
        if theid!="":
            sql ="select * from person where id={0}".format(theid)
            data = cur.execute(sql ).fetchall()
            if len(data)>0:
                cur.execute("delete from person where id=?",(theid))
                con.commit()
                self.lhelpr.set_text("Id {0} Eliminado!!".format(theid))
            else:
                self.lhelpr.set_text("Id {0} No encontrado!!".format(theid))

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()