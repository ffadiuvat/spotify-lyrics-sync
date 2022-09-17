import time


class Synchronizer:
  def __init__(self, broadcaster):
    self.broadcaster = broadcaster

  def show_artist_title(self, artist, title):
    self.broadcaster.send_artist_title(artist, title)

  def sync(self, timeline, progress_ms):
    tl = timeline
    for n in range(1, len(tl)):
      if (progress_ms <= tl[n]['startTimeMs'] and progress_ms >= tl[n-1]['startTimeMs']):
        current_line = tl[n-1]['words']
        self.broadcaster.send(current_line)
        sleep_time = (abs(tl[n]['startTimeMs']-progress_ms)/1000)+1
        time.sleep(sleep_time)
        # print('\033[10;0H\033[?25h')

  def show_no_lyric(self):
    self.broadcaster.send_no_lyric()
