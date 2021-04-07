# uzmi node.js image ( sa instaliranim node )
# nazovi ga basebuild
FROM node:14.16.1-stretch as basebuild
# dodajemo angularove alate tj. njegov cli i kesiramo
RUN npm install -g @angular/cli

# kopiraj basebuild (kesiran) u build
FROM basebuild as build
# setujemo folder gde cemo kopirati code od angulara
WORKDIR /app
# cache buster - zelimo uvek nove angular fielove
ADD https://google.com cache_bust
# kopiramo angular files iz front foldera
COPY front/ .
# instaliramo biblioteke iz package.json koje su potrebne angularu
RUN npm install
# buildujemo angular i smestamo buldovane fileove u folder dist
# obrati paznju na --output-path dist - ovde kazemo folder relativan u odnosu na /app
# obrati paznju na --prod - ovde kazemo da napravi produkcionu verziju
RUN ng build --prod --output-path dist

# uzimamo nginx kao finalni image
FROM nginx AS final
# interni port nginx-a koji cemo mapirati u compose file
# nginx koristi port 80 za http
EXPOSE 80

# uklanjamo fileove koji se po defaultu nalaze u folderu koji nginx servuje
RUN rm -rf /usr/share/nginx/html/*
# kopiramo angularove file-ove u folderu koji nginx servuje
# --from=build - iz koga prethodnog containera
# /usr/share/nginx/html ovo je neginx default folder
COPY --from=build /app/dist /usr/share/nginx/html
