from requests_html import HTMLSession
import re
class TemplateData(object):
    session = HTMLSession()
    """docstring for TemplateData. Get and split website into list with the
    correct parts"""
    list_days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    week = None
    num_people = None
    request = None
    def __init__(self, website):
        self.request = self.session.get(website).text
        self.request = self.request.lower()

    def splitweeks(self):
        string_days = "|".join(self.list_days)
        regex_day = re.compile(string_days)
        split_day = "ecodF vL1E9b iYl9db1ElEUg-6IfGnM2WAv8".split(string_days)
        self.week = re.split(regex_day,self.request)
        print(split_day)

if __name__ == '__main__':
    from template_data import TemplateData as TD
    html = "https://www.google.com/search?source=hp&ei=Y6QNW5v4Doyo8AOXj7HwDA&q=drexel+saxbys&oq=drexel+sax&gs_l=psy-ab.3.0.0j0i22i30k1l4.17324.1224644.0.1226513.51.34.12.0.0.0.449.4490.0j19j3j1j1.25.0....0...1.1.64.psy-ab..17.34.4362.6..35i39k1j0i131k1j0i20i264k1j0i10k1j0i131i20i264k1j0i22i10i30k1.260.K1K8kt3Aoho"
    template =  TD(html)
    template.splitweeks()
