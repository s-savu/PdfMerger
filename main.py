import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

selected_pdf_files = []


def add_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        selected_pdf_files.append(file_path)
        pdf_listbox.insert(tk.END, os.path.basename(file_path))
        pdf_listbox.itemconfig(tk.END, {'bg': 'light-gray', 'fg': 'black'})


def remove_pdf():
    selected_indices = pdf_listbox.curselection()
    for index in selected_indices:
        selected_pdf_files.pop(index)
        pdf_listbox.delete(index)


def merge_pdfs():
    if not selected_pdf_files:
        result_label.config(text="Select at least one PDF file to merge.", fg="red")
        return

    merger = PyPDF2.PdfMerger()

    for pdf_file in selected_pdf_files:
        merger.append(pdf_file)

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

    if save_path:
        merger.write(save_path)
        merger.close()
        result_label.config(text=f"PDF files have been merged and saved to:\n{save_path}", fg="green")


app = tk.Tk()
app.title("PDF Merger")

app.geometry("500x400")
app.configure(bg="#333")

title_label = tk.Label(app, text="PDF Merger", font=("Helvetica", 24), bg="#333", fg="white")
title_label.pack(pady=10)

pdf_frame = tk.Frame(app, bg="#333")
pdf_frame.pack()

style = ttk.Style()
style.configure("PDF.TListbox", background="#333", foreground="grey", selectbackground="grey",
                selectforeground="black")
pdf_listbox = tk.Listbox(pdf_frame, selectmode=tk.MULTIPLE, font=("Arial", 12), bg="#333", fg="white",
                         selectbackground="red", selectforeground="black", relief=tk.FLAT)
pdf_listbox.pack(side=tk.LEFT, padx=10, pady=10)

add_button = tk.Button(pdf_frame, text="Add PDF", command=add_pdf, bg="grey", fg="white", font=("Arial", 12))
remove_button = tk.Button(pdf_frame, text="Remove Selected", command=remove_pdf, bg="grey", fg="white",
                          font=("Arial", 12))
add_button.pack(side=tk.LEFT, padx=10)
remove_button.pack(side=tk.LEFT, padx=10)

merge_button = tk.Button(app, text="Merge Selected PDFs", command=merge_pdfs, bg="grey", fg="white",
                         font=("Arial", 14), padx=20, pady=10)
merge_button.pack(pady=20)

result_label = tk.Label(app, text="", font=("Arial", 12, "italic"), bg="#333", fg="green")
result_label.pack()

app.mainloop()
