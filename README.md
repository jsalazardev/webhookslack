# NotificationSlack

## Install library

- python -m pip install requests --user
- python -m pip install fire --user
- python -m pip install configparser --user

## Add permission run after clone repository

- chmod +x notification.py

# Modo de uso

## Parametros de la aplicación

###### Parametros
1. text        - Requerido
2. title       - Opcional
3. footer      - Opcional
4. status      - Opcional
5. username    - Opcional
6. field       - Opcional

###### Posibles valores
- status
  - good    [green] 'valor por default'
  - warning [yellow]
  - danger  [red]
  - [add color hex]

- username
  - deploy          [Amazon EC2]
  - pull-request    [Amazon CodeCommit]
  - notification    [Application]

## Funciones deplegadas
- deploy
- pull-request
- war
- notification

## Invocación de las funciones
- deploy
  - notification.py --text="El despligue de en las instancias de produccion se ha realizado con exito" --footer="WAR 2.6.12" deploy
  - notification.py --text="Ocurrio un problema con el ultimo WAR no inicia session" --footer="WAR 2.6.12" --status="danger" deploy
- pull-request
  - notification.py --text="Se solicita el siguiente pull-request" --title="Solicitud de pull-request CodeCommit"--footer="feature-new-user -> dev" pull-request
  - notification.py --text="El pull request tiene unos detalles que correguir antes de confirmar"--footer="feature-payments -> dev" --status="warning" pull-request
- war
  - notification.py --text="Se ha creado el siguiente war para despliegue" --field="http://host.domain.com" --footer="2.5.4" war
- notification
  - notification.py --text="Este solo es un mensaje para el grupo" notification
  - notification.py --text="Este solo es un mensaje para el grupo" --username="Terminal Unix" notification