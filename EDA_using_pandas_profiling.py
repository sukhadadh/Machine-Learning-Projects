import profile
import pandas as pd
from pandas_profiling import ProfileReport

nt = pd.read_csv(r"insurance.csv")
#print(nt.head(5))
profile = ProfileReport(nt)
profile.to_file(output_file="output.html")
print("report generated successfully")