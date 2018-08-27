import sys
import asyncio

from PythonTest.S18.charfinder import UnicodeNameIndex
# UnicodeNameIndex 类用于构建名称索引，提供查询方法

CRLF = b'\r\n'
PROMPT = b'?> '

index = UnicodeNameIndex()
""" 实例化 UnicodeNameIndex 类时，它会使用charfinder_index.pickle 文件（如果有的话）， 
或者构建这个文件，因此第一次运行时可能要等几秒钟服务器才能启动
"""

async def handle_queries(reader, writer):
    """
    这个协程要传给 asyncio.start_server 函数，
    接收的两个参数是 asyncio.StreamReader 对象和 asyncio.StreamWriter 对象。
    """
    while True:
        """这个循环处理会话，直到从客户端收到控制字符后退出。"""
        writer.write(PROMPT)  # 不能使用await, StreamWriter.write 方法不是协程，只是普通的函数；这一行代码发送 ?> 提示符。
        await writer.drain()
        """  StreamWriter.drain 方法刷新 writer 缓冲；因为它是协程，所以必须使用 await 调用。"""
        data = await reader.readline()
        # StreamReader.readline 方法是协程，返回一个 bytes 对象。
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            """ 
            Telnet 客户端发送控制字符时，可能会抛出 UnicodeDecodeError 异常；
            遇到这种情况时，为了简单起见，假装发送的是空字符。
            """
            query = '\x00'
        client = writer.get_extra_info('peername')
        #  返回与套接字连接的远程地址。
        print('Received from {}: {!r}'.format(client, query))
        # 在服务器的控制台中记录查询。
        if query:
            if ord(query[:1]) < 32:
                # 如果收到控制字符或者空字符，退出循环。
                break
            lines = list(index.find_description_strs(query))
            """
            返回一个生成器，产出包含Unicode 码位、真正的字符和字符名称的字符串
            （例如， U+0039\t9\tDIGIT NINE）；为了简单起见，我从中构建了一个列表
            """
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
                """
                使用默认的 UTF-8 编码把 lines 转换成 bytes 对象，
                并在每一行末尾添加回车符和换行 符；注意，参数是一个生成器表达式。 
                """
            writer.write(index.status(query, len(lines)).encode() + CRLF)
            #  输出状态，例如 627 matches for 'digit'

            await writer.drain()
            # 刷新输出缓冲
            print('Sent {} results'.format(len(lines)))
            # 在服务器的控制台中记录响应。

    print('Close the client socket')
    # 在服务器的控制台中记录会话结束。
    writer.close()
    # 关闭 StreamWriter 流。
# END TCP_CHARFINDER_TOP

# BEGIN TCP_CHARFINDER_MAIN
def main(address='127.0.0.1', port=2323):  # 调用 main 函数时可以不传入参数。
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, address, port,
                                loop=loop)
    """
    asyncio.start_server 协程运行结束后，
    返回的协程对象返回一个 asyncio.Server 实例，
    即一个 TCP 套接字服务器。 
    """

    server = loop.run_until_complete(server_coro)
    """
    驱动 server_coro 协程，启动服务器（server）。 
    """

    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    """
    获取这个服务器的第一个套接字的地址和端口，然后在服务器的控制台中显示出来。
    这是这个脚本在服务器的控制台中显示的第一个输出。
    """

    try:
        loop.run_forever()
        # 运行事件循环；main 函数在这里阻塞，直到在服务器的控制台中按 CTRL-C 键才会关闭。
    except KeyboardInterrupt:  # 按CTRL+C
        pass

    print('Server shutting down.')
    server.close()  # 关闭服务器
    loop.run_until_complete(server.wait_closed())
    # server.wait_closed() 方法返回一个期物；调用loop.run_until_complete 方法，运行期物。
    loop.close()
    # 终止事件循环


if __name__ == '__main__':
    main(*sys.argv[1:])
    """
    这是处理可选的命令行参数的简便方式：展开 sys.argv[1:]，
    传给 main 函数，未指定 的参数使用相应的默认值。
    """