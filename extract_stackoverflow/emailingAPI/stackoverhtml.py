import requests
from fpdf import FPDF

secondUrl = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(secondUrl).json()

responseLenght = len(response['items'])
header = f"DATA FETCHED FROM STACK-OVER-FLOW API CONTAINING: {responseLenght} RESULTS."

# Initialise an instance of FPDF for PDF Creation
pdf = FPDF()

def writeHTML():
	html=""
	count = 1
	with open('message.html','w') as file_html:
		file_html.write(f'''<!DOCTYPE html>
	<html lang="en">

	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>STACK OVERFLOW API</title>
	</head>
		<body style = "margin:auto; padding:5% 0;display:flex;width:90%;text-align:center;background:lightblue">
			<div style = "width:100%; padding: 10px;background:white;">
			<h1>{header}</h1>
	''')
		while count <= responseLenght:
			file_html.write(f'''
			<div style="padding:20px; text-align:justify">
			<h3>Number {count}</h3>
			<h3><img src="{response['items'][count-1]['owner']['profile_image']}" alt="profile_pix" width="100px"
							style="max-width: 100%; padding-top:0px"></h3>
			<h3>This question was asked by: {response['items'][count-1]['owner']['display_name']} with user ID: {response['items'][0]['owner']['user_id']}</h3>
			<h3>The title of the question is: {response['items'][count-1]['title']}</h3>
			<h3>The number of views on the question is: {response['items'][count-1]['view_count']}</h3>
			<h3><a href="{response['items'][count-1]['link']}">This is the link to the question</a></h3>
			</div>
	''')
			count += 1
			# Return only 50 results
			if count == 51:
				break
		file_html.write(f'''
			</div>
		</body>
	</html>
	''')
	with open ('message.html','r') as file_html:
		for item in file_html.readlines():
			html += item
	return html


def writeToPDF():
	count = 1

	# Add a PDF page
	pdf.add_page()

	# set font & fill style (using local font style due to unicode character formatting issues)
	pdf.add_font('Arial','',r"C:\Windows\Fonts\arial.ttf",uni=True)
	pdf.set_font('Arial', size=10)
	pdf.set_fill_color(255,255,0)

	# Print heading
	pdf.cell(w=100,h=5,txt=header,new_x='LMARGIN', new_y='NEXT',center=True)
	pdf.cell(w=0,h=5,new_x='LMARGIN', new_y='NEXT')
	
	while count <= responseLenght:
		# write results to PDF
		print(f"writing to PDF Results from stack-overflow API: {count}/{responseLenght}")
		pdf.cell(w=100,h=5,txt=f"Number {count}",new_x='LMARGIN', new_y='NEXT')
		pdf.image(w=24,h=24,name=response['items'][count-1]['owner']['profile_image'],alt_text="profile_image")
		pdf.multi_cell(w=180,h=5,new_x='LMARGIN', new_y='NEXT',
			txt=f"A. This question was asked by: {response['items'][count-1]['owner']['display_name']} with user ID: {response['items'][0]['owner']['user_id']}")
		pdf.multi_cell(w=180,h=5,new_x='LMARGIN', new_y='NEXT',
			txt=f"B. The title of the question is: '{response['items'][count-1]['title']}'")
		pdf.cell(w=180,h=5,new_x='LMARGIN', new_y='NEXT',
			txt=f"C. The number of views on the question so far is: {response['items'][count-1]['view_count']:,}")
		pdf.cell(w=40,h=5,new_x='LMARGIN', new_y='NEXT',
			txt="D. Link to the Question",
			link=response['items'][count-1]['link'],fill=True)
		pdf.cell(w=0,h=10,new_x='LMARGIN', new_y='NEXT')
		if (count % 4 == 0):
			pdf.add_page()
		count += 1
		# Return only 50 results
		if count == 51:
			break

# EXECUTE
try:
	writeHTML()
except Exception as error:
	print(error)

try:
	writeToPDF()
except Exception as error:
	print(error)

outputFile = input('Please type name for PDF file: ')
pdf.output(outputFile+'.pdf')
print(f"your file has been saved as {outputFile}.pdf")
