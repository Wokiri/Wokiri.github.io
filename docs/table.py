from bokeh.io import show
from bokeh.models import Div

import pandas as pd
import numpy as np

dataDF = pd.read_csv(r'./wv.csv', index_col=0)
dataDF['PC Achievement'] = np.around(dataDF['Number Targeted'] / dataDF['Number Achieved'] * 100, decimals=2)


div = Div(

    text=f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
<div class="d-flex justify-content-center">
    <div class="shadow-sm table-responsive border my-sm-5 p-4" style="max-height: 80vh;">
        <p class="text-center lead" style="color:#660066;font-weight:bold;">CREATE PROJECT RESULTS FOR 2021</p>
        {dataDF.to_html(classes=('table table-hover'))}
    </div>
</div>
    
</body>
</html>

    """,
    width=900,
    height=800
)

# print(dataDF.to_html(classes=('table table-hover')))

show(div)