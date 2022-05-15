import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import nerd

def test_default_section_title():
  assert nerd.Nerd().mainSection.title == 'Untitled'
  
def test_basic_section_append():
  s = nerd.Nerd().mainSection
  s.appendSection()
  assert [it.title for it in s.sections()] == ['Untitled', 'Untitled']
  
def test_basic_section_parents():
  s = nerd.Nerd().mainSection
  s.appendSection()
  assert s == s.subsections[0].parent
  
  
def test_append_titles():
  s = nerd.Nerd().mainSection
  s.appendSection().title = "H2 - 1"
  s.appendSection().title = "H2 - 2"
  assert [it.title for it in s.sections()] == ['Untitled', 'H2 - 1', 'H2 - 2']

def test_insert_titles():
  s = nerd.Nerd().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  assert [it.title for it in s.sections()] == ['Untitled', 'H2', 'H3']
  
def test_cursor_on_append():   # OBSOLETE
  s = nerd.Nerd().mainSection
  s.appendSection().title = "H2 - 1"
  s.appendSection().title = "H2 - 2"
  assert s.cursor.title == 'H2 - 2'

def test_cursor_on_insert():   # OBSOLETE
  s = nerd.Nerd().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  assert s.cursor.title == 'H3'

def text_cursor_insert_append():
  s = nerd.Nerd().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3 1"
  s.appendSection().title = "H3 2"
  assert s.cursor.title == 'H2'
  
def text_cursor_insert_insert():
  s = nerd.Nerd().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  s.insertSection().title = "H4"
  assert s.cursor.title == 'H3'
    
  
def test_cursor_on_float():
  s = nerd.Nerd().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  s.insertSection().title = "H4"
  assert s.cursor.title == 'H4'
  s.floatCursor()
  assert s.cursor.title == 'H3'
  
def test_reset_cursor():
  s = nerd.Nerd().mainSection
  s.insertSection()
  s.insertSection()
  s.insertSection()
  s.insertSection()
  s.floatCursor()
  s.appendSection()
  s.floatCursor()
  ss = s.insertSection()
  s.resetCursor()
  assert s.cursor == ss
  
def test_append_list():
  s = nerd.Nerd().mainSection
  s.appendUL(['Text1'])
  s.appendUL(['Text1', 'Text2'])
  assert len(s.sectionItems) == 2
  
  
def test_append_text():
  s = nerd.Nerd().mainSection
  s.appendText('Text1')
  s.appendText('Text2')
  assert len(s.sectionItems) == 2
  
def test_append_text_to_list():
  s = nerd.Nerd().mainSection
  s.appendUL(['Text1'])
  assert len(next(s.lists()).items) == 1
  next(s.lists()).appendText('Text2')
  assert len(next(s.lists()).items) == 2
  
def test_list_iterator():
  s = nerd.Nerd().mainSection
  s.appendUL(['Text1'])
  s.appendText('Text2')
  s.appendUL(['Text1', 'Text1'])
  s.appendUL(['Text1'])
  s.appendText('Text3')
  assert [1,2,1] == [len(it.items) for it in s.lists()]

def test_list_text_iterator():
  s = nerd.Nerd().mainSection
  s.appendUL(['Text1', 'Text1'])
  assert len(list(next(s.lists()).texts())) == 2
  
  
def test_list_iterator():
  s = nerd.Nerd().mainSection
  s.appendUL(['Text1'])
  s.appendText('Text1')
  s.appendText('Text2')
  s.appendUL(['Text1', 'Text1'])
  s.appendUL(['Text1'])
  assert len(list(s.texts())) == 6
  
  
# -------

def test_load_nerd_title():
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  assert f.mainSection.title == 'Sun'
  
def test_load_nerd_sections():
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  assert [it.title for it in f.mainSection.sections()] == ['Sun', 'Structure and fusion']
  
def test_load_nerd_lists():
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  assert len(list(list(f.mainSection.sections())[1].lists())) == 2
  
def test_load_nerd_texts():
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  assert len(list(list(f.mainSection.sections())[1].texts())) == 8
  
