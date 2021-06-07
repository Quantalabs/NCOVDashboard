import os

for file in os.listdir('python/'):
  os.chdir('python/')
  if not file.endswith('/'):
    os.system('python '+file)
  os.chdir('..')
