import fetch
import nerd
import triplegen
import graph
import shutil
import glob
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
files = glob.glob(dir_path+'/../import/fetch/list/*.ttl')

for file in files:
  try:
      file = file.replace('\\', '/')
      print(f'Load {file}:')
      fetchStage = fetch.Fetch(filename=file)
      nerdStage = nerd.WP.generate(fetchStage, None)
      nerdStage.asGraph().save(dir_path+'/../import/wp/'+file.split('/')[-1])
      print(f'++Save {dir_path+"/../import/wp/"+file.split("/")[-1]}')
      tgStage = triplegen.Gamma.generate(nerdStage, graph.GroundTruth.dbpedia_kb())
      tgStage.asGraph().save(dir_path+'/../import/gamma/'+file.split('/')[-1])
      print(f'++Save {dir_path+"/../import/gamma/"+file.split("/")[-1]}')
      shutil.move(file, dir_path+"/../import/fetch/done/"+file.split("/")[-1])
      print(f'++Save {dir_path+"/../import/fetch/done/"+file.split("/")[-1]}')
  except Exception:
      shutil.move(file, dir_path+'/../import/fetch/exception/'+file.split('/')[-1])