#!/usr/bin/env python
import os, sys
from xml.dom import minidom
'''
    Esta parte está fija y va cabiando dependiendo si se trata de un legado u otro
    print("\t<title>Festival de Música Tradicional de La Alpujarra</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/fondo-festival-de-musica-tradicional-de-la-alpujarra</link>")
    print("\t<description>El Festival de Música Tradicional de la Alpujarra, representa la principal manifestación cultural y musical del folclore alpujarreño. Es portador y conservador de la memoria cultura, folclórica e histórica de la comarca. Se celebra con carácter anual desde 1982, el segundo domingo  de agosto, en alguna localidad de las Alpujarra granadina o almeriense, que varía para cada ocasión. Tiene carácter de concurso, otorgándose varios premios según especialidades.</description>")

    print("\t<title>Legado Manuel Castillo</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/legado-manuel-castillo</link>")
    print("\t<description>Fue una figura dominante de la vida musical andaluza durante la segunda mitad del siglo XX, perteneciente a la Generación del 51.Su producción comprende cerca de 130 obras, abarcando la mayoría de los géneros musicales y estilos, a excepción del género operístico: mención especial merece su obra para piano.</description>")

    print("\t<title>Legado Rafael Díaz</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/legado-rafael-diaz</link>")
    print("\t<description>Rafael Díaz nació en Málaga en 1943 y en su Conservatorio hizo la carrera de Piano y Clarinete, posteriormente pasó al Conservatorio de Sevilla donde realizó con Manuel Castillo la carrera de Composición obteniendo Premio Fin de Carrera en Composición y con Manuel Galduf la carrera de Dirección de Orquesta.</description>")

    print("\t<title>Legado del tenor Manuel Villalba</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/legado-del-tenor-manuel-villalba</link>")
    print("\t<description>Manuel Villalba (1912-2001) fue un tenor sevillano conocido principalmente en los círculos cofrades de la ciudad hispalense. En 1935, con 23 años, regresó del Conservatorio de Madrid y en Sevilla consiguió los cargos de Seise y Comendador del Coro de Canónigos de la Catedral de Sevilla y profesor del conservatorio. Al parecer creó y dirigió una pequeña compañía de músicos, a modo de capilla musical, que se encargaba de los diversos cultos cofrades de una manera más o menos profesional.</description>")

    print("\t<title>Juan Alfonso García</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/juan-alfonso-garcia</link>")
    print("\t<description>Nacido en Los Santos de Maimona (Badajoz), el compositor y organista se establece en Granada a partir de 1946, donde cursa estudios eclesiásticos de humanidades y filosofía escolástica. Además, estudió piano y armonía en el conservatorio de Granada y órgano en el conservatorio de Sevilla.Juan Alfonso García fue sacerdote y organista de la catedral de Granada durante más de cuarenta años, además fue secretario de la cátedra Manuel de Falla de la Universidad de Granada entre 1971 y 1977 y, después, nombrado director honorífico de la misma. También destaca su puesto como comisario del Festival Internacional de Música y Danza de Granada y su membresía en el patronato de la casa-museo Manuel de Falla.</description>")
'''
def analiza_datafield(datafield, lista_codes):
        '''
        En esta función analizamos todas los datafield que hay dentro de cada record.
        '''
        datafields = datafield.getElementsByTagName("subfield")
        i = -1
        texto = ''
        for subfield in datafields:
            letra_subfield = subfield._attrs['code'].nodeValue
            i += 1
            if letra_subfield in lista_codes:
                subfield = datafield.getElementsByTagName("subfield")[i]
                texto += subfield.firstChild.data
        return texto

def carga(fichero):
    xml = minidom.parse(fichero)
    versionA= 'version="1.0"'
    versionA= 'version="1.0"'
    versionB= '<rss version="2.0">'
    encoding= 'encoding="UTF-8"'
    print(f'{"<?xml "}',versionA,encoding,' ?>')
    print(versionB)
    print("<channel>")
    print("\t<title>Legado Germán Álvarez-Beigbeder</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/legado-german-alvarez-beigbeder</link>")
    print("\t<description>Germán Álvarez Beigbeder (Jerez de la Frontera, 1882-1968), compositor y director, inmerso en el andalucismo musical, pero indagando también en la música francesa, sobre todo de César Franck y Saint-Saens, sin olvidar a los grandes del romanticismo europeo: Schumann o Johannes Brahms. Caracterizado por su gran facilidad melódica y firmeza en la armonía, entre sus obras figuran sinfonías y numerosas composiciones pianísticas, oratorios, instrumentales para orquesta y banda, etc.</description>")
    
    records = xml.getElementsByTagName("record")
    for record in records:
        #Lo primero generamos por defecto la cabecera para el rss
        print("\t<item>")
        '''
        Recorremos todos los record y dentro de cada record vemos todos los datafield del archivo que cargemos
        Si el datafield es un tag='245' que nos muestre el code a y b
        Si el datafield es un tag='260' que nos muestre el code a,b y c
        Si el datafield es un tag='505' que nos muestre el a y/o si hay tag='111' que muestre el code a,n,d y c
        '''
        descripcion = ''
        for datafield in record.getElementsByTagName("datafield"):
            tag = datafield._attrs['tag'].value
            if tag == '245':
                titulo = analiza_datafield(datafield, ['a','b'])
            if tag == '260':
                descripcion += analiza_datafield(datafield, ['a','b','c','e','f'])
            if tag == '505':
                descripcion += analiza_datafield(datafield, ['a'])
            if tag == '500':
                descripcion += analiza_datafield(datafield, ['a'])
            if tag == '597':
                descripcion += analiza_datafield(datafield, ['a'])
            if tag == '111':
                descripcion += analiza_datafield(datafield, ['a','n','d','c'])

        controlfield = record.getElementsByTagName("controlfield")[0]
        tagA = controlfield.attributes._attrs['tag'].nodeValue
        if tagA == '001':
            controlfield=controlfield.firstChild.data
            ini = 1 #posición inicial
            subcadena = controlfield[ini: -3]
            print(f"\t\t<title>{titulo}</title>")
            print(f"\t\t<link>https://www.juntadeandalucia.es/cultura/idea/opacidea/abnetcl.cgi?TITN={subcadena}</link>")
            print(f"\t\t<description>{descripcion}</description>")
        
        print("\t</item>")
    print("</channel>")
    print("</rss>")


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            carga(arg)