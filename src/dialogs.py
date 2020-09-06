# dialogs.py
#
# Copyright 2020 Иван Третьяк
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

class FileChooser(Gtk.ApplicationWindow):
    def __init__(self):
        self.dialog  = Gtk.FileChooserDialog(_("Choose a file"), None,
                                        Gtk.FileChooserAction.OPEN,
                                        (Gtk.STOCK_CANCEL,
                                         Gtk.ResponseType.CANCEL,
                                         Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.__add_filters()

    def __add_filters(self):
        filter_text = Gtk.FileFilter()
        filter_text.add_mime_type("image/jpeg")
        filter_text.add_mime_type("image/png")
        filter_text.set_name('Images')
        self.dialog.add_filter(filter_text)

        filter_text = Gtk.FileFilter()
        filter_text.add_mime_type("image/jpeg")
        filter_text.set_name('Images jpg')
        self.dialog.add_filter(filter_text)

        filter_text = Gtk.FileFilter()
        filter_text.add_mime_type("image/png")
        filter_text.set_name('Images png')
        self.dialog.add_filter(filter_text)

    def get_dialog(self):
        return self.dialog
