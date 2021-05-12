# WeatherBach
A Discord Bot that tells you the weather if you provide it a zipcode. Written in Python on Repl.it.

- Please checkout my notes to see how I set up the Discord bot! Go [here](https://github.com/bndiep/discordbot-notes).

## Commands:
- !weather {zipcode}: Gives the current weather given the user's zipcode.
  - WIP: Temperature is incredibly high. Need to figure out what values the API is using to get a better temp reading.
  - The units are in Kelvin by default, so I need to include units parameter and set it to imperial (I know, gross... imperial).
  - Make sure to spell 'imperial' correctly!
- !testing: Test command that replies '1, 2, 3!'
