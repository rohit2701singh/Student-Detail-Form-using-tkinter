from tkinter import *
from tkinter import messagebox
import pandas

FONT = ("times new roman", 13)
DATA_FONT = ("ariel", 11)


def submit_application():
    if not name_entry.get() or not guardian_entry.get() or course_state.get() not in course_option or \
            not phone_entry.get() or not email_entry.get() or not city_entry.get() or not checked_state.get():

        messagebox.showwarning(title="OOPS", message="all details should be filled before submission.")
    else:
        application = {
            "name": [name_entry.get()],
            "guardian_name": [guardian_entry.get()],
            "gender": [gender[gender_state.get() - 1]],
            "course": [course_state.get()],
            "phone_no.": [phone_entry.get()],
            "email_id": [email_entry.get()],
            "city_name": [city_entry.get()],
        }
        try:
            df = pandas.read_csv("candidate_data.csv")
        except (FileNotFoundError, pandas.errors.EmptyDataError):
            df = pandas.DataFrame(columns=['name', 'guardian_name', 'gender', 'course', 'phone_no', 'email_id', 'city_name'])
            df.to_csv("candidate_data.csv", index=False)

        applicant_data = pandas.DataFrame(application)
        applicant_data.to_csv("candidate_data.csv", index=False, mode="a", header=False)

        name_entry.delete(0, END)
        name_entry.focus()
        guardian_entry.delete(0, END)
        course_state.set("select category")
        gender_state.set(0)  # Set the value to 0 to deselect all Radiobutton
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        city_entry.delete(0, END)
        confirm_checkbox.deselect()


# create UI
window = Tk()
window.title("Exam Registration Form")
window.config(padx=40, pady=40, bg='#acc2d9')


# creating labels
data = pandas.read_csv("label_position_details.csv")
for i in range(len(data.label_name)):
    label_name = data.label_name[i]
    column_num = data.column[i]
    row_num = data.row[i]
    create_label = Label(text=label_name, bg='#acc2d9', font=FONT)
    create_label.grid(pady=8, padx=5, column=column_num, row=row_num)

heading_label = Label(text="Student Course Details", bg='#acc2d9', font=('times new roman', 20, "bold"))
heading_label.grid(pady=10, column=0, row=0, columnspan=2, sticky="W")

candidate_label = Label(text="Candidate info.", bg='#acc2d9', font=("times new roman", 15, "bold"), justify="left")
candidate_label.grid(pady=8, column=0, row=1, columnspan=2, sticky="W")

contact_label = Label(text="Contact info.", bg='#acc2d9', font=("times new roman", 15, "bold"), justify="left")
contact_label.grid(pady=8, column=0, row=6, columnspan=2, sticky="W")


# creating entry widget
name_entry = Entry(font=DATA_FONT, width=35)
name_entry.focus()
name_entry.grid(column=1, row=2, columnspan=2)

guardian_entry = Entry(font=DATA_FONT, width=35)
guardian_entry.grid(column=1, row=3, columnspan=2)

phone_entry = Entry(font=DATA_FONT, width=35)
phone_entry.grid(column=1, row=7, columnspan=2, sticky="W")

email_entry = Entry(font=DATA_FONT, width=35)
email_entry.grid(column=1, row=8, columnspan=2)

city_entry = Entry(font=DATA_FONT, width=35)
city_entry.grid(column=1, row=9, sticky="W", columnspan=2)


# radio buttons
gender_state = IntVar()
gender = ["male", "female"]
gender_button1 = Radiobutton(text="male", value=1, variable=gender_state, font=FONT)
gender_button2 = Radiobutton(text="female", value=2, variable=gender_state, font=FONT)
gender_button1.grid(column=1, row=4)
gender_button2.grid(column=2, row=4)

# option buttons
course_option = ["Python", "Web Development", "Data Science", "Machine Learning", "AI"]
course_state = StringVar()
course_state.set("select course")
course = OptionMenu(window, course_state, *course_option)
course.config(width=15, font=FONT)
course.grid(column=1, row=5)

# checkbox button
checked_state = IntVar()
confirm_checkbox = Checkbutton(text="I'm ready to submit the application.", bg='#acc2d9', variable=checked_state)
confirm_checkbox.config(font=FONT)
confirm_checkbox.grid(pady=8, padx=5, column=0, row=10, columnspan=2, sticky="W")

# submit button
submit_button = Button(text="Submit", width=10, font=FONT, command=submit_application)
submit_button.grid(column=2, row=11)

window.mainloop()
