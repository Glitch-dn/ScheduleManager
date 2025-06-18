'''
Realizza un programma Python che permetta a un utente di inserire, visualizzare e gestire una lista di appuntamenti (ad esempio per uno studio medico o uno studio professionale). Il programma dovrà:

Permettere l’inserimento di un nuovo appuntamento chiedendo all’utente:

Nome e cognome del cliente
Data e ora dell’appuntamento (in formato ISO, es: 2025-06-20 14:30)
Descrizione breve
Visualizzare tutti gli appuntamenti mostrando:

Numero progressivo
Nome cliente
Data/ora (formattata)
Giorni, ore e minuti mancanti all’appuntamento (rispetto all’orario attuale)
Permettere il confronto tra due appuntamenti selezionati tramite il loro numero, stampando:

Quale appuntamento viene prima
La differenza in giorni, ore e minuti tra i due
Aggiungere X giorni/minuti a un appuntamento (es. il cliente sposta l’orario), mostrando la nuova data.

Cercare un appuntamento per nome del cliente (confronto lessicografico).


'''
#import delle librerie necessarie

from datetime import datetime, timedelta

#Lista che conterrrà gli appuntamenti
appuntamenti = []

#Funzione per inserire un nuovo appuntamento
def inserisci_appuntamento():
    '''Richiede i dati per un nuovo appuntamento e lo aggiunge alla lista degli appuntamenti.'''
    print("\nInserisci nuovo appuntamento:\n")
    nome = input("Nome del cliente:\n ")
    cognome = input("Cognome del cliente:\n ")
    data_ora = input("Data e ora dell'appuntamento (in formato ISO, es: 2025-06-20 14:30):\n ")
    descrizione = input("Descrizione breve:\n ")
    # Converto la stringa in un oggetto datetime
    try:
        data_ora_dt = datetime.fromisoformat(data_ora)
    except ValueError:
        print("Formato data/ora non valido. Usa il formato ISO (es: 2025-06-20 14:30).")
        return
    # Aggiungo l'appuntamento alla lista
    appuntamento = {
        "nome": nome,
        "cognome": cognome,
        "data_ora": data_ora_dt,
        "descrizione": descrizione
    }
    appuntamenti.append(appuntamento)
    print(f"\nAppuntamento aggiunto: {nome} {cognome} il {data_ora_dt.strftime('%d/%m/%Y %H:%M')}.\n")


#Funzione per visualizzare tutti gli appuntamenti
def visualizza_appuntamenti():
    '''Visualizza tutti gli appuntamenti con dettagli formattati.'''
    if not appuntamenti:
        print("\nNessun appuntamento presente.\n")
        return
    print("\nLista degli appuntamenti:\n")
    for i, app in enumerate(appuntamenti, start=1):
        data_ora = app["data_ora"]
        tempo_mancante = abs(data_ora - datetime.now())
        giorni, ore, minuti = tempo_mancante.days, tempo_mancante.seconds // 3600, (tempo_mancante.seconds // 60) % 60 # Calcolo dei giorni, ore e minuti mancanti usando il metodo seconds della libreria datetime
        print(f"{i}. {app['nome']} {app['cognome']} - {data_ora.strftime('%d/%m/%Y %H:%M')} "
              f"({giorni} giorni, {ore} ore, {minuti} minuti mancanti)")
        

