import os
from gi.repository import GObject, Nautilus
from subprocess import call

class NautilusKonsole(GObject.GObject, Nautilus.MenuProvider):

    def startKonsole(self, menu, files):
        path = ''
        for file in files:
            filepath = file.get_location().get_path()
            if os.path.isfile(filepath):
                filepath = os.path.dirname(filepath)
            if os.path.exists(filepath):
                path = '"' + filepath + '" '
                break

        call('konsole --workdir ' + path + "&", shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='OpenInKonsole',
            label='Open in Konsole',
            tip='Opens the directory of the files in Konsole'
        )
        item.connect('activate', self.startKonsole, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='OpenInKonsole',
            label='Open in Konsole',
            tip='Opens the directory in Konsole'
        )
        item.connect('activate', self.startKonsole, [file_])

        return [item]
