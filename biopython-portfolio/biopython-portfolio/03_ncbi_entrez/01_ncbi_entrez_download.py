# =============================================================================
# Script: 01_ncbi_entrez_download.py
# Author: Isis Sebastião
# Description: Downloading genome sequences and annotation files from NCBI
#              using Biopython's Entrez module. Covers single-accession and
#              batch downloads from a list of IDs — a standard first step in
#              comparative genomics and pangenome construction pipelines.
#
# Install: pip install biopython
# NCBI Entrez docs: https://www.ncbi.nlm.nih.gov/books/NBK25497/
# =============================================================================

from Bio import Entrez
import os
import time

# =============================================================================
# SETUP: Always identify yourself to NCBI
# =============================================================================
# NCBI requires a valid email address for API usage. Without it, your requests
# may be blocked. Replace with your institutional email.

Entrez.email = "your_email@institution.ac.br"

# =============================================================================
# PART 1: Querying NCBI databases (Entrez einfo)
# =============================================================================

# List all available NCBI databases
handle = Entrez.einfo()
result = Entrez.read(handle)
handle.close()

print("Available NCBI databases:")
for db in result["DbList"][:10]:   # print first 10
    print(f"  {db}")

# =============================================================================
# PART 2: Downloading a single genome (FASTA + GenBank)
# =============================================================================

# Target accession: NZ_CP041838.1 (Mycobacterium tuberculosis)
# Used here as a reference example for learning purposes

accession = "NZ_CP041838.1"

# --- Download FASTA ----------------------------------------------------------
print(f"\nDownloading FASTA for {accession}...")

handle = Entrez.efetch(
    db       = "nucleotide",
    id       = accession,
    rettype  = "fasta",
    retmode  = "text"
)
with open(f"{accession}.fasta", "w") as output_file:
    output_file.write(handle.read())
handle.close()

print(f"  Saved: {accession}.fasta")

# --- Download GenBank (full annotation) --------------------------------------
print(f"Downloading GenBank for {accession}...")

handle = Entrez.efetch(
    db       = "nucleotide",
    id       = accession,
    rettype  = "gbwithparts",    # full GenBank with all features
    retmode  = "text"
)
with open(f"{accession}.gbff", "w") as output_file:
    output_file.write(handle.read())
handle.close()

print(f"  Saved: {accession}.gbff")

# =============================================================================
# PART 3: Batch download from a list of accession IDs
# =============================================================================
# In comparative genomics and pangenome studies, you typically download
# multiple genomes. This script reads accession IDs from a text file
# (one ID per line) and downloads FASTA + GenBank for each.
#
# Input file format (genome_ids.txt):
#   NZ_CP041838.1
#   NZ_CP041836.1

# --- Read genome IDs from file -----------------------------------------------

id_file = "data/genome_ids.txt"

genome_ids = []
with open(id_file) as f:
    genome_ids = [line.strip() for line in f if line.strip()]

print(f"\nFound {len(genome_ids)} genomes to download: {genome_ids}")

# --- Download loop -----------------------------------------------------------

for genome_id in genome_ids:

    print(f"\nDownloading: {genome_id}")

    # FASTA
    handle = Entrez.efetch(
        db      = "nucleotide",
        id      = genome_id,
        rettype = "fasta",
        retmode = "text"
    )
    with open(f"{genome_id}.fasta", "w") as fasta_out:
        fasta_out.write(handle.read())
    handle.close()

    # GenBank
    handle = Entrez.efetch(
        db      = "nucleotide",
        id      = genome_id,
        rettype = "gbwithparts",
        retmode = "text"
    )
    with open(f"{genome_id}.gbff", "w") as gbff_out:
        gbff_out.write(handle.read())
    handle.close()

    print(f"  Saved: {genome_id}.fasta and {genome_id}.gbff")

    # Pause between requests to respect NCBI rate limits
    # NCBI allows max 3 requests/second without an API key, 10/sec with one
    time.sleep(0.4)

print("\nAll genomes downloaded successfully.")

# =============================================================================
# NOTES
# =============================================================================
# rettype options for nucleotide database:
#   "fasta"        → FASTA sequence only
#   "gb"           → GenBank flat file
#   "gbwithparts"  → GenBank with all sequence parts (recommended for complete genomes)
#   "fasta_cds_aa" → FASTA of translated CDS (protein sequences)
#   "fasta_cds_na" → FASTA of CDS nucleotide sequences
#
# For large downloads (>100 genomes), consider using NCBI Datasets CLI:
#   https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/
