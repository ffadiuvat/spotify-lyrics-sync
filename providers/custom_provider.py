import logging
import re

from bs4 import BeautifulSoup
from lrc_kit import LyricsProvider

from providers.lyrics import CustomLyrics


class CustomLyricsProvider(LyricsProvider):
  name = 'Custom'
  def raw_search(self, search_request):
    search_page = self.session.get("https://www.syair.info/search", params={
    "q": f'{search_request.artist_normalized} {search_request.song}'
    }, headers = self.user_agent).text
    result_regex = re.compile(r'href=\"([^\"]+)\" target=\"_blank\" class=\"title\">([^<]+)<\/a><br>([^<]+)')
    results = re.findall(result_regex, search_page)
    best_result = (None, None)
    for result in results:
        href = result[0]
        text = result[1]
        lrc_preview = result[2]
        try:
            artist, song = text.replace('.lrc','').strip().lower().split(' - ', 1)
            logging.debug(f'A:{artist} S:{song}')
        except ValueError:
            continue
        logging.debug(search_request.as_string)
        if (search_request.artist in artist or search_request.artist_normalized in artist) and search_request.song in song:
            metadata = {
                'ar': artist,
                'ti': song
            }
            best_result = ("https://www.syair.info" + href, metadata)
            if '[offset' not in lrc_preview:
                break
    return best_result
  def fetch(self, lyric_url):
    lyrics_page = self.session.get(lyric_url, headers=self.user_agent).text
    parsed_page = BeautifulSoup(lyrics_page, 'html.parser')
    content = parsed_page.find('div',  id='entry')
    lyric_text = content.text.split('\n')
    return CustomLyrics(lyric_text)
