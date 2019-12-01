import urllib.request,json
from config import Config
from .models import Quotes

quotes_url = Config.QUOTES_URL
def GetQuotes():
  '''
  function that gets random quotes
  '''
  with urllib.request.urlopen(quotes_url) as url:
    get_quotes_data=url.read()
    quote_response=json.loads(get_quotes_data)

    quotes= None
    if quote_response:
      author=quote_response.get('author')
      quote=quote_response.get('quote')
      quotes=Quotes(author,quote)
  return quotes
