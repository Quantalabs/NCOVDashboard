import os

filelist = []

for root, dirs, files in os.walk('python/'):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))
  
for file in filelist:
  os.chdir('python/')
  if file.endswith('.py'):
    os.system('python '+file)
  os.chdir('..')
