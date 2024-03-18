#!/usr/bin/env python3
#######generate a PDF file to send to the supplier, indicating that the data was correctly processed
import reportlab
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
from datetime import date
x=date.today()

def generate(filename, title,pdfdata):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
  #  table_data=pdfdata
    
#  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
        #!/usr/bin/env python3
#report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    contents=[report_title]
    contents.append(Spacer(1,20))
    for element in pdfdata:
        for element1 in element:
            item_style=styles["BodyText"]
            item=Paragraph(f'{element1}',item_style)
            contents.append(item)
        contents.append(Spacer(1,20))
  #  empty_line=Spacer(1,20)
    report.build(contents)

generate('.//OneDrive//Desktop//report.pdf',f'Processed Update on {x.strftime("%b %d, %Y")}',pdfdata)

