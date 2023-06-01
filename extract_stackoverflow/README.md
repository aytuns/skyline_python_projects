# __PYTHON SCRIPT USING STACKOVERFLOW API__

## Build a platform, paste your endpoint, the application should download 50questions. Save and number them in a pdf

## This application should run as an executable file. Enter your endpoint and the application should fetch the following:

	- The title of the question

	- The total number of views

	- Read the link on the pdf

	- Picture of the question

	- Send an email of the received data and attach the PDF file generated.

## - fpdf was used to create the pdf file, so: py -m pip install fpdf2

## - in order to display __Unicode characters__ in PDF, use unicode font like Arial that support unicode. Locate fonts in "C:\Windows\Fonts" for windows users

## - pyinstaller was used to create the exe file, so: py -m pip install pyinstaller; then run pyinstaller --onefile file.py
