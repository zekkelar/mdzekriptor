import requests
import json
import os
import sys

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def konek():
	try:
		requests.get('http://google.com', timeout=10)
		print ("checking ur internet...")
		print ("OKE")
	except requests.ConnectionError:
		print ("You Are Not Connected to Internet... Quiting")
		exit()
konek()

def banner():
	print ("""
╔╦╗╔╦╗╔═╗  ╔╦╗╔═╗╔═╗╦═╗╦ ╦╔═╗╔╦╗   C0d3d By  : Zekkel AR
║║║ ║║╚═╗   ║║║╣ ║  ╠╦╝╚╦╝╠═╝ ║    Thanks To : Aalex, Faisal, Ago Oeng, dani
╩ ╩═╩╝╚═╝  ═╩╝╚═╝╚═╝╩╚═ ╩ ╩   ╩    Sulton, Jainudin, Anas, Magrisya

""")

class a:
	def __init__(self):
		self.zekkel = input("target list => ")
	def con(self):
		try:
			sukses = []
			nol = 0
			pukey = open(self.zekkel, 'r').readlines()
			print ("total list => %d" % len(pukey))
			for c in pukey:
				nol += 1
				x = c.strip()
				aku = ('https://md5.pinasthika.com/api/decrypt?value=%s' % x)
				oper = requests.get(aku).text
				data = oper
				data2 = json.loads(data)
				apa = print(""+C+"Result => "+G+"%s" % str(data2['result']))
				sukses.append(data2['result'])
		
			print (""+C+"sukses => "+C+"%d" % len(sukses))
			print ("Saved in Result.txt")
			with open("Result.txt", "w") as f:
				for s in sukses:
					f.write(str(s) + '\n')
		except KeyboardInterrupt:
			print ("CTRL + C :D")


if __name__ == "__main__":
	banner()
	nani = a()
	nani.con()

