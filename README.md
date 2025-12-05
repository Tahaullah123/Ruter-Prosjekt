# Entur Realtime Departures – Flask App

Denne Flask-appen henter sanntidsavganger fra Entur Journey Planner API og viser dem i en enkel webside. Den presenterer linje, destinasjon, planlagt avgang og forventet avgang på en ryddig måte.

## Funksjoner

* Henter sanntidsdata fra Entur sitt GraphQL-endepunkt
* Viser de neste 15 avgangene fra et valgt holdeplass-ID
* Formatterer avgangstidene til lettleste klokkeslett
* Bruker en enkel HTML-template (`index.html`) som er lett å bygge videre på

## Teknologier

* Python
* Flask
* Requests
* Entur GraphQL API



Dette henter data fra holdeplass **NSR:StopPlace:59636** og sender dem til `index.html` som:

* `stop`: navnet på holdeplassen
* `departures`: liste med

  * `line`
  * `line_name`
  * `destination`
  * `expected` (sanntid)
  * `aimed` (planlagt)
  * `realtime` (bool)


## Prosjektstruktur

```
project/
│
├── app.py
└── templates/
    └── index.html
```

## Videre utvikling
* Automatisk oppdatering av avgangslisten
* Bedre styling med CSS-rammeverk
