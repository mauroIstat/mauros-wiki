# Navigatore delle professioni

- Source files:
  - `raw/professioni/navigatore-professioni-landing.png`
  - `raw/professioni/navigatore-professioni-esempio-imprenditore.png`
  - `raw/professioni/navigatore-professioni-esempio-professore.png`
- Document type: schermate di sistema legacy / interfaccia di supporto alla codifica

## Ruolo nel workspace

Queste immagini documentano un sistema legacy Istat, il "Navigatore delle professioni", rilevante come punto di partenza per il nuovo paper. Nel manoscritto su ricerca semantica e professioni, il Navigatore e' importante non come soluzione finale, ma come baseline istituzionale da cui emergono alcune criticita' operative.

## Struttura osservabile del sistema

Dalle schermate emerge che il Navigatore combina due modalita' principali:

- esplorazione gerarchica della classificazione delle unita' professionali 2021
- ricerca libera tramite una casella testuale

La schermata iniziale mostra i nove Grandi gruppi della classificazione e spiega che la navigazione puo' avvenire sia attraverso l'albero classificatorio sia tramite ricerca nel box testuale.

## Comportamento osservabile nelle ricerche

Gli esempi mostrano che il sistema restituisce:

- un insieme di unita' professionali trovate per il termine cercato
- l'appartenenza gerarchica al Grande gruppo
- una descrizione dell'unita' selezionata
- un elenco di "voci professionali" associate

L'esempio `imprenditore` restituisce molte unita' professionali nello stesso grande gruppo, suggerendo che un termine generico puo' produrre numerosi risultati tra loro vicini ma non immediatamente disambiguati.

L'esempio `sono un professore di matematica` restituisce pochi risultati e sembra intercettare soprattutto il termine disciplinare `matematica` e la voce `professore`, collegando la query a una unita' professionale specifica della scuola secondaria superiore.

## Indicazioni utili per il paper

Le schermate suggeriscono alcune caratteristiche importanti del sistema legacy:

- il supporto alla codifica e' strettamente legato alla struttura gerarchica della classificazione
- la ricerca sembra lavorare su corrispondenze testuali con termini presenti nelle denominazioni o nelle voci professionali
- il sistema fornisce supporto descrittivo utile al codificatore umano
- termini generici o ambigui possono richiedere ulteriore interpretazione manuale

## Uso previsto nel nuovo paper

Nel paper, il Navigatore puo' essere presentato come uno strumento istituzionale gia' disponibile che:

- rende consultabile la classificazione
- supporta la codifica manuale o assistita
- mostra l'utilita' di descrizioni e voci professionali come base informativa
- evidenzia il bisogno di approcci piu' flessibili quando le query sono generiche, rumorose o formulate in linguaggio naturale

In questo senso, una metodologia di ricerca semantica puo' essere introdotta come estensione o superamento delle rigidita' residue del sistema legacy, senza negarne il valore operativo.
