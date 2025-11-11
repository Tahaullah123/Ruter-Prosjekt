"# Ruter-Prosjekt" 

Prosjektet henter data automatisk fra PokéAPI og lagrer resultatene lokalt i strukturerte JSON-filer.  
Dataene blir hentet i flere lag:
1. **Grunnleggende Pokémon-data**  
   Hentes fra `/api/v2/pokemon/`  
   Inneholder navn, id, typer, abilities, stats og bilder.  
2. **Artsdata**  
   Hentes fra `/api/v2/pokemon-species/`  
   Inneholder flavor text, habitat, generasjon, farge og utviklingslenke.  
3. **Evolusjonsdata**  
   Hentes fra `evolution_chain.url`  
   Viser hele evolusjonsrekken i strukturert rekkefølge.  
4. **Utvidet informasjon (valgfritt)**  
   Typer, moves, abilities og items kan hentes fra egne endepunkter.
