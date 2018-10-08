import cgi, os
import cgitb 

cgitb.enable()
  
print("Content-Type: text/html")    	# HTML is following
print()       

print("<h1> Welcome to Image URL Uploader </h1>") 

  
form = cgi.FieldStorage() 


print("<form method='post' action='save.py'>") 
print("<p>Image Title: <input type='text' name='title' /></p>") 
print("<p>Image URL: <input type='text' name='Url' /></p>") 
print("<p>Year: <input type='text' name='year' /></p>") 
print("<p>Artist: <input type='text' name='artist' /></p>") 
print("Description: <br> <textarea name='details' cols='40' rows='4'></textarea> <br>")
print("<input type = 'submit' value = 'Submit' />")
print("</form") 




