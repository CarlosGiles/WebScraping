# Automatizar la web y Web Scraping para una las noticias

Para hacer **web scraping** y **automatización web** es necesario conocer los elementos de una **página web**, por esta razón, se revisarán determinados elementos y tecnologías de una página.

![what-is-html](https://user-images.githubusercontent.com/92232878/182262874-8f556587-830c-48a7-a800-7a8182bd7c65.jpg)

## Tags y elementos

* Tendremos un tag de apertura y un tag de cierre:

![image](https://user-images.githubusercontent.com/92232878/182263047-7e26bd9a-751e-4bfe-8183-d12c4f5e7b0b.png)

* Los **tributos** van dentro **tag** de apertura y ayudan a personalizar:

![image](https://user-images.githubusercontent.com/92232878/182263642-8159cb11-3ded-4a0a-b3e6-6db4dea04052.png)

* Contenido, va entre los **tag** de apertura y cierre, es el contenido de la página y el elemento que se ve afectado por el **tag** y por los **atributos**:

![image](https://user-images.githubusercontent.com/92232878/182263811-a2ea9898-90f5-4937-bfd7-fb610d0b431c.png)

El conjunto de los elementos anteriores es conocido como **elemento html** o **nodo**:

![image](https://user-images.githubusercontent.com/92232878/182264040-b88809a0-773e-420c-b14e-e8d858c201ca.png)

## Distintos tags

![image](https://user-images.githubusercontent.com/92232878/182264294-b78e0627-4aff-4816-8606-f13a07b465d5.png)

* **head** es el encabezao de la sección y se usa normalente para metadata.
* **body** es el cuerpo del documento **html**.
* **header** contiene una introducción al contenido que normalmente va en la parte de arriba o inicial del **body**.
* **p** sinifica párrafo y contiene segmentos de texto.
* **h1**, **h2**, **h3**... son títulos y subtítulos respectivamente de forma ascendente.

Podemos ver estos tags en [esta página](https://subslikescript.com/movie/The_Luck_of_the_Irish-274636) que más adelante usaremos para hacer webscraping.
Para ello damos click derecho y nos vamos a ***inspeccionar***:

![image](https://user-images.githubusercontent.com/92232878/182265361-c3a63215-e2e6-42c9-ac45-567d65bb46e9.png)

Se abrirá la consola con el código html donde serán visibles los **tags**:

![image](https://user-images.githubusercontent.com/92232878/182265478-2636b994-8464-4412-93a0-2ae8c3e49cda.png)

### Los siguientes **tags** son los que veremos frecuentemente al hacer **webscraping**:

* **div** es un divisor o contenedor genérico.
* **nav** es la zona donde está la barra de aginación.
* **li** representa a elemntos de una lista.
* **a** es anchor, anclaje/enlace a documento u otra página.

![image](https://user-images.githubusercontent.com/92232878/182267782-69d2da6f-51e3-4813-a131-383f6820699f.png)

* **button** es un botón en el que podemos hacer click.
* **table** es una tabla con filas y columnas que contienen data que puede ser extraída.
* **td** "table data", siempre dentro de una tabla y son los datos de la misma.
* **tr** "table row", siempre dentro de una tabla y son las filas.
* **ul** unordered lista, lista desordenada.
* **iframe** permite colocar una página dentro de otra

![image](https://user-images.githubusercontent.com/92232878/182268498-02e3a5bd-11e5-4717-b635-efc9fcd5c50d.png)
