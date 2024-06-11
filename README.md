# math2docx
Open source Python library converting math formula to docx

## How to install?
```bash
pip install math2docx
```
## Example
```bash
import math2docx
from docx import Document

document = Document()
p = document.add_paragraph()

#LaTex Math Formula
latex_ = r"\cos (2\theta) = \cos^2 \theta - \sin^2 \theta"

math2docx.add_math(p, latex_ )
document.save("new_file.docx")

```
[About of LaTex Math Formula Format](https://ru.wikibooks.org/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B_%D0%B2_LaTeX)

## Results
![enter image description here](https://i.ibb.co/LzZRCBh/img1.png)





