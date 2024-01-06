import tkinter as tk
from tkinter import ttk
from autoscraper import AutoScraper
import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    url = url_entry.get()
    desired_price = float(price_entry.get())
    email_id = email_entry.get()

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText()
    price = soup.find('span', {'class': 'a-price-whole'}).getText()

    price1 = price.replace(",", "")
    new_price = float(price1)

    result_label.config(text=f"Product Title: {title.strip()}\nCurrent Price: {new_price}")

    if new_price <= desired_price:
        send_mail(email_id, url)
    else:
        root.after(10000, check_price)

def send_mail(email, product_url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("minorproject1sem5@gmail.com", "zanujsksnuqgnkou")
    subject = "Hey! The current price is below your desired price"
    body = "Check the link given below:"

    msg = f"subject:{subject}\n\n{body}\n{product_url}"
    server.sendmail("minorproject1sem5@gmail.com", email, msg)

    print("email sent")

    server.quit()

# GUI Setup
root = tk.Tk()
root.title("Price Tracker")

url_label = ttk.Label(root, text="Enter your product's URL:")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=10)

price_label = ttk.Label(root, text="Enter your desired price:")
price_label.pack(pady=10)

price_entry = ttk.Entry(root, width=20)
price_entry.pack(pady=10)

email_label = ttk.Label(root, text="Enter your email ID:")
email_label.pack(pady=10)

email_entry = ttk.Entry(root, width=30)
email_entry.pack(pady=10)

check_button = ttk.Button(root, text="Check Price", command=check_price)
check_button.pack(pady=20)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()