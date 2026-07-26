---
📅 created: 26.07.2026 22:23
aliases:
tags:
author: Martin
---


# [[Was Kommunen für ihre digitale Souveränität tun können]]


1. In Ausschrebigungen Daten unter offenen Lizenzen fordern
2. OpenSource in der BEschaffung verankern
3. Kommunale IT Fähigkeiten in der Verwaltung aufbauen
4. Ressourcen über mehrere Kommunen bündeln
5. Prüfen und wechseln zu quelloffenen Angeboten
6. Lokale Versuchslabore und Unternehmen beauftragen

## 1. In Ausschreibungen Daten unter offenen Lizenzen fordern

Bei Ausschreibungen und Vergapeprozessen muss Gießen unbeschränkten Zugriff auf erzeugte Daten einfordern, bestenfalls nach offenen Standards.
So entsteht Datenhoheit, rechtlich abgesichert, ohne später von den Herstellern abhängig zu sein um die Daten flott vollständig auszuwerten.

Rechtliche Rahmenbedingungen & Grundlagen
- **EU-Datenakt (Data Act) - Verordnung (EU) 2023/2854[22]**: Dateninhaber (UNternehmen) sind verpflichtet zur Erfüllung im öffentlichen Interesse liegender Aufgaben der öffentlichen Hand Daten von IoT-Geräten (maschinenlesbar) zur Verfügung zu stellen. Ausgneommen sind "kleine Unternehmen"[25].[23]

## 2. OpenSource in der Beschaffung verankern
OpenSource muss in den Beschaffungsprozess integriert werden. Dazu gibt es bereits zahlreiche rechtliche und vertragliche Vorlagen.

- **Sachliche Begründung gemäß § 31 VgV und **§ 23 Abs. 1 und Abs. 3 UVgO**.: Datenhoheit und Interoperabilität können in Ausschreibungen eingefordert werden.
	- Vendor-Lock-in-Effekte vermeiden und langfristige Datenhoheit absichern sind erforderliche sachliche Rechtfertigung.[27] 
	- Nach einem EuGH-Urteil sind elsbt herbeigeführte Vendor-Lock-Ins kein Grund einen Anbieter zu bevorzugen. [28]
- **EVB-IT-Vertragsmuster (März 2026)**[26]: Die vom BMDS überarbeiteten Vertragsmuster machen Open-Source-Software und offene Datenstandards zum neuen **Einkaufsstandard**. 
	- Die Pflicht zur Bereitstellung einer Software-Stückliste (SBOM) 
	- sowie Konzepte zur standardisierten Datenherausgabe bei Vertragsende sind direkt verankert. 
	- Auch Kommunen müssen diese Vorlagen verwenden [29]

Maßnahmen:
- **Daten-Eigentumsklausel**: Verträge mit Software-Diensten und IoT-Betreibern (z. B. Smart-City-Sensoren, Verkehrsdaten, Ampelanlagen, Vermessungsgeräte) müssen der Stadt vollen Zugriff auf die Rohdaten geben.
- **Nachnutzung vorbereiten**: Eigen- und Auftragsentwicklungen der Kommune müssen unter einer OpenSource Lizenz auf der Platform OpenCoDE bereitgestellt werden.[21 S.27]
- **Format-Vorgaben**: Vorschrift von offenen, maschinenlesbaren Standards (z. B. JSON, CSV, GeoJSON) bei der Datenübergabe im Lastenheft.
- **Lizenz-Zwang**: Durch Dienstleister erhobene kommunalen Daten unter der Lizenz **Creative Commons Zero (CC0)**[20] oder **Datenlizenz Deutschland (dl-de/by-2-0)** bereitstellen.

### EU-Datenakt (Data Act) - Verordnung (EU) 2023/2854
**Inhalt:** Die Verordnung trat am 11. Januar 2024 in Kraft und wird in den wesentlichen Teilen seit dem **12. September 2025** europaweit verbindlich angewendet.[22] [23] 
Sichert Nutzern von IoT-Geräten direkten unverschlüsselten Zugriff auf (maschinenlesbare) Rohdaten zu.[24]

