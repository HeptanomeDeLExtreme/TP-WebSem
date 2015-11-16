#TP-WebSem
<h1> Reblochon </h1>
The aim of this project is to develop a semantic meta-search engine.

<h2> Packages </h2>

https://pypi.python.org/pypi/simplejson
http://www.ivan-herman.net/Misc/PythonStuff/SPARQL/

Pour installer ces fichiers, télécharger le zip, et lancer la commande suivante avec le fichier setup présent dans chaque zip :
sudo python setup.py install

These packages are imported in a lazy fashion, ie, only when needed. Ie, if the user never intends to use the JSON format, the simplejson package is not imported and the user does not have to install it.

The package can be downloaded in zip and .tar.gz formats from http://www.ivan-herman.net/Misc/PythonStuff/SPARQL/. It is also available from Sourceforge under the project named "sparql-wrapper". Documentation is included in the distribution.
