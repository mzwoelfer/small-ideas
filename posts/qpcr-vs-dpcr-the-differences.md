---
📅 created: 12.07.2026 10:21
aliases:
tags:
author: Martin
---


# [[qPCR vs dPCR - the differences]]

## qPCR vs dPCR - the differences

## What is dPCR
- absolute Kopienzahl pro Mikroliter
- Probe in tausende winzige Reaktionen aufgeteilt (partitioniert)
- "Kammer leuchtet (DNA vorhanden) = 1" oder "Kammer leuchtet nicht = 0"
- Mit Poisson-Statistik[10] berechnet der Computer direkt die exakte Anzahl der Moleküle.

- zählt einzelne Moleküle - kann Expressionunterschiede von unter 10% oder Kopienzahlvarianten (CNVs) wie den Unterschied zwischen 5 und 6 Genkopien fehlerfrei und reproduzierbar auflösen.






ADVANTAGES[2]:
- **Absolute target quantification** – No need for standards, reference curves or extrapolations  
- **High tolerance to inhibitors** – Thanks to partitioning and endpoint measurement, dPCR efficiency remains unaffected by PCR inhibitors.  
- **Superior precision** –  Partitioning in digital PCR results in thousands of data points and more accurate results at the end of the amplification process, making digital PCR analysis suitable for detection of small fold change differences.  
- **Improved sensitivity** – digital PCR systems offer an improved limit of detection (LOD) as a smaller reaction volume increases the effective concentration of the target nucleic acid. Partitioning also positively affects enrichment as the target is separated from interfering compounds. The overall ratio of target versus background is improved as wild-type sequences and high-copy templates are diluted in each partition.  Hence, rare mutations and low-abundance targets are more accurately detected using dPCR than other PCR technologies.  
- **High reproducibility** – digital PCR analysis remains reproducible across laboratories as amplification efficiency bias is drastically reduced.  
- **Cost-efficiency** – Sample volumes and reagents are kept at minimal, lowering experimental costs; multiplexing possibilities enable higher throughput and productivity.  

Disadvantages?
- Dynamic range: The number of microunits in the digital PCR instrument is limited so the range of the number of DNA/RNA copies that can be detected by the digital PCR machine tends to be slightly narrower compared to qPCR.      
- **Large amplicons** – dPCR is not suitable for analysis of very large amplicons  
- **Bias and variance** – DNA denaturation during partitioning, where single strands separate into two different units, could cause overestimation; template linkage, sample inhomogeneity, partition volume variance and inhibiting factors, such as “molecular dropout” could cause underestimation.

---

Produkt von [[Qiagen]] - QIAcuity[20][21]



## Kosten
Im 5 Jahresvergleich mit gängigen qPCR Maschinen, deren Anschaffungskosten, laufenden Service Kosten, Software und  "Consumables" (Platten) sind [[dPCR]] Maschinen am teuersten. [7]

[[QIAcuity]] Nanoplates mit 8,5k (8.500 Partitionen per Well) und 96 wells kosten ca. 150€ pro Platte (1.561€ für 10 QIAcuity Nanoplate 8.5k 96-Well, 11 Nanoplate Seals)[8]
Zum Vergleich, eine "PCR Plate, 96-Well, ohne Stehrand" von Thermo Fisher kostet 6,56€ (25er Pack für 164€)[9]