**Kommunen/öffentliche Hand** - Kapitel V (Art. 14 bis 22 Data Act): 
Verpflichtet Dateninhabern (Unternehmen), Daten bei „außergewöhnlicher Notwendigkeit“ oder zur Erfüllung einer im öffentlichen Interesse liegenden Aufgabe der öffentlichen Hand zur Verfügung zu stellen. 
Zudem sichert das Prinzip „Access by Design“ (Art. 3) Nutzern von IoT-Geräten den direkten, unverschlüsselten Rohdatenzugriff.[22] [23] [24]

#### EVB-IT-Vertragsmuster (März 2026)
Der Anwendungsbereich ist extrem breit gefächert. Die EVB-IT müssen von Bundesbehörden verpflichtend (und von Kommunen meist freiwillig oder per Bundeslands-Erlass) für fast den gesamten IT-Einkauf genutzt werden.[29]

Die neuen Voralgen sehen vor:
- **Open Source wird Standard (OSS)**: Wenn eine Kommune eine Individualsoftware programmieren lässt, ist **Open Source nun der vertragliche Regelfall**.
- **Transparenzpflicht (SBOM):** Auftragnehmer müssen eine digitale Stückliste (Software Bill of Materials - SBOM) mitliefern. Die SBOM erhöht die Transparenz,  und sieht welche Open-Source-Bibliotheken verbaut wurden, um Sicherheitsrisiken schneller zu patchen. Die Cyberressilienz-Verordnung schreibt ein SBOM mitlerweile vor.[30]
- **Bereistellung per OpenCoDE**: Falls in der Vorlage angekreuzt, muss der Auftragnehmer die geschriebne Software auf dem Bundeseigenen Code-Verwaltungsplatform [[openCode]] [31] veröffentlichen.[32]

### Vergaberechtliche Begründung (Produktneutralität & herstellerneutrale Kriterien)
**Inhalt:**
Öffentliche Auftraggeber dürfen herstellerunabhängige Anforderungen an Datenstrukturen und Interoperabilität stellen, um Abhängigkeiten zu vermeiden. Pflicht zur funktionalen Leistungsbeschreibung.

**§ 31 VgV (Vergabeverordnung):**
Technische Leistungsbeschreibung, erlaubt Ziele für INteroperabilität und offene Datenformate festzulegen. Sofern sie für den Auftragsgegenstand sachlich gerechtfertigt sind.

Fordert Produktneutralität, erlaubt ausdrücklich spezifische technische Anforderungen (wie offene APIs), wenn der Verwendungszweck (z.B. die Integration in das städtische Open-Data-Portal) das erfordert.


---

## 3. Kommunale IT Fähigkeiten in der Verwaltung aufbauen


## 4. Ressourcen über mehrere Kommunen bündeln

Kommunale IT-Alleingänge erzeugen:
- hohe Lizenzkosten und 
- binden knappe personelle Ressourcen. 
Durch interkommunale Kooperation (IKZ) können Kommunen wie Gießen Entwicklungskosten für Open-Source-Software (OSS) teilen, Kosten senken und  gemeinsame Standards etablieren.

#### Rechtliche Rahmenbedingungen & Grundlagen

- **Hessisches Gesetz über kommunale Gemeinschaftsarbeit (KGG)**: Kommunne können REssourcen und Aufträge bündeln
    - **§ 1 KGG (Formen)**: Erlaubt Kommunen zusammenzuarbeiten. Über Arbeitsgemeinschaften, Verträge, Zweckverbände oder gemeinsame Kommunalunternehmen (gKU).
    - **§ 2 KGG (Öffentlich-rechtlicher Vertrag)**: Ermöglicht es Gießen, mit Partnerstädten (z. B. Marburg, Wetzlar) zu vereinbaren, dass eine Kommune die Softwareentwicklung oder das Hosting federführend für die anderen übernimmt.
