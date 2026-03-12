import wmi #biblioteka skirta darbui su Windows managment instrumentation
from datetime import datetime


#sukuriams rysys su Windows WMI sistema

c = wmi.WMI()

#dazniausiai grazinamas vienas objektas, todel imame pirma elementa [0]
bios = c.Win32_BIOS()[0]

print("BIOS INFORMACIJA")
print("-----------------------------")
#manufacturer - BIOS gamintojas
print("Gamintojas:", bios.Manufacturer)

#name - BIOS pavadinimas
print("Pavadinimas:", bios.Name)

#version - BIOS versija
print("Versija:", bios.Version)

#serial number - BIOS numeris
print("Serial number:", bios.Serialnumber)



# Pašaliname dalį po taško (.000000+000)
raw_date = bios.ReleaseDate.split(".")[0]

# Konvertuojame tekstą į datetime objektą
date_object = datetime.strptime(raw_date, "%Y%m%d%H%M%S")

# Suformatuojame į aiškų žmogui suprantamą formatą
formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")

print("Išleidimo data:", formatted_date)