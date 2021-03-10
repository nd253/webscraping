#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pdf_scraper.py
#  
#  Copyright 2021 Unknown <nils@t460>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import requests
import wget
from bs4 import BeautifulSoup


def main():
	#URL = "https://ae.cs.uni-frankfurt.de/algo220"   
	URL = "https://ae.cs.uni-frankfurt.de/teaching/altklausuren.html"
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	pdfs = []
	
	for link in soup.find_all('a'):
		if link['href'].endswith('.pdf'):
			pdfs.append(link.get('href'))
	
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
