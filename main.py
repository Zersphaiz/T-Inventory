from InventoryApp import InventoryApp
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import os
import datetime
import gevent
import bottle
import geventwebsocket
from PIL import Image, ImageTk

"""if __name__ == "__main__":
    # Step 1: Read the Excel file and load the data into a DataFrame
    file_path = 'rows.xlsx'  # Replace with the actual file path
    sheet_name = 'MainCategory'  # Replace with the name of the sheet you want to read

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        data_array = df.to_numpy()

        if data_array.size == 0:
            print("The Excel sheet is empty.")
        else:
            # Step 2: Print the data_array using a nested loop
            for row in data_array:
                for element in row:
                    print(element, end=' ')
                print()  # Move to the next line after printing each row

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")"""

app = InventoryApp()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()
