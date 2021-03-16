import requests
import wget
from bs4 import BeautifulSoup


def main():
	URL = str(input("Please enter the url: "))
	
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	pdfs = []
	
	# search html code for links with
	# '.pdf' ending
	for link in soup.find_all('a'):
		if link['href'].endswith('.pdf'):
			pdfs.append(link.get('href'))

	# convert pfds to a complete url:
	#ex. 'teaching/+altklausuren/ds_Klausur_SS_08.pdf' 
	# => https://ae.cs.uni-frankfurt.de/teaching/+altklausuren/ds_Klausur_SS_08.pdf
	
	urls = []
	
	user_url = str(input("Does the pdf url match the entered url or is it different?(Y/N)"))
	
	if user_url  == "Y":
		for i in range(len(pdfs)):
			url = URL + str(pdfs[i])
			urls.append(url)
	
	if user_url == "N":
		new_url = str(input("Please enter the new url: "))
		for i in range(len(pdfs)):
			url = new_url + str(pdfs[i])
			urls.append(url)
	
	
	for u in urls:
		file_name_start_pos = u.rfind("/")+1
		file_name = u[file_name_start_pos:]
		
		try:
			print("Downloading: ", u)
			r = requests.get(u, auth=('algo220','algo220algo220'),stream=True)
			if r.status_code == requests.codes.ok:
				with open(file_name,'wb') as f:
					for data in r:
						f.write(data)
		except:
			print("Error with: ", u)
	
	print("Finished downloading", len(urls), " pdfs")
if __name__ == '__main__':
    main()
