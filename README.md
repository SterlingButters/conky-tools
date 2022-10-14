# conky-tools
 Collection of conky python utilities

```
sudo apt install conky-all

conky -c <path/to/conkyrc> 

```

There are a number of python utilities not linked to the conky config. This is because I'm just playing around with what I can do.
See the conkyrc for which python scripts are linked. You'll need to create a `.env` file with the following keys:

```
CANVAS_DOMAIN=<domain for institution e.g. http://canvas.tamu.edu/>
CANVAS_TOKEN=<Canvas access token>
LECTURES_PATH=<path/to/lectures>
EMAIL=<Edu email address>
PASSWORD=<Gmail "App password" (requires MFA setup)>

OWM_TOKEN=<>

SPOTIFY_ID = <>
SPOTIFY_SECRET = <>
```

Notes (until I can push the changes):
1) You'll need to adjust paths in conkyrc
2) I used odrive to sync my drive locations. Odds are you don't need the odrive command in the Lectures section.
