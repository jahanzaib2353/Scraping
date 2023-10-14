import tkinter as tk
from tkinter import Entry, Button, Label
import urllib.request
from bs4 import BeautifulSoup

def scrape_and_display():
    url = entry.get()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('img')
    
    result_text.delete(1.0, tk.END)  # Clear previous results
    for tag in tags:
        result_text.insert(tk.END, tag.get('src', None) + '\n')

# Create the main window
root = tk.Tk()
root.title("Web Scraping Tool")

# Create and place widgets
label = Label(root, text="Enter URL:")
label.pack(pady=10)

entry = Entry(root, width=50)
entry.pack()

scrape_button = Button(root, text="Scrape", command=scrape_and_display)
scrape_button.pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Start the Tkinter main loop
root.mainloop()
