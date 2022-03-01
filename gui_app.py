import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from clips import Environment
import os

env = Environment()

def evaluate_condition(condition:bool,command:str):
    if condition:
        env.eval(command)
        print("Command executed: " + command)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.age = 0

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
        self.is_bad_sanitation = tk.BooleanVar(value=False)
        self.bad_sanitation = ttk.Checkbutton(self.leftconditionframe, text='Sanitasi Buruk', variable=self.is_bad_sanitation, onvalue=True, offvalue=False)
        self.bad_sanitation.pack(fill='x')
        self.is_tropical = tk.BooleanVar(value=False)
        self.tropical = ttk.Checkbutton(self.leftconditionframe, text='Tinggal di Daerah tropis', variable=self.is_tropical, onvalue=True, offvalue=False)
        self.tropical.pack(fill='x')
        self.is_asymptomatic = tk.BooleanVar(value=False)
        self.asymptomatic = ttk.Checkbutton(self.leftconditionframe, text='Tidak bergejala', variable=self.is_asymptomatic, onvalue=True, offvalue=False)
        self.asymptomatic.pack(fill='x')
        self.is_b_survivor = tk.BooleanVar(value=False)
        self.b_survivor = ttk.Checkbutton(self.leftconditionframe, text='Mantan pengidap Hepatitis B', variable=self.is_b_survivor, onvalue=True, offvalue=False)
        self.b_survivor.pack(fill='x')
        self.is_homosexual = tk.BooleanVar(value=False)
        self.homosexual = ttk.Checkbutton(self.leftconditionframe, text='Pernah berhubungan sesama jenis', variable=self.is_homosexual, onvalue=True, offvalue=False)
        self.homosexual.pack(fill='x')
        self.is_alcoholic = tk.BooleanVar(value=False)
        self.alcoholic = ttk.Checkbutton(self.leftconditionframe, text='Sering minum Alkohol', variable=self.is_alcoholic, onvalue=True, offvalue=False)
        self.alcoholic.pack(fill='x')
        self.is_hemodialisis = tk.BooleanVar(value=False)
        self.hemodialisis = ttk.Checkbutton(self.leftconditionframe, text='Rajin terapi Hemodialisis', variable=self.is_hemodialisis, onvalue=True, offvalue=False)
        self.hemodialisis.pack(fill='x')


        #BloodTest
        self.rightconditionframe = ttk.Frame(self.mainframe, borderwidth=5, relief='groove', )
        self.rightconditionframe.pack(side='left', padx=12)
        self.rightconditionlabel = ttk.Label(self.rightconditionframe, text='Kandungan di Darah', font=('Segoe UI', 12), padding=(10, 10, 10, 10), justify='left',)
        self.rightconditionlabel.pack(fill='x')
        self.is_antibody_hba = tk.BooleanVar(value=False)
        self.antibody_hba = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbA1c', variable=self.is_antibody_hba, onvalue=True, offvalue=False)
        self.antibody_hba.pack(fill='x')
        self.is_antibody_hbb = tk.BooleanVar(value=False)
        self.antibody_hbb = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbB', variable=self.is_antibody_hbb, onvalue=True, offvalue=False)
        self.antibody_hbb.pack(fill='x')
        self.is_antibody_hbc = tk.BooleanVar(value=False)
        self.antibody_hbc = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbC', variable=self.is_antibody_hbc, onvalue=True, offvalue=False)
        self.antibody_hbc.pack(fill='x')
        self.is_antibody_hbd = tk.BooleanVar(value=False)
        self.antibody_hbd = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbD', variable=self.is_antibody_hbd, onvalue=True, offvalue=False)
        self.antibody_hbd.pack(fill='x')
        self.is_antibody_hbe = tk.BooleanVar(value=False)
        self.antibody_hbe = ttk.Checkbutton(self.rightconditionframe, text='Antibody HbE', variable=self.is_antibody_hbe, onvalue=True, offvalue=False)
        self.antibody_hbe.pack(fill='x')
        self.is_alanine = tk.BooleanVar(value=False)
        self.alanine = ttk.Checkbutton(self.rightconditionframe, text='Alanin-Transaminase', variable=self.is_alanine, onvalue=True, offvalue=False)
        self.alanine.pack(fill='x')
        self.is_igG = tk.BooleanVar(value=False)
        self.IgG = ttk.Checkbutton(self.rightconditionframe, text='IgG', variable=self.is_igG, onvalue=True, offvalue=False)
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
        env.clear()
        env.load("./data/hepatitis.clp")
        env.eval('(assert (person (name "Pasien") (age %d)))'% self.age)
        env.eval('(assert (hepatitis_evidence_count))')
        evaluate_condition(self.is_bad_sanitation.get(), '(assert (has_condition bad_sanitation))')
        evaluate_condition(self.is_tropical.get(), '(assert (has_condition tropical))')
        evaluate_condition(self.is_asymptomatic.get(), '(assert (has_condition asymptomatic))')
        evaluate_condition(self.is_b_survivor.get(), '(assert (has_condition b_survivor))')
        evaluate_condition(self.is_homosexual.get(),'(assert (has_condition homosexual))')
        evaluate_condition(self.is_alcoholic.get(),'(assert (has_condition alcoholic))')
        evaluate_condition(self.is_hemodialisis.get(),'(assert (has_condition hemodialisis))')
        evaluate_condition(self.is_antibody_hba.get(),'(assert (blood_contain anti_hba))')
        evaluate_condition(self.is_antibody_hbb.get(),'(assert (blood_contain anti_hbb))')
        evaluate_condition(self.is_antibody_hbc.get(),'(assert (blood_contain anti_hbc))')
        evaluate_condition(self.is_antibody_hbd.get(),'(assert (blood_contain anti_hbd))')
        evaluate_condition(self.is_antibody_hbe.get(),'(assert (blood_contain anti_hbe))')
        evaluate_condition(self.is_alanine.get(),'(assert (blood_contain alanin))')
        evaluate_condition(self.is_igG.get(),'(assert (blood_contain igg))')
        env.run()
        result = ""
        message = ""
        for i in env.facts():
            result = str(i[0])

        if result == 'hepatitis_A':
            message = "Pasien ini diduga Hepatitis A"
        elif result == 'hepatitis_B':
            message = "Pasien ini diduga Hepatitis B"
        elif result == 'hepatitis_C':
            message = "Pasien ini diduga Hepatitis C"
        elif result == 'hepatitis_D':
            message = "Pasien ini diduga Hepatitis D"
        elif result == 'hepatitis_E':
            message = "Pasien ini diduga Hepatitis E"
        elif result == 'hepatitis_alcoholic':
            message = "Pasien ini diduga Hepatitis akibat efek samping alkohol"

        showinfo(title='Hasil Klasifikasi',
                 message=message)
    
    def age_slider_changed(self, value):
        self.ageinfo['text'] = str(int(float(value)))
        self.age = int(float(value))


if __name__ == "__main__":
    app = App()
    app.mainloop()
    dataPath = os.path.abspath(os.path.join(os.getcwd(), '.', 'data'))
    hepatitisPath = os.path.join(dataPath, 'hepatitis.clp')