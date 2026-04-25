set("log.stdout", true)

set("server.telnet", true)
set("server.telnet.port", 1234)
set("server.telnet.bind_addr", "0.0.0.0")

radio = mksafe(
  playlist(mode="normal", "/music")
)

output.icecast(
  %mp3(bitrate=128),
  host="icecast",
  port=8000,
  password="hackme",
  mount="/radio",
  radio
)
