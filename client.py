import grpc
import book_pb2
import book_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = book_pb2_grpc.GreeterStub(channel)

response = stub.SayHello(book_pb2.HelloRequest(name='World'))
print("Greeter client received: " + response.message)