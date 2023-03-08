import io.grpc.stub.StreamObserver;

public class Checkout extends CheckServiceGrpc.CheckServiceImplBase {
  @Override
  public void check(checkServiceOuterClass.HelloRequest request,
        StreamObserver<checkServiceOuterClass.HelloResponse> responseObserver) {
    System.out.println(request);

    checkServiceOuterClass.HelloResponse response = checkServiceOuterClass.HelloResponse.newBuilder()
      .setcheck("Pedido confirmado: " + request.getName())
      .build();

    responseObserver.onNext(response);

    responseObserver.onCompleted();
  }
}