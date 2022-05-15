import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import triplegen

def test_load_unit():
  Unit = triplegen.Triplegen.Unit
  f = triplegen.Triplegen(dir_path+'/../mocks/sun_gamma.ttl')
  evidence = """Sun: Structure
Core – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere."""
  statements = [
                   ("<http://dbpedia.org/resource/Sun>", "<http://www.w3.org/2004/02/skos/core#related>", "<http://dbpedia.org/resource/Structure>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>",  "<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>"),
                   ("<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Core"),
                   ("<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Radiative zone"),
                   ("<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Tachocline"),
                   ("<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Convective zone")
                  ]
  description = "Sun is related to the following Structure: Core, Radiative zone, Tachocline, Convective zone."
  assert Unit(evidence, statements, description) in f.units

def test_asgraph():
  Unit = triplegen.Triplegen.Unit
  f = triplegen.Triplegen(filename=dir_path+'/../mocks/sun_gamma.ttl')
  f.asGraph().save(dir_path+'/../mocks/output_test_gamma.ttl')
  g = triplegen.Triplegen(filename=dir_path+'/../mocks/output_test_gamma.ttl')
  evidence = """Sun: Structure
Core – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere."""
  statements = [
                   ("<http://dbpedia.org/resource/Sun>", "<http://www.w3.org/2004/02/skos/core#related>", "<http://dbpedia.org/resource/Structure>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>",  "<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>"),
                   ("<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Core"),
                   ("<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Radiative zone"),
                   ("<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Tachocline"),
                   ("<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Convective zone")
                  ]
  description = "Sun is related to the following Structure: Core, Radiative zone, Tachocline, Convective zone."
  assert Unit(evidence, statements, description) in g.units
  
  
# -------------

"""
Its scope is a full UL item, preceded by 'T types:'
It generates a bag of RDF statements.

If UL H parent contains any of ["type", "types", "category", "categories"]:
  For each entity, generate T -skos:narrower-> entity (through skos bag)

Given ent_i, T generate "{{ent_i.label@en}},{{}}and{{}} are kinds of {{T.label@en}}"
"""
def test_alpha_model():
  assert False

"""
Its scope is a LI element
It generates a single statement

Relation extraction (ent1, r, ent2): if ['is'] in r:
  ent1 a ent2.
  
Given ent1, ent2 generate "{{ent1.label}} is a {{ent2.label}}"
"""
def test_beta_model():
  assert False

"""
Its scope is a full UL with its parent Header and Title. 'Title: Heading\nSents'
Generates a statement bag

If a prefix from parent heading is article or redirect:
  T skos:related H
  H skos:narrower Bag skos:member ent_i

Given T, H, ent_i generate "{{T.label}} is related to the following {{H.label}}: {{ent_i.label}}"
"""
def test_gamma_model():  # TODO: make it unitary
  Unit = triplegen.Triplegen.Unit
  import nerd
  import graph 
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  g = triplegen.Gamma.generate(f, graph.GroundTruth.dbpedia_kb())
  evidence = """Sun: Structure
Core – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere.
"""
  statements = [
                   ("<http://dbpedia.org/resource/Sun>", "<http://www.w3.org/2004/02/skos/core#related>", "<http://dbpedia.org/resource/Structure>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>",  "<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>"),
                   ("<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>"),
                   ("<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Core"),
                   ("<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Radiative zone"),
                   ("<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Tachocline"),
                   ("<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Convective zone")
                  ]
  description = "Sun is related to the following Structure: Core, Radiative zone, Tachocline, Convective zone."
  assert Unit(evidence, statements, description) in g.units

"""
Its scope is a single LI
It generates a single statement

Relation extraction (ent1, text, ent2):
   ent1 skos:related ent2.
   
Given ent1, ent2: generate "{{ent1.label}} is related to {{ent2.label}}"
"""
def test_delta_model():
  assert False

"""
Its scope is a full UL item preceded by a title.
It generates a single RDF statement.

For each entity add all r to the relation collection, where (title -r-> entity).
  For each entity and r, generate title -r-> entity
  
Given Title,UL, (Title -r-> Entity), generate:
"{{Title.rdfs:label@en}} has {{Entity.rdfs:label@en}} as {{r.rdfs:label@en}}"
"""
def test_epsilon_model():
  assert False  

"""
Its scope is a single LI
It generates a single statement

Relation extraction (ent1, text, ent2):
    S a rdf:Statement.
S zeta:kindOfRelation text.
S = ent1 skos:related ent2.

Given ent1, ent2, text: generate "{{text}} is a relation between {{ent1.label}} and {{ent2.label}}"
"""
def test_zeta_model():
  assert False 
 
# ------

def test_json_export():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_gamma.json', 'r', encoding='utf-8'))
  export = triplegen.Triplegen(filename=dir_path+'/../mocks/sun_gamma.ttl').exportJSON()
  assert json_dict == export
  
def test_json_import():
  import triplegen
  Unit = triplegen.Triplegen.Unit
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_gamma.json', 'r', encoding='utf-8'))
  f = triplegen.Triplegen(filename=dir_path+'/../mocks/sun_gamma.ttl')
  evidence = """Sun: Structure
CCCC – the innermost 20–25% of the Sun\'s radius, where temperature and pressure are sufficient for nuclear fusion to occur. Hydrogen fuses into helium (which cannot itself be fused at this point in the Sun\'s life). The fusion process releases energy, and the core gradually becomes enriched in helium.
Radiative zone – Convection cannot occur until much nearer to the surface of the Sun. Therefore, between about 20–25% of the radius, and 70% of the radius, there is a \'radiative zone\' in which energy transfer occurs by means of radiation (photons) rather than by convection.
Tachocline – the boundary region between the radiative and convective zones.
Convective zone – Between about 70% of the Sun\'s radius and a point close to the visible surface, the Sun is cool and diffuse enough for convection to occur, and this becomes the primary means of outward heat transfer, similar to weather cells which form in the earth\'s atmosphere."""
  statements = [
                   ["<http://dbpedia.org/resource/Sun>", "<http://www.w3.org/2004/02/skos/core#related>", "<http://dbpedia.org/resource/Structure>"],
                   ["<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>"],
                   ["<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>"],
                   ["<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>",  "<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>"],
                   ["<http://dbpedia.org/resource/Structure>", "<http://www.w3.org/2004/02/skos/core#narrower>", "<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>"],
                   ["<https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958>", "<http://www.w3.org/2000/01/rdf-schema#label>", "CCCC"],
                   ["<https://calvoritmo.com/tfm/entity/ebf0c989-ddbd-4c0e-a488-79b666fc6ce6>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Radiative zone"],
                   ["<https://calvoritmo.com/tfm/entity/d12467c4-9e1e-4d34-ba4c-7039fabe03e9>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Tachocline"],
                   ["<https://calvoritmo.com/tfm/entity/bbc59a6b-a31f-40eb-86d0-ce0d06973971>", "<http://www.w3.org/2000/01/rdf-schema#label>", "Convective zone"]
                  ]
  description = "Sun is related to the following Structure: CCCC, Radiative zone, Tachocline, Convective zone."
  json_dict['units'][0] = {"evidence" : evidence, 
                                              "statements" : statements, 
                                              "description" : description}
  f.importJSON(json_dict)
  assert f.units[0].evidence == evidence
  assert f.units[0].description == description

  
