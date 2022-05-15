from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect, url_for
# pip install python-dotenv
from dotenv import load_dotenv

import requests

import json

import os

from utils import *

# pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from config import Config
load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
import backend

def sanitize(inputs):
  if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
    raise Exception()
  res = {}
  if request.method == 'GET':
    user_input = request.args.to_dict()
  else:
    user_input = request.json
  for req in inputs:
    if req['name'] not in user_input:
      raise Exception()
    if req['type'] == int:
      user_input[req['name']] = int(user_input[req['name']])
    if type(user_input[req['name']]) != req['type']:      
      raise Exception()
    res[req['name']] = user_input[req['name']]
  return res

@app.route('/')
def index():
  return redirect(url_for('app_gui'))  

# /app
@app.route('/app', methods = ['GET'])
def app_gui():
  return render_template('app.html')

# /app/filters/grefinement
@app.route('/app/filters/grefinement', methods = ['GET'])
def filters_grefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_graph',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_grefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/extraction
@app.route('/app/filters/extraction', methods = ['GET'])
def filters_extraction():
  try:
    user_input = sanitize([
    {'name': 'selected_grefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_extraction(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/fetch
@app.route('/app/filters/fetch', methods = ['GET'])
def filters_fetch():
  try:
    user_input = sanitize([
    {'name': 'selected_extraction',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_fetch(user_input)
    if reply == None:
      return "Client error", 400
  except Exception as e:
    print(e)
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/frefinement
@app.route('/app/filters/frefinement', methods = ['GET'])
def filters_frefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_fetch',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_frefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception as e:
    print(e)
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/nerd
@app.route('/app/filters/nerd', methods = ['GET'])
def filters_nerd():
  try:
    user_input = sanitize([
    {'name': 'selected_frefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_nerd(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/nrefinement
@app.route('/app/filters/nrefinement', methods = ['GET'])
def filters_nrefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_nerd',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_nrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/triplegen
@app.route('/app/filters/triplegen', methods = ['GET'])
def filters_triplegen():
  try:
    user_input = sanitize([
    {'name': 'selected_nrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_triplegen(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/tgrefinement
@app.route('/app/filters/tgrefinement', methods = ['GET'])
def filters_tgrefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_triplegen',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_tgrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception as e:
    print(e)
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/tripleval
@app.route('/app/filters/tripleval', methods = ['GET'])
def filters_tripleval():
  try:
    user_input = sanitize([
    {'name': 'selected_tgrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_tripleval(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/filters/terefinement
@app.route('/app/filters/terefinement', methods = ['GET'])
def filters_terefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_tripleval',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.filters_terefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/read/grefinement
@app.route('/app/read/grefinement', methods = ['GET'])
def read_grefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_grefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.read_grefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/read/frefinement
@app.route('/app/read/frefinement', methods = ['GET'])
def read_frefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_frefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.read_frefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception as e:
    print(e)
    return "Server error", 500
  return jsonify(reply), 200

# /app/read/nrefinement
@app.route('/app/read/nrefinement', methods = ['GET'])
def read_nrefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_nrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.read_nrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/read/tgrefinement             
@app.route('/app/read/tgrefinement', methods = ['GET'])
def read_tgrefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_tgrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.read_tgrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/read/terefinement
@app.route('/app/read/terefinement', methods = ['GET'])
def read_terefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_terefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.read_terefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/grefinement
@app.route('/app/create/grefinement', methods = ['POST'])
def create_grefinement():
  try:
    user_input = sanitize([
    {'name': 'name',
     'type': str},
    {'name': 'graph_refinement',
     'type': dict},
    {'name': 'selected_graph',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_grefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/extraction_prefix
@app.route('/app/create/extraction_prefix', methods=['POST'])
def create_extraction_prefix():
  try:
    user_input = sanitize([
    {'name': 'extraction_number',
     'type': int},
    {'name': 'extraction_prefix',
     'type': str},
    {'name': 'selected_grefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_extraction_prefix(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/extraction_url
@app.route('/app/create/extraction_url', methods=['POST'])
def create_extraction_url():
  try:
    user_input = sanitize([
    {'name': 'extraction_page',
     'type': str},
    {'name': 'selected_grefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_extraction_url(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/frefinement 
@app.route('/app/create/frefinement', methods=['POST'])
def create_frefinement():
  try:
    user_input = sanitize([
    {'name': 'name',
     'type': str},
    {'name': 'fetch_refinement',
     'type': dict},
    {'name': 'selected_fetch',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_frefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/nrefinement
@app.route('/app/create/nrefinement', methods=['POST'])
def create_nrefinement():
  try:
    user_input = sanitize([
    {'name': 'name',
     'type': str},
    {'name': 'nerd_refinement',
     'type': dict},
    {'name': 'selected_nerd',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_nrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/tgrefinement
@app.route('/app/create/tgrefinement', methods=['POST'])
def create_tgrefinement():
  try:
    user_input = sanitize([
    {'name': 'name',
     'type': str},
    {'name': 'triplegen_refinement',
     'type': dict},
    {'name': 'selected_triplegen',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_tgrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/create/terefinement
@app.route('/app/create/terefinement', methods=['POST'])
def create_terefinement():
  try:
    user_input = sanitize([
    {'name': 'name',
     'type': str},
    {'name': 'tripleval_refinement',
     'type': dict},
    {'name': 'selected_tripleval',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.create_terefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/update/grefinement
@app.route('/app/update/grefinement', methods = ['POST'])
def update_grefinement():
  try:
    user_input = sanitize([
    {'name': 'name',
     'type': str},
    {'name': 'graph_refinement',
     'type': dict},
    {'name': 'selected_grefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.update_grefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/update/frefinement  
@app.route('/app/update/frefinement', methods=['POST'])
def update_frefinement():
  try:
    user_input = sanitize([
    {'name': 'fetch_refinement',
     'type': dict},
    {'name': 'selected_frefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.update_frefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/update/nrefinement
@app.route('/app/update/nrefinement', methods=['POST'])
def update_nrefinement():
  try:
    user_input = sanitize([
    {'name': 'nerd_refinement',
     'type': dict},
    {'name': 'selected_nrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.update_nrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/update/tgrefinement
@app.route('/app/update/tgrefinement', methods=['POST'])
def update_tgrefinement():
  try:
    user_input = sanitize([
    {'name': 'triplegen_refinement',
     'type': dict},
    {'name': 'selected_tgrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.update_tgrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/update/terefinement
@app.route('/app/update/terefinement', methods=['POST'])
def update_terefinement():
  try:
    user_input = sanitize([
    {'name': 'tripleval_refinement',
     'type': dict},
    {'name': 'selected_terefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.update_terefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/remove/grefinement
@app.route('/app/remove/grefinement', methods = ['POST'])
def remove_grefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_grefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.remove_grefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/remove/frefinement
@app.route('/app/remove/frefinement', methods=['POST'])
def remove_frefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_frefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.remove_frefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/remove/nrefinement
@app.route('/app/remove/nrefinement', methods=['POST'])
def remove_nrefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_nrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.remove_nrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/remove/tgrefinement
@app.route('/app/remove/tgrefinement', methods=['POST'])
def remove_tgrefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_tgrefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.remove_tgrefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

# /app/remove/terefinement
@app.route('/app/remove/terefinement', methods=['POST'])
def remove_terefinement():
  try:
    user_input = sanitize([
    {'name': 'selected_terefinement',
     'type': int}
    ])
  except Exception:
    return "Client error", 400
  try:
    reply = backend.remove_terefinement(user_input)
    if reply == None:
      return "Client error", 400
  except Exception:
    return "Server error", 500
  return jsonify(reply), 200

if __name__ == '__main__':
  app.run()

from tables import FRefinement
from tables import NRefinement
from tables import TGRefinement
from tables import NExecution
from tables import TGExecution
from tables import TEExecution

from tables import Nerd
from tables import NRefinement
from tables import Triplegen
from tables import TGRefinement
from tables import Tripleval
from tables import TERefinement

import fetch
import nerd
import triplegen
import tripleval
import graph

@app.route('/app/bg/WP', methods=['POST', 'GET'])
def bg_WP():
  in_process = db.session.query(FRefinement).filter(~FRefinement.id.in_(db.session.query(NExecution.frefinement))).all()
  for frefinement in in_process:
    fStage = fetch.Fetch(filename=frefinement.filename)
    nStage = nerd.WP.generate(fStage, None)
    filename = f'data/nerd/{getuuid()}.ttl'
    nStage.asGraph().save(filename)
    n = Nerd(model=1, frefinement=frefinement.id)
    db.session.add(n)
    db.session.commit()
    db.session.refresh(n)
    db.session.add(NRefinement(nerd=n.id, name='None', filename=filename, is_none=True))
    db.session.add(NExecution(frefinement=frefinement.id))
    db.session.commit()
  return '{}', 200
  
@app.route('/app/bg/gamma', methods=['POST', 'GET'])
def bg_gamma():
  in_process = db.session.query(NRefinement).filter(~NRefinement.id.in_(db.session.query(TGExecution.nrefinement))).all()
  for nrefinement in in_process:
    nStage = nerd.Nerd(filename=nrefinement.filename)
    tgStage = triplegen.Gamma.generate(nStage, graph.GroundTruth.dbpedia_kb())
    filename = f'data/triplegen/{getuuid()}.ttl'
    tgStage.asGraph().save(filename)
    tg = Triplegen(model=1, nrefinement=nrefinement.id)
    db.session.add(tg)
    db.session.commit()
    db.session.refresh(tg)
    db.session.add(TGRefinement(triplegen=tg.id, name='None', filename=filename, is_none=True))
    db.session.add(TGExecution(nrefinement=nrefinement.id))
    db.session.commit()  
  return '{}', 200
  
@app.route('/app/bg/bart', methods=['POST', 'GET'])
def bg_bart():
  in_process = db.session.query(TGRefinement).filter(~TGRefinement.id.in_(db.session.query(TEExecution.tgrefinement))).all()
  for tgrefinement in in_process:
    tgStage = triplegen.Triplegen(filename=tgrefinement.filename)
    teStage = tripleval.BartLargeMNLI.generate(tgStage, None)
    filename = f'data/tripleval/{getuuid()}.ttl'
    teStage.asGraph().save(filename)
    te = Tripleval(model=1, tgrefinement=tgrefinement.id)
    db.session.add(te)
    db.session.commit()
    db.session.refresh(te)
    db.session.add(TERefinement(tripleval=te.id, name='None', filename=filename, is_none=True))
    db.session.add(TEExecution(tgrefinement=tgrefinement.id))
    db.session.commit()    
  return '{}', 200