# Yup
import pandas as pd

from my_lambdata.my_mod import enlarge

print('Hello Lambda! I know a lot of this already but practice makes perfect!')

df = pd.DataFrame({"x":[1,2,3,4,5], "y":[2,4,6,8,10]})
print(df.head())
print(f'X:{x} X Enlarged:{enlarge(x)}')