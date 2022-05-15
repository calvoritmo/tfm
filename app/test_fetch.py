import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import fetch

def test_default_section_title():
  assert fetch.Fetch().mainSection.title == 'Untitled'
  
def test_basic_section_append():
  s = fetch.Fetch().mainSection
  s.appendSection()
  assert [it.title for it in s.sections()] == ['Untitled', 'Untitled']
  
def test_basic_section_parents():
  s = fetch.Fetch().mainSection
  s.appendSection()
  assert s == s.subsections[0].parent
  
  
def test_append_titles():
  s = fetch.Fetch().mainSection
  s.appendSection().title = "H2 - 1"
  s.appendSection().title = "H2 - 2"
  assert [it.title for it in s.sections()] == ['Untitled', 'H2 - 1', 'H2 - 2']

def test_insert_titles():
  s = fetch.Fetch().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  assert [it.title for it in s.sections()] == ['Untitled', 'H2', 'H3']
  
#def test_cursor_on_append():
#  s = fetch.Fetch().mainSection
#  s.appendSection().title = "H2 - 1"
#  s.appendSection().title = "H2 - 2"
#  assert s.cursor.title == 'Untitled'

#def test_cursor_on_insert():
#  s = fetch.Fetch().mainSection
#  s.insertSection().title = "H2"
#  s.insertSection().title = "H3"
#  assert s.cursor.title == 'H2'

def text_cursor_insert_append():
  s = fetch.Fetch().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3 1"
  s.appendSection().title = "H3 2"
  assert s.cursor.title == 'H2'
  
def text_cursor_insert_insert():
  s = fetch.Fetch().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  s.insertSection().title = "H4"
  assert s.cursor.title == 'H3'
    
  
def test_cursor_on_float():
  s = fetch.Fetch().mainSection
  s.insertSection().title = "H2"
  s.insertSection().title = "H3"
  s.insertSection().title = "H4"
  assert s.cursor.title == 'H4'
  s.floatCursor()
  assert s.cursor.title == 'H3'
  
def test_reset_cursor():
  s = fetch.Fetch().mainSection
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
  s = fetch.Fetch().mainSection
  s.appendUL(['Text1'])
  s.appendUL(['Text1', 'Text2'])
  assert len(s.sectionItems) == 2
  
  
def test_append_text():
  s = fetch.Fetch().mainSection
  s.appendText('Text1')
  s.appendText('Text2')
  assert len(s.sectionItems) == 2
  
def test_append_text_to_list():
  s = fetch.Fetch().mainSection
  s.appendUL(['Text1'])
  assert len(next(s.lists()).items) == 1
  next(s.lists()).appendText('Text2')
  assert len(next(s.lists()).items) == 2
  
def test_list_iterator():
  s = fetch.Fetch().mainSection
  s.appendUL(['Text1'])
  s.appendText('Text2')
  s.appendUL(['Text1', 'Text1'])
  s.appendUL(['Text1'])
  s.appendText('Text3')
  assert [1,2,1] == [len(it.items) for it in s.lists()]

def test_list_text_iterator():
  s = fetch.Fetch().mainSection
  s.appendUL(['Text1', 'Text1'])
  assert len(list(next(s.lists()).texts())) == 2
  
  
def test_list_iterator():
  s = fetch.Fetch().mainSection
  s.appendUL(['Text1'])
  s.appendText('Text1')
  s.appendText('Text2')
  s.appendUL(['Text1', 'Text1'])
  s.appendUL(['Text1'])
  assert len(list(s.texts())) == 6
  
  
# -------

def test_load_fetch_title():
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  assert f.mainSection.title == 'Sun'
  
def test_load_fetch_sections():
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  assert [it.title for it in f.mainSection.sections()] == ['Sun', 'Structure and fusion']
  
def test_load_fetch_lists():
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  assert len(list(list(f.mainSection.sections())[1].lists())) == 2
  
def test_load_fetch_texts():
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  assert len(list(list(f.mainSection.sections())[1].texts())) == 8
  
def test_load_fetch_contents():
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  assert [text.text[:4] for text in list(f.mainSection.sections())[1].texts()] == [
    "The ",
    "<b>C",
    "<b>R",
    "<b>T",
    "<b>C",
    "Beca",
    "<b>P",
    "<b>A"
  ]
  
def test_asgraph():
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  f.asGraph().save('../mocks/output_test_fetch.ttl')
  g = fetch.Fetch(filename=dir_path+'/../mocks/output_test_fetch.ttl')
  assert [text.text[:4] for text in list(g.mainSection.sections())[1].texts()] == [
    "The ",
    "<b>C",
    "<b>R",
    "<b>T",
    "<b>C",
    "Beca",
    "<b>P",
    "<b>A"
  ]

# ------

def test_wikipedia_model():
  with open(dir_path+'/../mocks/Sun.html', 'r', encoding='utf-8') as f:
    raw = f.read()
  f = fetch.WikipediaHTML.generate(raw, None)
  assert [text.text[:4] for text in list(f.mainSection.sections())[1].texts()] == [
    "The ",
    "<b>C",
    "<b>R",
    "<b>T",
    "<b>C",
    "Beca",
    "<b>P",
    "<b>A"
  ]
  
# ------

def test_json_export():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_fetch.json', 'r', encoding='utf-8'))
  export = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl').exportJSON()
  assert json_dict == export
  
def test_json_import():
  import json
  json_dict =  json.load(open(dir_path+'/../mocks/sun_fetch.json', 'r'))
  json_dict['mainSection']['subsections'][0]['sectionItems'][1][0] = "CCCC"
  f = fetch.Fetch(filename=dir_path+'/../mocks/sun_fetch.ttl')
  f.importJSON(json_dict)
  assert [text.text[:4] for text in list(f.mainSection.sections())[1].texts()] == [
    "The ",
    "CCCC",
    "<b>R",
    "<b>T",
    "<b>C",
    "Beca",
    "<b>P",
    "<b>A"
  ]