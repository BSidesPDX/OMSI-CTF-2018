# BSidesPDX OMSI CTF 2018

## WHAT

Challenges built by: [TTimzen](https://twitter.com/TTimzen) & [pwnpnw](https://twitter.com/pwnpnw)

## Challenges

| Challenge Name | Category | Points | Port |
|----------------|----------|--------|------|
| bfbo | pwn | 100 | 10001 |
| bfpl | pwn | 200 | 10002 |
| sgnirts  | re | 100 | NA |
| sup3rs3ri4l | re | 200 | NA |
| tmi | web | 100 | 5000 |
| buynow | web | 200 | 5001 |

All flags are in `/flag`

## Local Deployment

To locally test, deploy or play challenges with Docker, run the following (Ubuntu)

1. `sudo apt install gcc-multilib gcc-mipsel-linux-gnu gcc-arm-linux-gnueabi g++-multilib linux-libc-dev:i386`
1. `make`
1. `docker-compose build && docker-compose up -d`
1. Containers are viewable at localhost:PORT (view with docker-compose ps)
1. `docker-compose kill` to stop the containers
1. `make clean` to clean the source folders

## BSidesPDX Presents OMSI CTF

CTF was ran during [OMSI Portland Mini Maker Faire](https://portland.makerfaire.com/) on Sept 15th and 16th.

We used [CTFd](https://ctfd.io/) for the scoreboard hosted at [BSidesPDXCTF.party](https://bsidespdxctf.party/).
