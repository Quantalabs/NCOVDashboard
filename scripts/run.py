import os

for file in os.listdir('python/'):
  os.chdir('python/')
  if file.endswith('.py'):
    os.system('python '+file)
  os.chdir('..')
