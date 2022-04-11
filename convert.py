from fpdf import FPDF
import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image

def convert(list_of_images):
    pdf = FPDF()
    for image in list_of_images:
        cover = Image.open(image)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        # given we are working with A4 format size 
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

        orientation = 'P' if width < height else 'L'

         #  make sure image size is not greater than the pdf format size
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

        pdf.add_page(orientation=orientation)
        pdf.image(image, 0, 0, width, height)

    pdf.output("output.pdf", "F")

window = tk.Tk()

files = fd.askopenfilenames(parent=window, title='Choose a file')
convert(files)