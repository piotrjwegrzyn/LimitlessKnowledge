# BITEhack 2023 - Blindless Colours

The SaaS service that provides API for converting images to AM/FM modulated signals. Those signals are capable for being interpreted as music tones (samples), vibrations for wearable devices or anything else what might be helpful for blind people in learning colours.

## Dockerhub
The compiled container is available [on Dockerhub](https://hub.docker.com/r/piotrjwegrzyn/bitehack2023_blindless_colours).

## Building from source
To build from source clone repository and build an image:
```
git clone https://github.com/piotrjwegrzyn/bitehack2023_blindless_colours
cd bitehack2023_blindless_colours
docker build -t piotrjwegrzyn/bitehack2023_blindless_colours:latest .
```

## Runtime
To deploy this app type:
```
docker run -tip 8080:8080 piotrjwegrzyn/bitehack2023_blindless_colours
```
