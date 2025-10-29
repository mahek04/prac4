import grpc
import quiz_pb2
import quiz_pb2_grpc

def run():
    
    channel = grpc.insecure_channel(f"127.0.0.1:{57000}")
    stub = quiz_pb2_grpc.QuizServiceStub(channel)

    # Step 1: Get Question
    question = stub.GetQuestion(quiz_pb2.QuestionRequest())
    print(f"Question: {question.question}")

    # Step 2: Get answer from user
    user_answer = input("Your answer: ")
    result = stub.SubmitAnswer(quiz_pb2.AnswerRequest(answer=user_answer))
    print(f"{result.explanation}")

if __name__ == "__main__":
    run()
