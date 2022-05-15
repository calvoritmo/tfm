import os
import csv
from transformers import pipeline

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/../import/results.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    with open(dir_path+'/../import/results_scored.csv', 'w', encoding='utf-8') as g:
        csv_writer = csv.writer(g)
      
        for row in csv_reader:
          if row != []:
            print(row, end=' ')
            classifier = pipeline("zero-shot-classification",
                               model="facebook/bart-large-mnli")
            quality_labels = ['Bad', 'Mediocre', 'Good']
            certainty_labels = ['NotSure', 'Sure']
            print("certainty", end=' ')
            certainty = classifier(f"From the text '{row[0]}' we can infer that '{row[1]}'", certainty_labels)['labels'][0]
            print("quality")
            quality = classifier(f"From the text '{row[0]}' we can infer that '{row[1]}'", quality_labels)['labels'][0]
            
            csv_writer.writerow(row + [certainty, quality])
            g.flush()