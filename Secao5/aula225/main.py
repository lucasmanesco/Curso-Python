# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_success('que legal')

# lf = LogFileMixin()
# lp.log_error('qualquer coisa')
# lp.log_success('que legal')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()
