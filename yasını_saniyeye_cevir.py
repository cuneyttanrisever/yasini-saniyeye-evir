from datetime import *
import os
os.system("clear")
print("Cüneyt TANRISEVER")
dogumg = datetime.strptime(raw_input("dogum gunu gun.ay.yil olarak gir. (d.m.Y): "), "%d.%m.%Y")
yas = dogumg.now() - dogumg
print("su ana kadar {} saniye gecti.".format(yas.total_seconds()))
