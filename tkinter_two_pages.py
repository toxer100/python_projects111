import tkinter as tk   
 
class App(tk.Tk):     
    def __init__(self):         
        super().__init__()           
        
        # Create the first frame         
        self.frame1 = tk.Frame(self)
        # Add widgets to frame1         
        tk.Label(self.frame1, text='Welcome to Page 1', font=('Arial', 20)).pack(pady=10)         
        tk.Button(self.frame1, text='Go to Page 2', command=self.show_frame2).pack()
        
        
        # Create the second frame         
        self.frame2 = tk.Frame(self) 
        
        # Add widgets to frame2         
        tk.Label(self.frame2, text='Welcome to Page 2', font=('Arial', 20)).pack(pady=10)         
        tk.Button(self.frame2, text='Go to Page 1', command=self.show_frame1).pack()  
        
        # Show the first frame
        self.show_frame1()
                       
    def show_frame1(self):
        self.frame2.pack_forget()         
        self.frame1.pack(fill='both', expand=True)
        
    def show_frame2(self):         
        self.frame1.pack_forget()         
        self.frame2.pack(fill='both', expand=True)

        
        
if __name__ == '__main__':     
    app = App()     
    app.mainloop() 
            