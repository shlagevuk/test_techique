

- ajout des donnees en CSV dans une BDD: OK
- Exposer service web: OK
- Conteneuriser: ~ MEH probleme de bind sur l'import et pas de test sur le serveur
- Automatisation des conteneurs: TODO
- Monitoring: TODO ~ elk ok mais pas de log docker & pas d'alerting auto
- gestion de log: elk + filebeat
- mise a jour simple des donnnes: OK
- inclure ES avec recherche full text: OK


Utilisation d'une stack elk docker a des fin de log/monitoring.

Reutilisation de elastic et kibana pour le stockage et la visualisation des données.

scripts python pour le feed des données et maj; et serveur web pour les requetes

TODO divers:
- installation auto de filebeat + config
- creation auto des dashboard kibana
- fix probleme de volume avec docker


Bon et ça manque de testing tout ça ^^'
