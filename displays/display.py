# import time
from abc import ABC, abstractmethod


class Display(ABC):
  @abstractmethod
  def show(self, data):
    pass

  @abstractmethod
  def show_raw(self, data):
    pass

  @abstractmethod
  def show_artist_title(self, artist, title):
    pass


class TerminalDisplay(Display):
  def show(self, data):
    print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(data))

  def show_artist_title(self, artist, title):
    print('\033[2J\033[2;0H\t♫ \033[1;35m {0} \033[0m - \033[1;32m {1} \033[0m'.format(artist,title))

  def show_raw(self, raw):
     print('\033[4;0H\033[K\t \033[1;36m >:{}:< \033[0m'.format(raw))
