# Biopython Portfolio

Python and Biopython scripts documenting foundational programming skills
and bioinformatics workflows for genomic data retrieval and sequence analysis.
Developed during structured Biopython training, with examples adapted to
plant genomics and comparative genomics contexts.

---

## Motivation

Python is the primary scripting language in modern bioinformatics. These scripts
consolidate core programming skills — data structures, control flow, and
biological sequence manipulation — alongside practical Biopython workflows for
sequence handling and NCBI data retrieval. The NCBI Entrez batch download
workflow is directly applicable to pangenome construction pipelines, where
multiple genome sequences must be retrieved and processed programmatically.

---

## Repository structure

```
biopython-portfolio/
│
├── 01_python_foundations/
│   ├── 01_variables_and_data_types.py   # str, int, float, list, bool with genomics examples
│   ├── 02_strings.py                    # indexing, slicing, GC content, FASTA header parsing
│   └── 03_lists_conditionals_loops_dicts.py  # core data structures + control flow
│
├── 02_biological_sequences/
│   └── 01_biological_sequences.py       # Seq, MutableSeq, transcription, translation, codon tables
│
└── 03_ncbi_entrez/
    ├── 01_ncbi_entrez_download.py       # single & batch genome download (FASTA + GenBank)
    └── data/
        └── genome_ids.txt               # example accession list
```

---

## Scripts overview

| Script | Topic | Key functions / modules |
|--------|-------|-------------------------|
| `01_variables_and_data_types.py` | Python data types | `str`, `int`, `float`, `list`, `bool`, type conversion |
| `02_strings.py` | String operations | indexing, slicing, `.count()`, `.find()`, `.split()`, f-strings |
| `03_lists_conditionals_loops_dicts.py` | Data structures & control flow | `list`, `dict`, `if/elif/else`, `for`, list comprehensions |
| `01_biological_sequences.py` | Seq & MutableSeq | `Bio.Seq`, `.transcribe()`, `.translate()`, `.back_transcribe()`, codon tables |
| `01_ncbi_entrez_download.py` | NCBI data retrieval | `Bio.Entrez`, `efetch`, `einfo`, batch download loop |

---

## Biological context

Examples throughout these scripts use data structures and problems common in genomics:

- **String indexing** applied to DNA sequences and NCBI accession IDs
- **Dictionaries** to represent gene presence/absence (PAV — Presence/Absence Variation), a core concept in pangenomics
- **Transcription and translation** using Biopython's `Seq` — including organism-specific codon tables from NCBI
- **Batch NCBI downloads** — the same loop used here to fetch *Mycobacterium tuberculosis* genomes scales directly to pangenome assembly workflows requiring dozens of accessions

---

## Dependencies

```bash
pip install biopython
```

Python ≥ 3.8 recommended.

---

## Author

**Isis Sebastião** — Agronomist | PhD in Biotechnology | Plant Genomics & Bioinformatics  
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--1596--2523-green)](https://orcid.org/0000-0002-1596-2523)
[![Lattes](https://img.shields.io/badge/Lattes-CNPq-blue)](http://lattes.cnpq.br/5220007563821018)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-isis--sebastiao-blue)](https://www.linkedin.com/in/isis-sebastiao/)
