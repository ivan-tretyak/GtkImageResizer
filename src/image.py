# image.py
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

from PIL import Image

class FileImage:
    def get_width(path2image):
        im = Image.open(path2image)
        return im.size[0]

    def get_height(path2image):
        im = Image.open(path2image)
        return im.size[1]

    def save_new_image(path2image, path4save, width, height):
        im = Image.open(path2image)
        rim = im.resize((int(width), int(height)), Image.ANTIALIAS)

        extension = os.path.splitext(path2image)[1]
        prefix = '_resize_' + str(width) + 'x' + str(height)
        prefix += extension

        file_for_save = os.path.splitext(os.path.basename(path2image))[0] + prefix
        file_for_save = os.path.join(path4save, file_for_save)

        try:
            rim.save(file_for_save)
        except:
            extension = '.png' if extension == '.jpg' else '.jpg'
            file_for_save = os.path.splitext(file_for_save)[0] + extension
            rim.save(file_for_save)
