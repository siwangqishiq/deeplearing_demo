import tkinter as tk

def mainloop():
    print("run...")
    window = tk.Tk()

    label = tk.Label(text="你好世界" ,width=40 , height=20,background="white")
    label.pack()
    confirm_btn = tk.Button(text="点我")
    confirm_btn.pack()
    window.mainloop()

if __name__ == "__main__":
    mainloop()