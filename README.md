# liquidsoap-radio

A minimal internet radio system built with Liquidsoap + Icecast, controlled via a simple Python CLI for queue-based playback.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone git@github.com:Lychee-acaca/liquidsoap-radio.git
cd liquidsoap-radio
```

### 2. Add music files

Put your audio files into the `music/` directory.

Supported formats:

- mp3
- flac
- wav

### 3. Start the system

```bash
docker compose up -d
```

This will start:

- Liquidsoap streaming server
- Icecast streaming server

After starting the system, open:

http://0.0.0.0:8123/radio

If the system is running correctly, audio should start streaming immediately.

To change the default port, edit `docker-compose.yml`.

### 4. Run the controller

```bash
python control.py
```
