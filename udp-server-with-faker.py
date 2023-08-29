import socket  # ソケットライブラリをインポート
import os  # OS操作用ライブラリをインポート
from faker import Faker  # Fakerライブラリをインポート

fake = Faker()  # Fakerインスタンスを作成

# UDPソケットを作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# サーバーのアドレスを設定
server_address = '/tmp/udp_socket_file'

# 古いソケットファイルがあれば削除
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

# サーバーが起動しているアドレスを表示
print('starting up on {}'.format(server_address))

# アドレスにソケットをバインド（紐付け）
sock.bind(server_address)

# 無限ループでデータの受信を待機
while True:
    print('\nwaiting to receive message')

    # メッセージを受信
    data, address = sock.recvfrom(4096)
    
    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    # Fakerでダミーデータを生成
    fake_response = fake.sentence().encode('utf-8')

    # データがあればクライアントに送信
    if data:
        sent = sock.sendto(fake_response, address)
        print('sent {} bytes back to {}'.format(sent, address))
