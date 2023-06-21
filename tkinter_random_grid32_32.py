import tkinter as tk 
import random  
 # Create the tkinter window 
root = tk.Tk() 
root.title("32x32 Grid")  

# Define the size of the grid 
GRID_SIZE = 32  

# Define the size of the cells 
CELL_SIZE = 20  

# Define a list to hold the labels for the columns 
labels = []  

# Define a list to hold the entry widgets for the grid 
entries = []  

# Create a nested loop to create the grid 
for i in range(GRID_SIZE):     
    
    # Create a list to hold the entry widgets for each row     
    row = []     
    for j in range(GRID_SIZE):         
        # Determine if the cell should be black or white         
        if random.randint(0, 1) == 0:             
            color = "black"         
        else:             
            color = "white"         
            # Create the entry widget         
            entry = tk.Entry(root, width=2, bg=color, justify="center", font=("Arial", 12))         
            entry.grid(row=i+1, column=j+1, padx=1, pady=1)       
            
            # Add the entry widget to the row list         
            row.append(entry)     
            
            # Add the row list to the entries list     
            entries.append(row)  
            
# Create the column labels 
for i in range(GRID_SIZE):     
    label = tk.Label(root, text=str(i+1), width=2, bg="white", font=("Arial", 8))     
    label.grid(row=0, column=i+1, padx=1, pady=1)     
    labels.append(label)  
                
# Create the row labels 
for i in range(GRID_SIZE):     
    label = tk.Label(root, text=str(i+1), width=2, bg="white", font=("Arial", 8))     
    label.grid(row=i+1, column=0, padx=1, pady=1)     
    labels.append(label)  
                    
# Start the tkinter event loop 
root.mainloop() 