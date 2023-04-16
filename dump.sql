--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

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

ALTER TABLE ONLY public.search_record DROP CONSTRAINT search_record_pkey;
ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
ALTER TABLE public.search_record ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE public.search_record_id_seq;
DROP TABLE public.search_record;
DROP TABLE public.alembic_version;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: digfutsys
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO digfutsys;

--
-- Name: search_record; Type: TABLE; Schema: public; Owner: digfutsys
--

CREATE TABLE public.search_record (
    id integer NOT NULL,
    owner character varying,
    group_name character varying,
    query_datetime timestamp without time zone,
    search_word character varying
);


ALTER TABLE public.search_record OWNER TO digfutsys;

--
-- Name: search_record_id_seq; Type: SEQUENCE; Schema: public; Owner: digfutsys
--

CREATE SEQUENCE public.search_record_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.search_record_id_seq OWNER TO digfutsys;

--
-- Name: search_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: digfutsys
--

ALTER SEQUENCE public.search_record_id_seq OWNED BY public.search_record.id;


--
-- Name: search_record id; Type: DEFAULT; Schema: public; Owner: digfutsys
--

ALTER TABLE ONLY public.search_record ALTER COLUMN id SET DEFAULT nextval('public.search_record_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: digfutsys
--

COPY public.alembic_version (version_num) FROM stdin;
ba2d3a5cd4a6
\.


--
-- Data for Name: search_record; Type: TABLE DATA; Schema: public; Owner: digfutsys
--

COPY public.search_record (id, owner, group_name, query_datetime, search_word) FROM stdin;
1       +79119124039    ТОЛЬЯТТИ        2023-04-16 14:16:37.750531      толь
2       +79119124039    ТОЛЬЯТТИ        2023-04-16 14:16:37.823177      толь
3       +79119124039    СОБЫТИЯ ТОЛЬЯТТИ        2023-04-16 14:16:37.828153      толь
4       +79119124039    Регион 63 | Самара | Тольятти   2023-04-16 14:16:37.831964      толь
5       +79119124039    Цвет Папоротника | Гильдия мастеров г. Тольятти 2023-04-16 14:16:37.835613      толь
6       +79119124039    Аджилити в Тольятти     2023-04-16 14:16:37.841706      толь
\.


--
-- Name: search_record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: digfutsys
--

SELECT pg_catalog.setval('public.search_record_id_seq', 6, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: digfutsys
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: search_record search_record_pkey; Type: CONSTRAINT; Schema: public; Owner: digfutsys
--

ALTER TABLE ONLY public.search_record
    ADD CONSTRAINT search_record_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--
