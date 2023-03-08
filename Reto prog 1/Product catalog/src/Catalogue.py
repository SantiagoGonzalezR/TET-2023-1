from concurrent import futures

import json
import grpc
import Service_pb2
import Service_pb2_grpc

HOST = '[::]:8080'

class CataService(Service_pb2_grpc.CataServiceServicer):
    def checkAvailability(self, response, context):
        item = response.item
        print("\nBuscando el producto: " + item)
        with open("catalogue.json", "r") as cata:
            catalogue = json.loads(cata.read())

        if (item in catalogue):
            print("\nObjeto : " + item +
                  " tiene un valor de " + str(catalogue[item]))
            return Service_pb2.TransactionResponse(status=1, product=catalogue[item])
        else:
            print("\nEl objeto: " + item + " no existe en el catalogo")
            return Service_pb2.TransactionResponse(status=0, product=0)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Service_pb2_grpc.add_ProductServiceServicer_to_server(CataService(), server)
  server.add_insecure_port(HOST)
  print("Service is running... ")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
    serve()