#Funzione per confrontare due appuntamenti
def confronta_appuntamenti():
    '''Confronta due appuntamenti selezionati e mostra quale viene prima e la differenza.'''
    if len(appuntamenti) < 2:
        print("\nNon ci sono abbastanza appuntamenti per il confronto.\n")
        return
    visualizza_appuntamenti()
    try:
        primo = int(input("\nInserisci il numero del primo appuntamento da confrontare: ")) - 1
        secondo = int(input("\nInserisci il numero del secondo appuntamento da confrontare: ")) - 1
        if (primo < 0 or primo >= len(appuntamenti)) or (secondo < 0 or secondo >= len(appuntamenti)):
            print("Numero di appuntamento non valido.\n")
            return
        app1, app2 = appuntamenti[primo], appuntamenti[secondo]
        if app1["data_ora"] < app2["data_ora"]:
            print(f"\nL'appuntamento {app1['nome']} {app1['cognome']} viene prima di {app2['nome']} {app2['cognome']}.")
            differenza = app2["data_ora"] - app1["data_ora"]
            giorni, ore, minuti = differenza.days, differenza.seconds // 3600, (differenza.seconds // 60) % 60
            print(f"Differenza: {giorni} giorni, {ore} ore, {minuti} minuti.")
        elif app1["data_ora"] > app2["data_ora"]:
            print(f"\nL'appuntamento {app2['nome']} {app2['cognome']} viene prima di {app1['nome']} {app1['cognome']}.")
            differenza = app1["data_ora"] - app2["data_ora"]
            giorni, ore, minuti = differenza.days, differenza.seconds // 3600, (differenza.seconds // 60) % 60
            print(f"Differenza: {giorni} giorni, {ore} ore, {minuti} minuti.")
        else:
            print("\nI due appuntamenti sono identici.")
    except ValueError:
        print("Input non valido. Inserisci un numero intero.\n")
        return

#Funzione per spostare un appuntamento
def sposta_appuntamento():
    if not appuntamenti:
        print("\nNessun appuntamento presente.\n")
        return
    visualizza_appuntamenti()
    try:
        indice = int(input("\nInserisci il numero dell'appuntamento da spostare: ")) - 1
        giorni = int(input("Quanti giorni vuoi aggiungere? (puoi inserire un numero negativo per sottrarre): "))
        minuti = int(input("Quanti minuti vuoi aggiungere? (puoi inserire un numero negativo per sottrarre): "))
        if indice < 0 or indice >= len(appuntamenti):
            print("Numero di appuntamento non valido.\n")
            return
        appuntamenti[indice]["data_ora"] += timedelta(days=giorni, minutes=minuti)
        print(f"\nAppuntamento spostato: {appuntamenti[indice]['nome']} {appuntamenti[indice]['cognome']} "
              f"nuova data/ora: {appuntamenti[indice]['data_ora'].strftime('%d/%m/%Y %H:%M')}.\n")
    except ValueError:
        print("Input non valido. Inserisci un numero intero.\n")


#Funzione per cercare un appuntamento per nome del cliente
def cerca_appuntamento():
    '''Cerca un appuntamento per nome del cliente e visualizza i risultati.'''
    if not appuntamenti:
        print("\nNessun appuntamento presente.\n")
        return
    nome_cercato = input("\nInserisci il nome del cliente da cercare: ").strip().lower()
    risultati = [app for app in appuntamenti if app["nome"].lower() == nome_cercato]
    if risultati:
        print("\nAppuntamenti trovati:")
        for i, app in enumerate(risultati, start=1):
            data_ora = app["data_ora"]
            print(f"{i}. {app['nome']} {app['cognome']} - {data_ora.strftime('%d/%m/%Y %H:%M')}")
    else:
        print(f"\nNessun appuntamento trovato per il cliente '{nome_cercato}'.\n")

#Funzione principale per il menu
def menu():
    '''Visualizza il menu principale e gestisce le operazioni scelte dall'utente.'''
    while True:
        print("\nMenu:")
        print("1. Inserisci nuovo appuntamento")
        print("2. Visualizza appuntamenti")
        print("3. Confronta due appuntamenti")
        print("4. Sposta un appuntamento")
        print("5. Cerca appuntamento per nome cliente")
        print("6. Esci")
        
        scelta = input("\nScegli un'opzione (1-6): ")
        
        if scelta == '1':
            inserisci_appuntamento()
        elif scelta == '2':
            visualizza_appuntamenti()
        elif scelta == '3':
            confronta_appuntamenti()
        elif scelta == '4':
            sposta_appuntamento()
        elif scelta == '5':
            cerca_appuntamento()
        elif scelta == '6':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova.")
# Avvio del programma
if __name__ == "__main__":
    menu()


