# PPKWU_LAB

This repo contains PPKWU task's solutions, where we are building REST API services.

## Documentation 

These documentation will show you how to use created REST API services.

### Prerquisites
Flask:
```
pip install Flask
```

## lab1 - Rest Api Rev service

Applictaion provides simple REV service

### Starting server

```
python3 server.py
```
Output:
```
* Running on http://127:0.0.1:25000/
```

### Make a request

```
curl http://127:0.0.1:25000/api/vcard/<searched_query>
```

```
Will generate and save vcf files with all responses from Panorama Firm"
```

File example:
```
BEGIN:VCARD
VERSION:3.0
EMAIL;TYPE=INTERNET:brak
FN:Fhu Nypel Usługi Hydrauliczne Łukasz Szydliński
N:Fhu Nypel Usługi Hydrauliczne Łukasz Szydliński;;;;
ORG:Fhu Nypel Usługi Hydrauliczne Łukasz Szydliński
TEL:698095573
END:VCARD
```

