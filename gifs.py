import tkinter as tk
from PIL import Image

root = tk.Tk()
file="gif_file.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
photoimage_objects = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
loop = None
def animation(count):
    global loop
    image = photoimage_objects[count]

    gif_label.configure(image=image)
    count += 1
    if count == frames:
        count = 0
    loop = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(loop)

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="start",command=lambda :animation(count))
start.pack()

stop = tk.Button(root,text="stop",command=stop_animation)
stop.pack()

root.mainloop()
