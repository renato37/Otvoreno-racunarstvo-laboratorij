--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

-- Started on 2020-10-26 20:47:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16622)
-- Name: dijelovi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dijelovi (
    id integer,
    dio character varying(255),
    materijal character varying(255) NOT NULL
);


ALTER TABLE public.dijelovi OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16608)
-- Name: glazbeni_instrumenti; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.glazbeni_instrumenti (
    naziv character varying(255) NOT NULL,
    wikipedija character varying(255) NOT NULL,
    vrsta_instrumenta character varying(255),
    zemlja_podrijetla character varying(255),
    "stoljeće_pojave" integer,
    "glazbeni_žanrovi" character varying(255)[],
    dijelovi integer,
    "način_sviranja" character varying(255),
    "najpoznatiji_izvođači" character varying(255)[],
    "najpoznatiji_proizvođači" character varying(255)[]
);


ALTER TABLE public.glazbeni_instrumenti OWNER TO postgres;

--
-- TOC entry 2820 (class 0 OID 16622)
-- Dependencies: 203
-- Data for Name: dijelovi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dijelovi (id, dio, materijal) FROM stdin;
2	Žice	Metal
2	Glava	Drvo
2	Tijelo	Drvo
2	Vrat	Drvo
1	Prve tri žice	Najlon
1	Druge tri žice	Metal
1	Glava	Drvo
1	Tijelo	Drvo
1	Vrat	Drvo
3	Tipke	Slonovača
3	Žice	Metal
3	Kućište	Drvo
3	Pedale	Metal
4	Žice	Metal
4	Glava	Drvo
4	Tijelo	Drvo
4	Vrat	Drvo
5	Cijela	Drvo
5	Cijela	Metal
6	Činele	Metal
6	Udaraljke	Drvo
6	Okvir bubnja	Metal
6	Bubanj	Koža
7	Tipke	Plastika
7	Kućište	Plastika
7	Elektronika	Tranzistori i diode
8	Mjeh	Koža
8	Svirale	Drvo
9	Tipke	Slonovača
9	Cijevi	Metal
9	Kućište	Drvo
9	Pedale	Metal
10	Tipke	Plastika
10	Gumbi	Plastika
10	Mjehov	Koža
\.


--
-- TOC entry 2819 (class 0 OID 16608)
-- Dependencies: 202
-- Data for Name: glazbeni_instrumenti; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.glazbeni_instrumenti (naziv, wikipedija, vrsta_instrumenta, zemlja_podrijetla, "stoljeće_pojave", "glazbeni_žanrovi", dijelovi, "način_sviranja", "najpoznatiji_izvođači", "najpoznatiji_proizvođači") FROM stdin;
Klasična gitara	https://en.wikipedia.org/wiki/Classical_guitar	Kordofon	Španjolska	18	{Klasika,Tango}	1	Trzanjem prstima po žicama	{"Joaquín Rodrigo"}	{Cordoba,YAMAHA}
Klavir	https://bs.wikipedia.org/wiki/Klavir	Glazbala s tipkama	Italija	18	{Klasika}	3	Pritiskanjem tipki batić udara po žicama	{"Wolfgang Amadeus Mozart","Johann Sebastian Bach","Ludwig van Beethoven"}	{FAZIOLI,Grotrian}
Električna gitara	https://hr.wikipedia.org/wiki/Elektri%C4%8Dna_gitara	Kordofon	Amerika	20	{Pop,Rock,Jazz,Blues}	2	Trzanjem trzalicom po žicama	{"Jimi Hendrix","Eric Clapton","Jimmy Page","Jeff Beck"}	{Gibson,Fender,Ibanez,Epiphone}
Tambura	https://hr.wikipedia.org/wiki/Tambura	Kordofon	Hrvatska	14	{Pop,"Narodna glazba",Jazz}	4	Trzanjem trzalicom po žicama	{"Mijo Majer","Milan Stahuljak","Siniša Leopold"}	{Molnar,"Kudlik Bela",Križanec}
Flauta	https://hr.wikipedia.org/wiki/Flauta	Aerofon	Njemažka	19	{Klasika}	5	Puhanjem se ostvaruje zvuk vibracijom zraka	{"Theobald Boehm","James Galway","James Phelan"}	{YAMAHA,"Junan XuQui Musical Co."}
Bubnjarski komplet	https://hr.wikipedia.org/wiki/Bubnjarski_komplet	Udaraljke	Velika Britanija	18	{Klasika,Jazz,Blues,Rock,Pop,"Hip hop"}	6	Udaranjem palica po membranama pojedinih dijelova	{"Roger Taylor","Steven Adler","Charlie Watts","John Bonham"}	{YAMAHA,Rockers,Gretsch}
Sintisajzer	https://hr.wikipedia.org/wiki/Sintesajzer	Elektrofoni	Amerika	20	{Rock,Pop}	7	Pritiskanjem gumba na tastaturi računalo pušta zvukove određene frekvencije	{"Brockett Parsons","Brittani Washington","Myron McKinley"}	{Casio,YAMAHA}
Gajde	https://hr.wikipedia.org/wiki/Gajde	Aerofon	Hrvatska	18	{"Narodna glazba"}	8	Protokom zraka kroz šuplje drvo stvaraju se određeni tonovi	{"Joza Bičanić","Marko Drventić","Adam Vuksanović"}	{"Joza Bičanić","Marko Drventić","Stjepan Večković"}
Orgulje	https://hr.wikipedia.org/wiki/Orgulje	Aerofon/Glazbala s tipkama	Francuska	8	{Klasika,"Crkvena glazba"}	9	Strujanjem zraka kroz cijevi različitih dimenzija dolazi do tonova različitih frekvencija	{"Višeslav Jaklin","Milan Hibšer"}	{Fabing,Fischer}
Harmonika	https://hr.wikipedia.org/wiki/Harmonika	Aerofon	Francuska	19	{"Narodna glazba",Klasika}	10	Pritiskanjem tipki i gumba te stiskanjem mjeha dolazi do strujanja zraka stvarajući tonove određenih frekvencija	{"Peter Soave","Franko Božac"}	{"Franzu Friedrichu Buschmannu",GOLDENCUP}
\.


--
-- TOC entry 2692 (class 2606 OID 16615)
-- Name: glazbeni_instrumenti glazbeni_instrumenti_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.glazbeni_instrumenti
    ADD CONSTRAINT glazbeni_instrumenti_pkey PRIMARY KEY (naziv);


-- Completed on 2020-10-26 20:47:26

--
-- PostgreSQL database dump complete
--

