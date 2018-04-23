# notificationSlack
Notificaciones en web hook slack

#install library
python -m pip install requests --user --no-warn-script-location
python -m pip install fire --user --no-warn-script-location

#add permission run after clone repository
chmod +x notification.py

#Modo de uso
Despues de otorgar permisos para ejecucion, los parametros que reciben son:
    text    -Requerido
    title   -Opcional
    footer  -Opcional
    status  -Opcional   ['good' *valor por default, 'warning', 'danger', '<color en hex>']

Funciones deplegadas
    deploy
    pull-request
    notification

Invocación de las funciones
    ./notification.py --text="El despligue de en las instancias de produccion se ha realizado con exito" --footer="WAR 2.6.12" deploy
    ./notification.py --text="Ocurrio un problema con el ultimo WAR no inicia session" --footer="WAR 2.6.12" --status="danger" deploy

    ./notification.py --text="Se solicita el siguiente pull-request" --title="Solicitud de pull-request CodeCommit"--footer="feature-new-user -> dev" pull-request
    ./notification.py --text="El pull request tiene unos detalles que correguir antes de confirmar"--footer="feature-payments -> dev" --status="warning" pull-request

    ./notification.py --text="Este solo es un mensaje para el grupo" notification


