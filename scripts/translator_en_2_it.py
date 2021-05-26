# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:27:58 2021

@author: AParmiggiani
"""

import shutil
import fileinput
#import sys

def replace_line(filename, text_to_search, replacement_text):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


try:
    shutil.rmtree('../content/it')
except:
    print(' \'../content/it\' directory not present')

shutil.copytree('../content/en', '../content/it')

replace_line('../content/it/authors/admin/_index.md', 
             'role: Facility Coordinator', 'role: Coordinatore di Facility')
replace_line('../content/it/authors/admin/_index.md', 
             'bio: My research interests include mechatronics, additive manufacturing, compliant mechanisms and robotics.',
             'bio: ')
replace_line('../content/it/authors/admin/_index.md',
             '- Mechatronics', '- Meccatronica')
replace_line('../content/it/authors/admin/_index.md',
             '- Robotics', '- Robotica')
replace_line('../content/it/authors/admin/_index.md',
             '- Additive Manufacturing', '- Fabbricazione Additiva')
replace_line('../content/it/authors/admin/_index.md',
             '- Digital Fabrication', '- Fabbricazione Digitale')
replace_line('../content/it/authors/admin/_index.md',
             '- Topology Optimization', '- Ottimizzazione Topologica')
replace_line('../content/it/authors/admin/_index.md',
             '- Compliant Mechanisms', '- Meccanismi Flessibili')
             

bio_str = """La costruzione di macchine e dispositivi meccanici mi appassiona da sempre.
Oggi mi occupo dello sviluppo di meccanismi ad alte prestazioni con movimentazioni complesse ma di semplice realizzazione, sfruttando i limiti delle tecnologie di fabbricazione per realizzare sistemi efficienti ed economici.

Questa pagina presenta una panoramica del mio lavoro degli ultimi anni.

### Breve Biografia

Nel 2006 ho conseguito la Laurea Magistrale con lode in Ingegneria Meccanica presso l'Università degli Studi di Modena e Reggio Emilia.
Mi sono poi trasferito a Genova dove ho iniziato il dottorato di ricerca all'Istituto Italiano di Tecnologia (IIT).
In IIT, ho lavorato allo sviluppo hardware del robot umanoide iCub con Lorenzo Natale, Giorgio Metta and Giulio Sandini.

Dopo aver conseguito il dottorato sono rimasto in IIT, dove ho assunto la guida dello sviluppo hardware del progetto iCub, come PostDoc a partire dal 2010 e come Tecnologo dal 2016.
Nell'agosto del 2019 sono diventato il coordinatore della facility IIT per la progettazione e la costruzione di sistemi meccanici.

<!--
{{< icon name="download" pack="fas" >}} Download my {{< staticref "media/demo_resume.pdf" "newtab" >}}resumé{{< /staticref >}}.
-->"""

with fileinput.FileInput('../content/it/authors/admin/_index.md', inplace=True) as file: 
    for idx, line in enumerate(file):
        if idx == 81: break
        else: print(line, end='')
    print(bio_str, end='')

replace_line('../content/it/home/about.md', 
             'title: About Me', 'title: Su Di Me')
replace_line('../content/it/home/contact.md', 
             'title: Contact', 'title: Contatti')
replace_line('../content/it/home/featured.md', 
             'title: Featured Publications', 'title: Pubblicazioni Scelte')
replace_line('../content/it/home/publications.md', 
             'title: Recent Publications', 'title: Ultime Pubblicazioni')
replace_line('../content/it/home/projects.md', 
             'title: Projects', 'title: Progetti')
replace_line('../content/it/home/projects.md', 
             'subtitle: ''', 'subtitle: (Inglese)')


