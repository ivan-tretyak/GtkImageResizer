# window.py
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

from gi.repository import Gtk, GdkPixbuf
import os
import threading

from .dialogs import FileChooser
from .image import FileImage

@Gtk.Template(resource_path='/com/github/ivantretyak/ImageResizer/window.ui')
class ImageresizerWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ImageresizerWindow'

    _image_display = Gtk.Template.Child()
    _height = Gtk.Template.Child()
    _width = Gtk.Template.Child()
    _chain_button = Gtk.Template.Child()
    _resize = Gtk.Template.Child()

    _file_chooser = Gtk.Template.Child()
    _header_bar = Gtk.Template.Child()

    w = None
    h = None
    f = None
    chain_status = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on__file_chooser_clicked(self, button):
        dialog = FileChooser()
        dialog = dialog.get_dialog()
        response = dialog.run()

        self.h = None
        self.w = None

        if response == Gtk.ResponseType.OK:
            f = dialog.get_filename()
            dialog.destroy()

            self._header_bar.set_title(os.path.basename(f))
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(f, 500, 500, True)
            self._image_display.set_from_pixbuf(pixbuf)

            self._width.set_value(FileImage.get_width(f))
            self._height.set_value(FileImage.get_height(f))

            self.w = self._width.get_value()
            self.h = self._height.get_value()
            self.f = f

            return 0
        else:
            dialog.destroy()
        del response

    @Gtk.Template.Callback()
    def on__resize_clicked(self, button):
        x = threading.Thread(target = self.__resize)
        x.start()

    @Gtk.Template.Callback()
    def on__width_value_changed(self, button):
        if self.chain_status and self.f is not None:
            new_h = int(self.h * self._width.get_value()) / self.w
            self._height.set_value(new_h)
            self.h = new_h
            self.w = self._width.get_value()
        else:
            self.w = self._width.get_value()

    @Gtk.Template.Callback()
    def on__height_value_changed(self, button):
        if self.chain_status and self.f is not None:
            new_w = (self.w * self._height.get_value()) / self.h
            self._width.set_value(new_w)
            self.w = new_w
            self.h = self._height.get_value()
        else:
            self.h = self._height.get_value()

    @Gtk.Template.Callback()
    def on__chain_button_toggled(self, button):
        self.chain_status = self._chain_button.get_active()

    def __resize(self):
        new_width = self._width.get_value()
        new_height = self._height.get_value()

        path4save = os.path.dirname(self.f)

        FileImage.save_new_image(self.f, path4save, new_width, new_height)
