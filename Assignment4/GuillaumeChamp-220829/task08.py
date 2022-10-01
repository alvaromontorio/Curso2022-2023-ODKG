# -*- coding: utf-8 -*-
"""Task08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1142NTVstm6668NxdC6Ok1QNJPB3tCbYS

**Task 08: Completing missing data**
"""
from rdflib import Graph, Namespace
from rdflib.namespace import RDF

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"
g1 = Graph()
g2 = Graph()
g1.parse(github_storage + "/rdf/data01.rdf", format="xml")
g2.parse(github_storage + "/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

data = Namespace("http://data.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
for s, p, o in g1.triples((None, RDF.type, data.Person)):
    for ss, pp, oo in g2.triples((s, vcard.Given, None)):
        g1.add((s, pp, oo))
    for ss, pp, oo in g2.triples((s, vcard.Family, None)):
        g1.add((s, pp, oo))
    for ss, pp, oo in g2.triples((s, vcard.Email, None)):
        g1.add((s, pp, oo))
# print g1
print("graph 1")
for s, p, o in g1.triples((None, RDF.type, data.Person)):
    for ss, pp, oo in g1.triples((s, None, None)):
        print(ss, pp, oo)
# print g2
print("graph 2")
for s, p, o in g2.triples((None, RDF.type, data.Person)):
    for ss, pp, oo in g2.triples((s, None, None)):
        print(ss, pp, oo)