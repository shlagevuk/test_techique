
import argparse
import csv
import json
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser(description="Insere les donnes d'un fichier CSV dans ES")
parser.add_argument("-f","--file",   required=True, action="store", type=str, help="chemin du fichier CSV")
parser.add_argument("-t","--target", required=True, action="store", type=str, help="adresse de ES")
parser.add_argument("-n","--name",   required=True, action="store", type=str, help="nom de l'index")
parser.add_argument("-v",            action="store", type=bool, help="verbose")
args = vars(parser.parse_args())

target_file= args["file"]
target_elastic= args["target"]
#todo gestion derreur
elastic_host= target_elastic.split(':')[0]
elastic_port= target_elastic.split(':')[1]
index_name= args["name"]
verbose= args['v']

#on recpere le contenu du csv
list=[]
with open(target_file , 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        list.append(row)

#on en sort les header (premiere ligne)
header=list.pop(0)
#connexion elasticearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

for item in list:
    if verbose:
        print("inserting")
        print(item)
    #insertion dnas ES, l'id correspond a la premiere colonne du csv
    # TODO ajouter une option "append" et ne plus prendre la premiere colonne du csv comme index
    es.index(index=args['file'], doc_type=index_name, id=item[0], body=json.dumps(dict(zip(header,item))))

#debug resultat
#print(es.get(index='test' + args['file'], doc_type='dealer', id=1))
