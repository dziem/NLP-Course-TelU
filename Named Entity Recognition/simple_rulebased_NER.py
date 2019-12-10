# Ade Romadhony
# Contoh sederhana NER berbasis aturan yang didefinisikan secara manual

# read the file
lines = []
with open('kalimat_POSTag.txt', 'r') as f:
    lines = f.readlines()
file = open('rulebased_output.txt','w') 
counter_line = 0
tokens = []
postags = []
for line in lines:
    line = line.rstrip('\n')
    if len(line)>1:
        line_part = line.split(" ")
        tokens.append(line_part[0])
        postags.append(line_part[1])
    else:
        #print(tokens)
        #print(postags)
        NE_labels = []
        counter_token = 0
        prev_NE_label = ""
        prev_token = ""
        for token in tokens:
            if postags[counter_token]=='NNP':
                if token[0].isupper():
                    if prev_token.lower() == 'di' or prev_token.lower() == 'ke' or prev_token.lower() == 'dari':
                        if prev_NE_label=="B-LOC" or prev_NE_label=="I-LOC":
                            NE_labels.append("I-LOC")
                        else:
                            NE_labels.append("B-LOC")
                    elif prev_NE_label=="B-PER" or prev_NE_label=="I-PER":
                        NE_labels.append("I-PER")
                    else:
                        NE_labels.append("B-PER")
                elif token.isupper():
                    if prev_NE_label=="B-ORG" or prev_NE_label=="I-ORG":
                        NE_labels.append("I-ORG")
                    else:
                        NE_labels.append("B-ORG")
                else:
                    if prev_NE_label=="B-LOC" or prev_NE_label=="I-LOC":
                        NE_labels.append("I-LOC")
                    elif prev_NE_label=="B-PER" or prev_NE_label=="I-PER":
                        NE_labels.append("I-PER")
                    elif prev_NE_label=="B-ORG" or prev_NE_label=="I-ORG":
                        NE_labels.append("I-ORG")
                    else:
                        NE_labels.append("O")
            else:
                NE_labels.append("O")
            prev_NE_label = NE_labels[counter_token]
            prev_token = token
            counter_token += 1
        for z in range(len(tokens)):
            file.write(tokens[z])
            file.write('\t')
            file.write(NE_labels[z])
            file.write('\n')
            if tokens[z] == '.':
                file.write('\n')
        #print(tokens)
        #print(NE_labels)
        tokens = []
        postags = []
print('finished')
file.close()