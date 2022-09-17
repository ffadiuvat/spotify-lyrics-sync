import configparser

from serial import Serial
from spotipy import Spotify, util

from daemon import Daemon
from displays import DisplayBroadcaster, LCDDisplay, TerminalDisplay
from playback import Playback
from providers.custom_provider import CustomLyricsProvider
from synchronizer import Synchronizer

cfg = configparser.ConfigParser()
cfg.read('./config.ini')

name = cfg['spotify']['username']
scope = cfg['oauth']['scope']
client_id = cfg['spotify']['client_id']
client_secret = cfg['spotify']['client_secret']
redirect_uri = cfg['oauth']['redirect_uri']

token = util.prompt_for_user_token(
  username=name,
  scope=scope,
  client_id=client_id,
  client_secret=client_secret,
  redirect_uri=redirect_uri,
)

if not token:
  raise Exception('Token are required!')

client = Spotify(auth=token)
engine = CustomLyricsProvider()
playback = Playback(client)

serial = Serial('COM4', 115200)
broadcaster = DisplayBroadcaster()
broadcaster.add_display(TerminalDisplay())
broadcaster.add_display(LCDDisplay(serial))

synchronizer = Synchronizer(broadcaster)
daemon = Daemon(engine, playback, synchronizer, broadcaster)


daemon.run()
