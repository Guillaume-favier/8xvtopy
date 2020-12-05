import sys
from colorama import Fore, Back, Style

	### HELP 

if len(sys.argv) != 1 and sys.argv[1] == '-h':
	print('8xv to py is simple program in python to convert python appvar from ti83 Premium CE python Edition to python files\nUsage : python3 pyto8xv.py <file1> <file2> <file3> ...\n You can Activate the verbose mod by doing \'-v\'')
	exit()

	### VERBOSE

verb=False
def verbose(txt):
	if verb:
		print(Fore.GREEN+'[Verbose] '+txt+Style.RESET_ALL)
if len(sys.argv) != 1 and sys.argv[len(sys.argv)-1] == '-v':
	verb=True
	verbose('Args : '+str(sys.argv))
	del sys.argv[len(sys.argv)-1]
	
### CONVERTION METHOD

def conv(inp,name='',meth=0):
	pass
	i=open(inp,'rb')
	i2=i.read()
	i3=i2
	
		### TEST OF THE FIRST METHOD TO DECONSTRUCT THE 8xv FILE. IF THIS METHOF FAIL IT MEANS THAN THE FILE WAS CREATED ON A CALCULATOR
	try:
		ii=i3.split(bytes('\x2E\x70\x79\x00','utf-8')) ### try to find the .py of the convertion of the file
		iii=ii[1]
		#print(str(ii[0]))
		name=ii[0].split(bytes('\x01','utf-8'))[1].decode('utf-8')
		verbose('The file was originally created on a pc with the name : '+name+".py")
		### TEST OF THE SECOND METHOD
	except IndexError:
		tmp=i2
		ii=tmp.split(bytes('\x50\x59\x43\x44\x00','utf-8')) ### try to find the PYCD.p to separate the header with the name of the file and the content
		iii=ii[0].split(bytes('\x15','utf-8')) ### get the name of the file in 
		#print(iii)
		name=iii[1].split(bytes('\x00\x00','utf-8'))[0].decode('utf-8')
		#print(name)
		#print(str(ii[1].decode('utf-8')))
		verbose('The file was originally created on a calculator with the name : '+name)
		pass
		### assemble the content of the file
	pcont=bytes('','utf-8')
	for x in range(len(ii)):
		if x==0:
			pass
		else:
			pcont+=ii[x]
	#print(pcont)
		### remove the last two caracters of the file because they are not content of the original python file
	try:
		cont=str(pcont[:-2].decode('utf-8'))
		verbose('Removing the two last caracter : '+ str(pcont[len(pcont)-2:]))
	except UnicodeDecodeError:
		print('File corupt. Please remove weird caracters at the end of the file but let the 2 first')
	#print(cont)
	name=str(name)
		### creation of the output file
	print(name+'.py will be created')
	o=open(str(name)+'.py','w+')
	o.write(str(cont))
	o.close()
	i.close()

### execute the convertion method in function of the args
if len(sys.argv) <=1:
	inp=input("What is the file path to your .8xv file ? \n> ")
	conv(inp)
elif len(sys.argv) == 2:
	inp=str(sys.argv[1])
	conv(inp)
	pass
### if there is multiples files
else:
	fnames = ''
	for x in range(len(sys.argv)):
		if x==0:
			pass
		elif x==1:
			fnames += '\"'+sys.argv[x]+'\"'
		else:
			fnames += ', \"'+sys.argv[x]+'\"'
			pass
	verbose('All the files to convert are : '+fnames)
	for x in range(len(sys.argv)):
		if x==0:
			pass
		else:
			print('Start of : '+sys.argv[x]+' '+str(x)+'/'+str(len(sys.argv)-2))
			conv(sys.argv[x])
		pass
	print('All done!')