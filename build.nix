with import <nixpkgs> {};

python36.withPackages (ps: with ps; [
  spotipy
  requests
  python-telegram-bot
  ])
