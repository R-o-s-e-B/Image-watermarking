from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image
from PIL import ImageTk, ImageDraw, ImageFont
from matplotlib import colors

filename = ''
s = Tk()
s.configure(bg="#213555")
s.title("Watermarking software")
s.geometry('1000x600')
Font_size = 100
save_n = False

def text():
    watermark_text = entry.get()
    return watermark_text

def color_change():
    color_val = color_entry.get()
    return color_val

def opacity_ch():
    opacity_val = slider.get()
    return opacity_val
def rotate_an():
    angle = rotator.get()
    return angle

def size_increase():
    global Font_size
    Font_size += 1
    return Font_size
def size_decrease():
    global Font_size
    Font_size -= 1
    return Font_size

def upload_file():
    global img
    global filename
    f_types = [('Jpg Files', '*.jpg'), ('png', '.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((700, 600))
    img = ImageTk.PhotoImage(img_resized)
    canvas.create_image(0,0, anchor=NW, image=img)

def main():
    global img
    text_n = text()

    opacity = opacity_ch()
    color = colors.to_rgba(color_change())

    color_list = [color[0], color[1], color[2], round(opacity, 2)]
    color_tup = (int(color_list[0] * 255), int(color_list[1] * 255),  int(color_list[2] * 255), int(color_list[3] * 255))
    print(color_tup)
    rotate_angle = int(rotate_an())
    print(rotate_angle)
    img_open = Image.open(filename).convert('RGBA')
    font = ImageFont.truetype("arial.ttf", Font_size)

    img_resized = img_open.resize((700, 600))

    mark_width, mark_height = font.getsize(text_n)
    watermark = Image.new('RGBA', (mark_width, mark_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    draw.text((0, 0), text=text_n, font=font, fill=color_tup)
    watermark = watermark.rotate(rotate_angle, expand=True)
    img_resized.paste(watermark, (200, 200), watermark)

    img = ImageTk.PhotoImage(img_resized)
    canvas.create_image(0, 0, anchor=NW, image=img)
    if save_n:
        img_resized.show()

def save():
    global save_n
    save_n = True
    main()

canvas = Canvas(width=680, height=580, bg='#213555', highlightthickness=0)
canvas.grid(pady=(10, 10), padx=(10, 10), row=0, column=0, rowspan=12, columnspan=4)

start = Button(s, text="Upload image", command=lambda : upload_file(), bg='#c8c4b6')
start.place(x=10, y=10)

properties = Canvas(width=288, height=580, bg='#4F709C', highlightthickness=0)
properties.grid(pady=(10, 10), padx=(0, 20), row=0, column=6, rowspan=12)

enter_text = Label(s, text="Enter text:", bg="#4F709C",  fg='#F5EFE7', font=('Helvetica 12'))
enter_text.grid(row=0, column=6, pady=(20, 0))
entry = Entry(s, width=30, bg='#F5EFE7')

entry.grid(row=1, column=6)

font_size = Label(s, text=f"Font size", bg="#4F709C",  fg='#F5EFE7', font=('Helvetica 12'), justify='left')
font_size.grid(row=2, column=6)
minus = Button(s, text='+', command=lambda :size_increase(), bg='#D8C4B6')
minus.place(x=900, y=150)
plus = Button(s, text='-', command=lambda :size_decrease(), bg='#D8C4B6')
plus.place(x=790, y=150)

color = Label(s, text="color:", bg="#4F709C", fg='#F5EFE7', font=('Helvetica 12'))
color.grid(row=3, column=6)

color_entry = Entry(s, bg='#F5EFE7')
color_entry.grid(row=4, column=6)

slider = ttk.Scale(
    s,
    from_=0.0,
    to=1.0,
    orient='horizontal', # horizontal
    length=120,
)

opacity = Label(s, text="opacity:", bg="#4F709C", fg='#F5EFE7', font=('Helvetica 12'))
opacity.grid(row=5, column=6)

slider.grid(row=6, column=6)

rotator = ttk.Scale(
    s,
    from_=0,
    to=360,
    orient='horizontal',
    length=120,
)

rotate = Label(s, text="Rotate:", bg="#4F709C", font=('Helvetica 12'), fg="#F5EFE7")
rotate.grid(row=7, column=6)

rotator.grid(row=8, column=6)

preview = Button(s, text="Preview", command=lambda:main(), bg='#D8C4B6')
preview.place(x=800, y=520)

save_now = Button(s, text="Save", command=lambda:save(), bg='#D8C4B6')
save_now.place(x=870, y=520)


s.mainloop()
