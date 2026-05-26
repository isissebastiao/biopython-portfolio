# =============================================================================
# Script: 02_strings.py
# Author: Isis Sebastião
# Description: String indexing, slicing, and manipulation in Python,
#              illustrated with DNA sequences, gene IDs, and species names.
# =============================================================================

# --- 1. Indexing: accessing individual characters ---------------------------
#
# Python indexing starts at 0 (zero-based), matching bioinformatics conventions
# used in BED format and most genomic coordinate systems.
#
#  Sequence:  A  T  G  C  C  T  A  G
#  Index:     0  1  2  3  4  5  6  7
#  Neg index:-8 -7 -6 -5 -4 -3 -2 -1

dna = "ATGCCTAG"

print(dna[0])     # A  — first nucleotide (start codon begins here)
print(dna[2])     # G  — third position (wobble position in codon)
print(dna[-1])    # G  — last nucleotide
print(dna[-3])    # T  — third from the end

# Gene ID indexing
gene_id = "AT1G01010"
print(gene_id[0:2])    # "AT" — chromosome prefix in Arabidopsis IDs
print(gene_id[2])      # "1"  — chromosome number

# --- 2. Slicing: extracting subsequences ------------------------------------
#
# Syntax: sequence[start:end]  — end index is NOT included

print(dna[0:3])    # ATG — start codon
print(dna[5:8])    # TAG — stop codon (amber)
print(dna[:3])     # ATG — from beginning to index 3 (exclusive)
print(dna[3:])     # CCTAG — from index 3 to end
print(dna[:])      # ATGCCTAG — full sequence (useful for copying)
print(dna[:-1])    # ATGCCTA — all except last nucleotide
print(dna[-3:])    # TAG — last 3 nucleotides (stop codon from end)

# Slicing with step: every 3rd character (codon positions)
codon_pos1 = dna[0::3]   # first position of each codon
print(codon_pos1)

# --- 3. String methods useful in bioinformatics -----------------------------

sequence = "atgcctag"

# Case conversion (sequences are often stored in uppercase)
print(sequence.upper())    # ATGCCTAG
print(sequence.lower())    # atgcctag

# Count nucleotide occurrences
print(dna.count("A"))      # count adenines
print(dna.count("G"))      # count guanines

# GC content calculation
gc = (dna.count("G") + dna.count("C")) / len(dna)
print(f"GC content: {gc:.1%}")

# Find a motif (returns index of first occurrence, -1 if not found)
promoter_motif = "TATA"
seq_with_tata  = "GCATATAGGCC"
print(seq_with_tata.find(promoter_motif))   # 3

# Replace: simulate a point mutation
mutated = dna.replace("A", "T")
print(f"Original: {dna}")
print(f"Mutated:  {mutated}")

# Strip whitespace (important when reading IDs from files)
raw_id = "  NZ_CP041838.1\n"
clean_id = raw_id.strip()
print(repr(clean_id))      # 'NZ_CP041838.1'

# Split: parse a FASTA header line
fasta_header = ">AT1G01010 | MYB transcription factor | Chr1:3631-5899"
parts = fasta_header.split("|")
gene_id   = parts[0].strip().lstrip(">")
function  = parts[1].strip()
location  = parts[2].strip()
print(gene_id)    # AT1G01010
print(function)   # MYB transcription factor
print(location)   # Chr1:3631-5899

# Join: reconstruct a sequence from a list of codons
codons = ["ATG", "CCT", "AG"]
full_seq = "".join(codons)
print(full_seq)   # ATGCCTAG

# --- 4. f-strings for formatted output --------------------------------------

gene      = "AT1G01010"
log2fc    = 2.31
padj      = 0.0012
direction = "upregulated"

print(f"Gene {gene} is {direction} (log2FC = {log2fc:.2f}, padj = {padj:.4f})")
