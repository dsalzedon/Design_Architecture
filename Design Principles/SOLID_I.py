# isp

class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFuncPrinter(Machine):
    # Works for Machine Class
    # bc has all the methods
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldPrinter(Machine):
    # breaks ISP
    # bc expose methods that wont be avail
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        # do nothing, is problematic
        pass

    def scan(self, document):
        raise NotImplementedError('Printer Cant scan!')


class Printer:
    @abstracmethod
    def print(self, document):
        pass


class Scanner:
    @abstracmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass
