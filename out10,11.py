Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=============== RESTART: C:\Users\Dell\OneDrive\Desktop\lab10.py ===============
After One Hot Encoding:
      TypeName   RAM  ...  TypeName_Ultrabook  TypeName_Workstation
0    Ultrabook   8GB  ...                 1.0                   0.0
1     Notebook  16GB  ...                 0.0                   0.0
2       Gaming   8GB  ...                 0.0                   0.0
3     Notebook   4GB  ...                 0.0                   0.0
4  Workstation  32GB  ...                 0.0                   1.0

[5 rows x 6 columns]

After Label Encoding RAM:
      TypeName  RAM  ...  TypeName_Ultrabook  TypeName_Workstation
0    Ultrabook    3  ...                 1.0                   0.0
1     Notebook    0  ...                 0.0                   0.0
2       Gaming    3  ...                 0.0                   0.0
3     Notebook    2  ...                 0.0                   0.0
4  Workstation    1  ...                 0.0                   1.0

[5 rows x 6 columns]

RAM Classes:
['16GB' '32GB' '4GB' '8GB']
>>> 
=============== RESTART: C:\Users\Dell\OneDrive\Desktop\lab11.py ===============
Original Data:
   YearsExperience  Salary
0              1.1   39343
1              1.3   46205
2              1.5   37731
3              2.0   43525
4              2.2   39891

Scaled Data:
   YearsExperience    Salary
0        -1.510053 -1.360113
1        -1.438373 -1.105527
2        -1.366693 -1.419919
3        -1.187494 -1.204957
4        -1.115814 -1.339781
