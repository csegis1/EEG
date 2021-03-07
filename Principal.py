# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:15:12 2018

@author: ricra
"""

from scipy import signal
import numpy as np
from skimage import img_as_ubyte
import modulos
from skimage import feature
ruta='C:/Users/ricra/Documents/Doctorado LKE/Datos/EEG Ataques/S-Set E'
archivos = modulos.ls(ruta)   # no especificar ruta para tomar el directorio actual
#ubicacion="C:/Users/ricra/Documents/Doctorado LKE/Pruebas/F001.txt"
#feats=cglcm(ubicacion)
vfeats=[]
vlabel=[]
picosenc=[] #picos encontrados
for archivo in archivos:
    rutat = ruta+'/'+archivo
    print(rutat)
    x=[] #vector con datos del archivo de texto
    x=np.loadtxt(rutat)
    f, t, Sxx = signal.spectrogram(x, fs=173.61,  window=(signal.hann(128)), nperseg=None, noverlap=85, nfft=2000, detrend='constant', return_onesided=True, scaling='density', axis=-1, mode='magnitude')
    #plt.pcolormesh(t, f, Sxx)
    #plt.ylabel('Frequency [Hz]')
    #plt.xlabel('Time [sec]')
    
    #normalized = cv2.normalize(Sxx, out, 0.9999999999, 0.0, cv2.NORM_MINMAX)
    mimax=modulos.minmax(Sxx)
    modulos.normalizar(Sxx,mimax)
    img= img_as_ubyte(Sxx)
    picoscord=feature.peak_local_max(img, min_distance=20) #coordenadas de los picos
    #encontrado las maginitudes de los picos
    for coorde in picoscord:
        picosenc.append(img[coorde[0],coorde[1]])
    
    picosel=modulos.pselect(picosenc) 
    vfeats.append(picosel)
    vlabel.append(0)
    picosenc=[]
  

ruta='C:/Users/ricra/Documents/Doctorado LKE/Datos/EEG Ataques/Z-Set A'
archivos = modulos.ls(ruta)   # no especificar ruta para tomar el directorio actual
#ubicacion="C:/Users/ricra/Documents/Doctorado LKE/Pruebas/F001.txt"
#feats=cglcm(ubicacion)

for archivo in archivos:
    rutat = ruta+'/'+archivo
    print(rutat)
    x=[] #vector con datos del archivo de texto
    x=np.loadtxt(rutat)
    f, t, Sxx = signal.spectrogram(x, fs=173.61,  window=(signal.hann(128)), nperseg=None, noverlap=85, nfft=2000, detrend='constant', return_onesided=True, scaling='density', axis=-1, mode='magnitude')
    #plt.pcolormesh(t, f, Sxx)
    #plt.ylabel('Frequency [Hz]')
    #plt.xlabel('Time [sec]')
    
    #normalized = cv2.normalize(Sxx, out, 0.9999999999, 0.0, cv2.NORM_MINMAX)
    mimax=modulos.minmax(Sxx)
    modulos.normalizar(Sxx,mimax)
    img= img_as_ubyte(Sxx)
    picos=feature.peak_local_max(img, min_distance=1)
    picosel=modulos.pselect(picos)
    vfeats.append(picosel)
    vlabel.append(1)
    picosenc=[]
    

  