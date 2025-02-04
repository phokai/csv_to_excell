import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl

def csv_to_excel(csv_file, excel_file):
    """CSV dosyasını Excel formatına dönüştürür."""
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(excel_file, index=False)
        messagebox.showinfo("Başarılı", f"CSV dosyası başarıyla Excel formatına dönüştürüldü: {excel_file}")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def excel_to_csv(excel_file, csv_file):
    """Excel dosyasını CSV formatına dönüştürür."""
    try:
        df = pd.read_excel(excel_file)
        df.to_csv(csv_file, index=False, encoding='utf-8')
        messagebox.showinfo("Başarılı", f"Excel dosyası başarıyla CSV formatına dönüştürüldü: {csv_file}")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def select_file(file_type):
    filetypes = [('CSV files', '*.csv')] if file_type == 'csv' else [('Excel files', '*.xlsx')]
    file = filedialog.askopenfilename(filetypes=filetypes)
    return file

def convert_csv_to_excel():
    csv_file = select_file('csv')
    if csv_file:
        excel_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if excel_file:
            csv_to_excel(csv_file, excel_file)

def convert_excel_to_csv():
    excel_file = select_file('excel')
    if excel_file:
        csv_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if csv_file:
            excel_to_csv(excel_file, csv_file)

def main():
    root = tk.Tk()
    root.title("CSV ↔ Excel Dönüştürücü")
    root.geometry("300x200")  # Pencere boyutunu ayarla
    
    tk.Button(root, text="CSV'den Excel'e Dönüştür", command=convert_csv_to_excel).pack(pady=10)
    tk.Button(root, text="Excel'den CSV'ye Dönüştür", command=convert_excel_to_csv).pack(pady=10)
    tk.Button(root, text="Çıkış", command=root.quit).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()