| Kriterium         | qPCR (Real-Time PCR)                                                                    | dPCR (Digitale PCR)                                                           | Quelle & Nachweis                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Ergebnis          | Relativer Messwert (Verhältnis/Schätzung zu einer Kontrollprobe)                        | Absoluter Messwert (Exakte Stückzahl der Genkopien im Röhrchen) [1]           | [[dPCR]]: absolute Quantifizierungen ohne Referenzmaterial oder externe Standards.                                                |
| Datenauslese      | S-Kurven (Interpretation und mathematische Berechnung nötig)                            | Digitales Punktemuster (Einfaches Zählen: Punkt leuchtet / leuchtet nicht)    | qPCR misst die kontinuierliche Fluoreszenz während der Zyklen; dPCR liest die Reaktionen am Endpunkt binär (positiv/negativ) aus. |
| Vorbereitungszeit | Hoch (Standardkurven müssen für jede Quantifizierung erstellt werden)                   | Niedrig (Keine Standardkurven nötig – spart Arbeitszeit)                      | Keine Standardkurven für Quantifizierung der digitalen PCR [3]                                                                    |
| Sensitivität      | Gut (Erkennt deutliche Unterschiede, z. B. Verdopplung der Genaktivität)                | Extrem hoch (Erkennt sehr kleine Unterschiede, z. B. 1,2-fache Änderung)      | [[dPCR]]: höhere Präzision und erkennt minimale Genexpressionsänderungen (< 10 % Unterschied).                                    |
| Robustheit        | Anfällig (Polymerase-Inhibitoren oder Verunreinigungen können die Messung beeinflussen) | Robuster gegenüber Inhibitoren (Partitionierung reduziert deren Einfluss) [4] | Die Partitionierung verbessert die Stabilität der Amplifikation auch bei mäßigen Polymerase-Inhibitoren.                          |
| Probendurchsatz   | Sehr hoch (96- oder 384-Well-Platten Standard)                                          | Mittel bis hoch                                                               | [[qPCR]] für große Probenzahlen; [[dPCR]] verarbeitet weniger Proben parallel.[6]                                                 |
| Gerätepreis       | Günstiger (ca. 15.000–50.000 $); weit verbreitet                                        | Teurer (ca. 70.000–150.000 $; höhere Investition) [6]                         | - qPCR geringere Geräte- und Verbrauchskosten während dPCR höhere Anschaffungs- und Betriebskosten verursacht.                    |
| Kosten pro RUn    | $1 to $3 per reaction                                                                   | $5 to $10 per reaction                                                        | [6]                                                                                                                               |

## When should your lab chose qPCR or dPCR?
qPCR: 
- high-throughput workflows
- routine quantification
- cost-conscious labs
qPCR:
- reliable performance  (especially for gene expression studies and pathogen detection)
- rare mutation detection
- low-abundance targets
- applications requiring absolute quantification

Die digitale PCR (dPCR) liefert im Gegensatz zur relativen Messung der qPCR absolute Genkopienzahlen und bietet eine extrem hohe Sensitivität sowie Robustheit gegenüber Probenverunreinigungen. Während qPCR-Geräte kostengünstiger sind und einen höheren Durchsatz bieten, punktet die dPCR durch wegfallende Standardkurven, was die Arbeitszeit verkürzt

Some labs adopt a **hybrid strategy**. 
Using [[qPCR]] for screening large sample sets and [[dPCR]] for follow-up quantification of rare events or challenging samples.[6]


## SOURCES
[1] Comparison of PCR Methods (dPCR vs qPCR vs end-point PCR). Qiagen. https://www.qiagen.com/us/knowledge-and-support/knowledge-hub/bench-guide/pcr/digital-pcr/digital-pcr-vs-quantitative-pcr-vs-end-point-pcr
[2] Fundamentals of digital PCR. https://www.qiagen.com/us/knowledge-and-support/knowledge-hub/bench-guide/pcr/digital-pcr/what-is-digital-pcr
[3] Digital PCR and Real-Time PCR (qPCR) Choices for Different Applications. 
https://www.bio-rad.com/de-de/life-science/learning-center/digital-pcr-and-real-time-pcr-qpcr-choices-for-different-applications
[4] Best Practices in qPCR and dPCR Validation in Regulated Bioanalytical Laboratories. https://www.bioagilytix.com/wp-content/uploads/2023/08/AAPS-Journal_Amanda-Hayes-Article_May-2022.pdf
[5] PCR digital frente a qPCR: ¿Qué tecnología se adapta mejor a su experimento https://unicornlifescience.com/es/digital-pcr-vs-qpcr-technology-best/
[6] Digital PCR vs. Real-Time PCR: Understanding the Key Differences. https://www.labmanager.com/digital-pcr-vs-real-time-pcr-understanding-the-key-differences-33665
[7] PCR Equipment Cost Breakdown: What Labs Actually Pay for qPCR Systems. https://unicornlifescience.com/pcr-equipment-cost-breakdown-labs-actually/
[8] QIAcuity Nanoplates und Zubehör. https://www.qiagen.com/de-de/products/instruments-and-automation/accessories/qiacuity-nanoplates-and-accessories?catno=250021
[9] PCR Plate, 96-Well, ohne Stehrand. https://www.thermofisher.com/order/catalog/product/de/de/AB0600
[10]  Poisson-Verteilung, Stochastik, Wahrscheinlichkeitsverteilung | Mathe by Daniel Jung. https://www.youtube.com/watch?v=UESWARetzXU

[20] Workflow und Produkte für die digitale PCR. https://www.qiagen.com/de-de/applications/digital-pcr/workflow-and-products
[21] QIAcuity Digital PCR System. https://www.qiagen.com/de-de/products/instruments-and-automation/pcr-instruments/qiacuity-digital-pcr-system?catno=911001



 🔮 Origin:: [[11.07.2026]]
