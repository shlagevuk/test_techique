
import csv
import json
from elasticsearch import Elasticsearch
import glob
import os
_path_csv="/data"

#connexion elasticearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#on liste les fichiers a parser
files_list = glob.glob(_path_csv + "/*.csv" )
print("INFO parsing " + str(files_list))

for file in files_list:
    data_list= []
    with open(file , 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data_list.append(row)
    #on en sort les header (premiere ligne)
    header=data_list.pop(0)

    for item in data_list:
        print("INFO inserting " + str(item))
        #insertion dnas ES, l'id correspond a la premiere colonne du csv
        # TODO ajouter une option "append" et ne plus prendre la premiere colonne du csv comme index
        es.index(index=os.path.basename(file), doc_type='text', id=item[0], body=json.dumps(dict(zip(header,item))))

#debug resultat
#print(es.get(index='test' + args['file'], doc_type='dealer', id=1))
