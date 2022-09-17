import time

from lrc_kit import SearchRequest

from playback import AddPlayingException, SpotifyNotRunningException


class Daemon:
  def __init__(self, engine, playback, synchronizer, broadcaster):
    self.should_run = True
    self.engine = engine
    self.pb = playback
    self.broadcaster = broadcaster
    self.synchronizer = synchronizer

  def run(self):
    while(self.should_run):
      try:
        self.pb.current()
        prev = {
          'song': self.pb.song,
          'artist': self.pb.artist
        }

        self.progress_ms = self.pb.progress_ms
        lyrics = self.engine.search(SearchRequest(self.pb.artist, self.pb.song))
        self.broadcaster.send_artist_title(self.pb.artist, self.pb.song)

        while( self.pb.is_playing and not self.pb.is_changed(prev['song'], prev['artist'])):
          if(not self.should_run):
            break
          if(not lyrics):
            self.broadcaster.send_raw('Lyrics is not available at the moment')
          else:
            timeline = lyrics.toSpotifyLyrics()
            self.synchronizer.sync(timeline, self.pb.progress_ms)
          self.pb.current()
      except SpotifyNotRunningException:
        self.broadcaster.send_raw('Spotify is not running')
        time.sleep(10)
      except AddPlayingException:
        self.broadcaster.send_raw('Playing ads')
      except Exception as e:
        raise e
