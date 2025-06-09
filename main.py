"""
Main entry point for Virtual Lottery application
"""
import tkinter as tk
import traceback
import sys
from modules.gui.main_window import MainWindow

def main():
    """Initialize and run the application"""
    try:
        root = tk.Tk()
        root.title("Lotería Virtual - El Hueso")
        root.geometry("700x900")  # Vertical format
        root.configure(bg='#F8F9FA')
        
        # Set theme
        root.tk.call('source', 'azure.tcl')
        root.tk.call('set_theme', 'dark')
        
        MainWindow(root)
        
        root.mainloop()
    except Exception as e:
        print(f"Error: {str(e)}")
        print(traceback.format_exc())
        sys.exit(1)

# Llamado de funcion __main__
if __name__ == "__main__":
    main() 