# -*- coding: utf-8 -*-
import sys, os, BaseHTTPServer


class ServerException(Exception):
    '''服务器内部错误'''
    pass

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    #错误页面
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """



    #处理get请求
    def do_GET(self):
        try:
            # 文件路径
            full_path = os.getcwd() + self.path

            # 如果路径不存在
            if not os.path.exists(full_path):
                # 抛出异常：文件未找到
                raise ServerException("'{0}' not found".format(self.path))

            # 如果路径是个文件
            elif os.path.isfile():
                # 调用 handle_file 处理文件
                self.handle_file(full_path)

            # 如果路径不是个文件
            else:
                # 抛出异常：未知对象
                raise ServerException("Unknown object '{0}'".format(self.path))

        #处理异常
        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content)

    def send_content(self, page):
       self.send_response(200)
       self.send_header("Content-Type", "text/html")
       self.send_header("Content-Length", str(len(page)))
       self.end_headers()
       self.wfile.write(page)
    def handle_file(self, full_path):
        try:
            with open(full_path,'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)





#--------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8003)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

