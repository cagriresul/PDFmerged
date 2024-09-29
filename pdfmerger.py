from pypdf  import PdfWriter

merger = PdfWriter()


for pdf in ['''PDF_NAME''' , '''PDF_NAME2''' ]
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