- **Inhouse-Vergabe und interkommunale Zusammenarbeit (§ 108 GWB)**:
	- **§ 108 Abs. 6 GWB**: Erlaubt die ausschreibungsfreie Vergabe von IT-Dienstleistungen zwischen den beteiligten Städten [GWB]. Die Kooperation darf nur dem öffentlichen Interesse dienen, und die Partner müssen weniger als 20 Prozent der Leistung am Markt erbringen [GWB]. Das Teilen von quelloffenem Programmcode erfüllt diese Kriterien vollständig.


#### Bestehende Strukturen und Projekte der Stadt Gießen

- **Allianz „Digitale Kommune@Hessen“**: Gießen bildet mit **Bad Nauheim, Fulda, Marburg, Limburg, Offenbach und Wetzlar** einen festen überregionalen Verbund um das Onlinezugangsgesetz umtusetzen. [42] 
- **Interkommunale Datenstrategie und Data Governance**: [43]
- **Projekt „Open Smart City“**: Gießen setzt mit Partnerstädten eine offene urbane Datenplattform und eine modulare Bürger-App um [Digitale Kommune Hessen]. Das Ziel ist der Aufbau eines gemeinsamen, herstellerunabhängigen Daten-Ökosystems auf Open-Source-Basis zur Vermeidung von US-amerikanischen Cloud-Abhängigkeiten [44] [Digitale Kommune Hessen].
- **Projekt „HessenNext“**: Städtebündnisses etabliert gemeinsame Digitalisierungslabore [41] und baut Sensortechnik aus (z. B. Bodenfeuchte, Hochwasserschutz, Verkehrsfluss und Bürgerbeteiligung).[40]


#### Konkrete Maßnahmen für die Stadt Gießen
- **Gemeinsame Vergabeverfahren**: Gießen nutzt die Allianz, um Softwareentwicklungen im Verbund auszuschreiben. Die Kosten für Software-Pflegeverträge (Maintenance) werden proportional auf die sechs Städte aufgeteilt.
- **Beteiligung am Kommunalen Open-Source-Board**: Einbringung personeller Ressourcen in dieses Gremium der kommunalen Spitzenverbände zur Definition bundesweiter OSS-Standards [Kommune21].

#### Verfügbare Mustersatzungen und Verträge
- **Mustervereinbarungen des IKZ-Kompetenzzentrums Hessen**: Standardisierte Vorlagen für öffentlich-rechtliche Verträge nach dem KGG [IKZ Hessen].
- **BMI-Vergabehandbuch für Kooperationen**: Vorlagen zur rechtssicheren Gestaltung von Verträgen nach § 108 GWB ohne Vergabe-Ausschreibung [BMI].




---

## Praxisbeispiele - Andere Städte und LÄnder schaffen (manchmal) den Wechsel

Übergeordnete Initiativen wie das Tech-Souveränitäts-Paket der EU-Kommission mangelt es an verbindlichen Vorgaben.
Neben den vorherschenden ideologischen oder Kostenaspekten rückt nun die digitale Souveränitet immer weiter in de nFokus.
Lokale Regierungen und Kommunen schaffen rasche Erfolge, brauchen langfristig finanzielle Absicherung um den Wechsel zu offenen Standards und OpenSoruce Software durchzuhalten.[5]
#### Schleswig-Holstein - IT Wechsel als Flächenland
[[Schleswig-Holstein]] wirft Microsoft-Produkte schrittweise aus der Verwaltung. 
Bis Ende 2025 etablierte die Verwaltung 25.000 IT-Arbeitsplätzen mit [[LibreOffice]] als Standard-Büropaket (Microsoft Office: Word, Excel, POwerpoint). 
Sie sersetzt Microsoft Exchange durch [[Open-Xchange]] und führt  [[Thunderbird]] als E-Mail-CLient ein. 
Zusätzlich setzt das Land auf offene Dokumentenformate.[1]

#### Dortmund - 2021 OpenSource per Ratsbeschluss
Der Stadtrat beschloss 2021: Bei Beschaffung oder Entwicklung neuer Software wird Open Source bevorzugt. 
Will eine Fachabteilung proprietäre Software kaufen, greift eine Begründungspflicht.

