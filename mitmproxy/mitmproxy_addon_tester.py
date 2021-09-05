import datetime

def request(flow):
    file="proxy_test.txt"
    with open(file, 'a') as output:
        output.write(f"\n==================================request=========================================\n")
        output.write(f"{datetime.datetime.now().strftime('%D %H:%M:%S')}\n")
        output.write(f"{flow.request.host}\n")
        for result in dir(flow.request):
            output.write(f"Flow request values {result}: {getattr(flow.request,result)}\n")
            #output.write(f"Flow request values timestamp_start: {datetime.datetime.fromtimestamp(flow.request.timestamp_start)}\n")
            #output.write(f"Flow request values timestamp_end: {datetime.datetime.fromtimestamp(flow.request.timestamp_end)}\n")


def response(flow):
    file="proxy_test.txt"
    with open(file, 'a') as output:
        output.write(f"\n=================================response=========================================\n")
        output.write(f"{datetime.datetime.now().strftime('%D %H:%M:%S')}\n")
        #output.write(f"{flow.response.host}")
        for result in dir(flow.response):
            output.write(f"Flow response value {result}: {getattr(flow.response,result)}\n")
            #output.write(f"Flow response values timestamp_start: {datetime.datetime.fromtimestamp(flow.response.timestamp_start)}\n")
            #output.write(f"Flow response values timestamp_end: {datetime.datetime.fromtimestamp(flow.response.timestamp_end)}\n")
