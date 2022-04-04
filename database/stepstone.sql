--
-- PostgreSQL database dump of the "stepstone" database.
--
-- The sample data used in the stepstone database was scraped from Stepstone.de in 2022


BEGIN;

SET client_encoding = 'UTF8';

--
-- Name: tbl_numresultsfound; Type: TABLE; Schema: public
--

CREATE TABLE tbl_numresultsfound (
    daterecoded timestamp without time zone,
    searchterm text,
    searchresults integer
);

--
-- Name: tbl_searchresults; Type: TABLE; Schema: public
--

CREATE TABLE tbl_searchresults (
    job_id integer,
    job_title character varying(200),
    job_link character varying(800),
    date_scraped timestamp without time zone
);


--
-- Data for Name: tbl_searchresults; Type: TABLE DATA; Schema: public
--

COPY tbl_searchresults (job_id, job_title, job_link, date_scraped) FROM stdin;
7582369	Wirtschaftsinformatiker/ Informatiker als SAP-Berater mit Schwerpunkt SD/MM (m/w/d)	/stellenangebote--Wirtschaftsinformatiker-Informatiker-als-SAP-Berater-mit-Schwerpunkt-SD-MM-m-w-d-Bremen-team-neusta-GmbH--7582369-inline.html	2021-11-23 23:47:13
7679410	Consultant IT-Projekte Non Food Einkauf International (m/w/d); Projektmanager; Wirtschaftsinformatiker ; Wirtschaftsingenieur ; Wirtschaftsmathematiker (m/w/d)	/stellenangebote--Consultant-IT-Projekte-Non-Food-Einkauf-International-m-w-d-Projektmanager-Wirtschaftsinformatiker-Wirtschaftsingenieur-Wirtschaftsmathematiker-m-w-d-Neckarsulm-Lidl-Stiftung-Co-KG--7679410-inline.html	2021-11-23 23:47:14
\.


-- 
-- Data for Name: tbl_numresultsfound; Type: TABLE DATA; Schema: public
--

COPY tbl_numresultsfound (daterecoded, searchterm, searchresults) FROM stdin;
2021-11-23 23:15:27	Wirtschaftsinformatiker	1857
2021-11-23 23:16:39	Wirtschaftsinformatiker	1857
2021-11-23 23:20:11	Wirtschaftsinformatiker	1857
2021-11-23 23:47:13	Wirtschaftsinformatiker	1843
2021-11-24 10:59:52	Wirtschaftsinformatiker	1848
2021-11-24 13:06:25	Wirtschaftsinformatiker	1847
2021-11-24 16:08:20	Wirtschaftsinformatiker	1861
2021-11-24 17:03:18	Wirtschaftsinformatiker	1865
2021-11-24 19:18:29	Wirtschaftsinformatiker	1866
\.

COMMIT;