> "Wo möglich Nutzung von Open Source Software. Von der Verwaltung entwickelte oder zur Entwicklung beauftragte Software wird der Allgemeinheit zur Verfügung gestellt." [3]

Sie muss nachweisen, warum eine quelloffene Lösung nicht infrage kommt.[2]


#### Münchens teure OpenSource Lektion
Münchens Projekt „LiMux“ (Linux auf den Verwaltungsrechnern) scheiterte 2017 am politischem Richtungswechsel und organisatorischen Mängeln. 

Die Lektion:
Fachverfahren müssen mitgedacht werden (z. B. die Software im Einwohnermeldeamt) Es reicht nicht nur das Betriebsystem auf den REchnern zu ändern.[4]

Dazu müssen vermehrt webbasierte Open-Source-Plattformen oder Low-Code-Umgebungen bereitgestellt werden.


#### Amsterdam ist bis 2035 vollständig digital autonom
Die niederländische Hauptstadt verpflichtet sich mit dem Masterplan bis zum Jahr 2035 vollständig digital autonom zu agieren und proprietäre Lizenzen konsequent zurückzufahren. [5]


#### Seixal (Portugal) mit Problemen beim OpenSource Kurs  
2017 startete die portugisische Stadt Seixal die MIgration zu LibreOffice als Microsoft Office Ersatz. 
Seit 2019 ist LibreOffice dort die Standard-Bürosoftware, um offene Standards (ODF) gemäß nationalem Gesetz (Lei n.º 36/2011[11]) umzusetzen. Die Stadt stellte einige Dokumente auf selbst gehostete und Webbasierte Vorlagen um. Zudem gebe es nicht ausreichend IT Personal. [8] 

Zudem gab es Probleme im DOkumentenaustausch mit externen Organisationen. Komplexe Dokumente und Vorlagen haben hohe Kompatibilitäts- und Pflegeaufwänden. 
Im Jahr 2025 überführte Seixal internen Vorlagen schrittweise zu Microsoft Office 365 kompatiblen Vorlagen.[9]

#### Französische Behörden und Kommunen die LibreOffice nutzen

MIMO, die französische inter-ministeriale Arbeitsgruppe für freie Software nutzt [[LibreOffice]] auf fast 500.000 PCs.[7]
Außerdem nutzen diverse franzäsische Bhörden der BEreiche Energie, Landwirtschaft und Bildung ebenfalls Libreoffice.[6]

#### Übersicht über weitere Städte und Bemühungen zu OpenSource zu wechseln

Cybernews macht auf einer Karte nachvollziehbar welche Städte und Behörden in Europa den Wechsel zu OpenSource vollziehen wollen. [10] hat einen Tracker erstellt um in Europa bemühung


## Beispiele

### IDEE: Datenhoheits-Textbaustein
§ X Datenhoheit, Datenzugriff und Lizenzierung
- **Ausschließliches kommunales Daten-Eigentum:** Sämtliche Daten, die im Rahmen dieses Auftrags durch den Auftragnehmer, dessen Softwarelösungen oder eingesetzte Hardware (z. B. Sensoren, IoT-Komponenten) erhoben, generiert, verarbeitet oder gespeichert werden (nachfolgend „Projektdaten“), stehen im ausschließlichen rechtlichen und wirtschaftlichen Eigentum der Stadt Gießen.
- **Datenzugang und Schnittstellen:** Der Auftragnehmer ist verpflichtet, der Stadt Gießen den unbeschränkten, kontinuierlichen und echtzeitnahen Zugriff auf alle Projektdaten in unverarbeiteter Rohform (Rohdaten) zu gewähren. Der Datenabruf muss über eine standardisierte, offene und dokumentierte Programmierschnittstelle (API, z. B. REST-API) sowie in einem offenen, maschinenlesbaren Format (z. B. JSON, GeoJSON, CSV) ohne zusätzliche Kosten für die Stadt Gießen ermöglicht werden. Eine Verschlüsselung oder proprietäre Kapselung der Daten, die den Export oder die Weiterverarbeitung behindert, ist unzulässig.
- **Open-Data-Lizenzierung:** Die Stadt Gießen ist berechtigt, die Projektdaten im Rahmen des Hessischen E-Government-Gesetzes (§ 13 HEGovG) als Open Data zu veröffentlichen. Der Auftragnehmer räumt der Stadt Gießen hierzu das unwiderrufliche, zeitlich, räumlich und inhaltlich unbeschränkte Recht ein, die Projektdaten unter den Bedingungen der **Datenlizenz Deutschland – Namensnennung – Version 2.0 (dl-de/by-2-0)** oder der Lizenz **Creative Commons Zero (CC0 1.0 Universal)** an Dritte weiterzugeben und zu veröffentlichen.
- **Herausgabe bei Vertragsende:** Bei Beendigung des Vertragsverhältnisses hat der Auftragnehmer alle Projektdaten vollständig, in einem strukturierten, gängigen und maschinenlesbaren Format an die Stadt Gießen zu übergeben. Eine Zurückbehaltung der Daten ist ausgeschlossen. Der Auftragnehmer löscht nach erfolgreicher Bestätigung der Datenübergabe durch die Stadt Gießen alle dort verbliebenen Datenkopien datenschutzkonform und weist dies schriftlich nach.

