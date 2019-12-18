#!/usr/bin/env python3
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "Not specified")
text2 = form.getfirst("TEXT_2", "Not specified")
text1 = html.escape(text1)
text2 = html.escape(text2)

if form.getvalue("phone"):
    checkbox_1 = "ON"
else:
    checkbox_1 = "OFF"

if form.getvalue("laptop"):
    checkbox_2 = "ON"
else:
    checkbox_2 = "OFF"

if form.getvalue("color"):
    number = form.getvalue("color")
else:
    number = "Not selected"



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("<p>phone: {}</p>".format(checkbox_1))
print("<p>laptop: {}</p>".format(checkbox_2))
print("<p>color: {}</p>".format(number))

print("""</body>
        </html>""")

