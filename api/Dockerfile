# ovo je bazni kontainer, u ovom slucaju sadrzi python preinstaliran ( linux )
# instaliran je i pip
FROM python:3.8 AS base
# koji port exposujemi u docker mrezi
EXPOSE 8004

# rename kontainera
FROM base AS build
# ovaj folder u rutu ce se koristi za apilikaciju
WORKDIR /app

# kopiramo listu potrebnih python biblioteka
COPY "api/requirements.txt" requirements.txt

# install python biblioteka
RUN pip install -r requirements.txt;

# rename kontainera
FROM build AS final
# cache buster - da bi uvek uzimali sveze .py fileove ( i ostale )
ADD https://google.com cache_buster

# kopiramo source iz api foldera ( sve ) - kontext je root projekta preslikano iz compose-a
COPY "api/" .

# ovim pokrecemo api tj program
CMD [ "python", "-u", "./server.py" ]