## GLOSSAR


## QUELLEN

[1]  Von Microsoft zu Open Source: Wie Schleswig-Holstein den Wechsel schaffen will. 14.02.25. Keywan Tonekaboni. Christian Wölbert. heise: https://www.heise.de/hintergrund/Von-Microsoft-zu-Open-Source-Wie-Schleswig-Holstein-den-Wechsel-schaffen-will-10279400.html (26.07.2026)

[2] Dortmund goes Open Source – Ein großer Erfolg für Nachhaltigkeit in der städtischen IT-Landschaft. 13.03.2021. https://osb-alliance.de/pressemitteilungen/dortmund-goes-open-source (26.07.2026)

[3] Antrag der Fraktionen Bündnis 90/Die Grünen, CDU, Die Linke+ und SPD zum Masterplan „Digitale Verwaltung - Arbeiten 4.0“ (Drucksache Nr.: 18828-20-E5). 19.01.2021. CDU-Fraktion, Fraktion Bündnis 90/Die Grünen, SPD-Fraktion, Fraktion Linke+. Ratsinformationssystem der Stadt Dortmund. https://rathaus.dortmund.de/dosys/gremrech.nsf/0/FA5AAC8313577C44C12586630046E675/$FILE/ZEGMF%2318828-20-E5.doc.pdf (26.07.2026)

[4] Die tragische Geschichte eines Leuchtturm-Projekts. 20.02.2017. Jörg Thoma. Golem. https://www.golem.de/news/limux-die-tragische-geschichte-eines-leuchtturm-projekts-1702-126230.html (26.07.2026)

[5] Local European Municipalities are Spearheading Independence from US Tech. 16.06.2026. https://reset.org/open-source-der-verwaltung-europaische-kommunen-gehen-bei-unabhangigkeit-us-technologien-voran/ (26.07.2026)

[6]  Users of LibreOffice. https://comptoir-du-libre.org/en/softwares/usersSoftware/33 (26.06.2026)

[7] Who uses LibreOffice?. LibreOffice. https://www.libreoffice.org/who-uses-libreoffice/ (26.07.2026)

[8]  Portugal’s Seixal completes switch to LibreOffice. 31.10.2019. Gijs Hillenius. European COmission. https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/under-pressure (26.07.2026)

[9] RELATÓRIO & CONTAS 2025. MENSAGEM
DO EXECUTIVO MUNICIPA. S. 120 - 125. https://www.cm-seixal.pt/sites/default/files/documents/relatorio_e_contas_2025_parte1.pdf (26.07.2026)

[10] Cybernews launcht Tracker für Europas Tech-Autonomie. Cybernews. Eglė Krištopaitytė. 15.07.2026. https://cybernews.com/de/tech/tech-autonomie-tracker/ (26.07.2026)

