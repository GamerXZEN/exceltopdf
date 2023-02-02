import pandas as pd
import glob
from fpdf import FPDF as FP
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
	data = pd.read_excel(filepath, sheet_name="Sheet 1")
	pdf = FP(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	filename = Path(filepath).stem
	invoice_nr = filename.split("-")
	pdf.set_font(family="Helvetica", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr[0]}")
	pdf.output(f"pdfs/{filename}.pdf")
