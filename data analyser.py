# DNA Sequence Analyzer Using Python

print("\n===================================")
print("      DNA SEQUENCE ANALYZER")
print("===================================\n")


# Function to analyze DNA sequence
def analyze_sequence(dna_sequence):

    print("\n--- Sequence Analysis ---")

    # Sequence length
    print("DNA Sequence:", dna_sequence)
    print("Sequence Length:", len(dna_sequence))

    # Nucleotide count
    print("\n--- Nucleotide Count ---")
    print("A:", dna_sequence.count("A"))
    print("T:", dna_sequence.count("T"))
    print("G:", dna_sequence.count("G"))
    print("C:", dna_sequence.count("C"))

    # GC Content
    gc_content = (
        dna_sequence.count("G") + dna_sequence.count("C")
    ) / len(dna_sequence) * 100

    print("\nGC Content:", round(gc_content, 2), "%")

    # AT Content
    at_content = (
        dna_sequence.count("A") + dna_sequence.count("T")
    ) / len(dna_sequence) * 100

    print("AT Content:", round(at_content, 2), "%")

    # DNA to RNA transcription
    rna_sequence = dna_sequence.replace("T", "U")

    print("\n--- Transcription ---")
    print("RNA Sequence:", rna_sequence)

    # Complement
    complement = dna_sequence.translate(
        str.maketrans("ATGC", "TACG")
    )

    print("\n--- Complement ---")
    print("Complement:", complement)

    # Reverse Complement
    reverse_complement = complement[::-1]

    print("Reverse Complement:", reverse_complement)

    # Protein translation
    codon_table = {
        "ATG": "M",

        "TTT": "F", "TTC": "F",
        "TTA": "L", "TTG": "L",

        "TCT": "S", "TCC": "S",
        "TCA": "S", "TCG": "S",

        "TAT": "Y", "TAC": "Y",

        "TGT": "C", "TGC": "C",
        "TGG": "W",

        "CCT": "P", "CCC": "P",
        "CCA": "P", "CCG": "P",

        "ACT": "T", "ACC": "T",
        "ACA": "T", "ACG": "T",

        "GCT": "A", "GCC": "A",
        "GCA": "A", "GCG": "A",

        "GTT": "V", "GTC": "V",
        "GTA": "V", "GTG": "V",

        "CGT": "R", "CGC": "R",
        "CGA": "R", "CGG": "R",

        "AGT": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",

        "GGT": "G", "GGC": "G",
        "GGA": "G", "GGG": "G"
    }

    protein = ""

    for i in range(0, len(dna_sequence) - 2, 3):

        codon = dna_sequence[i:i+3]

        if codon in codon_table:
            protein += codon_table[codon]

    print("\n--- Protein Translation ---")
    print("Protein Sequence:", protein)


# Get DNA sequence from user
dna_sequence = input("Enter your DNA sequence: ").upper()


# Validate DNA sequence
valid_bases = set("ATGC")

if len(dna_sequence) == 0:
    print("\nError: DNA sequence cannot be empty.")

elif set(dna_sequence).issubset(valid_bases):

    print("\n✓ Valid DNA sequence")

    analyze_sequence(dna_sequence)

else:

    print("\n✗ Invalid DNA sequence")
    print("Only A, T, G and C are allowed.")


print("\n===================================")
print("       Analysis Completed")
print("===================================")
