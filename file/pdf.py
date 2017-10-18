from __future__ import print_function, division, unicode_literals

# ==============================================================================
#                                                                 PDF2SPLIT_HTML
# ==============================================================================
import wand.image
import os
def pdf2split_html(pdf, saveto, left=0, right=0, top=0, bottom=0, res=100):
    """ Given a filepath to a pdf document that has two columns of text,
        and a (preferably not yet created or empty) directory to save
        the output files to, it does the following:

        - Creates the output directory
        - Splits all the pages in the original pdf document in half, and
          creates the left and right images for all pages.
        - creates an html file (index.html), which embeds all the columns one
          on top of the other in a continuous document.
    """
    print("- Opening pdf file: ", pdf)
    with(wand.image.Image(filename=pdf, resolution=res)) as document:
        print("- getting pages")
        pages=document.sequence
        n_pages=len(pages)
        width, height, _, _ = pages[0].page
        mid = width//2
        html = []

        print("- creating output dir")
        if not os.path.exists(saveto):
            os.makedirs(saveto)

        print("- splitting pages")
        for i, page in enumerate(pages):
            left_side = page[left:mid, top:height-bottom]
            right_side = page[mid:width-right, top:height-bottom]
            left_side.save(filename=os.path.join(saveto, "{:03d}_a.jpg".format(i)))
            right_side.save(filename=os.path.join(saveto, "{:03d}_b.jpg".format(i)))

            # Append these two images to the html page
            html.append("<img src='{0:03d}_a.jpg'/><br><img src='{0:03d}_b.jpg'/><br>".format(i))

        print("- creating html page")
        with open(os.path.join(saveto, "index.html"), mode = "w") as textFile:
            html = "\n".join(html)
            textFile.write(html)
        print("- DONE!")
