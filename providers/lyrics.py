
import re

from lrc_kit.lyrics import Lyrics


class CustomLyrics(Lyrics):

  def toSpotifyLyrics(self):
    res = []
    for i in range(len(self.lyrics)):
      line = self.lyrics[i]
      ms = self.toSpotifyLine(line)
      if (ms):
        res.append(ms)
    return res

  def toSpotifyLine(self, line):
    if(len(line) > 2
        and line[1].isnumeric()
        and line[2].isnumeric()
      ):
      time = line[1:9]
      split_min = time.split(':')
      minutes = int(split_min[0])
      split_sec = split_min[1].split('.')
      seconds = int(split_sec[0])
      ms = int(split_sec[1])
      return {
        'startTimeMs': ((minutes * 60 * 1000) + (seconds * 1000) + ms),
        'words': re.sub(r'\[\d{2}:\d{2}\.\d{2,3}\]','', line).replace('\r', '')
      }

    return None
