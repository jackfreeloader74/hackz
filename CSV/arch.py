from bs4 import BeautifulSoup
import numpy
import csv

soup = BeautifulSoup(open('tools.html'),'html.parser')

html='''
    <tr>
        <td class=tbl-name itemprop="name">zerowine</td>
        <td class="tbl-version vcat" itemprop="version">0.0.2</td>
        <td class="tbl-description dcat" itemprop="description">Malware Analysis Tool - research project to dynamically analyze the behavior of malware</td>
        <td class=tbl-categorie itemprop="genre"><a class=hcat href="malware.html" title=" blackarch-malware "> blackarch-malware </a></td>
        <td class=tbl-homepage itemprop="mainEntityOfPage"><a href="http://zerowine.sf.net/" target="_blank"><i class="fas fa-external-link-alt fa-lg"></i></a></td>
    </tr>'''

#print(html)
# soup = BeautifulSoup(html,'html.parser')

with open('archtools.csv','w',newline='') as csvfile:
    for row in soup.find_all('tr'):
        name = row.find(itemprop="name").string
        description = row.find(itemprop="description").string
        genre = row.find(itemprop="genre").string
        ref = row.find(itemprop="mainEntityOfPage").a.get('href')
        array = [name,description,genre[:-1],ref]
        writecsv = csv.writer(csvfile,delimiter=',')
        writecsv.writerow(array)




    


    #array.tofile('archtools.csv', sep=',',format='%10.5f')
    #numpy.savetxt('archtools.csv',array,delimiter=',')
    

