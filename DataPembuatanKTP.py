from tkinter import *
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side
from tkinter import font as tkfont
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
background_image = ImageTk.PhotoImage(Image.open("e3.jpg"))
l=tk.Label(image=background_image)
l.grid()

tk.Label(root, text="Some File").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
root.title("Data Pembuatan KTP")
root.geometry("750x500")
workbook = Workbook()
sheet = workbook.active

styling = tkfont.Font(family='Helvetica',weight='bold', size=15)
styling2 = tkfont.Font(family='Helvetica', size=9)

font = Font(bold=True)
border = Border(left=Side(border_style='thin',color='00000000'),
                right=Side(border_style='thin',color='00000000'),
                top=Side(border_style='thin',color='00000000'),
                bottom=Side(border_style='thin',color='00000000'))

alignment = Alignment(horizontal='center', vertical='center')


sheet['A1'] = "Keperluan\t:"
A1 = sheet['A1']
A1.font = font
sheet['A2'] = "Tanggal Pembuatan\t:"
A2 = sheet['A2']
A2.font = font

sheet['A3'] = "No"
A3 = sheet['A3']
A3.font = font
A3.border = border
A3.alignment = alignment

sheet['B3'] = "Nama"
B3 = sheet['B3']
B3.font = font
B3.border = border
B3.alignment = alignment

sheet['C3'] = "NoTelepon"
C3 = sheet['C3']
C3.font = font
C3.border = border
C3.alignment = alignment

