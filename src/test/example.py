import math2docx
from docx import Document

document = Document()
p = document.add_paragraph()

#LaTex Math Formula
latex_ = r"\cos (2\theta) = \cos^2 \theta - \sin^2 \theta"

math2docx.add_math(p, latex_ )
document.save("new_file.docx")
