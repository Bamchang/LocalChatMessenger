import os  # OS操作用ライブラリをインポート
import socket  # ソケットライブラリをインポート

# UDPソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバーとクライアントのアドレスを設定
server_address = '/tmp/udp_socket_file'
address = '/tmp/udp_client_socket_file'

# ユーザーからメッセージを受け取る
message = input("Enter your message: ").encode('utf-8')

# ここで既存のソケットファイルを削除
try:
    os.unlink(address)
except FileNotFoundError:
    pass

# アドレスにソケットをバインド（紐付け）
sock.bind(address)

# メッセージをサーバーに送信
try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # サーバーからの応答を待つ
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data.decode('utf-8')))

# 最後にソケットを閉じる
finally:
    print('closing socket')
    sock.close()
