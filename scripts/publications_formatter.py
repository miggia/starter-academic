# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:27:58 2021

@author: AParmiggiani
"""

import shutil
import fileinput

def replace_line(filename, text_to_search, replacement_text):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')

def add_project_line(filename, project_name):
    with fileinput.FileInput(filename, inplace=True) as file: 
        for idx, line in enumerate(file):
            if ('---' in line and idx > 2) : break
            else: print(line, end='')
        print('projects:\n', end='')
        print('- ' + project_name + '\n', end='')
        print('---')


# setting selected publications
replace_line('../content/en/publication/parmiggiani-21-effect/index.md', 
             'featured: false', 'featured: true')
replace_line(r'../content/en/publication/parmiggiani-17-design/index.md', 
             'featured: false', 'featured: true')
replace_line('../content/en/publication/parmiggiani-12-design/index.md', 
             'featured: false', 'featured: true')
replace_line('../content/en/publication/shah-19-comparison/index.md', 
             'featured: false', 'featured: true')

# setting projects to papers
icub_papers_list = ['../content/en/publication/billier-19-robot/index.md',
                    '../content/en/publication/bsili-18-evolutionary/index.md',
                    '../content/en/publication/eljaik-13-quantitative/index.md',
                    '../content/en/publication/natale-14-sensorimotor/index.md',      
                    '../content/en/publication/parmiggiani-09-joint/index.md', 
                    '../content/en/publication/parmiggiani-12-design/index.md', 
                    '../content/en/publication/parmiggiani-12-mechatronic/index.md',
                    '../content/en/publication/parmiggiani-14-alternative/index.md',
                    '../content/en/publication/parmiggiani-14-articulated/index.md', 
                    '../content/en/publication/parmiggiani-14-performance/index.md', 
                    '../content/en/publication/parmiggiani-15-design/index.md',
                    '../content/en/publication/sureshbabu-15-new/index.md'
                    ]

r1_papers_list = ['../content/en/publication/fiorio-17-parallel/index.md',
                  '../content/en/publication/lehmann-16-head/index.md',
                  '../content/en/publication/parmiggiani-17-design/index.md',
                  '../content/en/publication/sureshbabu-17-design-cost/index.md',      
                  '../content/en/publication/sureshbabu-17-design-force/index.md', 
                  '../content/en/publication/sureshbabu-17-parallel/index.md'         
                  ]

nuu_mech_papers_list = ['../content/en/publication/shah-18-comparison/index.md',
                        '../content/en/publication/shah-18-workspace/index.md',
                        '../content/en/publication/shah-19-comparison/index.md'
                        ]


am_composites_papers_list = ['../content/en/publication/parmiggiani-21-effect/index.md',
                             '../content/en/publication/pizzorni-21-adhesive/index.md'
                             ]

am_flexible_mech_papers_list = []

for paper in icub_papers_list:
    add_project_line(paper, 'icub')

for paper in r1_papers_list:
    add_project_line(paper, 'r1')

for paper in nuu_mech_papers_list:
    pass

for paper in am_composites_papers_list:
    pass


