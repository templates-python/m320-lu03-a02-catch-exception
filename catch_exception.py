class NameList:
    """
    Diese Klasse dient der Nutzung von try-except, um das "fangen" eines Fehlers zu implementieren.
    Es wird bewusst eine Liste implementiert, bei der falsche Indexe möglich sind, so dass ein
    IndexError erzeugt wird.
    """

    def __init__(self):
        self._name_list = ['Konrad', 'Greta', 'Mike', 'Frida', 'Ephron']


    def take_name(self, index):
        """
        Liefert den durch index angegebene nNamen aus der Liste.
        Der index wird NICHT überwacht!
        """
        return self._name_list[index]


if __name__ == '__main__':
    name_list = NameList()
    for idx in range(6):
        print(name_list.take_name(idx))