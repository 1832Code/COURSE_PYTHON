from barcode import EAN13
from barcode.writer import ImageWriter

valor_numerico = "590123412345"
bar_code = EAN13(valor_numerico, writer=ImageWriter())
bar_code.save("codigodebarras")