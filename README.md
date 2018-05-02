

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

#h3 TODO divers:
- installation auto de filebeat + config
- creation auto des dashboard kibana
- fix probleme de volume avec docker


#2 A destination des front-end:

Les requêtes se font simplement via des GET sur le serveur.

Deux variables peuvent être passé dans la requête:
- index, spécifie l'index sur lequel porte la recherche, par defaut "dealer.csv"
- id, l'id de l'élement à rechercher, par defaut 1.

#h2 A destination des ops:

Pour lancer l'application il suffit de run les playbooks dans l'ordre suivant:
- elk/main.yml qui lance une stack elk officielle dans docker sur les serveurs spécifiés dans le fichier elk/hosts
`ansible-playbook -i hosts elk/main.yml`

- input_run/main.yml qui lance l'import des données dans la base elasticsearch utilisé par elk. Les fichiers d'import doivent se trouver dans `{{ home_path }}/data` et avoir une extension en .csv . Tout les fichiers csv sont importés dans des index différents ayant des noms correspondant aux fichiers. l'import des fichier est en one shot, le script python importe les données des csv et s'arrête. Il faut relancer le conteneur pour refaire un import. note: non testé, probleme de volumes.
`ansible-playbook -i hosts output_run/main.yml`

- output_run/main.yml qui lance le serveur permettant de requetter elasticsearch. Expose un port pour faire les requetes à parametrer au niveau ansible. Note: pas testé, manque de temps.

Note: Les conteneurs d'in/out de données sont sur le reseau du host. En todo assez important il faudrait les binds sur un réseau du au conteneur d'elasticsearch.
