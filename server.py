import grpc
from concurrent import futures
import socket
import quiz_pb2
import quiz_pb2_grpc

class QuizServiceServicer(quiz_pb2_grpc.QuizServiceServicer):
    def __init__(self):
        self.question = "What is the capital of India?"
        self.answer = "New Delhi"

    def GetQuestion(self, request, context):
        return quiz_pb2.QuestionReply(question=self.question)

    def SubmitAnswer(self, request, context):
        correct = request.answer.strip().lower() == self.answer.lower()
        explanation = "Correct! " if correct else f"Wrong! The answer is {self.answer}."
        return quiz_pb2.AnswerReply(correct=correct, explanation=explanation)


def serve():
    port = 57000

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quiz_pb2_grpc.add_QuizServiceServicer_to_server(QuizServiceServicer(), server)
    server.add_insecure_port(f"127.0.0.1:{57000}")

    print(f"Quiz gRPC Server running on 127.0.0.1:{57000}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
