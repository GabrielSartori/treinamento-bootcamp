import jinja2

template_string = """

Olá {{nome}}

Sua senha 

{{link }}

"""

template = jinja2.Template(template_string)
rendered_template = template.rende({"nome": "Gabriel", "link": "htttptppt")