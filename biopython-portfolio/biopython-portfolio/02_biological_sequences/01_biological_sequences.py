# =============================================================================
# Script: 01_biological_sequences.py
# Author: Isis Sebastião
# Description: Working with biological sequences using Biopython's Seq and
#              MutableSeq objects. Covers transcription, back-transcription,
#              translation, codon tables, and in-place sequence editing.
#
# Install: pip install biopython
# Docs: https://biopython.org/wiki/SeqIO
# =============================================================================

from Bio.Seq import Seq, MutableSeq

# =============================================================================
# PART 1: Transcription
# =============================================================================

# In molecular biology, transcription produces mRNA from the coding (sense) strand.
# Biopython's .transcribe() replaces T → U following this convention.

coding_strand = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
template_strand = Seq("CCAT")   # short example for template-strand convention

# Direct transcription from the coding strand (bioinformatics convention)
mRNA_from_coding = coding_strand.transcribe()
print("mRNA (from coding strand):", mRNA_from_coding)

# Manual transcription using replace (equivalent result)
mRNA_manual = coding_strand.replace("T", "U")
print("mRNA (manual replace):    ", mRNA_manual)

# Transcription from the template strand (biological convention):
# reverse complement the template → then transcribe
mRNA_from_template = template_strand.reverse_complement().transcribe()
print("mRNA (from template):     ", mRNA_from_template)

# Back-transcription: convert mRNA back to DNA
mrna = Seq("AUUGG")
dna_back = mrna.back_transcribe()
print("Back-transcribed DNA:     ", dna_back)

# =============================================================================
# PART 2: Translation
# =============================================================================

# Translation converts an mRNA (or coding DNA) sequence into a protein.
# Stop codons are represented by '*' in Biopython.

mrna_seq = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
dna_seq  = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

# Standard translation (includes stop codon as *)
protein_from_mrna = mrna_seq.translate()
print("\nProtein (from mRNA):              ", protein_from_mrna)

protein_from_dna = dna_seq.translate()
print("Protein (from coding DNA):        ", protein_from_dna)

# Translate and stop at the first stop codon (cleaner output)
protein_no_stop = dna_seq.translate(to_stop=True)
print("Protein (to_stop=True):           ", protein_no_stop)

# Using organism-specific codon tables from NCBI
# Table 1  = Standard (default, eukaryotes)
# Table 11 = Bacterial, Archaeal, Plant Plastid
# Full list: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi

protein_bacteria = dna_seq.translate(table=11)
print("Protein (bacterial codon table):  ", protein_bacteria)

protein_mito = dna_seq.translate(table="Vertebrate Mitochondrial")
print("Protein (vertebrate mitochond.):  ", protein_mito)

# CDS validation: checks that sequence starts with start codon and ends
# with a stop codon — important for annotation QC
dna_cds = Seq("GTGGGCTAG")
try:
    protein_cds = dna_cds.translate(table=11, cds=True)
    print("CDS protein:                      ", protein_cds)
except Exception as e:
    print("CDS error:", e)

# =============================================================================
# PART 3: MutableSeq — editing sequences in place
# =============================================================================

# The standard Seq object is immutable (like Python strings).
# MutableSeq allows in-place modifications — useful for simulating mutations.

original = Seq("GATCC")
print("\nOriginal Seq type:", type(original))

# Convert to MutableSeq
mutable = MutableSeq(original)
print("MutableSeq type:  ", type(mutable))
print("MutableSeq value: ", mutable)

# Substitute a nucleotide at a specific position (point mutation)
mutable_copy = MutableSeq(original)
mutable_copy[0] = "C"
print("After substitution [0]→C:", mutable_copy)

# Remove a specific nucleotide (first occurrence)
mutable_copy = MutableSeq(original)
mutable_copy.remove("G")
print("After remove('G'):       ", mutable_copy)

# Remove the last nucleotide
mutable_copy = MutableSeq(original)
mutable_copy.remove(mutable_copy[-1])
print("After remove last nt:    ", mutable_copy)

# Reverse the sequence
mutable_copy = MutableSeq(original)
mutable_copy.reverse()
print("After reverse():         ", mutable_copy)

# Note: after each operation above, we reinitialize from `original`
# because MutableSeq modifies the object in place — order matters.
