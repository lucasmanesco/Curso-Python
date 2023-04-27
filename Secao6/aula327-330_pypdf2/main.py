# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feitat em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como anotações, transformar páginas,
# extrair texto e imagens, manipular metadados e mais.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
REL_BACEN = PASTA_ORIGINAIS / 'R20230420.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(REL_BACEN)

page1 = reader.pages[0]
page2 = reader.pages[1]

# tamanho do PDF:
print(len(reader.pages))

# extrair texto
print(page1.extract_text())

# extrair imagem
img0 = page1.images[0]
with open(PASTA_NOVA/img0.name, 'wb') as fp:
    fp.write(img0.data)

# extrair página
writer = PdfWriter()
writer.add_page(page1)
with open(PASTA_NOVA / 'page1.pdf', 'wb') as file:
    writer.write(file)

# unir páginas com Writer
writer = PdfWriter()
with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as file:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(file)

# separar todas as páginas do pdf
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as file:
        writer.add_page(page)
        writer.write(file)

# unir páginas com Merger
files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf',
]
merger = PdfMerger()
for file in files:  # type: ignore
    merger.append(file)
merger.write(PASTA_NOVA / 'merged.pdf')  # recomenda-se usar context manager
merger.close()
