import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";
import path from "path";

const PROTO_PATH = path.resolve("./proto/quiz.proto");

// Load the proto
const packageDef = protoLoader.loadSync(PROTO_PATH, {});
const quizProto = grpc.loadPackageDefinition(packageDef).quiz;

// Implement the service
const server = new grpc.Server();

server.addService(quizProto.QuizService.service, {
  GetQuestion: (_, callback) => {
    callback(null, {
      question: "What is the capital of France?",
      options: ["A) Paris", "B) Rome", "C) Berlin", "D) Madrid"],
    });
  },
  SubmitAnswer: (call, callback) => {
    const ans = call.request.answer.toUpperCase();
    const feedback =
      ans === "A"
        ? "✅ Correct!"
        : "❌ Wrong! The correct answer is A) Paris.";
    callback(null, { feedback });
  },
});

server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  (err, port) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`🟢 gRPC server running on port ${port}`);
    server.start();
  }
);
