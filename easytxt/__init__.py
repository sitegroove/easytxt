__version__ = "0.0.5"

from easytxt.parsers import parse_string
from easytxt.parsers.table import TableParser
from easytxt.parsers.text import TextParser

parse_string = parse_string
parse_table = TableParser
parse_text = TextParser
