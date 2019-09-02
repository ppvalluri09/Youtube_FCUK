import requests
from bs4 import BeautifulSoup
import os
import sys

'''

Other API 
https://api.youtubemultidownloader.com/video?url=https://www.youtube.com/watch?v=ujTCoH21GlA&list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr
'''

def download_videos(links, folder_name):

	if os.path.isdir(folder_name) == False:
		os.mkdir(folder_name)
	else:
		print('Directory already exists, try another name')
		sys.exit(1)

	for link in links:
		file_name = link.split('&')[-1][6:]
		print('Downloading File:- {}'.format(file_name))

		r = requests.get(link, stream=True)

		with open(folder_name + '/' + file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024 * 1024):
				if chunk:
					f.write(chunk)

		print('{} Downloaded'.format(file_name))

	print("Downloads done")
	return

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

base_url = 'https://video.genyt.net/'

video_type = int(sys.argv[2])

if video_type == 1:
	video_id = str(sys.argv[1][32:])
	page = requests.get(base_url + video_id, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	div_links = soup.find_all("div", {"class": "row my-3"})

	links = []
	formats = []

	for div in div_links:
		_links = div.find_all('a')
		for a in _links:
			links.append(a['href'])
			formats.append(a.get_text())

	print('Choose the Format:- \n')
	for i in range(len(links)):
		print(str(links.index(links[i])) + ') ' + formats[i] + '\n')
	format_ = int(input('Choose your format:- '))

	download_links = [links[format_]]
	folder_name = str(sys.argv[3])

	download_videos(download_links, folder_name)

elif video_type == 2:
	playlist_url = str(sys.argv[1])
	keepvid_url = 'https://keepvid.pro/youtube-playlist-downloader?video='
	URL = keepvid_url + playlist_url
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	print('Sorry WIP')
	sys.exit(1)

	










