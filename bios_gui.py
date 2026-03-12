#GUI applikacija BIOS informacijai gauti
import tkinter as tk
import wmi
from datetime import datetime


def parodyti_bios_info():
    c = wmi.WMI()
    bios = c.Win32_BIOS()[0]
    tekstas = "BIOS INFORMACIJA\n"
    tekstas += "------------------------------------\n"
    #cia bus BIOS informacija
    tekstas += f"Gamintojas: {bios.Manufacturer}\n"
    tekstas += f"Pavadinimas: {bios.Name}\n"
    tekstas += f"Versija: {bios.Version}\n"
    tekstas += f"Numeris: {bios.Serialnumber}\n"
    # Pašaliname dalį po taško (.000000+000)
    raw_date = bios.ReleaseDate.split(".")[0]

    # Konvertuojame tekstą į datetime objektą
    date_object = datetime.strptime(raw_date, "%Y%m%d%H%M%S")

    # Suformatuojame į aiškų žmogui suprantamą formatą
    formatted_date = date_object.strftime("%Y-%m-%d %H:%M:%S")
    tekstas += f"Isleidimo data: {formatted_date}\n"
    etikete.config(text=tekstas)


#sukuriame pagrindini langa
langas = tk.Tk()
langas.title("BIOS informacija")
langas.geometry("400x250")

#etikete tekstui
etikete = tk.Label(langas, text ="Paspausk mygtuka BIOS informacijai gauti", justify="left")
etikete.pack(pady=20)

mygtukas = tk.Button(langas, text="Gauti BIOS duomenis", command=parodyti_bios_info)
mygtukas.pack()


#programas ciklas
langas.mainloop()

