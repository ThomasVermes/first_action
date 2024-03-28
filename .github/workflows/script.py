# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:44:39 2024

@author: vermest
"""
import yaml
import datetime
import os

# Definisci i nuovi valori per versione e data di rilascio
new_version = os.environ.get('RELEASE_TAG')
new_release_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Leggi il contenuto del file CITATION.cff
with open('../CITATION.cff', 'r') as file:
    cff_data = yaml.safe_load(file)

# Aggiorna i valori dei campi version e date-released
cff_data['version'] = new_version
cff_data['date-released'] = new_release_date

# Sovrascrivi il file con i dati aggiornati
with open('../CITATION.cff', 'w') as file:
    yaml.dump(cff_data, file)
