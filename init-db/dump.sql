--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

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
-- Name: breeds; Type: TABLE; Schema: public; Owner: qwerty
--

CREATE TABLE public.breeds (
    name character varying NOT NULL,
    id integer NOT NULL,
    created_at character varying NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.breeds OWNER TO qwerty;

--
-- Name: breeds_id_seq; Type: SEQUENCE; Schema: public; Owner: qwerty
--

CREATE SEQUENCE public.breeds_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.breeds_id_seq OWNER TO qwerty;

--
-- Name: breeds_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qwerty
--

ALTER SEQUENCE public.breeds_id_seq OWNED BY public.breeds.id;


--
-- Name: cats; Type: TABLE; Schema: public; Owner: qwerty
--

CREATE TABLE public.cats (
    color character varying NOT NULL,
    age integer NOT NULL,
    description character varying NOT NULL,
    breed_id integer NOT NULL,
    id integer NOT NULL,
    created_at character varying NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


ALTER TABLE public.cats OWNER TO qwerty;

--
-- Name: cats_id_seq; Type: SEQUENCE; Schema: public; Owner: qwerty
--

CREATE SEQUENCE public.cats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cats_id_seq OWNER TO qwerty;

--
-- Name: cats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: qwerty
--

ALTER SEQUENCE public.cats_id_seq OWNED BY public.cats.id;


--
-- Name: breeds id; Type: DEFAULT; Schema: public; Owner: qwerty
--

ALTER TABLE ONLY public.breeds ALTER COLUMN id SET DEFAULT nextval('public.breeds_id_seq'::regclass);


--
-- Name: cats id; Type: DEFAULT; Schema: public; Owner: qwerty
--

ALTER TABLE ONLY public.cats ALTER COLUMN id SET DEFAULT nextval('public.cats_id_seq'::regclass);


--
-- Data for Name: breeds; Type: TABLE DATA; Schema: public; Owner: qwerty
--

COPY public.breeds (name, id, created_at, updated_at) FROM stdin;
сфинкс	1	2023-09-02T17:31:25.857666	2023-09-02 17:31:25.857666+00
мейн-кун	2	2023-09-02T17:31:25.857666	2023-09-02 17:31:25.857666+00
сиамский	3	2023-09-02T17:31:25.857666	2023-09-02 17:31:25.857666+00
британец	4	2023-09-02T17:31:25.857666	2023-09-02 17:31:25.857666+00
персидский	5	2023-09-02T17:31:25.857666	2023-09-02 17:31:25.857666+00
\.


--
-- Data for Name: cats; Type: TABLE DATA; Schema: public; Owner: qwerty
--

COPY public.cats (color, age, description, breed_id, id, created_at, updated_at) FROM stdin;
красный	10	толстый	1	2	2024-10-01 13:19:22.53712+00	2024-10-01 13:19:22.53712+00
красный	13	вечно голодный	3	4	2024-10-01 13:21:14.216862+00	2024-10-01 13:21:14.216862+00
серый	25	высокий	4	5	2024-10-01 13:21:30.119861+00	2024-10-01 13:21:30.119861+00
черный	15	худой	2	3	2024-10-01 13:20:59.079318+00	2024-10-01 13:21:49.356103+00
\.


--
-- Name: breeds_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qwerty
--

SELECT pg_catalog.setval('public.breeds_id_seq', 1, false);


--
-- Name: cats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: qwerty
--

SELECT pg_catalog.setval('public.cats_id_seq', 5, true);


--
-- Name: breeds breeds_pkey; Type: CONSTRAINT; Schema: public; Owner: qwerty
--

ALTER TABLE ONLY public.breeds
    ADD CONSTRAINT breeds_pkey PRIMARY KEY (id);


--
-- Name: cats cats_pkey; Type: CONSTRAINT; Schema: public; Owner: qwerty
--

ALTER TABLE ONLY public.cats
    ADD CONSTRAINT cats_pkey PRIMARY KEY (id);


--
-- Name: ix_breeds_id; Type: INDEX; Schema: public; Owner: qwerty
--

CREATE INDEX ix_breeds_id ON public.breeds USING btree (id);


--
-- Name: ix_breeds_name; Type: INDEX; Schema: public; Owner: qwerty
--

CREATE UNIQUE INDEX ix_breeds_name ON public.breeds USING btree (name);


--
-- Name: ix_cats_age; Type: INDEX; Schema: public; Owner: qwerty
--

CREATE INDEX ix_cats_age ON public.cats USING btree (age);


--
-- Name: ix_cats_color; Type: INDEX; Schema: public; Owner: qwerty
--

CREATE INDEX ix_cats_color ON public.cats USING btree (color);


--
-- Name: ix_cats_description; Type: INDEX; Schema: public; Owner: qwerty
--

CREATE INDEX ix_cats_description ON public.cats USING btree (description);


--
-- Name: ix_cats_id; Type: INDEX; Schema: public; Owner: qwerty
--

CREATE INDEX ix_cats_id ON public.cats USING btree (id);


--
-- Name: cats cats_breed_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: qwerty
--

ALTER TABLE ONLY public.cats
    ADD CONSTRAINT cats_breed_id_fkey FOREIGN KEY (breed_id) REFERENCES public.breeds(id);


--
-- PostgreSQL database dump complete
--