sheet['D3'] = "JenisKelamin"
D3 = sheet['D3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['E3'] = "Alamat"
E3 = sheet['E3']
E3.font = font
E3.border = border
E3.alignment = alignment

sheet['F3'] = "Agama"
F3 = sheet['F3']
F3.font = font
F3.border = border
F3.alignment = alignment

num = 0


def TambahData():
    global num
    num = num + 1
    sheetnum = num + 3

    sheet['A'+str(sheetnum)] = num
    DataNo = sheet['A'+str(sheetnum)]
    DataNo.border = border
    DataNo.alignment = alignment

    sheet['B'+str(sheetnum)] = namaEntry.get()
    DataNama = sheet['B'+str(sheetnum)]
    DataNama.border = border
    DataNama.alignment = alignment

    sheet['C' + str(sheetnum)] = jeniskelaminEntry.get()
    DataJenisKelamin = sheet['C' + str(sheetnum)]
    DataJenisKelamin.border = border
    DataJenisKelamin.alignment = alignment

    sheet['D' + str(sheetnum)] = noteleponEntry.get()
    DataNoTelepon = sheet['D' + str(sheetnum)]
    DataNoTelepon.border = border
    DataNoTelepon.alignment = alignment

    sheet['E' + str(sheetnum)] = alamatEntry.get()
    DataAlamat = sheet['E' + str(sheetnum)]
    DataAlamat.border = border
    DataAlamat.alignment = alignment

    sheet['F' + str(sheetnum)] = agamaEntry.get()
    DataAgama = sheet['F' + str(sheetnum)]
    DataAgama.border = border
    DataAgama.alignment = alignment

    sheet['B1'] = keperluanEntry.get()
    sheet['B2'] = tanggalEntry.get()

    namaEntry.delete(0, END)
    noteleponEntry.delete(0, END)
    jeniskelaminEntry.delete(0, END)
    alamatEntry.delete(0, END)
    agamaEntry.delete(0, END)

def SimpanData():
    global informasi
    workbook.save(filename=str(keperluanEntry.get())+":"+str(tanggalEntry.get())+".xlsx")

def BuatDataBaru():
    namaEntry.delete(0, END)
    noteleponEntry.delete(0, END)
    jeniskelaminEntry.delete(0, END)
    alamatEntry.delete(0, END)
    keperluanEntry.delete(0, END)
    tanggalEntry.delete(0, END)
    agamaEntry.delete(0, END)
    num = 0

frameJudul = Frame(root, bg='white')
frameJudul.place(rely=0.025,relx=0.5,relheight=0.1,relwidth=0.5,anchor='n')
judul = Label(frameJudul, bg='white', text='Data Pembuatan KTP', font=styling)
judul.place(relheight=1,relwidth=1)


frameKeperluan = Frame(root, bg='white')
frameKeperluan.place(rely=0.17,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
matkulinfo = Label(frameKeperluan, bg='white', text='Keperluan', font=styling2)
matkulinfo.place(relwidth=0.4,relheight=1)
keperluanEntry = Entry(frameKeperluan)
keperluanEntry.place(relx=0.4,relheight=1,relwidth=0.6)
keperluanEntry.get()

frameTanggal = Frame(root, bg='white')
frameTanggal.place(rely=0.24,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
tanggalinfo = Label(frameTanggal, bg='white', text='Tanggal Pembuatan', font=styling2)
tanggalinfo.place(relwidth=0.4,relheight=1)
tanggalEntry = Entry(frameTanggal)
tanggalEntry.place(relx=0.4,relheight=1,relwidth=0.6)
tanggalEntry.get()

frameNama = Frame(root, bg='white')
frameNama.place(rely=0.31,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
namainfo = Label(frameNama, bg='white', text='Nama', font=styling2)
namainfo.place(relwidth=0.4,relheight=1)
namaEntry = Entry(frameNama)
namaEntry.place(relx=0.4,relheight=1,relwidth=0.6)
namaEntry.get()

frameNoTelepon = Frame(root, bg='white')
frameNoTelepon.place(rely=0.38,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
noteleponinfo = Label(frameNoTelepon, bg='white', text='No Telepon', font=styling2)
noteleponinfo.place(relwidth=0.4,relheight=1)
noteleponEntry = Entry(frameNoTelepon)
noteleponEntry.place(relx=0.4,relheight=1,relwidth=0.6)
noteleponEntry.get()

frameJenisKelamin = Frame(root, bg='white')
frameJenisKelamin.place(rely=0.45,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
jeniskelamininfo = Label(frameJenisKelamin, bg='white', text='Jenis Kelamin', font=styling2)
jeniskelamininfo.place(relwidth=0.4,relheight=1)
jeniskelaminEntry = Entry(frameJenisKelamin)
jeniskelaminEntry.place(relx=0.4,relheight=1,relwidth=0.6)
jeniskelaminEntry.get()

frameAlamat = Frame(root, bg='white')
frameAlamat.place(rely=0.52,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
alamatinfo = Label(frameAlamat, bg='white', text='Alamat', font=styling2)
alamatinfo.place(relwidth=0.4,relheight=1)
alamatEntry = Entry(frameAlamat)
alamatEntry.place(relx=0.4,relheight=1,relwidth=0.6)
alamatEntry.get()

frameAgama = Frame(root, bg='white')
frameAgama.place(rely=0.59,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
agamainfo = Label(frameAgama, bg='white', text='Agama', font=styling2)
agamainfo.place(relwidth=0.4,relheight=1)
agamaEntry = Entry(frameAgama)
agamaEntry.place(relx=0.4,relheight=1,relwidth=0.6)
agamaEntry.get()

frameButton = Frame(root, bg='white')
frameButton.place(rely=0.695,relx=0.5,relheight=0.3,relwidth=0.3,anchor='n')
insert = Button(frameButton, text='Tambah', command=TambahData)
insert.place(rely=0,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
save = Button(frameButton, text='Simpan', command=SimpanData)
save.place(rely=0.25,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
createNewData = Button(frameButton, text='Buat Data Baru', command=BuatDataBaru)
createNewData.place(rely=0.5,relx=0.5,relheight=0.25,relwidth=1,anchor='n')
Exit = Button(frameButton, text='Keluar', command=root.quit)
Exit.place(rely=0.72,relx=0.5,relheight=0.25,relwidth=1,anchor='n')





root.mainloop()
