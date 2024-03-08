import grpc
import book_pb2
import book_pb2_grpc
from concurrent import futures

class GreeterServicer(book_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return book_pb2.HelloResponse(message='Hello, ' + request.name)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
book_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()