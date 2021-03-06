# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from kerastuner.protos import service_pb2 as kerastuner_dot_protos_dot_service__pb2


class OracleStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSpace = channel.unary_unary(
        '/kerastuner.Oracle/GetSpace',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.GetSpaceRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.GetSpaceResponse.FromString,
        )
    self.UpdateSpace = channel.unary_unary(
        '/kerastuner.Oracle/UpdateSpace',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.UpdateSpaceRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.UpdateSpaceResponse.FromString,
        )
    self.CreateTrial = channel.unary_unary(
        '/kerastuner.Oracle/CreateTrial',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.CreateTrialRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.CreateTrialResponse.FromString,
        )
    self.UpdateTrial = channel.unary_unary(
        '/kerastuner.Oracle/UpdateTrial',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.UpdateTrialRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.UpdateTrialResponse.FromString,
        )
    self.EndTrial = channel.unary_unary(
        '/kerastuner.Oracle/EndTrial',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.EndTrialRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.EndTrialResponse.FromString,
        )
    self.GetBestTrials = channel.unary_unary(
        '/kerastuner.Oracle/GetBestTrials',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.GetBestTrialsRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.GetBestTrialsResponse.FromString,
        )
    self.GetTrial = channel.unary_unary(
        '/kerastuner.Oracle/GetTrial',
        request_serializer=kerastuner_dot_protos_dot_service__pb2.GetTrialRequest.SerializeToString,
        response_deserializer=kerastuner_dot_protos_dot_service__pb2.GetTrialResponse.FromString,
        )


class OracleServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSpace(self, request, context):
    """Return the HyperParameter search space.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSpace(self, request, context):
    """Updates the HyperParameter search space.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTrial(self, request, context):
    """Creates a Trial.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTrial(self, request, context):
    """Updates a Trial with metrics and a step.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EndTrial(self, request, context):
    """Ends a Trial.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBestTrials(self, request, context):
    """Gets the best Trials.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTrial(self, request, context):
    """Gets a Trial by ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OracleServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSpace': grpc.unary_unary_rpc_method_handler(
          servicer.GetSpace,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.GetSpaceRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.GetSpaceResponse.SerializeToString,
      ),
      'UpdateSpace': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSpace,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.UpdateSpaceRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.UpdateSpaceResponse.SerializeToString,
      ),
      'CreateTrial': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTrial,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.CreateTrialRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.CreateTrialResponse.SerializeToString,
      ),
      'UpdateTrial': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTrial,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.UpdateTrialRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.UpdateTrialResponse.SerializeToString,
      ),
      'EndTrial': grpc.unary_unary_rpc_method_handler(
          servicer.EndTrial,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.EndTrialRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.EndTrialResponse.SerializeToString,
      ),
      'GetBestTrials': grpc.unary_unary_rpc_method_handler(
          servicer.GetBestTrials,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.GetBestTrialsRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.GetBestTrialsResponse.SerializeToString,
      ),
      'GetTrial': grpc.unary_unary_rpc_method_handler(
          servicer.GetTrial,
          request_deserializer=kerastuner_dot_protos_dot_service__pb2.GetTrialRequest.FromString,
          response_serializer=kerastuner_dot_protos_dot_service__pb2.GetTrialResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kerastuner.Oracle', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
