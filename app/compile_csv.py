import triplegen
import graph
import shutil
import glob
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
files = glob.glob(dir_path+'/../import/gamma/*.ttl')

with open(dir_path+'/../import/results.csv', 'a', encoding='utf-8') as f:
  csv_writer = csv.writer(f)
  for file in files:
    print(f'Load {file}:')
    file = file.replace('\\', '/')
    try:
      tg = triplegen.Triplegen(file)
      for unit in tg.units:
        csv_writer.writerow([unit.evidence, unit.description])
    except:
      pass
    shutil.move(file, dir_path+'/../import/gamma/done/'+file.split('/')[-1])