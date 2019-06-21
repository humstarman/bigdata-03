#!/usr/bin/env python

import urllib.request

def main():
	url = "https://www.baidu.com"
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
	}
	request = urllib.request.Request(url,headers=headers)
	response = urllib.request.urlopen(request)
	print(response)
	print(request.get_header("User-agent"))
	data = response.read().decode("utf-8")
	with open("02.html","w") as f:
		f.write(data)

if __name__ == "__main__":
	main()
