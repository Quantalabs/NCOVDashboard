import os

for file in os.listdir('python/'):
  os.chdir('python/')
  os.system('python '+file)
  os.chdir('..')
