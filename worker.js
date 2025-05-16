const mongoose = require("mongoose");

const WorkerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true, required: true },
  skills: [String],
  availability: { type: Boolean, default: true },
  role: { type: String, default: "worker" },
});

module.exports = mongoose.model("Worker", WorkerSchema);
