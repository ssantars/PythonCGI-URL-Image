
import cgi, os
import cgitb 
cgitb.enable()

import pymysql.cursors

test = 1
# Connect to the database
connection = pymysql.connect(
	host='localhost',
	user='gallery',
	password='eecs118',
	port=3306,
	database='gallery')

cursor = connection.cursor()   

#Create TABLE 1
try:
	cursor.execute("CREATE TABLE artist (artist_id INT(11) NOT NULL AUTO_INCREMENT,name VARCHAR(45) DEFAULT NULL,birth_year int(11) DEFAULT NULL,country varchar(45) DEFAULT NULL,description varchar(45) DEFAULT NULL,PRIMARY KEY(artist_id))")
except pymysql.err.InternalError:
	print('Artist Table already exists')
#Create TABLE 2
try:
	cursor.execute("CREATE TABLE detail (detail_id INT(11) NOT NULL AUTO_INCREMENT,image_id int(11) DEFAULT NULL,year int(11) DEFAULT NULL, type VARCHAR(45) DEFAULT NULL,width int(11) DEFAULT NULL, height int(11) DEFAULT NULL,location varchar(45) DEFAULT NULL,description varchar(45) DEFAULT NULL,PRIMARY KEY(detail_id))")
except pymysql.err.InternalError:
	print('Detail Table already exists')	
#Create TABLE 3
try:
	cursor.execute("CREATE TABLE gallery (gallery_id INT(11) NOT NULL AUTO_INCREMENT,name VARCHAR(45) DEFAULT NULL, description varchar(2000) DEFAULT NULL,PRIMARY KEY(gallery_id))")
except pymysql.err.InternalError:
	print('Gallery Table already exists')
#Create TABLE 4
try:
	cursor.execute("CREATE TABLE image (image_id INT(11) NOT NULL AUTO_INCREMENT,title VARCHAR(45) DEFAULT NULL,link VARCHAR(200) DEFAULT NULL,gallery_id int(11) DEFAULT NULL,artist_id int(11) DEFAULT NULL,detail_id int(11) DEFAULT NULL,PRIMARY KEY(image_id))")
except pymysql.err.InternalError:
	print('Image Table already exists')

form = cgi.FieldStorage() 

print("Content-Type: text/html")    	# HTML is following
print()   


#Add Artist
if "artist_submit" in form:
	Name = form.getvalue("name")	
	Year = int(form.getvalue("year"))
	Country = form.getvalue("country") 
	Artist_script = form.getvalue("artist_description") 
	sql = "INSERT INTO artist(name,birth_year,country,description) VALUES (%s,%s,%s,%s)"
	cursor.execute(sql,(Name,Year,Country, Artist_script))
	connection.commit()	
	
if "detail_submit" in form:
	Img_id = int(form.getvalue("img_id"))	
	Img_year = int(form.getvalue("img_year"))
	Type = form.getvalue("type") 
	Width = int(form.getvalue("img_width"))
	Height = int(form.getvalue("img_height"))
	Type = form.getvalue("type") 
	Loc = form.getvalue("loc") 
	Img_details = form.getvalue("img_details") 
	sql = "INSERT INTO detail(image_id,year,type,width,height,location,description) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	cursor.execute(sql,(Img_id,Img_year,Type,Width,Height,Loc,Img_details))
	connection.commit()	
	
if "image_submit" in form:
	Title = form.getvalue("img_title")
	Link = form.getvalue("url")
	G_ID = int(form.getvalue("g_id"))
	A_ID = int(form.getvalue("a_id"))
	D_ID = int(form.getvalue("d_id"))
	sql = "INSERT INTO image(title,link,gallery_id,artist_id,detail_id) VALUES (%s,%s,%s,%s,%s)"
	cursor.execute(sql,(Title,Link,G_ID,A_ID,D_ID))
	connection.commit()	

if "gallery_submit" in form:
	Gal_Name = form.getvalue("gal_name")
	Gal_Des = form.getvalue("gallery_description")
	sql = "INSERT INTO gallery(name,description) VALUES (%s,%s)"
	cursor.execute(sql,(Gal_Name,Gal_Des))
	connection.commit()	

if "view" in form:
	test = form.getvalue("view")
	print(test)

	


	
print("<div style='width:1200px;margin:auto'>")


