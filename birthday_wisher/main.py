
import datetime as dt
import smtplib
import pandas

now=dt.datetime.now()
current_day=now.day
current_month=now.month
my_email="aman.sharma617c@gmail.com"
my_password="yzzdzgrlftisfxlz"

with open("birthdays.csv") as data:
    birthday_data=pandas.read_csv(data)
    for index,row in birthday_data.iterrows():
        if row["day"]==current_day and row["month"]== current_month:
            with open(f"../birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt") as letter:
                lines = letter.read()
                lines = lines.replace("[NAME]", row["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(
                    from_addr=my_email, to_addrs="aman.sharma617a@yahoo.com",msg=f"Subject:Happy Birthday!!\n\n {lines}")






