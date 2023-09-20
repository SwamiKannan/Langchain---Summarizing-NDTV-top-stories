import dominate
from dominate.tags import *
import pickle
import webbrowser


def create_newspaper(source_file, headline_file,web_file):
    doc = dominate.document(title='Your NDTV Summary')

    with open(source_file, 'rb') as f:
        summary_dict = pickle.load(f)

    with open(headline_file,'r') as f:
        headlines=f.readlines()



    _html = html()
    _body = _html.add(body())
    title=div(h1('Welcome to your NDTV summary for today!'))
    title['align']='center'
    _body.add(title)
    _body.add(h2('Key highlights'))
    ## Add summaries to the newspaper
    for head in headlines:
        _body.add(p(head))


    for v in summary_dict.values():
        _body.add(br())
        _body.add(h2(v[0]))
        _body.add(h5(v[1]))
        _body.add(p(v[3]))
        _body.add(h5('Summary of news reduced from a length of ', v[4], ' letters to a length of ', v[5], ' letters'))
        _body.add(br())
    print(_html.render())
    with open(web_file, 'w') as f:
        f.write(_html.render())


def open_newspaper(source_file, headline_file, web_file):
    create_newspaper(source_file, headline_file,web_file)
    webbrowser.open(web_file)


open_newspaper('summary.pkl','headlines.txt', 'ndtv_summary.html')
