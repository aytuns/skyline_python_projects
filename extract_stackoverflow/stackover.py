import requests
from fpdf import FPDF
import time

firstUrl = input('input Stckoverflow API link: ')
secondUrl = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

# Set the proper header to be sent

try:
	response = requests.get(firstUrl).json()
except:
	response = requests.get(secondUrl).json()

responseLenght = len(response['items'])
header = f"DATA FETCHED FROM STACK-OVER-FLOW API CONTAINING: {responseLenght} RESULTS."

# Initialise an instance of FPDF for PDF Creation
pdf = FPDF()

def printToTerminal():
	count = 1
	# Print header
	print(header)

	while count <= responseLenght:
		# print results on terminal
		print("Number",count)
		print("This question was asked by:",response['items'][count-1]['owner']['display_name'], "with user ID:",response['items'][0]['owner']['user_id'])
		print("The title of the question is:",response['items'][count-1]['title'])
		print("The number of views on the question is:",response['items'][count-1]['view_count'])
		print("The link to the question is:",response['items'][count-1]['link'])
		print("The link to",response['items'][count-1]['owner']['display_name'],"profile image is:",response['items'][count-1]['owner']['profile_image'])
		print("\n")
		count += 1
		# Return only 50 results
		if count == 51:
			break


def writeToPDF():
	count = 1

	# Add a PDF page
	pdf.add_page()

	# set font fill style (using local font style due to unicode character formatting issues)
	pdf.add_font('Arial','',r"C:\Windows\Fonts\arial.ttf",uni=True)
	pdf.set_font('Arial', size=10)
	pdf.set_fill_color(255,255,0)

	# Print heading
	pdf.cell(w=100,h=5,txt=header,new_x='LMARGIN', new_y='NEXT',center=True)
	pdf.cell(w=0,h=5,new_x='LMARGIN', new_y='NEXT')
	
	while count <= responseLenght:
		# write results to PDF
		print(f"writing to PDF Result: {count}")
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
	printToTerminal()
except Exception as error:
	print(error)

try:
	writeToPDF()
except Exception as error:
	print(error)

outputFile = input('Please type name of file: ')
pdf.output(outputFile+'.pdf')
print(f"your file has been saved as {outputFile}.pdf")

time.sleep(10)