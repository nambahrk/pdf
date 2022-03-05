from pathlib import Path
import PyPDF2
import os
import glob  #これで一括取得

#同階層内のPDFファイル一覧
pdffiles = sorted(glob.glob("*.pdf"))

#１つのPDFファイルにまとめる
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdffiles:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))

#保存
with open("merged.pdf", "wb") as f:
    pdf_writer.write(f)
