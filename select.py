import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3
con = sqlite3.connect("contacts")
cur = con.cursor()
class MyAppWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ver contactos")
        
        self.set_default_size(400, 400)

        self.liststore = Gtk.ListStore(int,str,str,str,str)
        for row in cur.execute("select * from person"):
            self.liststore.append([row[0],row[1],row[2],row[3], row[4]])

        treeview = Gtk.TreeView(model=self.liststore)


        renderer_text1 = Gtk.CellRendererText()
        column_text1 = Gtk.TreeViewColumn("Id", renderer_text1, text=0)
        treeview.append_column(column_text1)

        renderer_text1 = Gtk.CellRendererText()
        column_text1 = Gtk.TreeViewColumn("Nombre", renderer_text1, text=1)
        treeview.append_column(column_text1)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Apellido", renderer_text, text=2)
        treeview.append_column(column_text)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Telefono", renderer_text, text=3)
        treeview.append_column(column_text)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Direccion", renderer_text, text=4)
        treeview.append_column(column_text)

        self.add(treeview)


win = MyAppWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()