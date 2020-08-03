
# protoabm

An example of:
- developing an ABM in [mesa](https://mesa.readthedocs.io/en/master/) 
- deployment as a containerised app service. 

The current example is an implementation of Conway's game of life (based on mesa's own example) that adds:
- user configurable parameters,
- colour-coding cells according to their age, 
- tracking the "demographics" of the population,
- a logger component to display error messages.

See it in action [here](https://protoabm.azurewebsites.net)

## Development

First set up a virtualenv (optional), then install dependencies (not optional):
```
$ pip install -r requirements.txt
```
and run the server:
```
$ mesa runserver ./conways_game_of_life
```
which will automatically launch a browser window.

## Further Information

- [Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [mesa documentation](https://mesa.readthedocs.io/en/master/index.html)

## Images

To get the latest image: 
```bash
$ docker pull docker pull virgesmith/protoabm:latest
```

Or build your own:
```
$ docker build -t protoabm .
```
