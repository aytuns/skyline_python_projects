import json
from fpdf import FPDF

file_js = open('stackoverjson.json','r')
text2 = json.load(file_js) #load the json
text3 = json.dumps(text2) #convert the json to string
response = json.loads(text3) #convert the string to json

responseLenght = len(response['items'])
count = 1

# Initialise an instance of FPDF for PDF Creation
pdf = FPDF()

# Add a PDF page
pdf.add_page()

# Set font style and size
pdf.set_font("helvetica", size=10)
pdf.set_fill_color(255,255,0)

header = f"DATA FETCHED FROM STACK-OVER-FLOW API CONTAINING: {responseLenght} ITEMS."
print(header)
pdf.cell(w=100,h=5,txt=header,new_x='LMARGIN', new_y='NEXT',align='X')
pdf.cell(w=0,h=5,new_x='LMARGIN', new_y='NEXT')

while count <= responseLenght:
	# print results on terminal
	print("Number",count)
	print("This question was asked by:",response['items'][count-1]['owner']['display_name'], "with user ID:",response['items'][0]['owner']['user_id'])
	print("The title of the question was:",response['items'][count-1]['title'])
	print("The number of views on the question was:",response['items'][count-1]['view_count'])
	print("The link to the question is:",response['items'][count-1]['link'])
	print("The link to",response['items'][count-1]['owner']['display_name'],"profile image is:",response['items'][count-1]['owner']['profile_image'])
	print("\n")
	
	# write results to PDF
	pdf.cell(w=100,h=5,txt=f"Number {count}",new_x='LMARGIN', new_y='NEXT')
	pdf.multi_cell(w=180,h=5,new_x='LMARGIN', new_y='NEXT',
		txt=f"This question was asked by: {response['items'][count-1]['owner']['display_name']} with user ID: {response['items'][0]['owner']['user_id']}")
	# pdf.image(w=24,h=24,
	# 	name=response['items'][count-1]['owner']['profile_image'])
	pdf.cell(w=0,h=5,new_x='LMARGIN', new_y='NEXT')
	pdf.multi_cell(w=180,h=5,new_x='LMARGIN', new_y='NEXT',
		txt=f"The title of the question was: '{response['items'][count-1]['title']}'")
	pdf.cell(w=180,h=5,new_x='LMARGIN', new_y='NEXT',
		txt=f"The number of views on the question was: {response['items'][count-1]['view_count']:,}")
	pdf.cell(w=35,h=5,new_x='LMARGIN', new_y='NEXT',
		txt="Link to the Question",
		link=response['items'][count-1]['link'],fill=True)
	pdf.cell(w=0,h=10,new_x='LMARGIN', new_y='NEXT')
	pdf.footer()
	count += 1
	# if (count-1 % 4 == 0):
	# 	pdf.add_page()


outputFile = input('Please type name of file: ')
pdf.output(outputFile+'.pdf')
print(f"your file has been saved as {outputFile}.pdf")


# write results to txt file

# with open('stackresult.txt','w') as file:
# 	while count <= responseLenght:
# 		file.write(f"Number {count}\n")
# 		file.write(f"This question was asked by: {response['items'][count-1]['owner']['display_name']} with user ID: {response['items'][0]['owner']['user_id']}\n")
# 		file.write(f"The title of the question was: '{response['items'][count-1]['title']}'\n")
# 		file.write(f"The number of views on the question was: {response['items'][count-1]['view_count']}\n")
# 		file.write(f"The link to the question is:{response['items'][count-1]['link']}\n")
# 		file.write(f"The link to {response['items'][count-1]['owner']['display_name']}profile image is: {response['items'][count-1]['owner']['profile_image']}\n")
# 		file.write("\n\n")
# 		count += 1

