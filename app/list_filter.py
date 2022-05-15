import glob
import os
import shutil
import fetch

dir_path = os.path.dirname(os.path.realpath(__file__))
files = glob.glob(dir_path+'/../import/fetch/*.ttl')

for file in files:
  file = file.replace('\\', '/')
  print(f'Processing {file}')
  try:
    f = fetch.Fetch(filename=file)
  except Exception:
    shutil.move(file, dir_path+'/../import/fetch/exception/'+file.split('/')[-1])
  else:
    if list(f.mainSection.lists()) == []:
      shutil.move(file, dir_path+'/../import/fetch/nolist/'+file.split('/')[-1])
    else:
      shutil.move(file, dir_path+'/../import/fetch/list/'+file.split('/')[-1])