import requests
import wget
from bs4 import BeautifulSoup


def main():
	#URL = "https://ae.cs.uni-frankfurt.de/algo220"   
	URL = "https://ae.cs.uni-frankfurt.de/teaching/altklausuren.html"
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
	for i in range(len(pdfs)):
		url = "https://ae.cs.uni-frankfurt.de/" + str(pdfs[i])
		urls.append(url)
		print(url)
	
	
	for u in urls:
		file_name_start_pos = u.rfind("/")+1
		file_name = u[file_name_start_pos:]
		
		try:
			r = requests.get(u, auth=('algo220','algo220algo220'),stream=True)
			if r.status_code == requests.codes.ok:
				with open(file_name,'wb') as f:
					for data in r:
						f.write(data)
		except:
			print("error with: ", u)
if __name__ == '__main__':
    main()
