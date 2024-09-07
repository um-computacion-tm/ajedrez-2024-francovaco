# Ajedrez Orientado a Objetos

Franco Vaccarezza 

## Testeos:

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-francovaco/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-francovaco/tree/main)

[![Maintainability](https://api.codeclimate.com/v1/badges/915564e25f37478337c6/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-francovaco/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/915564e25f37478337c6/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-francovaco/test_coverage)

## Descripción:

Este proyecto es un juego de ajedrez implementado en Python utilizando un enfoque orientado a objetos. El juego permite a dos jugadores enfrentarse, respetando parte las reglas estándar de los movimientos del ajedrez.

## Características:

El juego esta diseñado en Python orientado a objetos implementando algunas de las reglas del ajedrez.
El juego no cuenta con jaque, jaque mate, tablas, enrroque, coronación ni controles de tiempo.
El juego se ejecuta en la consola con un tablero mostrado en texto con símbolos Unicode. En este caso los símbolos estan invertidos, se utilizan los negros para las piezas blancas y los blancos par las piezas negras, ya que en la consola, con el fondo negro, los símbolos blancos se ven de color negro y los negros de color blanco. Es simplemente para no generar confusiones.
El código esta diseñado para futuras mejoras como puede ser una interfaz gráfica, guradado de partidas para su continuación en otro momento y el agregado de las reglas faltantes.
El juego finaliza cuando uno de los jugadores le come todas las piezas al otro o cuando los jugadores deseen finalizarlo ingresando la opción SALIR 

## ¿Como se juega?

Este ajedrez se juega como cualquier juego de ajedrez entre dos jugadores, inicia el juego con el turno de las fichas blancas y cada jugador va moviendo sus fichas y comiendo las del oponente en su turno. El jugador que se queda sin fichas pierde.
Además en cualquier momento de la partida los jugadores pueden finalizar el juego ingresando la opción SALIR. 

## Requisitos:

Para correr el juego se requiere [Docker](https://docs.docker.com) 

## Comandos que debe ejecutar desde la terminal

### Instalación:

Instalación de Docker

```bash
sudo apt install docker
```

Clonar el [repositorio](https://github.com/um-computacion-tm/ajedrez-2024-francovaco.git) del juego 

```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-francovaco.git
```
### Ejecutar el juego

Crear imágen de Docker del juego

```bash
docker buildx build -t ajedrez-2024-francovaco .
```

Ejecutar los tests y el juego

```bash
docker run -i ajedrez-2024-francovaco
```