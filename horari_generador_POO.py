#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: aldofusterturpin
"""

# per realitzar deepcopy() i evitar copiar només les referències, sinó estem
# fent una shallowcopy que no ens interessa
# per la combinació de grups
import copy

# per fer producte cartesià (les combinacions)
import itertools


def conversor(dia: str, hora: int):
    """Donat un dia i una hora en format ("dilluns", 8) retorna la tuple de 2
    índexos (x,y)que indica a quina fila i col és correspon a la classe
    TaulaMostraHorari"""
    # NOTA IMPORTANT: a la classe TaulaMostraHorari:
    # el dilluns a les 8 és (0,1)
    # el dilluns a les 9 és (1,1)
    # el dilluns a les 10 és (2,1)
    # ...
    # el dimarts a les 8 és (0,2)
    # el dimarts a les 9 és (1,2)
    # el dimarts a les 10 és (2,2)
    # etc
    # Això és així ja que el que és la matriu en sí a la classe TaulaMostraHorari és:
    # 8:00h           None            None            None            None            None
    #
    # 9:00h           None            None            None            None            None
    #
    # 10:00h          None            None            None            None            None
    # etc
    # ja que la fila "dilluns dimarts ..." està guardada en un altre atribut de
    # la classe TaulaMostraHorari i no es considera part de la matriu que
    # guarda la info dels objectes (tot i que a la hora de printar es mostra
    # COM SI fos una sola matriu)

    if (dia == "dilluns" and hora == 8):
        return (0, 1)

    if (dia == "dimarts" and hora == 8):
        return (0, 2)
    if (dia == "dimecres" and hora == 8):
        return (0,  3)
    if (dia == "dijous" and hora == 8):
        return (0, 4)
    if (dia == "divendres" and hora == 8):
        return (0, 5)

    if (dia == "dilluns" and hora == 9):
        return (1, 1)
    if (dia == "dimarts" and hora == 9):
        return (1, 2)
    if (dia == "dimecres" and hora == 9):
        return (1, 3)
    if (dia == "dijous" and hora == 9):
        return (1, 4)
    if (dia == "divendres" and hora == 9):
        return (1, 5)

    if (dia == "dilluns" and hora == 10):
        return (2, 1)
    if (dia == "dimarts" and hora == 10):
        return (2, 2)
    if (dia == "dimecres" and hora == 10):
        return (2, 3)
    if (dia == "dijous" and hora == 10):
        return (2, 4)
    if (dia == "divendres" and hora == 10):
        return (2, 5)

    if (dia == "dilluns" and hora == 11):
        return (3, 1)
    if (dia == "dimarts" and hora == 11):
        return (3, 2)
    if (dia == "dimecres" and hora == 11):
        return (3, 3)
    if (dia == "dijous" and hora == 11):
        return (3, 4)
    if (dia == "divendres" and hora == 11):
        return (3, 5)

    if (dia == "dilluns" and hora == 12):
        return (4, 1)
    if (dia == "dimarts" and hora == 12):
        return (4, 2)
    if (dia == "dimecres" and hora == 12):
        return (4, 3)
    if (dia == "dijous" and hora == 12):
        return (4, 4)
    if (dia == "divendres" and hora == 12):
        return (4, 5)

    if (dia == "dilluns" and hora == 13):
        return (5, 1)
    if (dia == "dimarts" and hora == 13):
        return (5, 2)
    if (dia == "dimecres" and hora == 13):
        return (5, 3)
    if (dia == "dijous" and hora == 13):
        return (5, 4)
    if (dia == "divendres" and hora == 13):
        return (5, 5)

    if (dia == "dilluns" and hora == 14):
        return (6, 1)
    if (dia == "dimarts" and hora == 14):
        return (6, 2)
    if (dia == "dimecres" and hora == 14):
        return (6, 3)
    if (dia == "dijous" and hora == 14):
        return (6, 4)
    if (dia == "divendres" and hora == 14):
        return (6, 5)

    if (dia == "dilluns" and hora == 15):
        return (7, 1)
    if (dia == "dimarts" and hora == 15):
        return (7, 2)
    if (dia == "dimecres" and hora == 15):
        return (7, 3)
    if (dia == "dijous" and hora == 15):
        return (7, 4)
    if (dia == "divendres" and hora == 15):
        return (7, 5)

    if (dia == "dilluns" and hora == 16):
        return (8, 1)
    if (dia == "dimarts" and hora == 16):
        return (8, 2)
    if (dia == "dimecres" and hora == 16):
        return (8, 3)
    if (dia == "dijous" and hora == 16):
        return (8, 4)
    if (dia == "divendres" and hora == 16):
        return (8, 5)

    if (dia == "dilluns" and hora == 17):
        return (9, 1)
    if (dia == "dimarts" and hora == 17):
        return (9, 2)
    if (dia == "dimecres" and hora == 17):
        return (9, 3)
    if (dia == "dijous" and hora == 17):
        return (9, 4)
    if (dia == "divendres" and hora == 17):
        return (9, 5)

    if (dia == "dilluns" and hora == 18):
        return (10, 1)
    if (dia == "dimarts" and hora == 18):
        return (10, 2)
    if (dia == "dimecres" and hora == 18):
        return (10, 3)
    if (dia == "dijous" and hora == 18):
        return (10, 4)
    if (dia == "divendres" and hora == 18):
        return (10, 5)

    if (dia == "dilluns" and hora == 19):
        return (11, 1)
    if (dia == "dimarts" and hora == 19):
        return (11, 2)
    if (dia == "dimecres" and hora == 19):
        return (11, 3)
    if (dia == "dijous" and hora == 19):
        return (11, 4)
    if (dia == "divendres" and hora == 19):
        return (11, 5)

    if (dia == "dilluns" and hora == 20):
        return (12, 1)
    if (dia == "dimarts" and hora == 20):
        return (12, 2)
    if (dia == "dimecres" and hora == 20):
        return (12, 3)
    if (dia == "dijous" and hora == 20):
        return (12, 4)
    if (dia == "divendres" and hora == 20):
        return (12, 5)


# atributs que comencen amb '_'es consideren protected
# atributs que comencen amb '__' es consideren private
# pero python no impedeix accedir a membres privats o protegits, és un  conveni
# sempre es pot accedir a membre atribut fent _nomClase.__nomAtribut, per tant,
# deixaré atributs com publics

class DiaHora(object):
    def __init__(self, dia: str, hora_inici: str, hora_final: str = None):
        self.dia = dia
        self.hora_inici = hora_inici

        # si no es dona hora_final, se suposa que es 1 h després de la inicial
        if (hora_final is None):
            cadena = (self.hora_inici[0] + self.hora_inici[1])
            temp_int = int(cadena) + 1
            if (temp_int < 10):
                self.hora_final = "0" + str(temp_int)
            else:
                self.hora_final = str(temp_int)

            self.hora_final += ":"
            cadena = (self.hora_inici[3] + self.hora_inici[4])
            temp_int = int(cadena)
            if (temp_int < 10):
                self.hora_final += "0" + str(temp_int)
            else:
                self.hora_final += str(temp_int)
        else:
            self.hora_final = hora_final

        # la (x,y) serveix per a poder pintar l'horari usant la classe
        # TaulaMostraHorari,es corresponen amb la fila i col de la matriu de la
        # classe TaulaMostraHorari
        self.x, self.y = conversor(self.dia, int(self.hora_inici[0]
                                                 + self.hora_inici[1]))

    def __str__(self):
        return ("{} de {}h a {}h".format(self.dia, self.hora_inici, self.hora_final))

    def __rep__(self):
        return self.__str__()

    def __eq__(self, hora2):
        return self.dia == hora2.dia and self.hora_inici == hora2.hora_inici

    def indexos(self):
        return (self.x, self.y)
        # pass

    # MOLT IMPORTANT: aquesta funció només funciona si tant la hora de inici
    # com de final,cadascuna d'elles està expressada amb 2 dígits per les hores
    # i 2 pels minuts. És a dir:
    #                           08:10 okay
    #                             8:10 error
    # per tant, quan es rebi el input, els dígits menors de 10 que no tinguin
    # el 0 al dvanat, s'hauràn de transformar: 8:20 -> 08:20; 9:1 -> 09:01, etc
    def compatible_amb(self, diaHora_param):
        if (self.dia != diaHora_param.dia):
            return True
        else:
            # forma més senzilla de pensar-ho, només NO és solapen
            # si l'esdeveniment comença i acaba abans que començi l'altre...

            # que és el mateix que: comença un cop ja ha acabat l'altre
            if (diaHora_param.hora_inici >= self.hora_final or
                    self.hora_inici >= diaHora_param.hora_final):
                return True

            # sinó es que hi ha solapament
            else:
                return False


# test de funció compatible_amb de la classe DiaHora
def test_DiaHora_compatible():
    diaHora1 = DiaHora("dilluns", "08:00", "14:00")
    diaHora2 = DiaHora("dilluns", "12:00", "14:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dilluns", "12:00", "14:00")
    diaHora2 = DiaHora("dilluns", "08:00", "14:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dilluns", "16:00", "18:00")
    diaHora2 = DiaHora("dilluns", "18:00", "19:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dilluns", "18:00", "19:00")
    diaHora2 = DiaHora("dilluns", "16:00", "18:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dijous", "09:00", "10:00")
    diaHora2 = DiaHora("dijous", "10:00", "11:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dijous", "10:00", "11:00")
    diaHora2 = DiaHora("dijous", "09:00", "10:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dijous", "08:00", "20:00")
    diaHora2 = DiaHora("dijous", "08:00", "08:10")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dijous", "13:00", "15:00")
    diaHora2 = DiaHora("dijous", "08:00", "14:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dijous", "19:00", "20:00")
    diaHora2 = DiaHora("dijous", "20:00", "21:00")
    print(diaHora1.compatible_amb(diaHora2))

    diaHora1 = DiaHora("dimecres", "09:00", "12:00")
    diaHora2 = DiaHora("dimecres", "10:00", "13:00")
    print(diaHora1.compatible_amb(diaHora2))


class Subgrup(object):
    def __init__(self, nom_assig: str, num_subgrup: int, llista_hores: list):
        # llista_hores és una llista d'objectes DiaHora corresponent a totes
        # les hores d'aquell subgrup
        self.nom_assig = nom_assig
        self.num_subgrup = num_subgrup
        self.llista_hores = copy.deepcopy(llista_hores)

    def __str__(self):
        ret_str = "{}{} -> ".format(self.nom_assig, self.num_subgrup)
        # utilitza ','per crear un sol string amb els elements que va retornant
        # la list comprehesion:
        ret_str += ", ".join(
            [diaHora.__str__() for diaHora in self.llista_hores])
        return ret_str

    def __rep__(self):
        return self.__str__()

    def __iter__(self):
        return self

    def compatible_amb(self, subGrup_param):
        for i in self.llista_hores:
            for j in subGrup_param.llista_hores:
                if not i.compatible_amb(j):
                    return False
        return True

    # innecessari però per fer interficie(conjunt de métodes, 'públics' que se
    # suposa que es poden cridar) més clara.
    def mostrar(self):
        print(self.__str__())

    def llista_indexos(self):
        return [diaHora.indexos() for diaHora in self.llista_hores]


class ConjuntSubgrups(object):
    def __init__(self):
        # llista d'objectes 'Subgrup':
        self.llista_subgrups = list()

        # atributs per poder fer la classe iterable
        self.__count = 0
        self.__size = 0

    def afegir(self, subgrup: Subgrup):
        self.llista_subgrups.append(copy.deepcopy(subgrup))
        self.__size += 1

    def __str__(self):
        # utilitzant list comprehesion-> una sola línia
        # menys llegible pero més compacte i eficient
        ret_str = "\n\n".join(
            [subGrup.__str__() for subGrup in self.llista_subgrups])

        # equivalent amb bucle 'normal'
        # ret_str = ""
        # for subGrup in self.llista_subgrups:
        #     ret_str += subGrup.__str__()
        #     ret_str += "\n\n"
        return ret_str

    def __rep__(self):
        return self.__str__()

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__count < self.__size):
            self.__count += 1
            return self.llista_subgrups[self.__count - 1]

        else:
            raise StopIteration

    # innecessari però per fer interficie(conjunt de métodes,'públics', que se
    # suposa que es poden cridar) més clara.
    def mostrar(self):
        print(self.__str__())


class TaulaMostraHorari(object):
    '''Com indica el nom, aquesta classe, donat un ConjuntSubgrups, crea un
    taula a la pantalla()(línia de comandes) per veure com ha quedat l'horari
    MOLT IMPORTANT: aquesta classe està pensada per usar-se quan ja se sap que un
    conjunt de subgrups que NO se solapen.
    És a dir, si es fa servir aquesta classe passant-li com a
    paràmetre al construcor un ConjuntSubgrups que té subgrups que es solapen,
    la taula mostrarà només un dels grups
    d'aquella hora -> realment no s'estaràn mostrant rn pantalla totes les
    hores, per tant:aquesta classe funciona perfectament quan se li passa un
    ConjuntSubgrups que no es solapen entre si i,per tant, mostra en pantalla
    l'horari de forma cómode'''
    # escribim de línia en línia

    def __init__(self, conjuntSubgrups: ConjuntSubgrups):
        # conté una llista de objectes SubGrup per mostrar-los en format horari
        self.llista_subgrups = copy.deepcopy(conjuntSubgrups.llista_subgrups)
        self.header = "               dilluns         dimarts         dimecres        dijous         divendres"
        self.taula = list()
        # afegim 5 referencies a objectes tipus subgrup,és a dir,
        # el grup de dilluns, dimarts, dimecres, dijous i divendres a les 8h,
        # d'esquerra a dreta
        # el grup de dilluns, dimarts, dimecres, dijous i divendres a les 9h,
        # d'esquerra a dreta
        # etc. Per entendre millor crear una instancia d'exemple i cirdar
        # métode mostrar

        # llista
        fila0 = list()
        fila0.append("8:00h")
        fila0.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila0))

        fila1 = list()
        fila1.append("9:00h")
        fila1.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila1))

        fila2 = list()
        fila2.append("10:00h")
        fila2.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila2))

        fila3 = list()
        fila3.append("11:00h")
        fila3.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila3))

        fila4 = list()
        fila4.append("12:00h")
        fila4.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila4))

        fila5 = list()
        fila5.append("13:00h")
        fila5.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila5))

        fila6 = list()
        fila6.append("14:00h")
        fila6.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila6))

        fila7 = list()
        fila7.append("15:00h")
        fila7.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila7))

        fila8 = list()
        fila8.append("16:00h")
        fila8.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila8))

        fila9 = list()
        fila9.append("17:00h")
        fila9.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila9))

        fila10 = list()
        fila10.append("18:00h")
        fila10.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila10))

        fila11 = list()
        fila11.append("19:00h")
        fila11.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila11))

        fila12 = list()
        fila12.append("20:00h")
        fila12.extend(["-"] * 5)
        self.taula.append(copy.deepcopy(fila12))

        # debug info
        [print(i) for i in self.llista_subgrups]
        self.actualitzar_vista_horari()

    def __str__(self):
        ret_str = "*" * 90
        ret_str = ret_str + '\n'
        ret_str = ret_str + self.header
        for fila in self.taula:
            ret_str = ret_str + "\n\n"
            for element in fila:
                ret_str = ret_str + element
                ret_str = ret_str + "\t\t"
        ret_str = ret_str + "*" * 90
        return ret_str

    def __rep__(self):
        return self.__str__()

    def horari_exemple(self):
        ret_str = "*" * 90
        ret_str = ret_str + '\n'
        ret_str = ret_str + self.header
        for fila in self.taula:
            ret_str = ret_str + "\n\n"
            for element in fila:
                ret_str = ret_str + element
                ret_str = ret_str + "\t\t"
        ret_str = ret_str + "*" * 90
        print(ret_str)

    def mostrar(self):
        print(self.__str__())

# de moment aquesta funció no és necessària ja que al constructor ja se li
# passa les dades que aquesta classe necessita
#    def afegir_subgrup(self, subgrup: Subgrup):
#        self.llista_subgrups.append(subgrup)

    # ara hem de recorrer tots els objectes SubGrup que hi ha a la
    # llista_subgrups i per cada subgrup:
    #   recorrer totes les dia+hore de classe d'aquell subgrup i per cada
    #   dia+hora(objecte DiaHora):
    #     actualitzar la nostra matriu perquè mostri el horari
    #     de forma agradable
    def actualitzar_vista_horari(self):
        for subgrup in self.llista_subgrups:
            for tupla in subgrup.llista_indexos():
                x = tupla[0]
                y = tupla[1]
                self.taula[x][y] = subgrup.nom_assig + str(subgrup.num_subgrup)


def combinar(conjuntSubgrups_llista: list):
    '''Donada una llista d'objectes ConjuntSubgrups, retorna una llista de
    ConjuntSubgrups nova. Aquesta llista conté totes les combinacions possibles
    del diferents elements de les diferents llistes. Per entendre millor,
    cridar a la funcio prova_combinar_subgrups'''
    return itertools.product(*conjuntSubgrups_llista)


def printar_llista_combinacions(llista_combinacions: list):
    """Donada una llista de combinacions, la pinta de manera cómode clara
    indicant quines combinacions hi ha a la llista que es
    passa com a parametre de ls funcio"""

    # debug info:
    # print("Tipus de l'objecte retornat", end=" ")
    # print(type(llista_combinacions))
    # print("_" * 3)

    n = 0
    for comptador, element in enumerate(llista_combinacions):
        n += 1
        # print("tipus" + str(type(element)))
        print("COMBINACIO {}".format(comptador))
        la_tupla = element
        for element in la_tupla:
            print("subgrup->", end=" ")
            element.mostrar()
            print()  # línia en blanc

    print("*" * 10)
    print("{} COMBINACIONS generades:".format(n))
    print("*" * 10)


def exemple_iterator_conjuntSubgrups():
    print("funció exemple_iterator_conjuntSubgrups cridada")

    conjuntSubgrupAssignatures = ConjuntSubgrups()
    subgrup1 = Subgrup('IDI',
                       32,
                       [DiaHora("dimarts", "12:00"),
                        DiaHora("dimarts", "13:00"),
                        DiaHora("divendres", "12:00"),
                        DiaHora("divendres", "13:00")])
    conjuntSubgrupAssignatures.afegir(subgrup1)
    subgrup2 = Subgrup('IDI',
                       33,
                       [DiaHora("dilluns", "08:00"),
                        DiaHora("dimecres", "18:00"),
                        DiaHora("dimarts", "09:00"),
                        DiaHora("dijous", "10:00")])
    conjuntSubgrupAssignatures.afegir(subgrup2)

    next(conjuntSubgrupAssignatures).mostrar()
    next(conjuntSubgrupAssignatures).mostrar()

    # a la següent crida saltarà StopIteration exception ja que el
    # 'conjuntSubgrupAssignatures' té 2 elements i estem fent next quan ja
    # hem recorregut els seus 2 elements (és l'esperat)  :)
    next(conjuntSubgrupAssignatures).mostrar()


def prova_combinar_subgrups():
    print("funció prova_combinar_subgrups cridada")
    conjuntSubgrupsAssig1 = ConjuntSubgrups()
    conjuntSubgrupsAssig2 = ConjuntSubgrups()

    subgrup1 = Subgrup('IDI',
                       32,
                       [DiaHora("dimarts", "12:00"),
                        DiaHora("dimarts", "13:00"),
                        DiaHora("divendres", "12:00"),
                        DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig1.afegir(subgrup1)
    subgrup2 = Subgrup('IDI',
                       33,
                       [DiaHora("dilluns", "08:00"),
                        DiaHora("dimecres", "18:00"),
                        DiaHora("dimarts", "09:00"),
                        DiaHora("dijous", "10:00")])
    conjuntSubgrupsAssig1.afegir(subgrup2)

    subgrup3 = Subgrup('PROP',
                       11,
                       [DiaHora("dilluns", "08:00"),
                        DiaHora("dilluns", "09:00"),
                        DiaHora("dimarts", "12:00"),
                        DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig2.afegir(subgrup3)

    subgrup4 = Subgrup('PROP',
                       12,
                       [DiaHora("dijous", "08:00"),
                        DiaHora("dijous", "09:00"),
                        DiaHora("divendres", "14:00"),
                        DiaHora("divendres", "15:00")])
    conjuntSubgrupsAssig2.afegir(subgrup4)

    llista_conjuntSubgrups = list()
    llista_conjuntSubgrups.append(conjuntSubgrupsAssig1)
    llista_conjuntSubgrups.append(conjuntSubgrupsAssig2)

    print("tenim una llista d'objectes conjuntSubgrups:")
    print("__INI__")
    for comptador, element in enumerate(llista_conjuntSubgrups):
        print("conjunt de subgrups {} de la llista:".format(comptador))
        element.mostrar()
        print("*" * 20)
    print("__FI__")

    print("la següent línia (mirar codi font) retorna un contenidor", end=" ")
    print("de tuples on cada tupla conte objectes 'subgrup', ", end=" ")
    print("cada pos del contenidor representa una combinació ", end=" ")
    print("dels diferents subgrups")
    llista_combinacions = itertools.product(*llista_conjuntSubgrups)
    printar_llista_combinacions(llista_combinacions)


def combinacio_compatible(combinacio: list):
    '''Donada una llista de subgrups, retorna true si són
    compatibles entre ells'''
    for subgrup in combinacio:
        for subgrup2 in combinacio:
            if (subgrup is not subgrup2):
                # aquest if s'usa ja que no hem de comparar elements
                # amb si mateixos(sinó falla perquè estariem preguntant si un
                # horari es compatible amb si mateix, cosa que
                # retorna False)

                # debug info:
                # print("subgrup1:")
                # subgrup.mostrar()
                # print("subgrup2:")
                # subgrup2.mostrar()
                # ###################

                if (not subgrup.compatible_amb(subgrup2)):
                    # print("2 anteriors NO COMPATIBLES")  # debug info
                    return False
                # else:
                    # print(" 2anteriors SÍ COMPATIBLES")  # debug info
    return True


def main():

    conjuntSubgrupsAssig1 = ConjuntSubgrups()

    subgrup = Subgrup('AC',
                      11,
                      [DiaHora("dilluns", "08:00"),
                       DiaHora("dilluns", "09:00"),
                       DiaHora("dimecres", "09:00"),
                       DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      12,
                      [DiaHora("dilluns", "08:00"),
                       DiaHora("dilluns", "09:00"),
                       DiaHora("divendres", "12:00"),
                       DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      13,
                      [DiaHora("dilluns", "08:00"),
                       DiaHora("dilluns", "09:00"),
                       DiaHora("dimecres", "08:00"),
                       DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      21,
                      [DiaHora("dilluns", "10:00"),
                       DiaHora("dilluns", "11:00"),
                       DiaHora("dijous", "09:00"),
                       DiaHora("dijous", "10:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      22,
                      [DiaHora("dilluns", "10:00"),
                       DiaHora("dilluns", "11:00"),
                       DiaHora("dimecres", "10:00"),
                       DiaHora("dijous", "10:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      31,
                      [DiaHora("dimarts", "08:00"),
                       DiaHora("dimarts", "09:00"),
                       DiaHora("dijous", "08:00"),
                       DiaHora("divendres", "10:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      32,
                      [DiaHora("dimarts", "08:00"),
                       DiaHora("dimarts", "09:00"),
                       DiaHora("dijous", "08:00"),
                       DiaHora("dijous", "12:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('AC',
                      33,
                      [DiaHora("dimarts", "08:00"),
                       DiaHora("dimarts", "09:00"),
                       DiaHora("dijous", "08:00"),
                       DiaHora("dijous", "11:00")])
    conjuntSubgrupsAssig1.afegir(subgrup)
    # _________________________________________________________________________________________________________________
    # _________________________________________________________________________________________________________________
    conjuntSubgrupsAssig2 = ConjuntSubgrups()

    subgrup = Subgrup('IDI',
                      11,
                      [DiaHora("dimarts", "08:00"),
                       DiaHora("dimarts", "09:00"),
                       DiaHora("divendres", "08:00"),
                       DiaHora("divendres", "09:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      12,
                      [DiaHora("dimarts", "08:00"),
                       DiaHora("dimarts", "09:00"),
                       DiaHora("divendres", "08:00"),
                       DiaHora("divendres", "09:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      13,
                      [DiaHora("dimarts", "08:00"),
                       DiaHora("dimarts", "09:00"),
                       DiaHora("divendres", "08:00"),
                       DiaHora("divendres", "09:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      21,
                      [DiaHora("dimarts", "10:00"),
                       DiaHora("dimarts", "11:00"),
                       DiaHora("divendres", "10:00"),
                       DiaHora("divendres", "11:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      22,
                      [DiaHora("dimarts", "10:00"),
                       DiaHora("dimarts", "11:00"),
                       DiaHora("divendres", "10:00"),
                       DiaHora("divendres", "11:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________

    subgrup = Subgrup('IDI',
                      23,
                      [DiaHora("dimarts", "10:00"),
                       DiaHora("dimarts", "11:00"),
                       DiaHora("divendres", "10:00"),
                       DiaHora("divendres", "11:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      31,
                      [DiaHora("dimarts", "12:00"),
                       DiaHora("dimarts", "13:00"),
                       DiaHora("divendres", "12:00"),
                       DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      32,
                      [DiaHora("dimarts", "12:00"),
                       DiaHora("dimarts", "13:00"),
                       DiaHora("divendres", "12:00"),
                       DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # ________________________________________________________________________________________________________________
    subgrup = Subgrup('IDI',
                      33,
                      [DiaHora("dimarts", "12:00"),
                       DiaHora("dimarts", "13:00"),
                       DiaHora("divendres", "12:00"),
                       DiaHora("divendres", "13:00")])
    conjuntSubgrupsAssig2.afegir(subgrup)
    # _________________________________________________________________________________________________________________
    # _________________________________________________________________________________________________________________
    conjuntSubgrupsAssig3 = ConjuntSubgrups()

    subgrup = Subgrup('AS',
                      13,
                      [DiaHora("divendres", "10:00"),
                       DiaHora("divendres", "11:00"),
                       DiaHora("dilluns", "12:00"),
                       DiaHora("dilluns", "13:00")])
    conjuntSubgrupsAssig3.afegir(subgrup)
    # _________________________________________________________________________________________________________________
    # _________________________________________________________________________________________________________________
    conjuntSubgrupsAssig4 = ConjuntSubgrups()

    subgrup = Subgrup('ER',
                      11,
                      [DiaHora("dimecres", "08:00"),
                       DiaHora("dimecres", "09:00"),
                       DiaHora("dijous", "12:00"),
                       DiaHora("dijous", "13:00")])
    conjuntSubgrupsAssig4.afegir(subgrup)
    # _________________________________________________________________________________________________________________
    # _________________________________________________________________________________________________________________

    # debug info per veure que al principi de tot es guarden correctament
    # els diferents subgrups:
    # conjuntSubgrupsAssig1.mostrar()
    # conjuntSubgrupsAssig2.mostrar()
    # conjuntSubgrupsAssig3.mostrar()
    # conjuntSubgrupsAssig4.mostrar()
    # _______________________________
    llista_conjuntSubgrups = list()
    llista_conjuntSubgrups.append(conjuntSubgrupsAssig1)
    llista_conjuntSubgrups.append(conjuntSubgrupsAssig2)
    llista_conjuntSubgrups.append(conjuntSubgrupsAssig3)
    llista_conjuntSubgrups.append(conjuntSubgrupsAssig4)

    # hem de convertir a list, usant list(...)
    # pk sinó tipus retorn és<class 'itertools.product'>
    llista_combinacions = list(itertools.product(*llista_conjuntSubgrups))
    # printar_llista_combinacions(llista_combinacions)
    # print(type(llista_combinacions))  # debug info

    i = 0
    # per a cada combinació de subgrups
    for combinacio in llista_combinacions:
        # print(combinacio)  # debug info
        # print("*"*10)      # debug info
        if (combinacio_compatible(combinacio)):
            i += 1
            [i.mostrar() for i in combinacio]
            print("*" * 20)
            # ############################################### FI de main()
    print("{} combinacions possibles".format(i))
# prova_combinar_subgrups()
# exemple_iterator_conjuntSubgrups()
# test_DiaHora_compatible()


main()
