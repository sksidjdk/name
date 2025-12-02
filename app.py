from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # HTTP 状态码 200 OK
        self.send_response(200)
        # 返回纯文本
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        # 实际返回内容
        message = "Hello, World from Python on Vercel!"
        self.wfile.write(message.encode("utf-8"))
