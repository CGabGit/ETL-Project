--
-- PostgreSQL database dump of the "stepstone" database.
--
-- The sample data used in the stepstone database was scraped from Stepstone.de in 2022


BEGIN;

SET client_encoding = 'UTF8';

--
-- Name: tbl_status ; Type: TABLE; Schema: public
--

CREATE TABLE tbl_status (
    is_finnished int,
    record_date text
);


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
-- Name: tbl_jobitems; Type: TABLE; Schema: public
--

CREATE TABLE tbl_jobitems (
    job_id integer,
    title text,
    companyname text,
    location text,
    contracttype text,
    worktype text,
    onlinedate timestamp without time zone,
    descriptiontext text,
    profiletext text
);

--
-- Name: word_freq ; Type: TABLE; Schema: public
--

CREATE TABLE tbl_word_freq (
    word text,
    frequency bigint,
    record_date text
);

--
-- Name: bigrams ; Type: TABLE; Schema: public
--

CREATE TABLE tbl_bigrams (
    bigrams text,
    frequency bigint,
    record_date text
);

--
-- Name: trigrams ; Type: TABLE; Schema: public
--

CREATE TABLE tbl_trigrams (
    trigrams text,
    frequency bigint,
    record_date text
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

--
--Data for Name: tbl_jobitems; Type: TABLE DATA; Schema: public
--

COPY tbl_jobitems (job_id, title, companyname, location, contracttype, worktype, onlinedate, descriptiontext, profiletext) FROM stdin;
7582369	Wirtschaftsinformatiker/ Informatiker als SAP-Berater mit Schwerpunkt SD/MM (m/w/d)	team neusta GmbH	Bremen	Feste Anstellung	Vollzeit	2021-10-06 07:24:31	<div class="at-section-text-description-content listingContentBrandingColor sc-lhVmIH kiChPJ"><ul><li>Konzernweite Betreuung für den Bereich SAP-SD /-MM</li><li>Projektmanagement für nationale und internationale Projekte</li><li>Intensive Zusammenarbeit mit unterschiedlichen Stakeholdern sowie Konzeption und Optimierung von Geschäftsprozessen</li><li>Begleitung des Changemanagements und technischer Änderungen</li><li>Koordination externer Berater und Projektteams</li><li>Umsetzung von Customizing- und Entwicklungsanforderungen der Fachbereiche</li><li>Customizing und Betreuung von modulübergreifenden Geschäftsprozessen</li><li>Durchführung von Funktions- und Integrationstests</li><li>First- und Second-Level Support (national und international)</li><li>Durchführung von Schulungen (national und international)</li></ul></div>	<div class="at-section-text-profile-content listingContentBrandingColor sc-lhVmIH kiChPJ"><ul><li>Abgeschlossenes Studium der Informatik, Wirtschaftsinformatik oder eine vergleichbare Ausbildung</li><li>Mehrere Jahre Berufserfahrung als SAP-Berater sowie Beraterkenntnisse in den SAP-Modulen SD und MM</li><li>Erfahrung in der Entwicklung und im Customizing von Unternehmensprozessen in SAP</li><li>Kenntnisse in der Implementierung von S/4HANA-Lösungen</li><li>Projektmanagement-Know-How im nationalen und internationalem Umfeld</li><li>Grundlegende Kenntnisse im Bereich Geschäftsprozessmodellierung sowie (IT-)Projektmanagement</li><li>Ausgeprägtes Verständnis für betriebswirtschaftliche Zusammenhänge sowie ein ausgeprägtes analytisches Denkvermögen</li><li>Sehr gute Deutsch- und Englischkenntnisse</li><li>Reisebereitschaft (inkl. Auslandsreisen)</li></ul></div>
\.
COMMIT;


