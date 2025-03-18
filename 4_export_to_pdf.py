import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load Excel file
excel_path = "sty.xlsx"
df = pd.read_excel(excel_path)

# Define PDF output
pdf_path = "styled_data.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

# Write Data to PDF
c.setFont("Helvetica", 10)
y = height - 40  # Starting position

for i, row in df.iterrows():
    row_text = " | ".join(str(x) for x in row.values)
    c.drawString(40, y, row_text)
    y -= 20
    if y < 40:  # Move to next page if needed
        c.showPage()
        c.setFont("Helvetica", 10)
        y = height - 40

c.save()
print(f"✅ Excel converted to PDF: {pdf_path}")
