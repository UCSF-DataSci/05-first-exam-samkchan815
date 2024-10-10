import random

seq = ""

output = "/mnt/c/Users/wammi/OneDrive/Desktop/datasci217/05-first-exam-samkchan815/data/random_sequence.fasta"
pair = ['A', 'C', 'G', 'T']

with open(output, 'w') as file:
    file.write('>\n')
    count = 0
    for i in range(0, 1000000):
        base = random.choice(pair)
        file.write(base)
        count += 1

        if count >= 79:
            file.write('\n')
            count = 0
file.close()

print('Random DNA sequence generated and saved to 05-first-exam-samkchan815/data/random_sequence.fasta')
