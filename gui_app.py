import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from numpy import pad


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Diagnosis Hepatitis')
        self.call("source", "sun-valley.tcl")
        self.call("set_theme", "light")
        self.frame = ttk.Frame(self, padding=(64, 64, 64, 64))

        # label
        self.titlelabel = ttk.Label(self, text='Aplikasi Hepatitis', font=('Segoe UI', 20), padding=(10, 10, 10, 10), justify='center')
        self.titlelabel.pack()

        self.information = ttk.Label(self, text='Aplikasi ini adalah implementasi Expert System untuk mengklasifikasikan jenis-jenis Hepatitis berdasarkan kondisi dan tes darah pasien', font=('Segoe UI', 11), padding=(10, 10, 10, 10), justify='left', wraplength=420)
        self.information.pack()

        slider_value= tk.IntVar()
        

        #AgeFrame
        self.ageframe = ttk.Frame(self, padding=(12, 12, 12, 12), borderwidth=5, relief='groove', )
        self.ageframe.pack()
        self.agelabel = ttk.Label(self.ageframe, text='Umur Pasien', font=('Segoe UI', 12), padding=(10, 10, 10, 10), justify='left',)
        self.agelabel.pack(side='left')
        self.ageslider = ttk.Scale(self.ageframe, from_=0, to=100, orient='horizontal', length=120, variable=slider_value, command=self.age_slider_changed)
        self.ageslider.pack(side='left')
        self.ageinfo = ttk.Label(self.ageframe, text="0", font=('Segoe UI', 12), padding=(10, 10, 10, 10), justify='left')
        self.ageinfo.pack(side='left')
        
        #mainframe
        self.mainframe = ttk.Frame(self, padding=(12, 12, 12, 12),)
        self.mainframe.pack()

        #Condition
        self.leftconditionframe = ttk.Frame(self.mainframe, borderwidth=5, relief='groove', )
        self.leftconditionframe.pack(side='left', padx=12)
        self.leftconditionlabel = ttk.Label(self.leftconditionframe, text='Kondisi & Latar Pasien', font=('Segoe UI', 12), padding=(10, 10, 10, 10), justify='left',)
        self.leftconditionlabel.pack(fill='x')
        self.bad_sanitation = ttk.Checkbutton(self.leftconditionframe, text='Sanitasi Buruk', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.bad_sanitation.pack(fill='x')
        self.tropical = ttk.Checkbutton(self.leftconditionframe, text='Tinggal di Daerah tropis', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.tropical.pack(fill='x')
        self.asymptomatic = ttk.Checkbutton(self.leftconditionframe, text='Tidak bergejala', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.asymptomatic.pack(fill='x')
        self.b_survivor = ttk.Checkbutton(self.leftconditionframe, text='Mantan pengidap Hepatitis B', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.b_survivor.pack(fill='x')
        self.homosexual = ttk.Checkbutton(self.leftconditionframe, text='Pernah berhubungan sesama jenis', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.homosexual.pack(fill='x')
        self.alcoholic = ttk.Checkbutton(self.leftconditionframe, text='Sering minum Alkohol', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.alcoholic.pack(fill='x')
        self.hemodialisis = ttk.Checkbutton(self.leftconditionframe, text='Rajin terapi Hemodialisis', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.hemodialisis.pack(fill='x')


        #BloodTest
        self.rightconditionframe = ttk.Frame(self.mainframe, borderwidth=5, relief='groove', )
        self.rightconditionframe.pack(side='left', padx=12)
        self.rightconditionlabel = ttk.Label(self.rightconditionframe, text='Kandungan di Darah', font=('Segoe UI', 12), padding=(10, 10, 10, 10), justify='left',)
        self.rightconditionlabel.pack(fill='x')
        self.antibody_hba = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbA1c', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.antibody_hba.pack(fill='x')
        self.antibody_hbb = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbB', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.antibody_hbb.pack(fill='x')
        self.antibody_hbc = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbC', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.antibody_hbc.pack(fill='x')
        self.antibody_hbd = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbD', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.antibody_hbd.pack(fill='x')
        self.antibody_hbe = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbE', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.antibody_hbe.pack(fill='x')
        self.alanine = ttk.Checkbutton(self.rightconditionframe, text='Alanin-Transaminase', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.alanine.pack(fill='x')
        self.IgG = ttk.Checkbutton(self.rightconditionframe, text='IgG', variable=tk.BooleanVar(value=True), onvalue=True, offvalue=False)
        self.IgG.pack(fill='x')
        
        #bottomframe
        self.bottomframe = ttk.Frame(self, padding=(32, 32, 32, 32), borderwidth=5, relief='groove',)
        self.bottomframe.pack( pady=(10, 10), side='bottom')
        # label
        self.label = ttk.Label(self.bottomframe, text="Identifikasi Jenis Hepatitis", justify='left')
        self.label.pack()

        # button
        self.button = ttk.Button(self.bottomframe, text='Cari tahu')
        self.button['command'] = self.button_clicked
        self.button.pack(padx=10, pady=10)

    def button_clicked(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')
    
    def age_slider_changed(self, value):
        self.ageinfo['text'] = str(int(float(value)))


if __name__ == "__main__":
    app = App()
    app.mainloop()