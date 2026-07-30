import { useState } from "react";
import {
  Alert,
  Button,
  CircularProgress,
  Paper,
  TextField,
  Typography,
} from "@mui/material";

import MainLayout from "../layouts/MainLayout";
import api from "../api/api";

export default function InterviewQuestions() {
  const [resumeId, setResumeId] = useState("");
  const [jobId, setJobId] = useState("");

  const [loading, setLoading] = useState(false);
  const [questions, setQuestions] = useState("");
  const [error, setError] = useState("");

  async function generateQuestions() {
    setLoading(true);
    setError("");

    try {
      const response = await api.post("/ai/interview", {
        resume_id: Number(resumeId),
        job_id: Number(jobId),
      });

      setQuestions(response.data.data);
    } catch (err) {
      setError(
        err.response?.data?.message ||
          "Failed to generate interview questions."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <MainLayout>
      <Typography variant="h4" gutterBottom>
        AI Interview Questions
      </Typography>

      <Paper sx={{ p: 3 }}>
        <TextField
          fullWidth
          margin="normal"
          label="Resume ID"
          value={resumeId}
          onChange={(e) => setResumeId(e.target.value)}
        />

        <TextField
          fullWidth
          margin="normal"
          label="Job ID"
          value={jobId}
          onChange={(e) => setJobId(e.target.value)}
        />

        <Button
          variant="contained"
          onClick={generateQuestions}
          disabled={loading}
        >
          {loading ? (
            <CircularProgress size={24} color="inherit" />
          ) : (
            "Generate Questions"
          )}
        </Button>
      </Paper>

      {error && (
        <Alert severity="error" sx={{ mt: 3 }}>
          {error}
        </Alert>
      )}

      {questions && (
        <Paper sx={{ p: 3, mt: 3 }}>
          <Typography variant="h5" gutterBottom>
            Interview Questions
          </Typography>

          <Typography sx={{ whiteSpace: "pre-wrap" }}>
            {questions}
          </Typography>
        </Paper>
      )}
    </MainLayout>
  );
}