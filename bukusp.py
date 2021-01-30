import buku
output = """<!DOCTYPE html><html> 
<head>
	<title>Buku</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glider-js@1/glider.min.css">
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
"""
list = {}
for rec in buku.BukuDb().get_rec_all() :
	tags = rec[3].split(',')
	for tag in tags :
		if tag == '' :
			continue
		if not tag in list :
			list[tag] = []
		list[tag].append({'title' : rec[2], 'link': rec[1], 'comment' : rec[4]})

for tag, bookmarks in list.items() :
	output += "<div class=\"glider-contain mutliple\">"
	output += f"<h3>{tag}</h3>"
	output += f"<div class=\"glider\" id=\"{tag}\">"
	for item in bookmarks:
		output += f"<div><a href=\"{item['link']}\">{item['title']}</a>"
		if item["comment"] != "" :
			output += f"<p>>> {item['comment']} </p>"
		output += "</div>"
	output += "</div>"
	output += f"<button aria-label=\"Previous\" class=\"glider-prev\" id=\"button-prev-{tag}\"></button>"
	output += f"<button aria-label=\"Next\" class=\"glider-next\" id=\"button-next-{tag}\"></button>"
	output += f"<div id=\"dots-{tag}\"></div>"
	output += "</div>"
output += r"""
	<script src="https://cdn.jsdelivr.net/npm/glider-js@1/glider.min.js"></script>
	<script src="glider-settings.js"></script>
</body>
</html>"""
with open("website/home.html", "w") as file :
	file.write(output)