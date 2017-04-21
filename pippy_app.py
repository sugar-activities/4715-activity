#!/usr/bin/python
# -*- coding: utf-8 -*-
# SDownloader 1: Descarga archivos de Internet

# Importamos los módulos necesarios
import os

#### Inicio ####
print
print "\033[34;1m ============ SDownloader 1 ============\033[0m"
print
print " >>> SDownloader es un programa para descargar archivos"
print " >>> de Internet fácilmente."
print " >>>"
url = raw_input(" >>> URL del archivo: ")
loc = ""
while not os.path.exists(loc):
    loc = raw_input(" >>> Lugar donde descargar el archivo (ej. /home/olpc): ")
print " >>>"
print " >>> Resumen:"
print " >>> Descargar %s en %s."%(url, loc)
raw_input(" >>> Presione enter para continuar.")
print " >>> Descargando..."
os.chdir(loc)
os.system("wget \"%s\""%url)
print " >>> Archivo descargado."
print " >>> Hasta luego."