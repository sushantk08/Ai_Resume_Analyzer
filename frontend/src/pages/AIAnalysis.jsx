import { useState } from "react";

import {
    Alert,
    Box,
    Button,
    CircularProgress,
    Paper,
    TextField,
    Typography,
} from "@mui/material";

import MainLayout from "../layouts/MainLayout";
import api from "../api/api";

export default function AIAnalysis() {

    const [resumeId, setResumeId] = useState("");
    const [jobId, setJobId] = useState("");

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState("");

    const [error, setError] = useState("");

    async function analyzeResume() {

        setLoading(true);
        setError("");

        try {

            const response = await api.post(
                "/ai/analyze",
                {
                    resume_id: Number(resumeId),
                    job_id: Number(jobId),
                }
            );

            setResult(response.data.data);

        } catch (err) {

            setError(
                err.response?.data?.message ||
                "AI analysis failed."
            );

        } finally {

            setLoading(false);

        }

    }

    return (

        <MainLayout>

            <Typography
                variant="h4"
                gutterBottom
            >
                AI Resume Analysis
            </Typography>

            <Paper
                sx={{
                    p: 3,
                    mb: 4,
                }}
            >

                <TextField
                    fullWidth
                    margin="normal"
                    label="Resume ID"
                    value={resumeId}
                    onChange={(e) =>
                        setResumeId(e.target.value)
                    }
                />

                <TextField
                    fullWidth
                    margin="normal"
                    label="Job ID"
                    value={jobId}
                    onChange={(e) =>
                        setJobId(e.target.value)
                    }
                />

                <Button
                    sx={{ mt: 2 }}
                    variant="contained"
                    onClick={analyzeResume}
                    disabled={loading}
                >

                    {loading ? (

                        <CircularProgress
                            size={24}
                            color="inherit"
                        />

                    ) : (

                        "Analyze Resume"

                    )}

                </Button>

            </Paper>

            {error && (

                <Alert severity="error">

                    {error}

                </Alert>

            )}

            {result && (

                <Paper
                    sx={{
                        p: 4,
                    }}
                >

                    <Typography
                        variant="h5"
                        gutterBottom
                    >
                        AI Feedback
                    </Typography>

                    <Box
                        sx={{
                            whiteSpace: "pre-wrap",
                            mt: 2,
                        }}
                    >
                        {result}
                    </Box>

                </Paper>

            )}

        </MainLayout>

    );

}