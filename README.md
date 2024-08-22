# Ajedrez Orientado a Objetos

Franco Vaccarezza 

## Testeos

### CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-francovaco/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-francovaco/tree/main)

### Maintainability 
[![Maintainability](https://api.codeclimate.com/v1/badges/915564e25f37478337c6/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-francovaco/maintainability)

### Test Coverage 
[![Test Coverage](https://api.codeclimate.com/v1/badges/915564e25f37478337c6/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-francovaco/test_coverage)


## Descripción:

Este proyecto es un juego de ajedrez implementado en Python utilizando un enfoque orientado a objetos. El juego permite a dos jugadores enfrentarse, respetando parte las reglas estándar de los movimientos del ajedrez.

## Características:

El juego esta diseñado en Python orientado a objetos implementando algunas de las reglas del ajedrez. No cuenta con enroque, jaque, jaque mate y tablas.
El juego se ejecuta en la consola con un tablero mostrado en texto con simbolos Unicode.
El código esta diseñado para futuras mejoras como puede ser una interfaz gráfica, guradado de partidas para su continuación en otro momento y el agregado de las reglas faltantes.
El juego finaliza cuando uno de los jugadores le come todas las piezas al otro, cuando los jugadores deseen finalizarlo ingresando la opcion SALIR o cuando alguno de los  jugadores se quede sin posibles movimientos.

## ¿Como se juega?

El juego se juega como cualquier juego de ajedrez entre dos jugadores, inicia el juego con el turno de las fichas blancas y cada jugador va moviendo sus fichas y comiendo las del oponente en su turno. El jugador que se queda sin fichas pierde, o también pierde en el caso de que se quede sin posibles movimientos.
Además en cualquier momento de la partida los jugadores pueden finalizar la partida ingresando la opción SALIR. 

## Requisitos:

Para correr el juego se requiere Python 3.x

## instalación:

Clonar el [repositorio](https://github.com/um-computacion-tm/ajedrez-2024-francovaco.git) del juego 


```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-francovaco.git
```
Ejecutar el juego

Depués de clonar el repositorio se debe ingresar a la carpeta y dentro de ella en la terminal ejecutar el siguiente comando

```bash
python cli.py
```