#!/usr/bin/env python
import datetime
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from utils import get_glade_file_path, get_wal_colors


class PolybarCalendar(Gtk.Builder):
    def __init__(self):
        Gtk.Builder.__init__(self)
        self.add_from_file(get_glade_file_path('calendar.glade'))
        self.window = self.get_object('calendarwindow')
        self.calendar = self.get_object('calendar')
        date = datetime.date.today()
        self.calendar.select_day(date.day)
        self.calendar.select_month(date.month-1, date.year)

def gtk_style():
    colors = get_wal_colors()
    css = b"""
* {
    transition-property: color, background-color, border-color, background-image, padding, border-width;
    transition-duration: 0.15s;
    font-size: 16px;
    color: %s
}
.time {
    color: %s;
}
.frame {
    background-color: %s;
}
.calendar {
    background-color: %s;
}
.calendar:selected {
    color:%s;
    background-color:%s;
}
.textview {
    background-color:%s;
}

""" % (
        str.encode(colors['color7']),
        str.encode(colors['color3']),
        str.encode(colors['color0']),
        str.encode(colors['color0']),
        str.encode(colors['color0']),
        str.encode(colors['color1']),
        str.encode(colors['color1'])
    )

    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )


win = PolybarCalendar().window
win.connect("destroy", Gtk.main_quit)
win.show_all()
gtk_style()
Gtk.main()
