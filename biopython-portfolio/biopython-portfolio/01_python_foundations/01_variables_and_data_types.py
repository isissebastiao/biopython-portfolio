# =============================================================================
# Script: 01_variables_and_data_types.py
# Author: Isis Sebastião
# Description: Python variable types illustrated with biological examples —
#              gene names, expression rates, species lists, and boolean flags.
# =============================================================================

# --- 1. String: text values --------------------------------------------------

gene = "DNAI1"                          # gene name
organism = "Arabidopsis thaliana"       # species name
accession = "NZ_CP041838.1"            # NCBI accession number

print(gene)
print(type(gene))                       # <class 'str'>

# --- 2. Integer: whole numbers -----------------------------------------------

chromosome_count = 5                    # number of chromosomes in Arabidopsis
read_depth = 30                         # sequencing coverage (30x)

print(chromosome_count)
print(type(chromosome_count))           # <class 'int'>

# --- 3. Float: decimal numbers -----------------------------------------------

gc_content = 0.36                       # GC content (36%)
ka_ks_ratio = 0.42                      # synonymous/non-synonymous substitution ratio

print(gc_content)
print(type(gc_content))                 # <class 'float'>

# --- 4. List: ordered collection of values -----------------------------------

species_list = ["Arabidopsis thaliana", "Oryza sativa", "Zea mays"]
gene_ids     = ["AT1G01010", "AT1G01020", "AT1G01030"]

print(species_list)
print(type(species_list))               # <class 'list'>

# --- 5. Tuple: immutable ordered collection ----------------------------------

# Useful for fixed values that should not change (e.g., genomic coordinates)
gene_location = (3631, 5899)            # (start, end) position on Chr1
print(gene_location)
print(type(gene_location))             # <class 'tuple'>

# --- 6. Boolean: True or False -----------------------------------------------

is_coding     = True                    # is the sequence a coding region?
has_introns   = False                   # does the gene have introns?

print(is_coding)
print(type(is_coding))                  # <class 'bool'>

# --- 7. Arithmetic with biological variables ---------------------------------

# BMI-style calculation adapted to genomics context
genome_size_mb   = 135.0               # Arabidopsis genome size in Mb
coding_region_mb = 48.6               # estimated coding sequence in Mb

coding_fraction = coding_region_mb / genome_size_mb
print(f"Coding fraction: {coding_fraction:.2%}")

# --- 8. String concatenation -------------------------------------------------

genus   = "Arabidopsis"
species = "thaliana"
full_name = genus + " " + species
print(full_name)

# f-string formatting (recommended)
gene_label = "AT1G01010"
log2fc     = 2.3
print(f"Gene {gene_label} has a log2FC of {log2fc}")

# --- 9. Type conversion ------------------------------------------------------

read_count_str = "1500"
read_count_int = int(read_count_str)        # convert string → int
print(type(read_count_int))                 # <class 'int'>

coverage_int   = 30
coverage_float = float(coverage_int)        # convert int → float
print(type(coverage_float))                 # <class 'float'>

age_int = 34
message = "Researcher age: " + str(age_int) + " years"   # int → str for concatenation
print(message)
