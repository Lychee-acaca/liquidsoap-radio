import socket
import readline  # noqa: F401

HELP = """\
commands:
  n  -> next song
  l  -> list queue
  q  -> quit
"""


def send(cmd):
    with socket.socket() as s:
        s.connect(("localhost", 1234))
        s.sendall((cmd + "\n").encode())
        return s.recv(8192).decode(errors="ignore")


def next_song():
    send("music.skip")


def get_queue():
    raw = send("request.all")
    return [x for x in raw.split() if x.isdigit()]


def get_metadata(rid):
    return send(f"request.metadata {rid}")


def print_queue():
    for rid in get_queue():
        print("----")
        print(get_metadata(rid))


print(HELP)

# =========================
# CLI LOOP
# =========================
while True:
    cmd = input("> ").strip()

    if cmd == "n":
        next_song()

    elif cmd == "l":
        print_queue()

    elif cmd == "q":
        break

    else:
        print(HELP)
