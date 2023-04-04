# locale para internacionalização
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, '')  # padrão do sistema
# locale.setlocale(locale.LC_ALL, 'pt_BR')
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Windows: Get-WinSystemLocale
# Linux / Mac: locale -a
# Linux / Mac: locale -a | grep 'pt_BR

print(locale.getlocale())

print(calendar.calendar(2023))