[11] Lei n.º 36/2011. https://files.dre.pt/1s/2011/06/11800/0359903600.pdf (26.07.2026)


[20] Was ist CC? creativecommons.net. https://de.creativecommons.net/was-ist-cc/ (26.07.2026)

[21] Open-Source-Software in Kommunen. November 2023. https://www.iese.fraunhofer.de/content/dam/iese/publikation/smart-cities-open-source-software-in-kommunen-fraunhofer-iese.pdf

[22] https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng

[23] Data Act - das müssen Unternehmen wissen. IHK München. https://www.ihk-muenchen.de/ratgeber/digitalisierung/datenmanagement/data-act/ (26.07.2026)

[24] Data Act: Was Online-Händler jetzt wissen müssen. https://www.haendlerbund.de/de/ratgeber/recht/data-act (26.07.2026)

[25]  Da­ten­zu­gang und Da­ten­nut­zung. BNetzA. https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/DataAct/Hintergrund/1-Daten/artikel.html (26.07.2026)

[26] Aktuelle EVB-IT. https://www.digitale-verwaltung.de/Webs/DV/DE/aktuelles-service/it-einkauf/evb-it-und-bvb/aktuelle_evb-it-node.html (26.07.2026)

[27] Vergabeverfahren zur Bereitstellung, Entwicklung und Änderung von Computersoftware Zur Zulässigkeit der Beschränkung eines öffentlichen Auftragsgegenstandes auf „Open Source Software“. Wissenschaftlicher Dienst Bundestag. https://www.bundestag.de/resource/blob/1165534/WD-7-010-26.pdf (26.07.2026)

[28] Bundestags-Gutachten schafft Klarheit: Open-Source-First ist vergaberechtlich zulässig. 16.07.2026. Open Source Business Alliance. https://osb-alliance.de/pressemitteilungen/bundestags-gutachten-schafft-klarheit-open-source-first-ist-vergaberechtlich-zulaessig (26.07.2026)

[29] Open Source als Standard bei IT-Ausschreibungen: Die neuen EVB-IT-Vertragsvorlagen. https://www.bbh-blog.de/allgemein/open-source-als-standard-bei-it-ausschreibungen-die-neuen-evb-it-vertragsvorlagen/ (26.07.2026)

[30]  VERORDNUNG (EU) 2024/2847 DES EUROPÄISCHEN PARLAMENTS UND DES RATES vom 23. Oktober 2024 über horizontale Cybersicherheitsanforderungen für Produkte mit digitalen Elementen und zur Änderung der  Verordnungen (EU) Nr. 168/2013 und (EU) 2019/1020 und der Richtlinie (EU) 2020/1828 (Cyberresilienz-Verordnung). https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=OJ:L_202402847 (26.07.2026)

[31] https://opencode.de/de (26.07.2026)

[32] Neue EVB-IT-Vertragsvorlagen stärken die Beschaffung von Open Source Software durch die Verwaltung. https://osb-alliance.de/pressemitteilungen/neue-evb-it-vertragsvorlagen-staerken-die-beschaffung-von-open-source-software-durch-die-verwaltung (26.07.2026)


[40] Sechs Städte setzen digitale Impulse. https://www.kommune21.de/k21-meldungen/sechs-staedte-setzen-digitale-impulse/ (26.07.2026)

[41] Digitale Impulse für smarte Städte. https://digitales.hessen.de/presse/digitale-impulse-fuer-smarte-staedte (26.07.2026)

[42] https://www.digitalekommunehessen.de/ikz/ (26.07.2026)

[43] Interkommunale Datenstrategie und Data Governance. Städte Fulda, Gießen, Offenbach am Main & Wetzlar. https://www.digitalekommunehessen.de/wp-content/uploads/2025/02/Interkommunale-Datenstrategie-und-Data-Governance_GI_OF_FD_WZ.pdf (26.07.2026)

[44] Open Smart City. https://www.digitalekommunehessen.de/projekte/open-smart-city/ (26.07.2026)




 🔮 Origin:: [[26.07.2026]]
