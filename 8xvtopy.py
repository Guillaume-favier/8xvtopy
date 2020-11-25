import sys
if sys.argv[1] == '-h':
	print('8xv to py is simple program in python to convert python appvar from ti83 Premium CE python Edition to python files\nUsage : python3 8xvtopy.py <Input file path> <Output file path>')
	print('or you can convert more than 2 files in one command with :\n python3 pyto8xv.py [file1] [file2] <file3> ...')
	exit()

def conv(inp,name='',meth=0):
	pass
	i=open(inp,'rb')
	i2=i.read()
	try:
		ii=i.read().split(bytes('\x2E\x70\x79\x00','utf-8'))
		iii=ii[1]
		#print(str(ii[0]))
		if meth != 2:
			name=ii[0].split(bytes('\x01','utf-8'))[1].decode('utf-8')
	except IndexError:
		tmp=i2
		ii=tmp.split(bytes('\x50\x59\x43\x44\x00','utf-8'))
		if meth !=2:
			iii=ii[0].split(bytes('\x15','utf-8'))
			#print(iii)
			name=iii[1].split(bytes('\x00\x00','utf-8'))[0].decode('utf-8')
			#print(name)
			#print(str(ii[1].decode('utf-8')))
			pass
		pass
	pcont=bytes('','utf-8')
	for x in range(len(ii)):
		if x==0:
			pass
		else:
			pcont+=ii[x]
	cont=str(pcont[:-2].decode('utf-8'))
	#print(cont)
	name=str(name)

	if meth!=2:
		print(name+'.py will be created')
		o=open(str(name)+'.py','w+')
	else:
		o=open(name,'w+')
	o.write(str(cont))
	o.close()
	i.close()

if len(sys.argv) <=1:
	inp=input("Quel est le chemain vers votre fichier .8xv ? \n> ")
	conv(inp)
elif len(sys.argv) == 2:
	inp=str(sys.argv[1])
	conv(inp)
	pass
elif len(sys.argv) == 3:
	inp=str(sys.argv[1])
	name=str(sys.argv[2])
	conv(inp,name,2)
	pass
else:
	for x in range(len(sys.argv)-1):
		if x==0:
			pass
		else:
			print('Start of : '+sys.argv[x]+' '+str(x)+'/'+str(len(sys.argv)-2))
			conv(sys.argv[x])
		pass
	print('All done!')