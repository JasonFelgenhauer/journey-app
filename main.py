from tkinter import *
import time
import datetime
from plyer import notification

class JourneyApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Journey App")
        self.root.geometry("400x400")
        self.root.minsize(400, 400)
        self.root.maxsize(800, 800)
        self.root.config(bg='#2B4579')
        self.is_counter_running = False
        self.remaining_time = "08:00:00"

        self.frame = Frame(self.root, bg='#2B4579')
        self.frame.pack(fill=BOTH, expand=True)

        self.clock = Label(self.frame, text='23:45:20', font=('Arial', 20, 'bold'), fg='#EC8218', bg='#13293D', pady=20)
        self.clock.pack(side=TOP, fill=X)

        self.start_journey_btn = Button(self.frame, command=self.start_journey, text='Start Journey', font=('Arial', 20, 'bold'), fg='#EC8218', bg='#13293D', pady=20, padx=10, bd=0, activebackground='#EC8218', activeforeground='#13293D')
        self.start_journey_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.footer = Label(self.frame, text='© {} - Journey App By Mr__Wigy'.format(datetime.date.today().strftime('%Y')), font=('Arial', 10, 'bold'), fg='#EC8218', bg='#13293D', pady=20)
        self.footer.pack(side=BOTTOM, fill=X)

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def update_counter(self):
        if self.is_counter_running:
            if self.remaining_time == "00:00:00":
                self.counter.config(text="Journée terminée !")
                notification.notify(
                    title="Journey App",
                    message="Tu as fini ta journée, rentre chez toi !",
                    app_icon=None,
                    timeout=10
                )
                self.is_counter_running = False
                self.pause_resume_btn.config(state=DISABLED)
            else:
                remaining_seconds = int(self.remaining_time.split(":")[2])
                remaining_minutes = int(self.remaining_time.split(":")[1])
                remaining_hours = int(self.remaining_time.split(":")[0])

                if remaining_seconds > 0:
                    remaining_seconds -= 1
                elif remaining_minutes > 0:
                    remaining_minutes -= 1
                    remaining_seconds = 59
                elif remaining_hours > 0:
                    remaining_hours -= 1
                    remaining_minutes = 59
                    remaining_seconds = 59

                self.remaining_time = "{:02d}:{:02d}:{:02d}".format(remaining_hours, remaining_minutes, remaining_seconds)
                self.counter.config(text=self.remaining_time)
                self.root.after(1000, self.update_counter)

    def start_journey(self):
        self.start_journey_btn.place_forget()
        self.clock.pack_forget()

        self.counter = Label(self.frame, text=self.remaining_time, font=('Arial', 20, 'bold'), fg='#EC8218', bg='#13293D', pady=20)
        self.counter.pack(side=TOP, fill=X)

        self.pause_resume_btn = Button(self.frame, command=self.pause_resume_counter, text='Pause', font=('Arial', 20, 'bold'), fg='#EC8218', bg='#13293D', pady=20, padx=10, bd=0, activebackground='#EC8218', activeforeground='#13293D')
        self.pause_resume_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.is_counter_running = True
        self.update_counter()

    def pause_resume_counter(self):
        if self.is_counter_running:
            self.is_counter_running = False
            self.pause_resume_btn.config(text="Resume")
        else:
            self.is_counter_running = True
            self.pause_resume_btn.config(text="Pause")
            self.update_counter()

    def run(self):
        self.update_clock()
        self.root.mainloop()

if __name__ == '__main__':
    app = JourneyApp()
    app.run()
