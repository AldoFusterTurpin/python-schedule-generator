#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: aldofusterturpin
"""

import itertools

'''
Per a aquest programa, com he de fer un horari evitant que es solapin assignatures, faré
servir el següents codis per referir-me a les diferents hores dels diferents dies:
-----------------------------------------------------------------------------------
			dilluns 	dimarts 	dimecres 	  dijous 		divendres

8h-9h   	dilluns8	dimarts8    dimecres8    dijous8     divendres8
9h-10h  	dilluns9    dimarts9    dimecres9    dijous9     divendres9
10h-11h		dilluns10   dimarts10   dimecres10   dijous10    divendres10
11h-12h		dilluns11   dimarts11   dimecres11   dijous11    divendres11
12h-13h		dilluns12   dimarts12   dimecres12   dijous12    divendres12
13h-14h		dilluns13   dimarts13   dimecres13   dijous13    divendres13
14h-15h		dilluns14   dimarts14   dimecres14   dijous14    divendres14
15h-16h		dilluns15   dimarts15   dimecres15   dijous15    divendres15
16h-17h		dilluns16   dimarts16   dimecres16   dijous16    divendres16
17h-18h		dilluns17   dimarts17   dimecres17   dijous17    divendres17
18h-19h		dilluns18   dimarts18   dimecres18   dijous18    divendres18
19h-20h		dilluns19   dimarts19   dimecres19   dijous19    divendres19
20h-21h		dilluns20   dimarts20   dimecres20   dijous20    divendres20
------------------------------------------------------------------------------------
per ex: si una classe comença el dimecres a les 12h, aquella classe tindrà codi 'dimecres12',
per ex: si una classe comença el divendres a les 10h, aquella classe tindrà codi 'divendres10'
les classes sempre indiquen l'hora que comença, ja que comptaré que totes les classes duren una hora(realment
duren dos però separaré les classes de 2 hores en dues classes de 1 hora per comoditat de programació)
'''

# no s'usa
# def printar(mapa):
# 	for i in mapa:
# 		print("KEY: {} --------> VALUE: {}".format(i, mapa_assig[i]))
########################################################################################################


# al final no utilitzo aquesta funció però pot ser molt útil
# def crearMatriu(n_files, m_columnes, ini_val):
# 	'''retorna una matriu de n_files x m_columnes inicialitzada al valor passat com a tercer parámetre'''
# 	matriu = [0] * n_files
# 	for i in range(n_files):
# 		matriu[i] = [ini_val] * m_columnes
# 	return matriu
# 	#return [[ini_val for ini_val in range(m_columnes)] for y in range(n_files)] #equivalent a tota la funció usant list comprehensions en una sola línia
#######################################################################################################
# test:
# print(crearMatriu(5,2, -1))


def horariMatins():
    '''
    cada element de la llista es una altre llista, que conté en aquest ordre:
    grup concret de l'assignatura
    assignatura
    hora inici 1(per ex.dilluns de 8h a 9h -> seria dilluns8),
    hora inici 2 (per ex.dijous de 14h a 15h -> seria dijous14),
    hora inici 3,
    hora inici 4
    (no cal distingir si lab o teoria)
    '''
    # quatre llistes diferents, en una mateixa llista agrupo tots els subgrups d'una mateixa assignatura
    # això ho faig així perquè desprès, hauré de fer totes les combinacions possibles entre diferents grups però
    # de diferents assignatures, de tal manera que per poder-ho fer facilment, agrupo cada assig en una llista diferent
    # i desprès faré servir la biblioteca 'itertools' perquè hem fagi totes les combinacions d'elements entre els elements de les
    # quarte llistes(producte cartesià). Agafa un sol element de cada llista i fa la combinació amb les altres llistes. Més clarament, exemple:
    # l1 = ['a','b','c']
    # l2 = [1, 2, 3]
    # l1 = [True, False]
    # I la combinació que he explicat abans, donaria:
    # (a, 1, True)
    # (a, 1, False)
    # (a, 2, True)
    # (a, 2, False)
    # etc..

    l1 = [['AC_11', 'AC', 'dilluns8', 'dilluns9', 'dimecres9', 'divendres13'],
          ['AC_12', 'AC', 'dilluns8', 'dilluns9', 'divendres12', 'divendres13'],
          ['AC_13', 'AC', 'dilluns8', 'dilluns9', 'dimecres8', 'divendres13'],
          ['AC_21', 'AC', 'dilluns10', 'dilluns11', 'dijous9', 'dijous10'],
          ['AC_22', 'AC', 'dilluns10', 'dilluns11', 'dimecres10', 'dijous10'],
          ['AC_31', 'AC', 'dimarts8', 'dimarts9', 'dijous8', 'divendres10'],
          ['AC_32', 'AC', 'dimarts8', 'dimarts9', 'dijous8', 'dijous12'],
          ['AC_33', 'AC', 'dimarts8', 'dimarts9', 'dijous8', 'dijous11']]

    l2 = [['IDI_11', 'IDI', 'dimarts8', 'dimarts9', 'divendres8', 'divendres9'],
          ['IDI_12', 'IDI', 'dimarts8', 'dimarts9', 'divendres8', 'divendres9'],
          ['IDI_13', 'IDI', 'dimarts8', 'dimarts9', 'divendres8', 'divendres9'],
          ['IDI_21', 'IDI', 'dimarts10', 'dimarts11', 'divendres10', 'divendres11'],
          ['IDI_22', 'IDI', 'dimarts10', 'dimarts11', 'divendres10', 'divendres11'],
          ['IDI_23', 'IDI', 'dimarts10', 'dimarts11', 'divendres10', 'divendres11'],
          # 'IDI_24': None, AQUEST GRUP NO, QUE ESTA EN RESERVA!
          ['IDI_31', 'IDI', 'dimarts12', 'dimarts13', 'divendres12', 'divendres13'],
          ['IDI_32', 'IDI', 'dimarts12', 'dimarts13',
           'divendres12', 'divendres13'],
          ['IDI_33', 'IDI', 'dimarts12', 'dimarts13', 'divendres12', 'divendres13']]

    l3 = [['AS_11', 'AS', 'divendres10', 'divendres11', 'dilluns8', 'dilluns9'],
          ['AS_12', 'AS',  'divendres10', 'divendres11', 'dilluns10', 'dilluns11'],
          ['AS_13', 'AS', 'divendres10', 'divendres11', 'dilluns12', 'dilluns13']]

    l4 = [['ER_11', 'ER', 'dimecres8', 'dimecres9', 'dijous12', 'dijous13'],
          ['ER_12', 'ER', 'dimecres8', 'dimecres9', 'dijous8', 'dijous9'],
          ['ER_13', 'ER', 'dimecres8', 'dimecres9', 'divendres12', 'divendres13']]

    llista = []
    llista.append(l1)
    llista.append(l2)
    llista.append(l3)
    llista.append(l4)

    # _______________
    # retorna una llista de tuples(on cada tupla és una combinació de les 4 assignatures)->cada tupla conté 4 llistes,
    # cadascuna  d'aquestes llistes representa la info d'1 subgrup d'una assignatura concreta
    llista_combinacions = list(itertools.product(*llista))
    # _______________

    # debug info, per veure quin format té la llista amb el producte cartesià de les assignatures
    # print("-" * 100)
    # print("-" * 100)
    # print("llista_combinacions({} combinacions possibles):".format(len(llista_combinacions)))
    # print(llista_combinacions)
    # print("-" * 100)
    # print("-" * 100)

    grups_no_solapats = [
        i for i in llista_combinacions if (horaris_no_es_solapen(i))]

    # debug info
    # print("Hi ha {} combinacions de grups que no es solapen, són les següents: ".format(len(grups_no_solapats)))
    # [print(i, "\n\n") for i in grups_no_solapats] #debug info

    # per saber cuantes combinacions passen el filtre
    comptador = 0

    # a info[0] guardo tots els grups de l'assignatura AC per saber quin marge tinc a la hora de fer l'horari
    # a info[1] guardo tots els grups de l'assignatura IDI per saber quin marge tinc a la hora de fer l'horari
    # les altres 2 assignatures no cal aquesta info pk van fixes perquè he fet prematrícula
    info = [set(), set()]  # llista amb 2 sets buits
    print("Combinació de grups que no es solapen i passen filtres")
    for tupla_assignatures in grups_no_solapats:
        # print("tupla_assignatures -> {}".format(tupla_assignatures))#debug info
        if (passa_filtres(tupla_assignatures)):
            comptador += 1
            # assignem a cada assignatura la seva info
            info_assig0 = tupla_assignatures[0]
            info_assig1 = tupla_assignatures[1]
            info_assig2 = tupla_assignatures[2]
            info_assig3 = tupla_assignatures[3]

            # el grup de la assignatura sempre es troba a la posició zero
            grup_assig0 = info_assig0[0]
            grup_assig1 = info_assig1[0]
            grup_assig2 = info_assig2[0]
            grup_assig3 = info_assig3[0]

            # com són sets, ignorarà els repetits, que es precisament el que vull aquí per saber els diferents
            # grups disponibles d'una mateixa assignatura
            info[0].add(grup_assig0)
            info[1].add(grup_assig1)

            print(grup_assig0)
            print(grup_assig1)
            print(grup_assig2)
            print(grup_assig3)
            print("-"*10)  # delimitació visual

    print("{} combinacions han passat el filtre".format(comptador))

    print("{} grups diferents disponibles d' AC:".format(len(info[0])), end=' ')
    [print(i, end=', ')for i in info[0]]

    print("\n{} grups diferents disponibles d' IDI:".format(len(info[1])), end=' ')
    [print(i, end=', ')for i in info[1]]
    print()
    # print(info) #debug info
############################################################################################


def horaris_no_es_solapen(tuple_in: tuple):
    '''La funció espera una tupla de 4 llistes on cada llista es la info d'una assigantura,
    retorna True si els grups no es solapen, altrament retorna False'''
    assig0 = tuple_in[0]
    assig1 = tuple_in[1]
    assig2 = tuple_in[2]
    assig3 = tuple_in[3]
    #________________________
    # debug info:
    # print("assig0 -> ", assig0)
    # print("assig1 -> ", assig1)
    # print("assig2 -> ", assig2)
    # print("assig3 -> ", assig3)
    #________________________
    llista_aux = []
    # afegim a la llista aux les (hora+dia) de les diferents classes i després recorrem aquesta per mirar solapament(+ info a sota)
    for i in assig0[2:]:  # assig1[2:] perquè les hores de classe estàn a la pos 2,3,4,5 de cada llista que és la info que aquí necessitem
        llista_aux.append(i)

    for i in assig1[2:]:
        llista_aux.append(i)

    for i in assig2[2:]:
        llista_aux.append(i)

    for i in assig3[2:]:
        llista_aux.append(i)

    # a llista_aux tenim els strings que representen els horaris de les assignatures,
    # ara només hem de mirar que cada element aparegui només un cop, ja que sinó, vol dir que
    # 2 subgrups de diferents assigantures començen a la mateixa hora i mateix dia, per tant aquell
    # horari ja no és vàlid
    for i in llista_aux:
        if llista_aux.count(i) != 1:  # si algun horari coincideix, és a dir,
            return False  # diferents assignatures comencen a mateix dia i hora -> retorna False
    return True  # altrament retorna True ja que cada hora i dia de cada assignatura apareix només un cop la combinació actual
################################################################################################


def passa_filtres(tuple_combinacions: tuple):
    '''Funció que reb una tupla de llistes d'assignatures(cada llista de la tupla és la info d'1 assignatura)
    i retorna true si compleixen les condicions que jo vull.
    per ex: que aparegui l' assignatura AS del grup 13, etc.
    Retorna cert si el conjunt d'assignatures passa el filtre; altrament retorna False'''

    # primer filtre: aquelles combinacions que apareix el grup 12 de AS
    # segon filtre: aquelles combinacions que apareix el grup 11 de Er

    # print("tuple_combinacions(el que reb la funcio): {}".format(tuple_combinacions)) #debug info

    condicio1 = condicio2 = False

    for llista in tuple_combinacions:
        if (llista[0] == 'AS_13'):
            condicio1 = True
        elif (llista[0] == 'ER_11'):
            condicio2 = True

    return (condicio1 and condicio2)


############################################################################################



# main
quatri = "2017/2018_Q2"
print("Program made by ALDO FUSTER TURPIN")
print("------------- HORARIS DEL QUATRI {}: -------------".format(quatri))
horariMatins()
