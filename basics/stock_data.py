from urllib import request
goog_url='http://chart.finance.yahoo.com/table.csv?s=GOOG&a=0&b=6&c=2017&d=1&e=6&f=2017&g=d&ignore=.csv'
def download_stock_data(csv_url):
 response=request.urlopen(csv_url)
 csv=response.read()
 csv_str=str(csv)
 lines=csv_str.split("\n")
 dest_url=r'droiddanger_da_data.csv'
 fx=open(dest_url, 'w')
 for line in lines:
  fx.write(line +"\n")
 fx.close()

download_stock_data(goog_url)
