import time


class Display:

  def show(self, timeline, progress_ms):
    tl = timeline
    for n in range(1, len(tl)):
      if (progress_ms <= tl[n]['startTimeMs'] and progress_ms >= tl[n-1]['startTimeMs']):
        current_line = tl[n-1]['words']
        print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
        sleep_time = (abs(tl[n]['startTimeMs']-progress_ms)/1000)+1
        time.sleep(sleep_time)
        print('\033[10;0H\033[?25h')

  def show_no_lyric(self):
    current_line = " >: Don't have lyrics right now :< "
    print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
    sleep_time=5.0
    time.sleep(sleep_time)
