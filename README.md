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
curl http://127:0.0.1:25000/rev/SimpleString
```
Response:
```
{
    "data": "gnirtSelpmiS"
}
```

## lab2 - String Api 

Applictaion check if provided string contains:
* lower letter
* upper letter
* special sign
* digit

### Make a request #1

```
curl http://127:0.0.1:25000/api/check/SimpleString
```
Response:
```
{
    "digit": false,
    "lowerCase": true,
    "specialSign": false,
    "upperCase": true
}
```

### Make a request #2

```
curl http://127:0.0.1:25000/api/check/Simple123String%
```
Response:
```
{
    "digit": true,
    "lowerCase": true,
    "specialSign": true,
    "upperCase": true
}
```

## lab3 - Mobile WEEIA Calendar

Application is designed for creating 'ics' files, that could be imported to different calendar apps.
Events are parsed from: http://www.weeia.p.lodz.pl/ 

### Request syntax
```
curl http://127:0.0.1:25000/api/calendar/<year>/<month>
```

### Make a request #1

```
curl http://127:0.0.1:25000/api/calendar/2020/3
```
Response:
```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/lLljaA
BEGIN:VEVENT
DTSTART;VALUE=DATE:20200309
SUMMARY:First Step to Fields Medal
.
.
.
END:VCALENDAR

Via browser, server will produce file named: "my.ics";
```

This project is licensed under the MIT License.

