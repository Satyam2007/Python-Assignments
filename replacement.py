from Bio.Seq import MutableSeq
a = MutableSeq("ATGCGCATACGACTACAGCAGA")
print("DNA sequence is:",a)
mutation = {"A":"T","T":"T","G":"G","C":"C"}
new_seq = ""

for i in range(0,len(a)):
    new_seq += mutation[a[i]]

print("Mutated strand is:", new_seq)