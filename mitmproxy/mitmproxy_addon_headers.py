
def response(flow):
    file="response_proxy_log2.txt"
    with open(file, 'a') as output:
        output.write(f"{flow.response.headers}\n")

def request(flow):
    file="request_proxy_log2.txt"
    with open(file, 'a') as output:
        output.write(f"\n=======================================================================\n")
        output.write(f"\nHost: {flow.request.host}\n")
        headers=flow.request.headers
        for header in headers:
            output.write(f"\nHeader is: {header} and value is {headers[header]}\n")
