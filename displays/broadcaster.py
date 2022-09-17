class DisplayBroadcaster:
  def __init__(self):
    self.displays = []

  def add_display(self, display):
    self.displays.append(display)

  def send(self, data):
    for display in self.displays:
      display.show(data)

  def send_raw(self, data):
    for display in self.displays:
      display.show_raw(data)

  def send_artist_title(self, artist, title):
    for display in self.displays:
      display.show_artist_title(artist, title)
