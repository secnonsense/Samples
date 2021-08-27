def response(flow):
    file="response_proxy_log.txt"
    with open(file, 'a') as output:
        output.write(f"{flow.response.headers}\n")

def request(flow):
    file="request_proxy_log.txt"
    with open(file, 'a') as output:
        if "cookie" in flow.request.headers:
            if "LOGIN_INFO" in flow.request.headers['cookie']:
                    cookies=flow.request.headers['cookie'].split(',')
                    for cookie in cookies:
                        if "LOGIN_INFO" in cookie:
                            output.write(f"\nCookie Value is: {cookie}\n")