print("<div style='float:left;width:25%;background-color:gray;padding-left:15px'>")
print("<form method='post' action='hello.py'>") 
print("<p>Artist Name: <input type='text' name='name' /></p>") 
print("<p>Artist Year: <input type='text' name='year' /></p>") 
print("<p>Artist Country: <input type='text' name='country' /></p>") 
print("Artist Description: <br> <textarea name='artist_description' cols='30' rows='4'></textarea> <br>")
print("<input type = 'submit' value = 'Submit' name = 'artist_submit' />")

print("<p>Image ID: <input type='text' name='img_id' /></p>") 
print("<p>Year: <input type='text' name='img_year' /></p>") 
print("<p>Type of Image: <input type='text' name='type' /></p>") 
print("<p>Width: <input type='text' name='img_width' /></p>") 
print("<p>Height: <input type='text' name='img_height' /></p>") 
print("<p>Location: <input type='text' name='loc' /></p>") 
print("Image Description: <br> <textarea name='img_details' cols='30' rows='4'></textarea> <br>")
print("<input type = 'submit' value = 'Submit' name = 'detail_submit' />")

print("<p>Image Title: <input type='text' name='img_title' /></p>") 
print("<p>URL: <input type='text' name='url' /></p>") 
print("<p>Gallery ID: <input type='text' name='g_id' /></p>") 
print("<p>Artistic ID: <input type='text' name='a_id' /></p>") 
print("<p>Detail ID: <input type='text' name='d_id' /></p>") 
print("<input type = 'submit' value = 'Submit' name = 'image_submit' />")

print("<p>Gallery Name: <input type='text' name='gal_name' /></p>") 
print("Gallery Description: <br> <textarea name='gallery_description' cols='30' rows='4'></textarea> <br>")
print("<input type = 'submit' value = 'Submit' name = 'gallery_submit' />")
print("</form") 

print("</div>")
print("</div>")


	
print("<div style='float:left;width:45%;background-color:green'>")
cursor.execute("SELECT * FROM image")
for (description) in cursor:
	print("<div style='float:left;width:50%;height:300px;text-align:center'>")
	print("<image style='height:240px;width:100%;' src = "+description[2]+">")
	print(description[1] +"<br>" + str(description[0]) + "/" + str(cursor.rowcount))
	print("<form method='post' action='hello.py'>") 
	print("<button type = 'input' value = "+str(description[0])+" name = 'view'>View</button>")
	print("</form>")
	print("</div>")

print("</div>")

print("<div style='float:left;width:28%;height:700px;background-color:red'>")

sql_img= "SELECT * FROM image WHERE image_id = %s"
sql_art= "SELECT * FROM artist WHERE artist_id = %s"
sql_det= "SELECT * FROM  detail WHERE detail_id = %s"
cursor.execute(sql_img,test)

for (description) in cursor:
	print("<image style='height:30%;width:80%;display:block;margin-left:auto;margin-right:auto;margin-top:10%' src = "+description[2]+">")
	print("<p style= 'white-space: normal;word-wrap:break-word; font-size:14px'>")
	print("Image ID: " + str(description[0]) + "<br>" + "Title: " + description[1] +"<br>" + "URL: " + description[2] )
	print("</p>")
	
cursor.execute(sql_art,test)
for (description) in cursor:
	print("<p style= 'white-space: normal;word-wrap:break-word; font-size:14px'>")
	print("Artist ID: " + str(description[0]) + "<br>" + "Artist Name: " + description[1] +"<br>" + "Artist Year: " + str(description[2]) + "<br>" + "Artist Country: " + description[3] + "<br>" + "Artist Description: " + description[4] + "<br>" )
	print("</p>")
	
	#print("ID: " + str(description[0]) + "<br>" + "Detail Year: " + str(description[1]) +"<br>" + "Type of Image: " + description[2] + "<br>" + "Width: " + str(description[3]) + "<br>" + "Height: " + str(description[4]) + "<br>" + "Location: " + description[5] + "<br>" + "Image Description: " + description[6] + "<br>") )
cursor.execute(sql_det,test)
for (description) in cursor:
	print("<p style= 'white-space: normal;word-wrap:break-word; font-size:14px'>")
	print("ID: " + str(description[0]) + "<br>" + "Detail Year: " + str(description[2]) +"<br>")
	print("Type of Image: " + description[3] + "<br>" + "Width: " + str(description[4]) + "<br>")
	print("Height: " + str(description[5]) + "<br>" + "Location: " + description[6] + "<br>" + "Image Description: " + description[7] + "<br>") 
	print("</p>")
	
print("</div>")
print("</div>")

print(test)