def test_load_nerd_contents():
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  assert [text.text[:4] for text in list(f.mainSection.sections())[1].texts()] == [
    "The ",
    "Core",
    "Radi",
    "Tach",
    "Conv",
    "Beca",
    "Phot",
    "Atmo"
  ]
  
# -------

def test_load_annotations():
  from nerd import Nerd
  Annotation = Nerd.Section.Text.Annotation
  
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  
  texts = list(list(f.mainSection.sections())[1].texts())
  text = texts[7]
  entity = "https://calvoritmo.com/tfm/entity/"

  assert set(list(text.annotations())) == set([
    Annotation("Atmosphere", entity+"70e3ae27-8b71-4ac6-ae0a-8644533da354", 0, 10, "b"),
    Annotation("chromosphere", "http://dbpedia.org/resource/Chromosphere", 66, 78, "a"),
    Annotation("solar transition region", "http://dbpedia.org/resource/Solar_transition_region", 80, 103, "a"),
    Annotation("corona", "http://dbpedia.org/resource/Solar_corona", 105, 111, "a"),
    Annotation("heliosphere", "http://dbpedia.org/resource/Heliosphere", 116, 127, "a"),
    Annotation("solar eclipse", "http://dbpedia.org/resource/Solar_eclipse", 210, 223, "a")  
  ])

def test_asgraph():
  f = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  f.asGraph().save(dir_path+'/../mocks/output_test_nerd.ttl')
  g = nerd.Nerd(filename=dir_path+'/../mocks/output_test_nerd.ttl')
  assert [text.text[:4] for text in list(g.mainSection.sections())[1].texts()] == [
    "The ",
    "Core",
    "Radi",
    "Tach",
    "Conv",
    "Beca",
    "Phot",
    "Atmo"
  ]
  
# -------------

def test_WP_model():
  import fetch
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  g = nerd.WP.generate(f, None)
  assert [text.text[:4] for text in list(g.mainSection.sections())[1].texts()] == [
    "The ",
    "Core",
    "Radi",
    "Tach",
    "Conv",
    "Beca",
    "Phot",
    "Atmo"
  ]

def test_Spotlight_model():
  import fetch
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  g = nerd.Spotlight.generate(f, None)
  assert [text.text[:4] for text in list(g.mainSection.sections())[1].texts()] == [
    "The ",
    "Core",
    "Radi",
    "Tach",
    "Conv",
    "Beca",
    "Phot",
    "Atmo"
  ]

def test_SpacyNER_model():
  import fetch
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  g = nerd.SpacyNER.generate(f, None)
  assert [text.text[:4] for text in list(g.mainSection.sections())[1].texts()] == [
    "The ",
    "Core",
    "Radi",
    "Tach",
    "Conv",
    "Beca",
    "Phot",
    "Atmo"
  ]
  
def test_FullNerd_model():
  import fetch
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  g = nerd.FullNerd.generate(f, None)
  assert [text.text[:4] for text in list(g.mainSection.sections())[1].texts()] == [
    "The ",
    "Core",
    "Radi",
    "Tach",
    "Conv",
    "Beca",
    "Phot",
    "Atmo"
  ]

# ------

def test_json_export():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_nerd.json', 'r', encoding='utf-8'))
  export = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl').exportJSON()
  assert json_dict == export
  
def test_json_import():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_nerd.json', 'r', encoding='utf-8'))
  json_dict['mainSection']['subsections'][0]['sectionItems'][1][1]['annotations'] = [{
				"surface" : "Core",
				"start"   :   0,
				"end"     :   4,
				"uri"     : "https://calvoritmo.com/tfm/entity/4d96d16c-655f-4d6a-8733-370a7986e958",
				"source"  : "b"
			  },
			  {
				"surface" : "nuclear fusion",
				"start"   :   99,
				"end"     :   113,
				"uri"     : "http://dbpedia.org/resource/Nuclear_fusion",
				"source"  : "a"
			  }
			  ]
  g = nerd.Nerd(filename=dir_path+'/../mocks/sun_nerd.ttl')
  g.importJSON(json_dict)
  assert len(list([text for text in list(g.mainSection.sections())[1].texts()][1].annotations())) == 2

  