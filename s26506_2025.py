# Cel programu:
# Program generuje losową sekwencję DNA w formacie FASTA na podstawie danych podanych przez użytkownika.
# Sekwencja zawiera w losowym miejscu imię użytkownika (niezależne od statystyk nukleotydów).
# Program zapisuje dane do pliku, pokazuje statystyki i oblicza zawartość CG.

import random  # do losowania sekwencji i pozycji wstawienia imienia
from datetime import datetime  # MODIFIED (dodano znacznik czasu do pliku)

def generate_dna_sequence(length):
    """Generuje losową sekwencję DNA o zadanej długości."""
    return ''.join(random.choices('ACGT', k=length))

def calculate_stats(sequence):
    """Oblicza procentową zawartość A, C, G, T oraz zawartość CG."""
    length = len(sequence)
    counts = {nuc: sequence.count(nuc) for nuc in 'ACGT'}
    percentages = {nuc: round((counts[nuc] / length) * 100, 1) for nuc in counts}
    cg_content = round(((counts['C'] + counts['G']) / length) * 100, 1)
    return percentages, cg_content

def insert_name(sequence, name):
    """Wstawia imię użytkownika w losowej pozycji sekwencji."""
    pos = random.randint(0, len(sequence))  # wybiera losową pozycję
    return sequence[:pos] + name + sequence[pos:]

def save_fasta_file(file_name, header, sequence_with_name):
    """Zapisuje dane w formacie FASTA do pliku."""
    with open(file_name, 'w') as f:
        f.write(f">{header}\n")
        f.write(sequence_with_name + '\n')

# ======= Główna część programu =======

# Pytania do użytkownika
length = int(input("Podaj długość sekwencji: "))
seq_id = input("Podaj ID sekwencji: ")
description = input("Podaj opis sekwencji: ")
name = input("Podaj imię: ")

# Generowanie sekwencji
sequence = generate_dna_sequence(length)

# ORIGINAL:
# sequence_with_name = insert_name(sequence, name)
# MODIFIED (dodano wyróżnik dla imienia, aby było łatwo odróżnić je w pliku):
sequence_with_name = insert_name(sequence, f"[{name}]")  # MODIFIED (dla przejrzystości i aby imię było widoczne)

# ORIGINAL:
# header = f"{seq_id} {description}"
# MODIFIED (dodano znacznik czasu w nagłówku FASTA):
header = f"{seq_id} {description} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"  # MODIFIED (dodano timestamp)

# ORIGINAL:
# file_name = f"{seq_id}.fasta"
# MODIFIED (dodano "_DNA" do nazwy pliku, by było wiadomo co zawiera):
file_name = f"{seq_id}_DNA.fasta"  # MODIFIED (czytelniejsza nazwa pliku)

# Zapis sekwencji do pliku
save_fasta_file(file_name, header, sequence_with_name)

# Obliczanie statystyk
percentages, cg_content = calculate_stats(sequence)

# Wyświetlenie informacji
print(f"Sekwencja została zapisana do pliku {file_name}")
print("Statystyki sekwencji:")
for nuc in 'ACGT':
    print(f"{nuc}: {percentages[nuc]}%")
print(f"%CG: {cg_content}")
