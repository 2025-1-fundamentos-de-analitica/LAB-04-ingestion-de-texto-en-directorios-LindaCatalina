# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import os
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    ZIPFILE = "files/input.zip"
    outdir = "input"

    if not os.path.exists(ZIPFILE):
        print(f"El archivo {ZIPFILE} no existe.")
        return
    with zipfile.ZipFile(ZIPFILE, 'r') as ZIPFILE_ref:
        ZIPFILE_ref.extractall(outdir)
        print(f"El archivo {ZIPFILE} descomprimido correctamente en {outdir}")


pregunta_01()

outdir = os.path.join('files', 'output')
if not os.path.exists(outdir):
    os.makedirs(outdir)

phrases_test = []
targets_test = []
phrases_train = []
targets_train = []

testdir = os.path.join('input', 'input', 'test')
traindir = os.path.join('input', 'input', 'train')

sentdirs = ['positive', 'negative', 'neutral']

for sent in sentdirs:
    sent_path = os.path.join(testdir, sent)
    
    if not os.path.exists(sent_path):
        print(f"El directorio {sent_path} no existe.")
        continue


    for filename in os.listdir(sent_path):
        file_path = os.path.join(sent_path, filename)
        
        if os.path.isfile(file_path): 
            with open(file_path, 'r', encoding='utf-8') as file:
                phrase = file.read().strip()
            phrases_test.append(phrase)
            targets_test.append(sent)



for sent in sentdirs:
    sent_path = os.path.join(traindir, sent)
    
    if not os.path.exists(sent_path):
        print(f"El directorio {sent_path} no existe.")
        continue

    for filename in os.listdir(sent_path):
        file_path = os.path.join(sent_path, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                phrase = file.read().strip()
                
            phrases_train.append(phrase)
            targets_train.append(sent)


test_data = pd.DataFrame({'phrase': phrases_test, 'target': targets_test})
train_data = pd.DataFrame({'phrase': phrases_train, 'target': targets_train})

test_data = test_data.sample(frac=1, random_state=42).reset_index(drop=True)
train_data = train_data.sample(frac=1, random_state=42).reset_index(drop=True)

test_data.to_csv(os.path.join(outdir, "test_dataset.csv"), index=False)
train_data.to_csv(os.path.join(outdir, "train_dataset.csv"), index=False)

print("Archivos 'train_dataset.csv' y 'test_dataset.csv' generados correctamente en la carpeta 'files/output'.")