import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Menu")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Nuevo contacto")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.add(self.button1)

        self.button2 = Gtk.Button(label="Ver contactos")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.add(self.button2)

        self.button3 = Gtk.Button(label="Editar contactos")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.add(self.button3)

        self.button4 = Gtk.Button(label="Editar contactos")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.add(self.button4)

 
    def on_button1_clicked(self, widget):
        subprocess.Popen(["python", "new.py"])

    def on_button2_clicked(self, widget):
        subprocess.Popen(["python", "select.py"])

    def on_button3_clicked(self, widget):
        subprocess.Popen(["python", "edit.py"])

    def on_button4_clicked(self, widget):
        subprocess.Popen(["python", "delete.py"])

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()