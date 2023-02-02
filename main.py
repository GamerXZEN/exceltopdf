import pandas as pd
import glob
from fpdf import FPDF as FP
from pathlib import Path

from pandas import Series

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
	data = pd.read_excel(filepath, sheet_name="Sheet 1")
	datal = [dfa.replace("_", " ").title() for dfa in list(data.columns)]

	pdf = FP(orientation="P", unit="mm", format="A4")
	pdf.add_page()

	filename = Path(filepath).stem
	invoice_nr, date = filename.split("-")

	pdf.set_font(family="Helvetica", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

	pdf.set_font(family="Helvetica", size=15, style="B")
	pdf.cell(w=50, h=8, txt=f"Date:{date}", ln=1)

	pdf.set_font(family="Helvetica", style="B", size=10)
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=30, h=8, txt=str(datal[0]), border=1)
	pdf.cell(w=70, h=8, txt=str(datal[1]), border=1)
	pdf.cell(w=35, h=8, txt=str(datal[2]), border=1)
	pdf.cell(w=26, h=8, txt=str(datal[3]), border=1)
	pdf.cell(w=25, h=8, txt=str(datal[4]), border=1, ln=1)

	for index, row in data.iterrows():
		pdf.set_font(family="Helvetica", size=10)
		pdf.set_text_color(80, 80, 80)
		pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
		pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
		pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
		pdf.cell(w=26, h=8, txt=str(row["price_per_unit"]), border=1)
		pdf.cell(w=25, h=8, txt=str(row["total_price"]), border=1, ln=1)

	pdf.set_font(family="Times", style="B", size=13)
	pdf.set_text_color(0, 0, 0)
	pdf.ln(13)
	pdf.cell(w=0, h=12, txt=f"The total amount due is {data['total_price'].sum()} dollars", ln=1)
	pdf.cell(w=25, h=12, txt="PythonHow")
	pdf.image("pythonhow.png", w=10)

	pdf.output(f"pdfs/{filename}.pdf")
