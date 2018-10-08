import cgi, os
import cgitb
cgitb.enable()
  
print("Content-Type: text/html")    	# HTML is following
print()       


print("<h1>Image URL Archive</h1>") 
# Using the inbuilt methods 
  
form = cgi.FieldStorage() 

if form.getvalue("title"):
	title = form.getvalue("title") 
	print(title + "<br>")
else:
	print("<p>Title Missing</p>")

if form.getvalue("Url"):
	url = form.getvalue("Url")
	print(url + "<br>")
	print("<image src = "+url+">") 
	
else:
	print("<p>Url Missing</p>")
	
if form.getvalue("year"):
    year = form.getvalue("year") 
    print("<br>" + year + "<br>")
else:
	print("<p>Year Missing</p>")

if form.getvalue("artist"):
    artist = form.getvalue("artist") 
    print(artist + "<br>")
else:
	print("<p>Artist Missing</p>")

if form.getvalue("details"):
    details = form.getvalue("details") 
    print(details + "<br>")
else:
	print("<p>Description Missing</p>")
	
