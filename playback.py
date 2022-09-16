class AddPlayingException(Exception):
  pass

class SpotifyNotRunningException(Exception):
  pass

class Playback:
  def __init__(self, client):
    self.client = client
    self.is_playig = False
    self.progress_ms = 0
    self.device = ''
    self.song = ''
    self.song_id = ''
    self.artist = ''
    self.album = ''

  def current(self):
    result = self.client.current_playback()
    if not result:
      raise SpotifyNotRunningException

    if(result['currently_playing_type'] == 'ad'):
      raise AddPlayingException
    else:
      self.is_ad = False
      self.is_playing = result['is_playing']
      self.progress_ms = result['progress_ms']
      self.device = result['device']['name']
      self.set_song(result['item']['name'])
      self.song_id = result['item']['id']
      self.set_artist(result['item']['artists'][0]['name'])
      self.album = result['item']['album']['name']

  def is_changed(self, song, artist):
    return (
      self.song != song or
      self.artist != artist
    )

  def set_song(self, value):
    self.song = value.replace('`', '\'')

  def set_artist(self, value):
    self.artist = value.replace('`', '\'')
