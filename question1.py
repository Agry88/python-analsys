import sweetviz as sv
import dataset

import dataset
def Question1():
    print("探索性分析")

    data = dataset.Dataset()

    #EDA using Autoviz
    sweet_report = sv.analyze(data)

    #Saving results to HTML file
    sweet_report.show_html('sweet_report.html')


Question1()