import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import tripleval

def test_load_unit():
  Unit = tripleval.Tripleval.Unit
  f = tripleval.Tripleval(dir_path+'/../mocks/sun_gamma_eval.ttl')
  evidence = """Sun:
Structure:
Core – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere."""
  description = "Sun is related to the following Structure: Core, Radiative zone, Tachocline and Convective zone."
  quality = "Good"
  certainty = "Sure"
  assert Unit(evidence, description, quality, certainty) in f.units()
  
def test_asgraph():
  f = tripleval.Tripleval(filename=dir_path+'/../mocks/sun_gamma_eval.ttl')
  f.asGraph().save(dir_path+'/../mocks/output_test_gamma_eval.ttl')
  g = tripleval.Tripleval(filename=dir_path+'/../mocks/output_test_gamma_eval.ttl')
  evidence = """Sun:
Structure:
Core – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere."""
  description = "Sun is related to the following Structure: Core, Radiative zone, Tachocline and Convective zone."
  quality = "Good"
  certainty = "Sure"
  assert Unit(evidence, description, quality, certainty) in g.units()
  
  
# TODO: test models

def test_bart_large_mnli():
  assert False

# ------

def test_json_export():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_gamma_eval.json', 'r'))
  export = tripleval.Tripleval(filename=dir_path+'/../mocks/sun_gamma_eval.ttl').exportJSON()
  assert json_dict == json.loads(export)
  
def test_json_import():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_gamma_eval.json', 'r'))
  # json_dict[whatever...] = TalTal
  # assert text.text[:4] ... == "The ", ..., "TalT", ...  
  evidence = """Sun:
Structure:
CCCC – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere."""
  description = "Sun is related to the following Structure: CCCC, Radiative zone, Tachocline and Convective zone."
  quality = "Mediocre"
  certainty = "NotSure"
  json_dict['units'] = json_dict['units'] + [{"evidence" : evidence, 
                                              "quality" : quality, 
                                              "certainty" : certainty, 
                                              "description" : description}]
  f = tripleval.Tripleval(filename=dir_path+'/../mocks/sun_gamma_eval.ttl')
  f.importJSON(json_dict)
  assert Unit(evidence, description, quality, certainty) in f.units()