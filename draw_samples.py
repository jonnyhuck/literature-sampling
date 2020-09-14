from pandas import read_excel, concat

# setup the input data. extra forces additional samples if required (e.g. fulltext is not available)
datasets = [
    {'filename':'./data/Mental Mapping Numbered.xlsx',  'n': 85,    'extra': 0},
    {'filename':'./data/PGIS Numbered.xlsx',            'n': 243,   'extra': 2},
    {'filename':'./data/Sketch Mapping Numbered.xlsx',  'n': 33,    'extra': 0},
    {'filename':'./data/Unclassified Numbered.xlsx',    'n': 179,   'extra': 2},
    ]

# loop through each dataset
samples = []
for d in datasets:

    # open data files
    df = read_excel(d['filename'])

    # calculate sample size (20% + extras)
    sample_size = int(round(d['n'] * 0.2)) + d['extra']

    # extract random sample (set seed for reproducibility)
    samples.append(df.sample(n=sample_size, random_state=1824))

# concatenate the results into a single dataframe and write to file
concat(samples).to_csv("./sample.csv")

print("done!")
