def img2pdf(images, output, orientation="P", units="cm", size=(10, 15)):
    from fpdf import FPDF

    # Initialize PDF document
    pdf = FPDF(orientation = orientation,
               unit = units,
               format = size)

    # Margin around image
    pdf.set_margins(left=0.0, top=0.0, right=0.0)

    # prevent the full page images trigering a new page break
    pdf.set_auto_page_break(auto=False, margin = 0.0)

    # Use each image as a page
    for image in images:
        pdf.add_page(orientation = orientation)
        pdf.image(image, x=None, y=None, w=size[0], h=size[1])

    # Save the pdf doc
    pdf.output(name = output)
    print "Created PDF document: {}".format(output)


