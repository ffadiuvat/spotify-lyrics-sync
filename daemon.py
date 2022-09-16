import time

from lrc_kit import SearchRequest

from playback import AddPlayingException, SpotifyNotRunningException


class Daemon:
  def __init__(self, engine, playback, display):
    self.should_run = True
    self.display = display
    self.engine = engine
    self.pb = playback

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
        print('\033[2J\033[2;0H\t♫ \033[1;35m {0} \033[0m - \033[1;32m {1} \033[0m'.format(self.pb.artist,self.pb.song))

        while( self.pb.is_playing and not self.pb.is_changed(prev['song'], prev['artist'])):
          if(not self.should_run):
            break
          if(not lyrics):
            self.display.show_no_lyric()
          else:
            timeline = lyrics.toSpotifyLyrics()
            self.display.show(timeline, self.pb.progress_ms)
          self.pb.current()
      except SpotifyNotRunningException:
        print(
          '\033[4;0H\033[K\t \033[1;36m >: Spotify Is Not Running :<\033[0m'
        )
        time.sleep(10)
      except AddPlayingException:
        print(
          '\033[4;0H\033[K\t \033[1;36m >: Playing Ads :<\033[0m'
        )
      except Exception as e:
        raise e
