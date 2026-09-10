import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def ma_function(name):
    logging.info("Yes vous avez démarré le thread! %s: starting", name)
    time.sleep(2)
    logging.info("Le thread est fini ! %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    # Par défaut un thread n'est pas un daemon, donc il peut se terminer. Cette fonction crée un thread mais ne le démarre pas encore.
    '''Décomposition :
threading.Thread(...) : crée un nouvel objet représentant un thread.
target=ma_function : indique que le thread devra exécuter la fonction ma_function.
args=(1,) : indique que ma_function recevra 1 comme argument.
La virgule est importante : (1,) est un tuple à un seul élément.
daemon=True : le thread est un thread daemon. Le programme Python pourra se terminer même si ce thread est encore en train de fonctionner.
x = ... : l'objet Thread est stocké dans la variable x'''
    #x = threading.Thread(target=ma_function, args=(1,))

    # Le thread est défini comme étant un daemon c'est à dire qu'il est tué quand le programme est fini. Du coup mon thread a pas pu se terminer !
    x = threading.Thread(target=ma_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()   #Démarre le thread
    logging.info("Main    : wait for the thread to finish")

    #Pour dire à un thread d'attendre qu'un autre thread finisse, tu appelles .join(). Si tu décommentes cette ligne, le thread principal va se mettre en pause et attendre que le thread x ait fini de s'exécuter.
    x.join()    #Le thread doit attendre qu'un autre thread soit terminé

    logging.info("Main    : all done")