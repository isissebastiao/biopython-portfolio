# =============================================================================
# Script: 03_lists_conditionals_loops_dicts.py
# Author: Isis Sebastião
# Description: Core Python data structures and control flow — lists,
#              conditionals (if/elif/else), for loops, and dictionaries —
#              applied to biological sequence and genomics data.
# =============================================================================

# =============================================================================
# PART 1: Lists
# =============================================================================

# --- Creating lists ----------------------------------------------------------

expression_values = [10, 5, 8, 6, 9]       # read counts per sample
gene_ids = ["AT1G01010", "AT1G01020", "AT1G01030", "AT1G01040", "AT1G01050"]

# --- Indexing and slicing ----------------------------------------------------
# Index starts at 0; negative indices count from the end

print(expression_values[0])     # 10  — first element
print(expression_values[3])     # 6   — fourth element
print(expression_values[-1])    # 9   — last element
print(expression_values[1:-1])  # [5, 8, 6] — middle elements (end exclusive)
print(expression_values[2:4])   # [8, 6]
print(expression_values[:])     # full list copy
print(expression_values[:-1])   # all except last

# --- Aggregation -------------------------------------------------------------

total = sum(expression_values)
print(f"Total reads: {total}")
print(f"Mean expression: {total / len(expression_values):.1f}")

# --- List modification -------------------------------------------------------

gene_ids.append("AT1G01060")         # add to end
gene_ids.insert(0, "AT1G00990")      # insert at position 0
gene_ids.remove("AT1G01030")         # remove by value
print(gene_ids)

# --- Sorting -----------------------------------------------------------------

sorted_expr = sorted(expression_values, reverse=True)   # descending
print(sorted_expr)

# =============================================================================
# PART 2: Conditionals (if / elif / else)
# =============================================================================

# --- Gene expression classification ------------------------------------------

log2fc_values = [2.1, -1.4, 0.3, 3.8, -2.6]

for log2fc in log2fc_values:
    if log2fc > 1:
        status = "upregulated"
    elif log2fc < -1:
        status = "downregulated"
    else:
        status = "not significant"
    print(f"log2FC = {log2fc:+.1f} → {status}")

# --- Sequence type detection (DNA vs RNA) ------------------------------------

sequences = ["ATCG", "UAGC", "ACCTGA", "AGCU", "AUGCUG", "AGCAGCT"]

for seq in sequences:
    if "U" in seq:
        print(f"{seq} → RNA")
    else:
        print(f"{seq} → DNA")

# --- Student grade classification (Python conditionals in practice) ----------

student_scores = {
    "Student_1": [5, 6, 4, 3],
    "Student_2": [9, 4, 4, 3],
    "Student_3": [9, 4, 4, 7]
}

for student, scores in student_scores.items():
    mean = sum(scores) / len(scores)
    result = "approved" if mean >= 5 else "failed"
    print(f"{student}: mean = {mean:.1f} → {result}")

# =============================================================================
# PART 3: For loops
# =============================================================================

# --- Iterating over sequences ------------------------------------------------

dna_sequences = [
    "ATCATACGACAGCATACG",
    "CAGATGCAGCATCAGCGATACGAAGTAAGACGAT",
    "AGATGATGATAGTAGTAATAGTAGATGATAGTA"
]

# Filter sequences shorter than 20 nucleotides
print("\nSequences < 20 nt:")
for seq in dna_sequences:
    if len(seq) < 20:
        print(f"  {seq} ({len(seq)} nt)")

# Count each nucleotide per sequence
bases = ["A", "T", "C", "G"]
print("\nNucleotide composition:")
for seq in dna_sequences:
    counts = {b: seq.count(b) for b in bases}
    gc = (counts["G"] + counts["C"]) / len(seq)
    print(f"  {seq[:10]}... | A:{counts['A']} T:{counts['T']} "
          f"C:{counts['C']} G:{counts['G']} | GC: {gc:.1%}")

# --- Species name formatting -------------------------------------------------

species_raw = [
    "escherichia coli", "pseudomonas acetoxians",
    "arabidopsis thaliana", "escherichia albertii", "oryza sativa"
]

# Filter Escherichia species and format as proper scientific names
print("\nEscherichia species (formatted):")
for spp in species_raw:
    if "escherichia" in spp:
        genus, epithet = spp.split()
        print(f"  {genus.capitalize()} {epithet}")

# =============================================================================
# PART 4: Dictionaries
# =============================================================================

# --- Gene presence/absence across genomes (PAV — common in pangenomics) ------

gene_presence = {
    "genome1": "adh",
    "genome2": "trpD",
    "genome3": "adh",
    "genome4": "adh",
    "genome5": "gyrB"
}

# Count how many genomes carry the 'adh' gene
target_gene = "adh"
genomes_with_adh = [g for g, gene in gene_presence.items() if gene == target_gene]
print(f"\nGenomes carrying '{target_gene}': {len(genomes_with_adh)}")
for g in genomes_with_adh:
    print(f"  {g}")

# --- Protein sequence lengths ----------------------------------------------------------------

proteins = ["MVKALIRQGRT", "PRQGEVVLS", "EGLEAVESV"]

protein_lengths = {}
for prot in proteins:
    protein_lengths[prot] = len(prot)

print("\nProtein lengths:")
for seq, length in protein_lengths.items():
    print(f"  {seq}: {length} aa")

# Equivalent using list comprehension
lengths_list = [len(p) for p in proteins]
print(lengths_list)

# --- Gene annotation dictionary ----------------------------------------------

gene_annotation = {
    "AT1G01010": {"function": "MYB transcription factor", "chr": "Chr1", "log2fc": 2.1},
    "AT1G01020": {"function": "Stress response protein",  "chr": "Chr1", "log2fc": -1.4},
    "AT1G01030": {"function": "Unknown",                  "chr": "Chr1", "log2fc":  0.3},
}

# Access nested values
print("\nGene annotations:")
for gene_id, info in gene_annotation.items():
    print(f"  {gene_id}: {info['function']} | log2FC = {info['log2fc']:+.1f}")

# Filter upregulated genes (log2FC > 1)
print("\nUpregulated genes:")
upregulated = {k: v for k, v in gene_annotation.items() if v["log2fc"] > 1}
for gene_id, info in upregulated.items():
    print(f"  {gene_id}: {info['function']}")
