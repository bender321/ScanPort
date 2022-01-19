# ScanPort
### Použití:
- v terminálu spustit skript run.sh
#### přepínače:
- -v pro vizualizaci outputu výsledků
- -r pro čtení ze souboru, který je předem definovaný jako scan_results.json
- -s pro uložení výsledku do souboru scan_results.json
- -t=x pro nastavení kolikrát se má scanování uzkutečnit (x je int, např. -t=5)


### Příklad:
- ./run.sh -v -s -t=3 22 25 80 
- pozn. seznam portů je vždy nutné psát až po přepínačích a ve formě čísel, jinak program skončí s hlášením: Wrong parameters were given...
- nutno mít oba skripty ve stejném adresáři, případně je potřeba upravit cestu k python skriptu v run.sh 
- defaultní host je v main.py nastaven jako HOST=127.0.0.1, lze ho změnit v python skriptu, stejně tak jako časový rozestup mezi scany WAIT_POINT
