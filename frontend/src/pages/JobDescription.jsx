import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
    Box,
    Button,
    Paper,
    TextField,
    Typography,
} from "@mui/material";

import { toast } from "react-toastify";

import MainLayout from "../layouts/MainLayout";
import api from "../api/api";

export default function JobDescription() {

    const navigate = useNavigate();

    const [resumeId, setResumeId] = useState("");

    const [jobTitle, setJobTitle] = useState("");

    const [company, setCompany] = useState("");

    const [jobDescription, setJobDescription] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleAnalyze() {

        if (!resumeId || !jobDescription) {

            toast.error(
                "Resume ID and Job Description are required."
            );

            return;
        }

        setLoading(true);

        try {

            const response = await api.post(
                "/analyze",
                {
                    resume_id: Number(resumeId),
                    job_title: jobTitle,
                    company: company,
                    job_description: jobDescription,
                }
            );

            toast.success(
                "Resume analyzed successfully."
            );

            navigate(
                "/result",
                {
                    state: response.data.data,
                }
            );

        } catch (error) {

            toast.error(
                error.response?.data?.message ||
                "Analysis failed."
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
                Job Description
            </Typography>

            <Paper
                sx={{
                    p: 4,
                    borderRadius: 3,
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
                    label="Job Title"
                    value={jobTitle}
                    onChange={(e) =>
                        setJobTitle(e.target.value)
                    }
                />

                <TextField
                    fullWidth
                    margin="normal"
                    label="Company"
                    value={company}
                    onChange={(e) =>
                        setCompany(e.target.value)
                    }
                />

                <TextField
                    fullWidth
                    multiline
                    rows={10}
                    margin="normal"
                    label="Paste Job Description"
                    value={jobDescription}
                    onChange={(e) =>
                        setJobDescription(e.target.value)
                    }
                />

                <Box mt={3}>

                    <Button
                        variant="contained"
                        onClick={handleAnalyze}
                        disabled={loading}
                    >
                        {loading
                            ? "Analyzing..."
                            : "Analyze Resume"}
                    </Button>

                </Box>

            </Paper>

        </MainLayout>

    );

}