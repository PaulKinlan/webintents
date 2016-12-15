import unittest
import intentparser

class IntentParserTestFunction(unittest.TestCase):

  def setUp(self):
    self.parser = intentparser.IntentParser()

  def test_basic(self):
    intentStr = "<intent type='image/*' action='http://webintents.org/test' />"
    intents = self.parser.parse(intentStr, "http://basedomain.org/")

    self.assertEqual(len(intents), 1)
    self.assertEqual(intents[0]["type_major"], "image")
    self.assertEqual(intents[0]["type_minor"], "*")
    self.assertEqual(intents[0]["action"], "http://webintents.org/test")
    self.assertEqual(intents[0]["href"], "http://basedomain.org/")
    self.assertEqual(intents[0]["domain"], "basedomain.org")

  def test_parse_page_title(self):
    title_string = "<html><head><title>Testing</title></head></html>"
    title = self.parser._parse_page_title(title_string)
    self.assertEqual(title, "Testing")

  def test_href(self):
    intentStr = "<intent type='image/*' action='http://webintents.org/test' href='http://paul.kinlan.me/index.html' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(intents[0]["href"], "http://paul.kinlan.me/index.html")

  def test_domain(self):
    intentStr = "<intent type='image/*' action='http://webintents.org/test' href='http://paul.kinlan.me/index.html' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(intents[0]["domain"], "paul.kinlan.me")

  def test_intent_page_title_default(self):
    intentStr = "<title>Test Title</title><intent type='image/*' action='http://webintents.org/test' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(len(intents), 1)
    self.assertEqual(intents[0]["type_major"], "image")
    self.assertEqual(intents[0]["type_minor"], "*")
    self.assertEqual(intents[0]["action"], "http://webintents.org/test")
    self.assertEqual(intents[0]["title"], "Test Title")

  def test_multiline_basic(self):
    intentStr = "<intent \ntype='image/*' \naction='http://webintents.org/test'\n\t/>"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(len(intents), 1)
    self.assertEqual(intents[0]["type_major"], "image")
    self.assertEqual(intents[0]["type_minor"], "*")
    self.assertEqual(intents[0]["action"], "http://webintents.org/test")

  def test_multiline_basic_no_space(self):
    intentStr = "<intent\ntype='image/*' \naction='http://webintents.org/test'\n\t/>"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(len(intents), 1)
    self.assertEqual(intents[0]["type_major"], "image")
    self.assertEqual(intents[0]["type_minor"], "*")
    self.assertEqual(intents[0]["action"], "http://webintents.org/test")



  def test_disposition(self):
    intentStr = "<intent \ntype='image/*' \naction='http://webintents.org/test' disposition='inline' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(len(intents), 1)
    self.assertEqual(intents[0]["type_major"], "image")
    self.assertEqual(intents[0]["type_minor"], "*")
    self.assertEqual(intents[0]["action"], "http://webintents.org/test")
    self.assertEqual(intents[0]["disposition"], "inline")

  def test_icon(self):
    intentStr = "<intent \ntype='image/*' \naction='http://webintents.org/test' icon='fav2.ico' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(len(intents), 1)
    self.assertEqual(intents[0]["type_major"], "image")
    self.assertEqual(intents[0]["type_minor"], "*")
    self.assertEqual(intents[0]["action"], "http://webintents.org/test")
    self.assertEqual(intents[0]["icon"], "http://webintents.org/fav2.ico")

  def test_multipleintents(self):
    intentStr = "<intent \ntype='image/*' \naction='http://webintents.org/view' icon='fav2.ico' />\n"
    intentStr += "<intent \ntype='image/*' \naction='http://webintents.org/pick' icon='fav2.ico' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(len(intents), 2)

  def test_default_disposition_value(self):
    intentStr = "<intent \ntype='image/*' \naction='http://webintents.org/test' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(intents[0]["disposition"], "window")

  def test_default_icon(self):
    intentStr = "<intent \ntype='image/*' \naction='http://webintents.org/test' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(intents[0]["icon"], "http://webintents.org/favicon.ico")

  def test_default_type(self):
    intentStr = "<intent action='http://webintents.org/test' />"
    intents = self.parser.parse(intentStr, "http://webintents.org/")

    self.assertEqual(intents[0]["type_major"], "*")
    self.assertEqual(intents[0]["type_minor"], None)

